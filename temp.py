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
        variables.append(terms[idx - 1][:len(terms[idx-1]) -1])
        terms = terms[idx + 1:]
        try:
            idx = terms.index("int")
        except ValueError:
            return variables

lines = ["this is a line", 
        "This line has x: int and y: int and josh: int",
        "This line does not."]

print(get_variables(lines))
