# cooling_heating_days.py

def main():
    print("This program determines the number of cooling and heating degree-days.\n")

    cooling = 0
    heating = 0

    xStr = input("Enter an average daily temperature (<Enter> to quit): ")
    while xStr != "":
        x = eval(xStr)
        if x > 80:
            heating += (x - 80)
        elif x < 60:
            cooling += (60 - x)
        xStr = input("Enter an average daily temperature (<Enter> to quit): ")

    print(f"\nCooling degree-days: {cooling}, heating degree-days: {heating}.")

main()
