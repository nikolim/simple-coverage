import inspect
from sys import settrace
from termcolor import colored

# global array to save called instructions
called_instructions = []


def extract_instructions(func) -> dict:

    # extract source code from function
    source_lines = inspect.getsourcelines(func)

    # get number of comments (skip docstrings)
    number_comments = func.__code__.co_lnotab[1]

    # get line number of first instruction
    first_line_of_code = func.__code__.co_firstlineno + number_comments

    instructions = {}
    for i, line in enumerate(source_lines[0][number_comments:]):
        if (
            line  # ignore empty lines
            and line != "\n"  # ignore new lines
            and not line.replace(" ", "")
            .replace("\t", "")
            .startswith("#")  # ignore comments
        ):
            # write instruction with line number into dict
            instructions[first_line_of_code + i] = line.replace("\n", "")

    return instructions


def analyse_instructions(instruction_dict) -> None:
    called_counter = 0  # counter for called instructions
    branch_counter = 0  # counter for braches
    branch_visited = 0  # counter for visited branches
    prev_indention_level = 1  # assume first line is indented in function
    else_counter = 0  # counter for else statements
    indention_level = 1
    new_branch = False

    # iterate over instructions
    for key, line in instruction_dict.items():

        # check for branches with increased indention level
        level = line.count("    ") + line.count("\t")
        if level > prev_indention_level:
            indention_level += 1
            branch_counter += 1
            new_branch = True
        if level < prev_indention_level:
            indention_level -= 1

        # just print "else" instructions
        if line.replace(" ", "").replace("\t", "") == "else:":
            print(f"IGNORE line {key}: {instruction_dict[key]}")
            else_counter += 1
        else:
            if key in called_instructions:
                called_counter += 1
                if new_branch:
                    branch_visited += 1
                print(colored(f"CALLED line {key}: {instruction_dict[key]}", "green"))
            else:
                print(colored(f"MISSED line {key}: {instruction_dict[key]}", "red"))

        new_branch = False
        prev_indention_level = indention_level

    instruction_coverage = round(
        called_counter / (len(instruction_dict) - else_counter) * 100, 2
    )
    print(f"\nInstruction coverage: {instruction_coverage} %")

    if branch_counter > 0:
        branch_coverage = round(branch_visited / branch_counter * 100, 2)
        print(f"Branch coverage: {branch_coverage} %")

