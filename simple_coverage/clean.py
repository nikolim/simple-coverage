import os

file_name = "simple-coverage.json"


def clean():
    """
    Delete coverage if it exists. To this if you want to reset the coverage.
    or the json file is corrupted.
    """
    # check if simple-coverage.json exists
    if os.path.isfile(file_name):
        # delete file
        os.remove(file_name)


if __name__ == "__main__":
    clean()
