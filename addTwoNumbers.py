# Function to add two numbers
def add_two_numbers(a, b):
    return a + b


def __main__():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")


if __name__ == "__main__":
    __main__()
