import unittest
import os
import json
from unittest.mock import patch
from app import app, tasks

class FlaskTestCase(unittest.TestCase):
    # Setup and teardown routines for the test case
    def setUp(self):
        # Initialize a test client for the application and enable testing mode.
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Reset the tasks dictionary after each test to avoid state leakage between tests.
        tasks.clear()

    # Testing successful task submissions using mock to simulate asynchronous operations
    @patch('app.async_simmulated_annealing')
    def test_submitsa_task_success(self, mock_async_simmulated_annealing):

        data = {'file': (open('./uploads/amostra_total.csv',
                         'rb'), 'amostra_total.csv')}
        response = self.app.post(
            '/submitsa', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 202)
        response_data = json.loads(response.data)
        self.assertIn('task_id', response_data)
        mock_async_simmulated_annealing.assert_called_once()

    @patch('app.async_two_opt')
    def test_submittwoopt_task_success(self, mock_async_two_opt):
        data = {'file': (open('./uploads/amostra_total.csv',
                         'rb'), 'amostra_total.csv')}
        response = self.app.post(
            '/submitto', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 202)
        response_data = json.loads(response.data)
        self.assertIn('task_id', response_data)
        mock_async_two_opt.assert_called_once()

    # Testing scenarios where no file is submitted
    def test_submitsa_task_no_file(self):
        # Test for error response when no file is submitted for simulated annealing.
        response = self.app.post('/submitsa', data={}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'Arquivo csv não informado / Formato inválido')

    def test_submittwoopt_task_no_file(self):
        # Similar test for two-opt optimization.
        response = self.app.post('/submitto', data={}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'Arquivo csv não informado / Formato inválido')

    # Testing task status retrieval
    def test_task_status_not_found(self):
        # Test retrieving status for a non-existent task ID; expect a 404 error.
        response = self.app.get('/status/non_existent_task_id')
        self.assertEqual(response.status_code, 404)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'Task not found')

    def test_task_status_queued(self):
        # Test retrieving status for an existing queued task; expect a 200 status and specific task status.
        task_id = 'test_task_id'
        tasks[task_id] = {'status': 'queued', 'result': None, 'error': None}
        response = self.app.get(f'/status/{task_id}')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['status'], 'queued')
        self.assertIsNone(response_data['error'])

    
    @patch('app.async_run_create_routes_for_cluster')
    def test_submittsp_task_success(self, mock_async_run_create_routes_for_cluster):
        data = {'file': (open('./uploads/amostra_total.csv', 'rb'), 'amostra_total.csv')}
        response = self.app.post(
            '/submittsp', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 202)
        response_data = json.loads(response.data)
        self.assertIn('task_id', response_data)
        mock_async_run_create_routes_for_cluster.assert_called_once()

    def test_submittsp_task_no_file(self):
        response = self.app.post('/submittsp', data={}, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'Arquivo CSV não informado / formato inválido')

if __name__ == '__main__':
    unittest.main()

