import os

file_name = "simple-coverage.json"

def clean():
	# check if simple-coverage.json exists
	if os.path.isfile(file_name):
		# delete file
		os.remove(file_name)


if __name__ == "__main__":
	clean()