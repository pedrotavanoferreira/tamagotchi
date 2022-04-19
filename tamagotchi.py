from microbit import *

steps = 0
while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(Image.HAPPY)
        sleep(2000)
        display.clear
    if button_a.is_pressed():
        if (steps > 9):
            display.scroll(str(steps))
            sleep(2000)
            display.clear()
        else:
            display.show(str(steps))
            sleep(2000)
            display.clear()