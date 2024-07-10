import warnings
import pandas as pd
from sklearn.cluster import MiniBatchKMeans
from haversine import haversine
import networkx as nx
import numpy as np
from tqdm import tqdm  # Importing tqdm for progress bar
import random
import osmnx as ox

# Supress specific FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Reading the data
df = pd.read_csv("../data/amostra_total.csv", sep=';')

coords = df[['LATITUDE', 'LONGITUDE']].values

def calculate_route_duration(route, locations, read_time=2, speed=5):
    """
    Calculate the total duration of a route.

    Parameters:
    route (list): The route as a list of location indices.
    locations (list): The list of location coordinates.
    read_time (int, optional): The time spent reading at each location. Defaults to 2 minutes.
    speed (int, optional): The travel speed in km/h. Defaults to 5 km/h.

    Returns:
    float: The total duration of the route in minutes.
    """
    total_time = 0
    for i in range(len(route) - 1):
        loc1 = locations[route[i]]
        loc2 = locations[route[i + 1]]
        distance = haversine(loc1, loc2)
        travel_time = (distance / speed) * 60
        total_time += travel_time + read_time
    return total_time


ox.config(use_cache=True, log_console=False)

def get_osmnx_distance(loc1, loc2, G):
    orig_node = ox.distance.nearest_nodes(G, loc1[1], loc1[0])
    dest_node = ox.distance.nearest_nodes(G, loc2[1], loc2[0])

    route = nx.shortest_path(G, orig_node, dest_node, weight='length')
    
    distance = sum(ox.utils_graph.get_route_edge_attributes(G, route, 'length'))
    
    return distance / 1000


def get_centroid(locations):
    """
    Calculates the centroid of a list of locations.

    Args:
        locations (list): A list of tuples representing the latitude and longitude of each location.

    Returns:
        tuple: A tuple representing the latitude and longitude of the centroid.
    """
    lat = np.mean([loc[0] for loc in locations])
    lon = np.mean([loc[1] for loc in locations])
    return (lat, lon)

def solve_tsp_networkx(locations):
    """
    Solve the Traveling Salesman Problem (TSP) using NetworkX.

    Parameters:
    locations (list): The list of location coordinates.

    Returns:
    list: The optimized route as a list of location indices.
    """
    centroid = get_centroid(locations)
    G = ox.graph_from_point(centroid, dist=400, network_type='walk')
    
    G_complete = nx.complete_graph(len(locations))
    
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            distance = get_osmnx_distance(locations[i], locations[j], G)
            G_complete[i][j]['weight'] = distance
            G_complete[j][i]['weight'] = distance
    
    tsp_path = nx.approximation.traveling_salesman_problem(G_complete, cycle=False, method=nx.approximation.christofides)
    
    return tsp_path

def create_routes_for_cluster(cluster_data, max_duration=360, speed=5):
    """
    Create routes for a cluster of locations.

    Parameters:
    cluster_data (DataFrame): The data for the cluster.
    max_duration (int, optional): The maximum duration of a route in minutes. Defaults to 360 minutes.
    speed (int, optional): The travel speed in km/h. Defaults to 5 km/h.

    Returns:
    list: A list of routes, where each route is a list of location indices.
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

max_duration = 6 * 60  # 6 hours in minutes
total_days = 22

# Parameters for MiniBatchKMeans
n_clusters = 150
batch_size = 1000

kmeans = MiniBatchKMeans(n_clusters=(n_clusters * total_days), batch_size=batch_size, random_state=42)
labels = kmeans.fit_predict(coords)
df['Cluster'] = labels

all_routes = []
unique_clusters = list(set(labels))

# Randomly select 20% of the clusters
selected_clusters = random.sample(unique_clusters, int(0.005 * len(unique_clusters)))
total_routes = 0

# Adding progress bar for clusters
for cluster_label in tqdm(selected_clusters, desc="Processing Clusters"):
    try:
        cluster_data = df[df['Cluster'] == cluster_label]
        if not cluster_data.empty:
            routes = create_routes_for_cluster(cluster_data, max_duration)
            total_routes += len(routes)
            
            # Adding progress bar for routes
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

# Calculate the required number of readers
num_readers = total_routes // total_days
if total_routes % total_days != 0:
    num_readers += 1  # Add an extra reader if there are remaining days

df_routes = pd.DataFrame(all_routes, columns=[
    'CLUSTER', 'ROUTE', 'INDEX', 
    'LATITUDE', 'LONGITUDE', 'ROUTE_CODE', 'SEQUENCE', 
    'STREET', 'NUMBER'
])
df_routes.to_csv('../results/routes_clusters.csv', index=False)

print("File 'routes_clusters.csv' saved successfully.")
print(f"Required number of readers: {num_readers}")
