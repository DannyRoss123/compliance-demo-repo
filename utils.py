import requests
import pickle

def fetch_data(url):
    response = requests.get(url, verify=False)
    return response.json()

def load_config(path):
    with open(path, "rb") as f:
        return pickle.load(f)

def divide(a, b):
    return a / b
