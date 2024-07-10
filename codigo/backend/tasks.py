import logging
import pandas as pd
import os
from simmulated_annealing import run_simmulated_annealing, build_points_df
from data_pipeline import process_data
from two_opt import run_two_opt_builder 
from new_algorithm import run_create_routes_for_cluster, calculate_route_duration

# Dictionary to store task information
tasks = {}

def async_simmulated_annealing(task_id, file_path, read_time=2, speed=5, max_duration=360, max_duration_hours=6, fraction=0.01):

    """
    Asynchronously performs simulated annealing optimization on the given data.
    Processes the file to optimize routing and saves the result.

    Args:
        task_id (int): The ID of the task.
        file_path (str): The path to the input file.
        max_duration_hours (int, optional): The maximum duration in hours for the optimization. Defaults to 6.
        fraction (float, optional): The fraction of data to be used for optimization. Defaults to 0.01.

    Returns:
        None
    """
    try:
        tasks[task_id] = {'status': 'processing'}
        data = pd.read_csv(file_path, sep=';')
        # Assuming process_data to subset and prepare the data
        data = process_data(data, fraction)

        # Convert max_duration from minutes to hours for compatibility with run_simmulated_annealing function
        max_hours_per_route = max_duration / 60

        routes, durations = run_simmulated_annealing(data, max_hours_per_route, 1000, 2500, 0.008)
        points_df = build_points_df(routes, durations)

        os.makedirs('results', exist_ok=True)
        result_path = f'results/result_{task_id}.csv'
        points_df.to_csv(result_path, index=False)

        tasks[task_id]['status'] = 'completed'
        tasks[task_id]['result'] = result_path
    except Exception as e:
        logging.error(f"Error in async task {task_id}: {e}")
        tasks[task_id]['status'] = 'failed'
        tasks[task_id]['error'] = str(e)


def async_two_opt(task_id, file_path, read_time=2, speed=5, max_duration=360, max_duration_hours=6, fraction=0.001):
    """
    Asynchronously performs two-opt optimization on the given data.
    Processes the file to optimize routing using a two-opt strategy and saves the result.

    Args:
        task_id (int): The ID of the task.
        file_path (str): The path to the input file.
        max_duration_hours (int, optional): The maximum duration in hours for the optimization. Defaults to 6.
        fraction (float, optional): The fraction of data to be used for optimization. Defaults to 0.01.

    Returns:
        None
    """
    try:
        tasks[task_id]['status'] = 'processing'
        data = pd.read_csv(file_path, sep=';')
        data = process_data(data, fraction)
        routes, durations = run_two_opt_builder(data, max_duration/60)
        points_df = build_points_df(routes, durations)
        os.makedirs('results', exist_ok=True)
        result_path = f'results/result_{task_id}.csv'
        points_df.to_csv(result_path, index=False)
        tasks[task_id]['status'] = 'completed'
        tasks[task_id]['result'] = result_path
    except Exception as e:
        logging.error(f"Error in async task: {e}")
        tasks[task_id]['status'] = 'failed'
        tasks[task_id]['error'] = str(e)



def async_run_create_routes_for_cluster(task_id, file_path, read_time=2, speed=5, max_duration=360):
    """
    Asynchronously runs the function to create routes for clusters using the input file.
    Processes the file and attempts to optimize the routing of clustered data.

    Args:
        task_id (str): The task ID.
        file_path (str): The path to the input file.

    Returns:
        None
    """
    try:
        tasks[task_id]['status'] = 'processing'
        result_data = run_create_routes_for_cluster(file_path, read_time, speed, max_duration)
        result_path = f'results/{task_id}_routes_clusters.csv'  # Inclui o task_id no nome do arquivo para evitar colisões de nome

        # Salva os resultados adicionais como parte do objeto de tarefa
        tasks[task_id]['result'] = result_path
        tasks[task_id]['additional_info'] = result_data  # Armazena os dados adicionais
        tasks[task_id]['status'] = 'completed'
        
        # Salva os resultados em um arquivo CSV
        pd.DataFrame(result_data).to_csv(result_path, index=False)
    except Exception as e:
        logging.error(f"Error in async task: {task_id}: {e}")
        tasks[task_id]['status'] = 'failed'
        tasks[task_id]['error'] = str(e)