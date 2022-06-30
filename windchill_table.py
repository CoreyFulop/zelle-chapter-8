# windchill_table.py

def print_windchill(t, v):
    windchill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    print(f"{windchill:>6.2f}", end = " ")

temperatures = list(range(-20, 70, 10)) # Fahrenheit
wind_speeds = list(range(0, 55, 5)) # mph

def main():
    print(" T \ V ", end = "")
    for wind_speed in wind_speeds:
        print(f"{wind_speed:^6}", end = " ")
    print()
    for temp in temperatures:
        print(f"{temp:>3}", end = " | ")
        for wind_speed in wind_speeds:
            print_windchill(temp, wind_speed)
        print()

if __name__ == "__main__":
    main()
