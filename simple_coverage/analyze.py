from termcolor import colored


def analyse_instructions(instruction_dict, called_instructions) -> None:
    """
    Analyse the instructions and print the coverage to console.

    @param instruction_dict: dict of instructions
    @param called_instructions: list of called instructions
    """
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
        if line.replace(" ", "").replace("\t", "") in ["else:", "except:"]:
            print(f"IGNORE line {key}: {instruction_dict[key]}")
            else_counter += 1
        else:
            if int(key) in called_instructions:
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
