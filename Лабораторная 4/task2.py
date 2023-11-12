# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    jsonArray = []
    with open(INPUT_FILENAME) as file:
        data = csv.DictReader(file)
        for row in data:
            jsonArray.append(row)

    with open(OUTPUT_FILENAME, "w") as file:
        jsonString = json.dumps(jsonArray, indent=4)
        file.write(jsonString)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
