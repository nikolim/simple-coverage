import os
import json


file_name = "simple-coverage.json"
# get current interpreter dir
curr_working_dir = os.getcwd()
file_path = os.path.join(curr_working_dir, file_name)


def save_coverage_output(func_name, instructions_dict, called_instructions):

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
            # append called instructions to existing function
            data[func_name]["called_instructions"].extend(called_instructions)
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
