import z3

def process_program(program):
    print("wow, yep. That's a nice program.")

def main():
    program1 = """PV1(int y) {
                    x := -50;
                    while (x < 0) {
                        x := x + y;
                        y++
                    }
                    assert(y > 0)
                }"""

    process_program(program1)

if __name__ == '__main__':
    main()
