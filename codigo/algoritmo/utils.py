import numpy as np
import pandas as pd


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the Earth's surface using the Haversine formula.

    Parameters:
    - lat1 (float): Latitude of the first point in degrees.
    - lon1 (float): Longitude of the first point in degrees.
    - lat2 (float): Latitude of the second point in degrees.
    - lon2 (float): Longitude of the second point in degrees.

    Returns:
    - distance (float): The distance between the two points in kilometers.
    """
    # Earth's radius in kilometers
    earth_radius = 6371.0
    
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    # Distance in kilometers
    distance = earth_radius * c
    return distance


def calculate_travel_time(prev_point, next_point):
    velocity = 5  # Average velocity in km/h of 'leituristas'

    distance = haversine(prev_point['LATITUDE'], prev_point['LONGITUDE'], next_point['LATITUDE'], next_point['LONGITUDE'])
    return distance / velocity


def calculate_total_duration(current_duration, travel_time, len_route):
    reading_time_per_point = 0.04  # Average reading time per point in hours

    total_duration = current_duration + travel_time + (reading_time_per_point * len_route)
    print(f'Total duration: {total_duration}')
    return total_duration

# Function to build DataFrame for points
def build_points_df(routes, durations):
    """
    Build DataFrame for points.

    Parameters:
    - routes (list of lists): List containing routes, where each route is a list of points.

    Returns:
    - points_df (DataFrame): DataFrame containing columns LATITUDE, LONGITUDE, ROTA, and SEQUENCIA.
    """
    points = []
    for i, (route, duration) in enumerate(zip(routes, durations)):
        for j, point in enumerate(route):
            points.append((f'Rota_{i+1}', point['LATITUDE'], point['LONGITUDE'], j+1, duration))
    points_df = pd.DataFrame(points, columns=['ROTA', 'LATITUDE', 'LONGITUDE', 'SEQUENCIA', 'DURAÇÃO'])
    return points_df



def calculate_total_distance(route):
    """
    Calculate the total distance of a route.

    Parameters:
    - route (list of dictionaries): List containing dictionaries representing points with 'LATITUDE' and 'LONGITUDE' keys.

    Returns:
    - total_distance (float): The total distance of the route in kilometers.
    """
    total_distance = 0.0
    for i in range(len(route) - 1):
        point1 = route[i]
        point2 = route[i + 1]
        distance = haversine(
            point1['LATITUDE'], point1['LONGITUDE'], point2['LATITUDE'], point2['LONGITUDE'])
        total_distance += distance
    return total_distance