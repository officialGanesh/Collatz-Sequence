# import the required module
import pyinputplus as pyip

number = pyip.inputNum("Enter Your Number: ",greaterThan=0)


def collatz_sequence(number):
    """This function can print the collatz sequence."""
    while number != 1:
        try:
            if (number % 2 == 0):
                number = number // 2
                print(number)

            elif (number % 2 == 1):
                number = (3 * number) + 1
                print(number)
            else:
                return 1

        except Exception as e:
            print("Something went wrong 💢")

if __name__ == '__main__':

    collatz_sequence(number)
    print("Code Completed 🔥")