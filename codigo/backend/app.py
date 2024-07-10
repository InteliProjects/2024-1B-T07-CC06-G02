import logging
import threading
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
from tasks import async_simmulated_annealing, async_two_opt, async_run_create_routes_for_cluster, tasks
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

# Set basic configuration for logging, with the debug level set to DEBUG.
logging.basicConfig(level=logging.DEBUG)

@app.route('/submitsa', methods=['POST'])
def submitsa_task():
    """
    Endpoint for submitting a task for simulated annealing.

    This endpoint expects a POST request with a file parameter containing a CSV file.
    The file is saved in the 'uploads' directory with a unique filename.
    A task ID is generated and associated with the task.
    The task is added to the 'tasks' dictionary with an initial status of 'queued' and no result or error.
    A new thread is started to execute the 'async_simmulated_annealing' function with the task ID and file path as arguments.
    The function returns a JSON response with the task ID and a status code of 202 (Accepted) if successful.
    If an error occurs during the submission process, an error message is returned with a status code of 400 (Bad Request) or 500 (Internal Server Error).

    Returns:
        A JSON response containing the task ID and a status code.

    Raises:
        None
    """
    try:
        file = request.files['file']
        if not file or not file.filename.endswith('.csv'):
            return jsonify({'error': 'Arquivo csv não informado / Formato inválido'}), 400

        task_id = str(uuid.uuid4())
        file_path = f'uploads/{file.filename}'
        os.makedirs('uploads', exist_ok=True)
        file.save(file_path)
        tasks[task_id] = {'status': 'queued', 'result': None, 'error': None}

        read_time = int(request.args.get('read_time', 2))
        speed = int(request.args.get('speed', 5))
        max_duration = int(request.args.get('max_duration', 360))

        threading.Thread(target=async_simmulated_annealing, args=(task_id, file_path, read_time, speed, max_duration)).start()

        return jsonify({'task_id': task_id}), 202
    except Exception as e:
        logging.error(f"Error submitting task: {e}")
        return jsonify({'error': 'Unexpected error'}), 500



@app.route('/submitto', methods=['POST'])
def submittwoopt_task():
    """
    Endpoint for submitting a task for two-opt optimization.
    """
    try:
        file = request.files['file']
        if not file or not file.filename.endswith('.csv'):
            return jsonify({'error': 'Arquivo csv não informado / Formato inválido'}), 400

        task_id = str(uuid.uuid4())
        file_path = f'uploads/{file.filename}'
        os.makedirs('uploads', exist_ok=True)
        file.save(file_path)
        tasks[task_id] = {'status': 'queued', 'result': None, 'error': None}

        read_time = int(request.args.get('read_time', 2))
        speed = int(request.args.get('speed', 5))
        max_duration = int(request.args.get('max_duration', 360))

        threading.Thread(target=async_two_opt, args=(task_id, file_path, read_time, speed, max_duration)).start()

        return jsonify({'task_id': task_id}), 202
    except Exception as e:
        logging.error(f"Error submitting task: {e}")
        return jsonify({'error': 'Unexpected error'}), 500

    

@app.route('/submittsp', methods=['POST'])
def submit_tsp_task():
    """
    Endpoint for submitting a task for Traveling Salesman Problem (TSP) using NetworkX.
    This endpoint expects a POST request with a file parameter containing a CSV file.
    The file is saved in the 'results' directory with a unique filename.
    A task ID is generated and associated with the task.
    The task is added to the 'tasks' dictionary with an initial status of 'queued' and no result or error.
    A new thread is started to execute the 'async_run_create_routes_for_cluster' function with the task ID and file path as arguments.
    The function returns a JSON response with the task ID and a status code of 202 (Accepted) if successful.
    If an error occurs during the submission process, an error message is returned with a status code of 400 (Bad Request) or 500 (Internal Server Error).
    """
    try:
        file = request.files.get('file')  # Use .get for better error handling
        if not file or not file.filename.endswith('.csv'):
            return jsonify({'error': 'Arquivo CSV não informado ou formato inválido'}), 400

        task_id = str(uuid.uuid4())
        file_path = os.path.join('results', f'{task_id}_{file.filename}')
        os.makedirs('results', exist_ok=True)
        file.save(file_path)
        
        tasks[task_id] = {'status': 'queued', 'result': None, 'error': None}

        read_time = int(request.args.get('read_time', 2))
        speed = int(request.args.get('speed', 5))
        max_duration = int(request.args.get('max_duration', 360))

        thread = threading.Thread(target=async_run_create_routes_for_cluster, args=(task_id, file_path, read_time, speed, max_duration))
        thread.start()

        return jsonify({'task_id': task_id}), 202
    except Exception as e:
        logging.error(f"Erro ao submeter a tarefa: {e}")
        return jsonify({'error': 'Erro inesperado'}), 500

@app.route('/status/<task_id>', methods=['GET'])
def task_status(task_id):
    """
    Get the status of a task.

    Parameters:
    - task_id (str): The ID of the task.

    Returns:
    - JSON response containing the status, error (if any), and result (if completed) of the task.
    """
    task = tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    response = {
        'status': task['status'],
        'error': task.get('error')
    }

    if task['status'] == 'completed':
        try:
            result_path = task['result']
            points_df = pd.read_csv(result_path)
            # Converter todo o DataFrame para dicionário
            response['result'] = points_df.to_dict(orient='records')
        except Exception as e:
            response['status'] = 'failed'
            response['error'] = str(e)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
