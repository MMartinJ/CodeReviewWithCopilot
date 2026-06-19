# Simple utility to add two numbers
def add_two_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: First addend.
        b: Second addend.

    Returns:
        The numeric sum of a and b.
    """
    return a + b


def get_number(prompt: str) -> float:
    """Prompt the user for a number and return it as a float.

    Keeps prompting until a valid number is entered.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main() -> None:
    """Entry point for the script: read two numbers, add them, and print the result."""
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")

    total = add_two_numbers(first_number, second_number)
    print(f"The sum of {first_number} and {second_number} is {total}")


if __name__ == "__main__":
    main()
