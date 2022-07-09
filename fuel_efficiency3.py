# fuel_efficiency3.py

def main():
    print("This program determines the fuel efficiency for a multi-stage journey.\n")

    starting_odom = eval(input("Enter the odometer reading before starting the journey: "))

    initial_odom = starting_odom
    total_gals_used = 0
    mpg_list = []

    i = 1

    infile_name = input("Enter the input file name: ")
    infile = open(infile_name, "r")

    line = infile.readline()
    while line != "":

        line_list = line.split()

        odom = eval(line_list[0])
        gals = eval(line_list[1])

        leg_distance = odom - initial_odom
        leg_mpg = round(leg_distance/gals, 2)

        total_gals_used += gals
        mpg_list.append(leg_mpg)

        i += 1
        
        line = infile.readline()

        initial_odom = odom
        

    print()

    if bool(mpg_list) == False:
        print("There is no journey to analyse!")
    else:
        j = 1
        for mpg in mpg_list:
            print(f"Leg {j}: {mpg} mpg.")
            j += 1
        print(f"Total journey: {round((odom - starting_odom)/total_gals_used, 2)} mpg")

if __name__ == "__main__":
    main()
