# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: November 2022
# ICS3U-Unit4-01.py File,
# learning while statement in python.


def main():

    # input and variables
    input_number = input("Input a number to add all the whole numbers up to it: ")
    counter = 0
    answer = 0

    # process and output
    print("")
    try:
        input_number_asint = int(input_number)
        while counter < input_number_asint:
            counter += 1
            answer += counter
            print("{0:,}".format(counter), end="")
            if counter < input_number_asint:
                print(" + ", end="")
        print(" = {0:,}".format(answer))
    except ValueError:
        print("Invalid input, Please try again following the requirements.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
