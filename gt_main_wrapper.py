import sys
from main import Main


def call_main():
    """
        ***********************************************
        * This is the driver code. Don't change it!!!
        * *********************************************

        Format of the 'args' array: `<Input 1> <Input 2> <Input 3>`
        Example: ["Input1 Input2 Input3"]

        The code evaluator will execute this code by using the command:
        python main.py "Input1 Input2 Input3"

        So the value of the variable 'input' given below will be the string: "Input1 Input2 Input3"
    """
    if len(sys.argv) < 2:
        raise ValueError("No command line arguments passed")

    commands = sys.argv[1:]
    main = Main()

    for command in commands:
        main.handle(command)


if __name__ == "__main__":
    call_main()
