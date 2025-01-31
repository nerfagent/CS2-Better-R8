import time
import keyboard
from pynput.mouse import Button, Controller

def main(holding_time,release_time,button_on,button_off):
    mouse = Controller()
    R8 = False
    time.sleep(3) # CONSTANT_DELAY
    while True:
        # print("OFF")
        while R8:
            # print("ON")
            mouse.press(Button.left)
            time.sleep(holding_time)

            if keyboard.is_pressed(button_on):
                mouse.release(Button.left)
                time.sleep(release_time)

            if keyboard.is_pressed(button_off):
                R8 = False

        time.sleep(0.1) # CONSTANT_DELAY
        if keyboard.is_pressed(button_on):
            R8 = True


if __name__ == "__main__":
    # You may modify these variables if you wanna use this program in other games. For example, you can use this for Charge Rifle in Apex Legends.
    holding_time = 0.19
    release_time = 0.01
    button_on = 'o'
    button_off = 'p'
    main(holding_time,release_time,button_on,button_off)
