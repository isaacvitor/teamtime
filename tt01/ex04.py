"""Sub generator"""
from collections import namedtuple


Result = namedtuple('Result', 'count average')
data = {
    'Girls;Kg':
    [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'Girls;m':
    [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'Boys;Kg':
    [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'Boys;m':
    [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

# Report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print(f'Count:{result.count}, Group:{group}, AVG:{result.average:.2f} {unit}')


# Subgenerator
def average():
    total = 0.0
    count = 0
    avg = None
    while True:
        in_value = yield
        if in_value is None:
            break
        total += in_value
        count += 1
        avg = total/count
    return Result(count, avg)

# Delegating generator
def grouper(results, key):
    while True:
        results[key] = yield from average()

# Caller
def caller(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group) 
        for value in values:
            group.send(value)
        group.send(None)
    #print(results)
    report(results)


#Flow: Caller -> Delegating Generator <- "bi-directional" -> Subgenerator
caller(data)
