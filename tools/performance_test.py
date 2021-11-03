"""Module for testing load performance of particular API with POST requests"""

import functools
import json
import time
from concurrent.futures import ThreadPoolExecutor as Pool

import requests

JSON_PATH = 'post.json'
NUM_OF_SIMULT_REQUESTS = 1000
URL = "http://127.0.0.1:8000/clients"


def time_it(num_requests, url, fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        stop = time.time()
        duration = stop - start
        print(f"{num_requests / duration:.0f} requests/sec | {num_requests} reqs | {url} | {fn.__name__}")
        return res

    return wrapper


def read_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data


def post(url):
    json_data = read_json(JSON_PATH)
    resp = requests.post(url, json=json_data)
    if not resp.status_code == 200:
        raise Exception(f'Bad status code : {resp.status_code}')
    return resp.json()


def thread_pool(url, n):
    data = read_json(JSON_PATH)
    with Pool() as pool:
        result = pool.map(post, [url] * n, [data] * n)
    return result


def run_bench(num_requests, func, url):
    time_it(num_requests, url, func)(url, num_requests)


if __name__ == "__main__":
    func = thread_pool
    run_bench(NUM_OF_SIMULT_REQUESTS, func, URL)
