# syracuse_sequence.py

def syracuse(x):
    if x%2 == 0:
        return int(x/2)
    else: # x is odd
        return int(3*x + 1)

def main():
    print("This program prints the Syracuse (aka Collatz, Hailstone) sequence for", end = " ")
    print("a given natural number, n.\n")

    n = eval(input("Enter n: "))

    print(f"\nThe Syrancuse sequence starting with {n} is: {n}", end = "")
    if n != 1:
        print(",", end = "")

    while n != 1:
        n = syracuse(n)
        print(f" {n}", end = "")
        if n != 1:
            print(",", end = "")
    
    print(".")

if __name__ == "__main__":
    main()
