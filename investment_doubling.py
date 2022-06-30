# investment_doubling.py

def main():
    print("This program determines how long it takes for an investment to double", end = " ")
    print("at a given interest rate.\n")

    apr = eval(input("Enter the APR: "))

    balance = 1 # This variable can be changed if different inital investment required, 
                # without breaking the code.

    double_initial_investment = 2 * balance

    duration = 0
    while balance < double_initial_investment:
        balance = balance * (1 + apr)
        duration += 1
    print(f"\nWith an APR of {apr}, it will take {duration} years to double your initial investment.")

if __name__ == "__main__":
    main()