# fuel_efficiency2.py

def main():
    print("This program determines the fuel efficiency for a multi-stage journey.\n")

    starting_odom = eval(input("Enter the odometer reading before starting the journey: "))

    initial_odom = starting_odom
    total_gals_used = 0
    mpg_list = []

    i = 1

    xStr = input(f"\nFor leg {i}, enter a final odometer reading and amount of gas used (separated by a space, or <Enter> to quit): ")
    while xStr != "":

        xLis = xStr.split()

        odom = eval(xLis[0])
        gals = eval(xLis[1])

        leg_distance = odom - initial_odom
        leg_mpg = round(leg_distance/gals, 2)

        total_gals_used += gals
        mpg_list.append(leg_mpg)

        i += 1
        
        xStr = input(f"For leg {i}, enter a final odometer reading and amount of gas used (separated by a space, or <Enter> to quit): ")

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
