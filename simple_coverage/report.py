from dis import Instruction
import os
import json

from simple_coverage.analyze import analyse_instructions


def create_report():
    """
    Create a report based on the simple-coverage.json file
    and print it to the console.
    """
    # load simple-coverage.json
    file_name = "simple-coverage.json"
    if os.path.isfile(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
    else:
        print("No coverage data found")
        return

    for key in data:
        print(f"Function: {key} \n")
        analyse_instructions(
            dict(data[key]["instructions"]), data[key]["called_instructions"]
        )
        print(f"\n")


if __name__ == "__main__":
    create_report()
