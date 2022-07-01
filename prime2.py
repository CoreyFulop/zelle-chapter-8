# prime2.py
# Another attempt at exercise 5.

def main():
    print("This program determines if an integer n > 2 is prime.\n")

    # Ensure a valid input
    n = -1 # Illegal value so the loop below starts
    while (n <= 2) or (n%1 != 0):
        n = eval(input("Enter n > 2: "))

    prime = True
    i = 2
    while i <= n**0.5:
        if n%i == 0:
            prime = False
            break
        else: # i doesn't divide n without a remainder
            i += 1
    
    if prime == False:
        print(f"{n} is not a prime number as it is divisible by {i}.")
    else: # n is a prime number
        print(f"{n} is a prime number.")

main()