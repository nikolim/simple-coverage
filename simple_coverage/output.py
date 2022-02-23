import os
import json


file_name = "simple-coverage.json"
# get current interpreter dir
curr_working_dir = os.getcwd()
file_path = os.path.join(curr_working_dir, file_name)


def save_coverage_output(func_name, instructions_dict, called_instructions):
    """
    Save all instructions of a function and an array with the callend instruction
    to json file (simple-coverage.json).

    @param func_name: name of function
    @param instructions_dict: dict of instructions
    @param called_instructions: list of called instructions
    """

    # check if file exists
    if not os.path.isfile(file_path):
        # if not create a new json log file
        with open(file_path, "w") as file:
            json.dump(
                {
                    func_name: {
                        "instructions": instructions_dict,
                        "called_instructions": called_instructions,
                    }
                },
                file,
            )
    else:
        # if file exists append to existsing json log file
        with open(file_path, "r") as file:
            data = json.load(file)

        # check if function already exists
        if func_name in data:
            # append new called instructions to existing function
            for instruction in called_instructions: 
                if instruction not in data[func_name]["called_instructions"]:
                    data[func_name]["called_instructions"].append(instruction)
        else:
            # otherwise create new entry for new function
            data.update(
                {
                    func_name: {
                        "instructions": instructions_dict,
                        "called_instructions": called_instructions,
                    }
                }
            )
        with open(file_path, "w") as file:
            json.dump(data, file)
