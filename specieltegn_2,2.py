from machine import Pin
from gpio_lcd import GpioLcd

lcd = GpioLcd(
    rs_pin=Pin(27),
    enable_pin=Pin(25),
    d4_pin=Pin(33),
    d5_pin=Pin(32),
    d6_pin=Pin(21),
    d7_pin=Pin(22),
    num_lines=4,
    num_columns=20
)

lcd.clear()  # ryd display for tegn

# hvis man vil lave sine egne tegn til displayet
# kan man gøre det fra linket og lave et bytearray til tegnet
# https://maxpromer.github.io/LCD-Character-Creator/
lcd_custom_char_degrees = bytearray([    0x0E,
  0x0A,
  0x0A,
  0x0A,
  0x0A,
  0x1F,
  0x15,
  0x1F])

lcd.putstr("du bare en")  # skriver streng til display
lcd.move_to(11, 0)  # rykker markør til den 15. kolonne på 1. linje

# 1. argument er plads i CGRAM hukommelse på LCD, man kan give integers 0-7
# de tilgås med chr(0) chr(7),
lcd.custom_char(0, lcd_custom_char_degrees)  # 2. argument er specialtegnet

# skriver angivet tegn til LCD på nuværende cursor plads og rykker 1 frem
lcd.putchar(chr(0))