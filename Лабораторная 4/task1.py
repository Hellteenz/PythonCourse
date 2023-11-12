# TODO решите задачу
import json

def task() -> float:
    sum = 0
    filename = "input.json"
    score = "score"
    weight = "weight"
    with open(filename) as file:
        data = json.load(file)
    for pair in data:
        sum += pair[score] * pair[weight]
    return round(sum, 3)


print(task())