import pandas as pd
from sklearn.cluster import MiniBatchKMeans
from haversine import haversine
import networkx as nx
import numpy as np
from tqdm import tqdm  # Importing tqdm for progress bar
import random

def calculate_route_duration(route, locations, read_time=2, speed=5):
    """
    Calculates the total duration of a route based on locations and travel parameters.
    """
    total_time = 0
    for i in range(len(route) - 1):
        loc1 = locations[route[i]]
        loc2 = locations[route[i + 1]]
        distance = haversine(loc1, loc2)
        travel_time = (distance / speed) * 60
        total_time += travel_time + read_time
    return total_time

def solve_tsp_networkx(locations):
    """
    Solves the Traveling Salesman Problem (TSP) using NetworkX library with a heuristic method.
    """
    G = nx.complete_graph(len(locations))
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            distance = haversine(locations[i], locations[j])
            G[i][j]['weight'] = distance
            G[j][i]['weight'] = distance
    tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=False, method=nx.approximation.christofides)
    return tsp_path

def create_routes_for_cluster(cluster_data, max_duration=360, speed=5):
    """
    Creates optimized routes for a cluster of locations within a specified maximum duration.
    """
    locations = cluster_data[['LATITUDE', 'LONGITUDE']].values.tolist()
    route = solve_tsp_networkx(locations)
    adjusted_routes = []
    current_route = []
    current_duration = 0
    
    for i in range(len(route) - 1):
        loc1 = locations[route[i]]
        loc2 = locations[route[i + 1]]
        distance = haversine(loc1, loc2)
        travel_time = (distance / speed) * 60
        read_time = 2
        segment_time = travel_time + read_time
        
        if current_duration + segment_time > max_duration:
            adjusted_routes.append(current_route)
            current_route = [route[i]]
            current_duration = segment_time
        else:
            current_route.append(route[i])
            current_duration += segment_time
    
    current_route.append(route[-1])
    adjusted_routes.append(current_route)
    
    return adjusted_routes


def run_create_routes_for_cluster(file_path, read_time=2, speed=5, max_duration=360, total_days=22, n_clusters=150, batch_size=1000):
    df = pd.read_csv(file_path, sep=';')
    coords = df[['LATITUDE', 'LONGITUDE']].values

    kmeans = MiniBatchKMeans(n_clusters=(n_clusters * total_days), batch_size=batch_size, random_state=42)
    labels = kmeans.fit_predict(coords)
    df['Cluster'] = labels

    all_routes = []
    unique_clusters = list(set(labels))
    selected_clusters = random.sample(unique_clusters, int(0.2 * len(unique_clusters)))
    total_routes = 0

    for cluster_label in tqdm(selected_clusters, desc="Processing Clusters"):
        try:
            cluster_data = df[df['Cluster'] == cluster_label]
            if not cluster_data.empty:
                routes = create_routes_for_cluster(cluster_data, max_duration, speed)
                total_routes += len(routes)
                
                for route_idx, route in enumerate(tqdm(routes, desc=f"Processing Routes of Cluster {cluster_label}", leave=False)):
                    for point in route:
                        all_routes.append([
                            cluster_label, route_idx,
                            cluster_data.iloc[point]['INDICE'], 
                            cluster_data.iloc[point]['LATITUDE'], 
                            cluster_data.iloc[point]['LONGITUDE'],
                            cluster_data.iloc[point]['CODIGO_ROTA'],
                            cluster_data.iloc[point]['SEQUENCIA'],
                            cluster_data.iloc[point]['LOGRADOURO'],
                            cluster_data.iloc[point]['NUMERO']
                        ])
        except Exception as e:
            print(f"Error processing cluster {cluster_label}: {e}")

    num_readers = total_routes // total_days
    if total_routes % total_days != 0:
        num_readers += 1

    df_routes = pd.DataFrame(all_routes, columns=[
        'CLUSTER', 'ROUTE', 'INDEX', 
        'LATITUDE', 'LONGITUDE', 'ROUTE_CODE', 'SEQUENCE', 
        'STREET', 'NUMBER'
    ])
    
    total_distance = 0
    total_time = 0
    for _, group in df_routes.groupby(['CLUSTER', 'ROUTE']):
        points = group[['LATITUDE', 'LONGITUDE']].values.tolist()
        route_time = calculate_route_duration(list(range(len(points))), points, read_time, speed)
        total_time += route_time/60
        for i in range(len(points) - 1):
            total_distance += haversine(points[i], points[i + 1])

    total_days = np.ceil(total_time / 6)
    average_daily_time = total_time / total_days if total_days > 0 else 0

    # Append the calculated metrics as new columns to the DataFrame
    df_routes['TOTAL_DAYS'] = total_days
    df_routes['NUM_READERS'] = num_readers
    df_routes['TOTAL_DISTANCE'] = total_distance
    df_routes['AVERAGE_DAILY_TIME'] = average_daily_time

    # Save to CSV to avoid overwriting previous data
    df_routes.to_csv('./results/routes_clusters.csv', index=False)
    print("File 'routes_clusters.csv' successfully saved.")

    return df_routes