import z3
import sys


def process_program(input_file, output_file):
    lines = input_file.readlines()
    func_start = get_func_start(lines)
    func_end = get_func_end(lines, func_start)

    print("func_start: " + str(func_start))
    print("func_end: " + str(func_end) + "\n")

    lines = lines[func_start:func_end + 1]
    # parse for variables
    variables = get_variables(lines)
    print("variables: " + str(variables))

    # TODO - form constraints with variables
    if len(variables) == 0:
        print("0 vars")
    if len(variables) == 1:
        print("1 vars")
    elif len(variables) == 2:
        print("2 vars")
    else:
        print("Sorry, you exceeded our generous max of 2 variables")
        exit(1)


def get_func_start(lines):
    func_start = 0
    for line in lines:
        if len(line) < 3 or line[:3] != 'def':
            func_start += 1
            continue
        else:
            return func_start
    raise EOFError()


def get_func_end(lines, func_start):
    func_end = func_start
    for line in lines[func_start + 1:]:
        if not line.startswith(" "):
            print("end of function")
            break
        func_end += 1
    return func_end


def get_variables(lines):
    variables = []
    for line in lines:
        variables += _get_line_variables(line)
    return variables


def _get_line_variables(line):
    variables = []

    terms = line.split()
    print(terms)
    idx = -1

    try:
        idx = terms.index("int")
    except ValueError:
        return variables
    while True:
        variables.append(terms[idx - 1][:len(terms[idx - 1]) - 1])
        terms = terms[idx + 1:]
        try:
            idx = terms.index("int")
        except ValueError:
            return variables


def close_files(input_file, output_file):
    input_file.close()
    output_file.close()


def main(argv):
    ifilename = ''
    ofilename = 'out.txt'
    if len(argv) < 1:
        print("Usage: please include a python input file")
        exit(1)

    ifilename = argv[0]
    input_file = open(ifilename, "r")
    output_file = open(ofilename, "w")

    process_program(input_file, output_file)

    close_files(input_file, output_file)


if __name__ == '__main__':
    main(sys.argv[1:])
