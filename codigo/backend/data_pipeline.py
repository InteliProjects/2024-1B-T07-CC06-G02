import pandas as pd

def remove_nan(data: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with NaN values from the DataFrame.

    Args:
    - data: DataFrame containing the data.

    Returns:
    - DataFrame without NaN values.
    """
    return data.dropna()

def remove_duplicates(data: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the DataFrame.

    Args:
    - data: DataFrame containing the data.

    Returns:
    - DataFrame without duplicate rows.
    """
    return data.drop_duplicates()

def reset_index(data: pd.DataFrame) -> pd.DataFrame:
    """
    Resets the DataFrame indices starting from 1.

    Args:
    - data: DataFrame containing the data.

    Returns:
    - DataFrame with indices reset starting from 1.
    """
    return data.reset_index(drop=True)

def select_random_routes(data: pd.DataFrame, fraction: float) -> pd.Series:
    """
    Randomly selects a fraction of unique routes from the DataFrame.

    Args:
    - data: DataFrame containing the data.
    - fraction: Fraction of unique routes to be selected (between 0 and 1).

    Returns:
    - Series containing the selected routes.
    """
    unique_routes = data['CODIGO_ROTA'].unique()
    return pd.Series(unique_routes).sample(frac=fraction, random_state=1)

def filter_data_by_routes(data: pd.DataFrame, routes: pd.Series) -> pd.DataFrame:
    """
    Filters the original DataFrame based on the selected routes.

    Args:
    - data: DataFrame containing the original data.
    - routes: Series containing the selected routes.

    Returns:
    - DataFrame containing the data filtered by the selected routes.
    """
    return data[data['CODIGO_ROTA'].isin(routes)]

def remove_columns(data: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Removes the specified columns from the DataFrame.

    Args:
    - data: DataFrame containing the data.
    - columns: List of column names to be removed.

    Returns:
    - DataFrame with the specified columns removed.
    """
    return data.drop(columns=columns)

def process_data(data: pd.DataFrame, fraction=0.001) -> pd.DataFrame:
    """
    Performs data processing, following a pipeline of operations.

    Args:
    - data: DataFrame containing the original data.
    - fraction: Fraction of unique routes to be selected (between 0 and 1).

    Returns:
    - DataFrame containing the processed data.
    """
    # Remove NaN
    data = remove_nan(data)
    
    # Remove duplicates
    data = remove_duplicates(data)
    
    # Select routes randomly
    selected_routes = select_random_routes(data, fraction)
    
    # Filter data by selected routes
    filtered_data = filter_data_by_routes(data, selected_routes)

    # Reset indices starting from 1
    filtered_data = reset_index(filtered_data)
    
    # Remove columns
    columns_to_remove = ['SEQUENCIA', 'LOGRADOURO', 'NUMERO', 'INDICE', 'CODIGO_ROTA']
    filtered_data = remove_columns(filtered_data, columns_to_remove)
    
    return filtered_data
