from gpio_lcd import GpioLcd
from machine import Pin
from time import sleep

# GpioLcd klassen instantieres
lcd = GpioLcd(rs_pin=Pin(27),
    enable_pin=Pin(25),
    d4_pin=Pin(33),
    d5_pin=Pin(32),
    d6_pin=Pin(21),
    d7_pin=Pin(22),
    num_lines=4,
    num_columns=20,
    backlight_pin=Pin(23, Pin.OUT)
)

lcd.clear()  # metoden clear fjerner alle karakterer på display
lcd.move_to(1, 0)  # metoden move_to rykker markøren hen til 2. kolonne på 1. linje
lcd.putstr("LucAss 1")  # metoden putstr tager en streng som argument og viser på display

lcd.move_to(1, 1)  # metoden move_to rykker markøren hen til 2. kolonne på 2. linje
lcd.putstr("G 2")  # bemærk at det kun er ASCII karakterer som er direkte anvendelige

lcd.move_to(1, 2)
lcd.putstr("LINJE 3")  # hvis man vil anvende specialtegn skal man selv konstruere dem

lcd.move_to(1, 3)
lcd.putstr("LINJE 4")

lcd.move_to(0, 0)  # metoden move_to rykker markøren hen til 1. kolonne på 1. linje
lcd.blink_cursor_on()  # metoden blink_cursor_on() tænder blinkende markør