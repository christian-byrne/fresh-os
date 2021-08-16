
from pynput.keyboard import Key, Controller
import webbrowser
keyboard = Controller()

# SPECIAL KEYS = https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
# CUSTOM CHROME HOTKEYS = chrome://extensions/shortcuts
#                         Merge Windows Hotkey = Alt + Shift + Z
# MERGE ALL CHROME WINDOWS CRX = https://singleclickapps.com/merge-windows/


def init_browser(url):
    # import webbrowser
    webbrowser.open(url)


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
    default = "https://google.com"
    import time
    # from pynput.keyboard import Key, Controller
    # keyboard = Controller()
    init_browser(default)
    time.sleep(.5)

    ctrl_letter("l")
    time.sleep(.3)
    keypress_string("chrome://history/syncedTabs")
    time.sleep(.3)
    press_enter()

    # getting to the "open all" dropdown button
    # tab tab up enter down enter
    time.sleep(.3)
    ctrl_letter("l")
    time.sleep(.35)
    press_tab()
    time.sleep(.3)
    press_tab()
    time.sleep(.3)
    press_tab()
    time.sleep(.3)
    press_arrow_keys(["up"])
    time.sleep(.3)
    press_enter()
    time.sleep(.3)
    press_arrow_keys(["down"])
    time.sleep(.3)
    press_enter()
    time.sleep(.35)

    # Merge Windows CRX Hotkey
    keyboard.press(Key.alt)
    keyboard.press(Key.shift)
    keyboard.press("z")
    keyboard.release(Key.alt)
    keyboard.release(Key.shift)
    keyboard.release("z")

if __name__ == "__main__":
    main()