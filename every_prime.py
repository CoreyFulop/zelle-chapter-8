# every_prime.py

def check_prime(x):
    prime = True
    i = 2
    while i <= x**0.5:
        if x%i == 0:
            prime = False
            break
        else: # i doesn't divide x without a remainder
            i += 1
    return prime

def main():
    print("This program determines the primes <= an integer n.\n")

    # Ensure a valid input
    n = -1 # Illegal value so the loop below starts
    while (n <= 2) or (n%1 != 0):
        n = eval(input("Enter n > 2: "))

    primes_list = []

    j = 2
    while j <= n:
        prime = check_prime(j)
        if prime == True:
            primes_list.append(j)
        j += 1

    print(f"The list of primes less than or equal to {n} is: {primes_list}.")

if __name__ == "__main__":
    main()
    