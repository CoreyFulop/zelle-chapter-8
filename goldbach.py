# goldback.py

def check_prime(x):
    """
    Checks if x is a prime number.
    Returns a bool.
    """
    prime = True
    i = 2
    while i <= x**0.5:
        if x%i == 0:
            prime = False
            break
        else: # i doesn't divide without a remainder
            i += 1
    return prime

def populate_list(a_list, n):
    """
    Populates an empty list with prime numbers less than n.
    """
    j = 2
    while j < n:
        prime = check_prime(j)
        if prime == True:
            a_list.append(j)
        j += 1
    return a_list

def find_sum_terms(list1, list2, n):
    """
    Returns an element each from list1 and list2 than sum to n.
    """
    for x in list1:
        for y in list2:
            if x + y == n:
                return x, y

def main():
    print("This program implements the Goldbach conjecture.\n")

    # Ensure valid input
    n = -1 # Illegal value so loop implements
    while n <= 2 or n%2 != 0:
        n = eval(input("Enter an even n > 2: "))

    # Get list of primes less than n
    primes1 = []
    primes1 = populate_list(primes1, n)

    # Get another list of primes less than n
    primes2 = []
    primes2 = populate_list(primes2, n)

    # Find two primes less than n that sum to n
    p1, p2 = find_sum_terms(primes1, primes2, n)

    print(f"\n{p1} and {p2} sum to {n}.")
            
if __name__ == "__main__":
    main()
