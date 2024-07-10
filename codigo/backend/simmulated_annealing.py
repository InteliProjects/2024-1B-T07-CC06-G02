from utils import calculate_total_duration, calculate_travel_time, haversine, calculate_total_distance
import random
import math
import pandas as pd


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



def get_neighbor_solution(current_route):
    """
    Generate a neighboring solution from the current route.

    Parameters:
    - current_route (list of dictionaries): List containing dictionaries representing points with 'LATITUDE' and 'LONGITUDE' keys.

    Returns:
    - neighbor_route (list of dictionaries): The neighboring solution route.
    """
    # Clone the current route to modify it
    neighbor_route = current_route[:]

    # Choose two random indices for swapping
    index1, index2 = random.sample(range(len(neighbor_route)), 2)

    # Swap the points at the chosen indices
    neighbor_route[index1], neighbor_route[index2] = neighbor_route[index2], neighbor_route[index1]

    return neighbor_route


def run_simmulated_annealing(data, max_duration_hours, max_iterations, initial_temperature, cooling_rate):
    """
    Build routes based on input data and maximum duration per route using Simulated Annealing.

    Parameters:
    - data (DataFrame): DataFrame containing latitude and longitude columns.
    - max_duration_hours (float): Maximum duration allowed for each route in hours.
    - max_iterations (int): Maximum number of iterations for Simulated Annealing.
    - initial_temperature (float): Initial temperature for Simulated Annealing.
    - cooling_rate (float): Cooling rate for Simulated Annealing.

    Returns:
    - routes (list of lists): List containing routes, where each route is a list of points.
    """
    reading_time_per_point = 0.04  # Average reading time per point in hours

    # Initialize Simulated Annealing
    current_route = data.to_dict('records')  # Initial route
    current_distance = calculate_total_distance(current_route)
    best_route = current_route[:]
    best_distance = current_distance
    temperature = initial_temperature


    for _ in range(max_iterations):
        # Generate a neighbor solution
        new_route = get_neighbor_solution(current_route)
        new_distance = calculate_total_distance(new_route)

        # Calculate the difference in distance
        delta_distance = new_distance - current_distance

        if delta_distance < 0 or random.random() < math.exp(-delta_distance / temperature):
            current_route = new_route[:]
            current_distance = new_distance
            if current_distance < best_distance:
                best_route = current_route[:]
                best_distance = current_distance

        temperature *= cooling_rate

    # Construct routes based on the best solution found
    routes = []
    durations = []
    current_route = []
    current_duration = 0

    for point in best_route:
        if not current_route:
            current_route.append(point)
        else:
            travel_time = calculate_travel_time(current_route[-1], point)
            total_duration = calculate_total_duration(
                current_duration, travel_time, len(current_route))

            if total_duration > max_duration_hours:
                finish_route(routes, current_route)
                durations.append(current_duration)
                current_route = []
                current_duration = 0

            current_route.append(point)
            current_duration += travel_time + reading_time_per_point

    finish_route(routes, current_route)
    durations.append(current_duration)
    calculate_metrics(routes, durations)

    return routes, durations



def calculate_metrics(routes, durations):
    total_distance = sum(calculate_total_distance(route) for route in routes)
    total_days = len(routes)
    average_daily_time = sum(durations) / total_days
    num_readers = calculate_needed_people(durations, 6, total_days)
    return {
        "AVERAGE_DAILY_TIME": average_daily_time,
        "TOTAL_DISTANCE": total_distance,
        "TOTAL_DAYS": total_days,
        "NUM_READERS": num_readers
    }

def calculate_needed_people(durations, work_hours_per_day, days):
    total_hours_needed = sum(durations)
    total_person_days_needed = total_hours_needed / work_hours_per_day
    people_needed = math.ceil(total_person_days_needed / days)
    return people_needed

def build_points_df(routes, durations):
    # Calcule as métricas com base nas rotas e durações
    metrics = calculate_metrics(routes, durations)

    # Lista para armazenar todos os pontos com detalhes adicionais
    points = []
    for i, (route, duration) in enumerate(zip(routes, durations)):
        for j, point in enumerate(route):
            points.append((f'Rota_{i+1}', point['LATITUDE'], point['LONGITUDE'], j+1, duration))

    # Cria um DataFrame a partir da lista de pontos com colunas específicas
    points_df = pd.DataFrame(points, columns=['ROTA', 'LATITUDE', 'LONGITUDE', 'SEQUENCIA', 'DURAÇÃO'])


    points_df['AVERAGE_DAILY_TIME'] = metrics['AVERAGE_DAILY_TIME']
    points_df['TOTAL_DISTANCE'] = metrics['TOTAL_DISTANCE']
    points_df['TOTAL_DAYS'] = metrics['TOTAL_DAYS']
    points_df['NUM_READERS'] = metrics['NUM_READERS']

    # Adicione as métricas calculadas como colunas constantes em cada linha do DataFrame


    return points_df