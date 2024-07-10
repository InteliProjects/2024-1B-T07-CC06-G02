from utils import calculate_total_duration, calculate_travel_time, haversine, calculate_total_distance
import random
import math
import pandas as pd

# Function to start a new route by adding a point
def start_new_route(route, point):
    """
    Adds a new point to the current route.

    Parameters:
    - route (list): Current route being built.
    - point (dict): Point to add to the route.
    """
    route.append(point)

# Function to finish the current route and add to the list of routes
def finish_route(routes, route):
    """
    Finalizes the current route and adds it to the list of all routes.

    Parameters:
    - routes (list): List of all routes.
    - route (list): Current route being finalized.
    """
    if route:
        routes.append(route)

# Function to find the nearest neighbor of each point
def nearest_neighbor(data):
    """
    Builds a route using the nearest neighbor heuristic.

    Parameters:
    - data (DataFrame): Data containing points with latitude and longitude.

    Returns:
    - list: Route built by following the nearest neighbor heuristic.
    """
    data_records = data.to_dict('records')
    unvisited = data_records[:]
    current_point = unvisited.pop(0)
    route = [current_point]

    while unvisited:
        next_point = min(unvisited, key=lambda point: haversine(current_point['LATITUDE'], current_point['LONGITUDE'], point['LATITUDE'], point['LONGITUDE']))
        unvisited.remove(next_point)
        route.append(next_point)
        current_point = next_point

    return route

# Function to optimize a route using the two-opt algorithm
def two_opt(route, improvement_threshold=0.001, max_iterations=100):
    """
    Optimizes a given route using the two-opt swapping algorithm.

    Parameters:
    - route (list): Initial route.
    - improvement_threshold (float): Minimum improvement required to accept a swap.
    - max_iterations (int): Maximum number of iterations to perform.

    Returns:
    - list: Optimized route.
    """
    best_distance = calculate_total_distance(route)
    for iteration_count in range(max_iterations):
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = reversed(route[i:j])
                new_distance = calculate_total_distance(new_route)
                if best_distance - new_distance > improvement_threshold:
                    route = new_route
                    best_distance = new_distance
                    improved = True
                    break
            if improved:
                break
        if not improved:
            break
    return route

# Function to construct routes considering a maximum duration
def two_opt_builder(data, max_duration_hours):
    """
    Constructs optimized routes for a dataset within a specified maximum duration.

    Parameters:
    - data (DataFrame): Data containing points with latitude and longitude.
    - max_duration_hours (float): Maximum allowed duration for any route in hours.

    Returns:
    - list: List of routes, each not exceeding the maximum duration.
    """
    initial_route = nearest_neighbor(data)
    optimized_route = two_opt(initial_route)
    routes = []
    durations = []
    current_route = []
    current_duration = 0

    for point in optimized_route:
        if not current_route:
            start_new_route(current_route, point)
        else:
            travel_time = calculate_travel_time(current_route[-1], point)
            total_duration = calculate_total_duration(current_duration, travel_time, len(current_route))

            if total_duration > max_duration_hours:
                finish_route(routes, current_route)
                durations.append(current_duration)
                current_route = []
                current_duration = 0

            start_new_route(current_route, point)
            current_duration += travel_time + 0.04  # Assuming 2 minutes (0.04 hours) per stop

    finish_route(routes, current_route)
    durations.append(current_duration)

    return routes, durations 
