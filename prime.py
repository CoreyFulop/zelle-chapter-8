# prime.py

import math

def main():
    print(f"This program determines if an integer n > 2 is a prime number.\n")

    # Recieve a valid input
    n = - 1 # Starting with an illegal value to get into the loop below
    while (n <= 2) or (n%1 != 0):
        n = eval(input("Enter an integer > 2: "))

    test_upper_limit = int(math.sqrt(n)//1) # Greatest integer <= sqrt(n)

    # Prime test begins
    divisor = False

    for i in range(2, test_upper_limit + 1):
        if n%i == 0:
            divisor = i
            print(f"{n} is not prime, as it is divisible by {divisor}.")
            break
    
    if divisor == False:
        print(f"{n} is a prime number.")
    # Prime test ends

main()
