import csv
import random
import datetime

users = ['jainil#1', 'dima#2', 'bratva#3', 'ballu#4']
dataset_path = 'MonitorLog2025-03-28_22-44-33-860.csv'
log_path = 'accessLogs.txt'

def read_dataset():
    with open(dataset_path, mode='r', newline='') as file:
        reader = list(csv.DictReader(file))
    return reader

def simulate_access(dataset):
    user = random.choice(users)
    row = random.choice(dataset)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    access_info = {'timestamp of accesss': timestamp, 'user': user, 'data accessed by user': row}
    print(access_info)
    log_access(access_info)
    return access_info

def log_access(info):
    with open(log_path, mode='a') as logfile:
        logfile.write(f"{info['timestamp of accesss']} - {info['user']} accessed: {info['data accessed by user']}\n")

dataset = read_dataset()
for _ in range(5):
    access_info = simulate_access(dataset)
    print(access_info)