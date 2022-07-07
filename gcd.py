# gcd.py

def valid_input():
    """
    Requests and returns a positive integer.
    """
    x = -1 # Invalid input to start loop
    while x < 1 or x%1 != 0:
        x = eval(input("Enter a positive integer: "))
    return x

def main():
    print("This program implements Euclid's algorithm for", end = " ")
    print("finding the greatest common divisor of two positive integers.\n")

    # Get input
    m = valid_input()
    n = valid_input()

    # Save the original inputs
    x, y = m, n

    # Euclid's algorithm
    while m > 0:
        n, m = m, n%m

    print(f"\nThe greatest common divisor of {x} and {y} is {n}.")

if __name__ == "__main__":
    main()
