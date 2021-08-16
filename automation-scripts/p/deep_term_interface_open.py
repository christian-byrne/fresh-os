
from pynput.keyboard import Key, Controller
keyboard = Controller()



def ctrl_letter(char):
    char = str(char)
    #from pynput.keyboard import Key
    keyboard.press(Key.ctrl)
    keyboard.press(char)
    keyboard.release(Key.ctrl)
    keyboard.release(char)


def press_enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def keypress_string(type_this):
    for character in type_this:
        keyboard.press(character)
        keyboard.release(character)


def press_tab():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)


def press_arrow_keys(list_arrows):
    for direction in list_arrows:
        keyboard.press(Key[direction])
        keyboard.release(Key[direction])


def exit_program():
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)


def main():
    import time
    import os


    # Full Screen
    time.sleep(.35)
    keyboard.press(Key.shift)
    time.sleep(.35)
    ctrl_letter("f")
    keyboard.release(Key.shift)

    # Split Horizontal
    time.sleep(.35)
    keyboard.press(Key.shift)
    time.sleep(.35)
    ctrl_letter("h")
    keyboard.release(Key.shift)

    # Split Vertical
    time.sleep(.35)
    keyboard.press(Key.shift)
    time.sleep(.35)
    ctrl_letter("j")
    keyboard.release(Key.shift)

    # Down one (from top right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("j")
    keyboard.release(Key.alt)
    keyboard.release("j")

    # Split Vertical
    time.sleep(.35)
    keyboard.press(Key.shift)
    time.sleep(.35)
    ctrl_letter("j")
    keyboard.release(Key.shift)


    # Right one (from bottom right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("l")
    keyboard.release(Key.alt)
    keyboard.release("l")

    # Split Vertical
    time.sleep(.35)
    keyboard.press(Key.shift)
    time.sleep(.35)
    ctrl_letter("j")
    keyboard.release(Key.shift)


    time.sleep(.5)
    keypress_string("pypractice")
    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    # Up one (from bottom right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("k")
    keyboard.release(Key.alt)
    keyboard.release("k")

    keypress_string("bpytop -b 'cpu net'")
    time.sleep(1)
    press_enter()
    time.sleep(1)

    # Left one (from bottom right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("h")
    keyboard.release(Key.alt)
    keyboard.release("h")

    time.sleep(1)
    keypress_string("htop --sort-key=STIME -t --delay=500")
    time.sleep(1)
    press_enter()
    time.sleep(1)


    # Down one (from bottom right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("j")
    keyboard.release(Key.alt)
    keyboard.release("j")

    time.sleep(.5)
    keypress_string("ls")
    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

if __name__ == "__main__":
    main()
