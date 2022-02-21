from sys import gettrace, settrace
from termcolor import colored
from functools import wraps
from inspect import getsourcelines

from simple_coverage.analyze import analyse_instructions
from simple_coverage.output import save_coverage_output

# global array to save called instructions
called_instructions = []


def tracer(frame, event, arg=None) -> None:
    # callback for settrace which records the called instructions in global array
    line_number = frame.f_lineno
    if line_number not in called_instructions:
        called_instructions.append(frame.f_lineno)
    return tracer


def extract_instructions(func) -> dict:
    # extract source code from function
    source_lines = getsourcelines(func)
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


# coverage decorator which writes coverage to file
def log_coverage(func):
    def inner_func_log(*args, **kwargs):
        global called_instructions
        # extract source code from function
        instruction_dict = extract_instructions(func)
        prev_tracer = gettrace()
        # setup systrace
        settrace(tracer)
        # call function below decorator
        results = func(*args, **kwargs)
        # reset tracer
        settrace(prev_tracer)
        # write coverage to file
        save_coverage_output(
            func_name=func.__name__,
            instructions_dict=instruction_dict,
            called_instructions=called_instructions,
        )
        called_instructions = []
        return results

    return inner_func_log


# coverage decorator which prints coverage to console
def print_coverage(func):
    def inner_func_print(*args, **kwargs):
        global called_instructions
        # extract source code from function
        instruction_dict = extract_instructions(func)
        # previous tracer
        prev_tracer = gettrace()
        # setup systrace
        settrace(tracer)
        # call function below decorator
        results = func(*args, **kwargs)
        # reset tracer
        settrace(prev_tracer)
        # print coverage to console
        print(f"Function: {func.__name__}{args} \n")
        analyse_instructions(instruction_dict, called_instructions)
        # reset global var after finishing with one function
        called_instructions = []
        return results

    return inner_func_print


# meta decotest decorator
def doctest_wrapper(decorator):
    def wrapper(func):
        return wraps(func)(decorator(func))

    return wrapper
