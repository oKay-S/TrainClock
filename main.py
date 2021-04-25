from clock import Clock  # imports the clock class
from station import Station  # imports the station class
import lcddriver
import time

lcd= lcddriver.lcd()
lcd.lcd_clear
display = lcddriver.lcd()
program = 0 #sets program to 0 for infinite loop creation

display = lcddriver.lcd()


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
            checktime = Clock.date() + " " + Clock.time()
            lcd.lcd_display_string(checktime, 1)
            num_cols = 20
            num_line = 2
            ntrain = Station.updateTrains()
            display.lcd_display_string(ntrain[:num_cols], num_line)
            time.sleep(1)
            for i in range(len(ntrain) - num_cols + 1):
                text = ntrain
                text_to_print = text[i:i + num_cols]
                display.lcd_display_string(text_to_print, num_line)
                time.sleep(0.1)

main()  # calls the main method