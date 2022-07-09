# cooling_heating_days_list.py

def main():
    print("This program determines the toal number of cooling and heating degree-days.\n")

    cooling = 0
    heating = 0

    infile_name = input("Enter the data file name: ")
    infile = open(infile_name, "r")

    line = infile.readline()
    while line != "":
        x = eval(line)
        if x > 80:
            heating += (x - 80)
        elif x < 60:
            cooling += (60 - x)
        line = infile.readline()

    print(f"\nCooling degree-days: {cooling}, heating degree-days: {heating}.")
    
main()
