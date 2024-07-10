import pandas as pd

from utils import build_points_df
from data_pipeline import process_data
from simmulated_annealing import simmulated_annealing
from example_algorithm import bad_algorithm
from two_opt import nearest_neighbor, two_opt_builder
# Function to read and process the CSV file


def read_and_process_csv(file):
    """
    Read and process the CSV file.

    Parameters:
    - file (str): Path to the CSV file.

    Returns:
    - data (DataFrame): Processed DataFrame.
    """
    data = pd.read_csv(file, sep=';')

    data = process_data(data)
    return data

if __name__ == '__main__':
    # Read and process the CSV file
    data = read_and_process_csv('../data/amostra_total.csv')
    
    # Maximum duration of routes in hours
    max_duration_hours = 6

    # Build routes using the selected algorithm    
    selected_algorithm = 3

    if selected_algorithm == 1:
        routes, durations = bad_algorithm(data, max_duration_hours)
    elif selected_algorithm == 2:
        routes, durations = simmulated_annealing(data, max_duration_hours, 1000, 2500, 0.008)
    elif selected_algorithm == 3:
        routes, durations = two_opt_builder(data, max_duration_hours)

    # Build DataFrame for points
    points_df = build_points_df(routes, durations)


    # Save the DataFrames to CSV files
    points_df.to_csv('../results/pontos_rotas.csv', index=False)
