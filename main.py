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
            lcd.lcd_clear()
            lcd.lcd_display_string(Clock.date(), 1)
            lcd.lcd_display_string(Clock.time(), 2)
            time.sleep(10)
            lcd.lcd_clear()
            num_cols = 16
            num_line = 2
            traininfo = Station.updateTrainsCalling()

            destinationtime = traininfo[0]
            platformstatus = traininfo[1]
            calling = traininfo[2]

            display.lcd_display_string(destinationtime[:num_cols], 1)
            display.lcd_display_string(platformstatus[:num_cols], 2)
            time.sleep(1)
            for i in range(len(destinationtime) - num_cols + 1):
                text = destinationtime
                text_to_print = text[i:i + num_cols]
                display.lcd_display_string(text_to_print, 1)
                time.sleep(0.1)
            time.sleep(5)
            display.lcd_display_string(destinationtime[:num_cols], 1)


            time.sleep(1)
            for i in range(len(platformstatus) - num_cols + 1):
                text = platformstatus
                text_to_print = text[i:i + num_cols]
                display.lcd_display_string(text_to_print, 2)
                time.sleep(0.1)
            time.sleep(5)

            display.lcd_display_string(calling[:num_cols], 2)
            time.sleep(1)
            for i in range(len(calling) - num_cols + 1):
                text = calling
                text_to_print = text[i:i + num_cols]
                display.lcd_display_string(text_to_print, 2)
                time.sleep(0.1)

            lcd.lcd_clear()
            display.lcd_display_string(destinationtime[:num_cols], 1)
            display.lcd_display_string(platformstatus[:num_cols], 2)
            time.sleep(1)
            for i in range(len(platformstatus) - num_cols + 1):
                text = platformstatus
                text_to_print = text[i:i + num_cols]
                time.sleep(0.1)
                display.lcd_display_string(text_to_print, 2)
            display.lcd_display_string(platformstatus[:num_cols], 2)
            time.sleep(10)

main()  # calls the main method