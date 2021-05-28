import json
import numpy as np

def read_counts(path):
    return np.asarray([int(line) for line in open(path).readlines()])

def read_data(path='json.json'):
    data = json.loads(open('json.json').read())
    for d in data:
        d['counts'] = read_counts(d['path'])
    return data
