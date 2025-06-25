class Main:
    def handle(self, input_str):
        """
        ***********************************************
        * This method parses each input and assigns it *
        * to different variables.                      *
        ***********************************************

        Format of input_str: "Input1 Input2 Input3"
        Example: "Input1 Input2 Input3"

        We split the string and retrieve the input data into input1, input2, input3.
        Once retrieved, it is available as string data for you to implement the solution.

        Main.handle() will be called in a loop for each input command.
        """

        input_list = input_str.strip().split(" ")
        input1 = input_list[0]
        input2 = input_list[1]
        input3 = input_list[2]

        # Start your implementation from here.
        print("Input1:", input1)
        print("Input2:", input2)
        print("Input3:", input3)
