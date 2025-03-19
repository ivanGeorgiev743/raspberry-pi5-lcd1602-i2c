# Initializing the lcd_library and sleep function from the time library.
from lcd_library import LCD
from time import sleep

# Creating the lcd object using the LCD class from the lcd_library.
lcd = LCD(2, 0x3f, True)

# Creating while loop that stores the messages for the lcd. It secures us that the lcd will always work and prevents it to stop.
while True:
	# The lcd messages.
	lcd.message("Hello World!", 1)
	lcd.message("Have a nice day!", 2)
