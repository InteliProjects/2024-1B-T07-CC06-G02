from utils import calculate_total_duration, calculate_travel_time


def start_new_route(route, point):
    """
    Adds a new point to the given route.

    Parameters:
    route (list): The list representing the current route.
    point: The point to be added to the route.

    Returns:
    None
    """
    route.append(point)

def finish_route(routes, route):
    """
    Adds the given route to the list of routes if it is not empty.

    Parameters:
    - routes (list): The list of routes.
    - route (list): The route to be added.

    Returns:
    None
    """
    if route:
        routes.append(route)

def bad_algorithm(data, max_duration_hours):
    """
    Build routes based on input data and maximum duration per route.

    Parameters:
    - data (DataFrame): DataFrame containing latitude and longitude columns.
    - max_duration_hours (float): Maximum duration allowed for each route in hours.

    Returns:
    - routes (list of lists): List containing routes, where each route is a list of points.
    """
    reading_time_per_point = 0.04  # Average reading time per point in hours
    

    routes = []
    durations = []
    current_route = []
    current_duration = 0

    for i, point in data.iterrows():
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

            current_route.append(point)
            current_duration += travel_time + reading_time_per_point

    finish_route(routes, current_route)
    durations.append(current_duration)

    return routes, durations