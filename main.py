from clock import Clock  # imports the clock class
from station import Station  # imports the station class

program = 0  # sets program to 0 for infinite loop creation


# Main body of code

def main():  # constucts the main method
    now = 0
    print(Station.updateStation())  # prints the station suffix
    print(Clock.date())  # prints the time
    while program == 0:
        if now != Clock.time():
            now = Clock.time()
            print(Clock.time())
            print(Station.updateTrains())


main()  # calls the main method