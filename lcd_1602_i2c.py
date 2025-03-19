from lcd_library import LCD
from time import sleep

lcd = LCD(2, 0x3f, True)

while True:
	lcd.message("Hello World!", 1)
	lcd.message("Have a nice day!", 2)
