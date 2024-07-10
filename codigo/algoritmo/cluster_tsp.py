import pandas as pd
from sklearn.cluster import MiniBatchKMeans
from sklearn.preprocessing import StandardScaler
from haversine import haversine
import networkx as nx


df = pd.read_csv("../data/amostra_total.csv", sep=';')

scaler = StandardScaler()
coords = df[['LATITUDE', 'LONGITUDE']].values
coords_normalized = scaler.fit_transform(coords)

def calculate_route_duration(route, locations, read_time=2, speed=5):
    """
    Calculate the total duration of a route.

    Parameters:
        route (list): List of indices representing the order of locations in the route.
        locations (list): List of tuples containing (latitude, longitude) of locations.
        read_time (float): Time spent at each location for reading, in minutes. Default is 2 minutes.
        speed (float): Average speed of travel between locations, in kilometers per hour. Default is 5 km/h.

    Returns:
        float: Total duration of the route in minutes.
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
    Solve the Traveling Salesman Problem (TSP) using NetworkX library.

    This function constructs a complete graph where each node represents a location to be visited,
    and each edge represents the distance between two locations. The distance between locations is
    calculated using the haversine formula, which considers the curvature of the Earth's surface.

    Parameters:
        locations (list): A list of tuples containing latitude and longitude coordinates of locations
                          to be visited.

    Returns:
        list: A list of indices representing the optimized route for visiting all locations.
    """
    G = nx.complete_graph(len(locations))
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            distance = haversine(locations[i], locations[j])
            G[i][j]['weight'] = distance
            G[j][i]['weight'] = distance
    tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True, method=nx.approximation.christofides)
    return tsp_path

max_duration = 6 * 60

# Primeiro clustering com 350 clusters (leituristas)
n_clusters_leituristas = 350
kmeans_leituristas = MiniBatchKMeans(n_clusters=n_clusters_leituristas, random_state=88, batch_size=200)
labels_leituristas = kmeans_leituristas.fit_predict(coords_normalized)
df['Cluster_Leiturista'] = labels_leituristas

# Segundo clustering dentro de cada cluster de leituristas para 22 subclusters (dias de leitura)
n_clusters_dias = 22
all_routes = []

# Leitura total : range(n_clusters_leituristas)
for leiturista in range(5):  # Ajustar para range(n_clusters_leituristas) para leitura total
    cluster_data = df[df['Cluster_Leiturista'] == leiturista]
    if not cluster_data.empty:
        coords_cluster = cluster_data[['LATITUDE', 'LONGITUDE']].values
        coords_cluster_normalized = scaler.fit_transform(coords_cluster)
        kmeans_dias = MiniBatchKMeans(n_clusters=n_clusters_dias, random_state=88, batch_size=50)
        labels_dias = kmeans_dias.fit_predict(coords_cluster_normalized)
        cluster_data['Cluster_Dia'] = labels_dias

        # Roteirização otimizada dentro de cada subcluster de dia (usado 5 para rodar rápido o teste) Leitura total: range(n_clusters_dias)
        for dia in range(n_clusters_dias):  # Ajustar para range(n_clusters_dias) para leitura total
            subcluster_data = cluster_data[cluster_data['Cluster_Dia'] == dia]
            if not subcluster_data.empty:
                locations = subcluster_data[['LATITUDE', 'LONGITUDE']].values.tolist()
                route = solve_tsp_networkx(locations)
                
                # Divide a rota em partes menores se exceder 6 horas
                adjusted_routes = []
                current_route = []
                current_duration = 0
                for i in range(len(route) - 1):
                    loc1 = locations[route[i]]
                    loc2 = locations[route[i + 1]]
                    distance = haversine(loc1, loc2)
                    travel_time = (distance / 5) * 60
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
                for idx, adj_route in enumerate(adjusted_routes):
                    for point in adj_route:
                        all_routes.append([
                            leiturista, dia, idx, 
                            subcluster_data.iloc[point]['INDICE'], 
                            subcluster_data.iloc[point]['LATITUDE'], 
                            subcluster_data.iloc[point]['LONGITUDE'],
                            subcluster_data.iloc[point]['CODIGO_ROTA'],
                            subcluster_data.iloc[point]['SEQUENCIA'],
                            subcluster_data.iloc[point]['LOGRADOURO'],
                            subcluster_data.iloc[point]['NUMERO']
                        ])

df_routes = pd.DataFrame(all_routes, columns=[
    'CLUSTER_LEITURISTA', 'CLUSTER_DIA', 'ROTA', 'INDICE', 
    'LATITUDE', 'LONGITUDE', 'CODIGO_ROTA', 'SEQUENCIA', 
    'LOGRADOURO', 'NUMERO'
])
df_routes.to_csv('../results/rotas_clusters.csv', index=False)

print("Arquivo 'rotas_clusters.csv' salvo com sucesso.")
