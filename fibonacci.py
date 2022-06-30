# fibonacci.py

def main():
    print(f"This program outputs the nth Fibonacci number.\n")
    n = eval(input("Enter n: "))

    n1, n2 = 1, 1

    if n == 1 or n == 2:
        fib_n = n1
    else:
        for i in range(n-2):
            n1, n2 = n2, n1 + n2
        fib_n = n2
    print(f"The {n} Fibonacci number is {fib_n}.")

main()
