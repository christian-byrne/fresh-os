import os, argparse, random, webbrowser, time, subprocess
from pynput.keyboard import Key, Controller
keyboard = Controller()

# Template to call process without logging and disown from shell
nohup = "nohup >/dev/null {} & disown"


# ────────────────────────────────────────────────────────────────────────────────
# ─── TERMINAL CLI APPS ──────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


def left_term_panel():
    # Up one (from bot left)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("k")
    keyboard.release(Key.alt)
    keyboard.release("k")

    keypress_string("cointop --only-table --colorscheme mars")
    time.sleep(.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # Pan Right
    time.sleep(.5)
    keyboard.press(Key.shift)
    for _ in range(12):
        keyboard.press(".")
        keyboard.release(".")
        time.sleep(.01)
    keyboard.release(Key.shift)

    time.sleep(.5)
    for _ in range(31):
        keyboard.press(Key.f3)
        keyboard.release(Key.f3)
        time.sleep(.01)

    # Zoom Out
    time.sleep(.2)
    keyboard.press(Key.ctrl)
    for _ in range(3):
        keyboard.press("-")
        keyboard.release("-")
    keyboard.release(Key.ctrl)


def new_cointop(theme, screensize="normal"):
    os.system(
        nohup.format(
            "deepin-terminal -m " + screensize + " -l '" + theme + "' -e cointop"
        )
    )


def bottom_bar_term(theme, coin1, coin2, coin3, right=False, custom_coin_theme=False):
    switch_deepin_configs()
    time.sleep(.25)
    os.system("nohup >/dev/null deepin-terminal -m fullscreen -l '" + theme + "' &")
    os.system("disown")

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
    time.sleep(.5)
    if not custom_coin_theme:
        keypress_string("cointop --only-table --colorscheme 'homebrew'")
    else:
        keypress_string("cointop --only-table --colorscheme '" + custom_coin_theme + "'")
    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(.9)
    keyboard.press("p")
    keyboard.release("p")
    keyboard.press("p")
    keyboard.release("p")

    # Pan Right
    time.sleep(.5)
    keyboard.press(Key.shift)
    for _ in range(12):
        keyboard.press(".")
        keyboard.release(".")
        time.sleep(.01)
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
    if not custom_coin_theme:
        keypress_string("cointop --only-table --colorscheme 'homebrew'")
    else:
        keypress_string("cointop --only-table --colorscheme '" + custom_coin_theme + "'")
    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(.8)
    keyboard.press("2")
    keyboard.release("2")

    # Pan Right
    time.sleep(.5)
    keyboard.press(Key.shift)
    for _ in range(12):
        keyboard.press(".")
        keyboard.release(".")
        time.sleep(.01)
    keyboard.release(Key.shift)

    # Up one (from bottom right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("k")
    keyboard.release(Key.alt)
    keyboard.release("k")


    # Left one
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("h")
    keyboard.release(Key.alt)
    keyboard.release("h")

    # Down one
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("j")
    keyboard.release(Key.alt)
    keyboard.release("j")

    time.sleep(.5)
    keypress_string("cointop --hide-statusbar --hide-marketbar --colorscheme 'homebrew'")
    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


    time.sleep(.4)
    keyboard.press(Key.shift)
    keyboard.press("f")
    keyboard.release(Key.shift)
    keyboard.release("f")

    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(.15)

    # Decrease Graph Size in Main Term Window
    keyboard.press(Key.ctrl)
    for _ in range(4):
        keyboard.press("k")
        keyboard.release("k")
        time.sleep(.01)
    keyboard.release(Key.ctrl)
    time.sleep(.05)

    for _ in range(17):
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        time.sleep(.01)


def terminal_gui(theme, coin1, coin2, coin3, right=False, custom_coin_theme=False):
    switch_deepin_configs()
    time.sleep(.3)
    os.system("nohup >/dev/null deepin-terminal -m fullscreen -l '" + theme + "' &")
    os.system("disown")

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
    time.sleep(.5)
    if not custom_coin_theme:
        keypress_string("cointop --only-table --colorscheme 'synthwave'")
    else:
        keypress_string("cointop --only-table --colorscheme '" + custom_coin_theme + "'")
    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(.9)
    keyboard.press("p")
    keyboard.release("p")
    keyboard.press("p")
    keyboard.release("p")

    # Pan Right
    time.sleep(.5)
    keyboard.press(Key.shift)
    for _ in range(12):
        keyboard.press(".")
        keyboard.release(".")
        time.sleep(.01)
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

    if not custom_coin_theme:
        keypress_string("cointop --only-table")
    else:
        keypress_string("cointop --only-table --colorscheme '" + custom_coin_theme + "'")

    time.sleep(.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(.8)
    keyboard.press("2")
    keyboard.release("2")

    # Pan Right
    time.sleep(.5)
    keyboard.press(Key.shift)
    for _ in range(12):
        keyboard.press(".")
        keyboard.release(".")
        time.sleep(.01)
    keyboard.release(Key.shift)

    # Up one (from bottom right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("k")
    keyboard.release(Key.alt)
    keyboard.release("k")

    if not right:
        keypress_string("clear; coinmon")
        time.sleep(.4)
        press_enter()
        time.sleep(.7)
        keyboard.press(Key.ctrl)
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        keyboard.release(Key.ctrl)
        time.sleep(.2)
    else:
        time.sleep(.5)
        keypress_string("cointop --hide-statusbar --hide-marketbar --colorscheme 'homebrew'")
        time.sleep(.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(.4)
        keyboard.press(Key.shift)
        keyboard.press("f")
        keyboard.release(Key.shift)
        keyboard.release("f")
        time.sleep(.2)

    # Left one (from bottom right)
    time.sleep(.35)
    keyboard.press(Key.alt)
    time.sleep(.35)
    keyboard.press("h")
    keyboard.release(Key.alt)
    keyboard.release("h")

    time.sleep(1)
    keypress_string("cointop --only-chart --colorscheme 'system'")
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

    if right:
        keypress_string("clear; coinmon")
        time.sleep(.4)
        press_enter()
        time.sleep(.7)
        keyboard.press(Key.ctrl)
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        
        keyboard.press("=")
        keyboard.release("=")
        time.sleep(.05)
        
        keyboard.release(Key.ctrl)
        time.sleep(.2)
    else:
        time.sleep(.5)
        keypress_string("cointop --hide-statusbar --hide-marketbar --colorscheme 'homebrew'")
        time.sleep(.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(.4)
        keyboard.press(Key.shift)
        keyboard.press("f")
        keyboard.release(Key.shift)
        keyboard.release("f")
        time.sleep(.2)

    # Decrease Graph Size in Main Term Window
    keyboard.press(Key.ctrl)
    for _ in range(4):
        keyboard.press("k")
        keyboard.release("k")
        time.sleep(.01)
    keyboard.release(Key.ctrl)
    time.sleep(.05)

    for _ in range(8):
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        time.sleep(.01)


# ────────────────────────────────────────────────────────────────────────────────
# ─── KRAKEN BROWSER TERMINAL ────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


# ───────────────────────────────────────────────── CHROMIUM WITHOUT BORDERS ─────
# --app=URL: Runs URL in "app mode": with no browser toolbars.
# For example: 'chromium-browser --app=/path/to/my-file.html'
# else (normal chromium with borders, address bar, etc.):
# URL is simply a positional argument


def format_kraken_URL(coin, reference_currency, period):
    """
    Format a Kraken terminal URL based on a reference currency compared
    against a COIN.
    """
    url = "https://trade.kraken.com/charts/KRAKEN:" + coin + "-" + reference_currency + "?period=" + period
    return url


def kraken(browser, direction="up", coin="DOGE", reference_currency="BTC", dimensions="960,600", period="1d"):
    """
    Open URL (with specified browser software) in either fullscreen, 
    half the screen (split vertically), or at custom dimensions
    __Params__
    browser:  
            chromium = the chromium browser emulator (can create custom
                       user profiles and crx files)
            chrome   = chrome with standard user settings
            firefox  = firefox software
            selenium = the selenium automation emulator
    direction: 
            left/right = browser will take up left/right half of 
                         the screen
            up         = browser goes fullscreen
            down       = the default size that the software was last used at
            h          = hide/minimize the window after opening
            custom     = use the dimensions param to determine the size
                         and don't maximize to half/full screen
    coin: 
            The abbreviation of the coin analyzed in the terminal.
            Should be all caps (e.g., BTC).
    dimensions:
            The dimenisions of the browser window. overidden if
            direction is left/right/full. Format is height,width.
    period:
            The domain of the graph displayed in the terminal.
            1m, 3m, 5m, 15m, 30m       = minute periods
            1h, 2h, 4h, 6h, 12h        = hour periods
            1d, 3d                     = day periods
            1w, 1w_Monday, 1w_Thursday = week periods
    """

    url = format_kraken_URL(coin, reference_currency, period)

    if browser == "chromium":
        os.system(
            nohup.format(
                "chromium-browser --new-window --window-size=" + dimensions + " --app=" + url
            )
        )
    
    elif browser == "chrome":
        # second param of open: 1 = new window
        webbrowser.open(
            url, 
            1
        )

    if direction != "custom":
        time.sleep(1)
        keyboard.press(Key.cmd)
        if direction == "h":
            keyboard.press("h")
            keyboard.release("h")
        else:
            keyboard.press(Key[direction])
            keyboard.release(Key[direction])
        keyboard.release(Key.cmd)


# ────────────────────────────────────────────────────────────────────────────────
# ─── TERMINAL CLI APPS ──────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


def cryptowatch(direction):
    """
    direction: 
            vertical   = browser will take up left/right half of 
                         the screen
            horizontal = the default size that the software was last used at
            minimize   = hide/minimize the window after opening
            fullscreen = fullscreen
            4          = open 4 windows
            right      = only 1 window, taking right half of screen
            left       = only 1 window, taking left half of screen
    """

    os.system(
        nohup.format(
            "cryptowatch"
        )
    )
    
    time.sleep(1)

    if direction == "vertical":
        time.sleep(1)
        keyboard.press(Key.cmd)
        keyboard.press(Key["right"])
        keyboard.release(Key["right"])
        keyboard.release(Key.cmd)
        time.sleep(.25)
        os.system(
            nohup.format(
                "cryptowatch"
            )
        )
        time.sleep(.5)
        keyboard.press(Key.cmd)
        keyboard.press(Key["left"])
        keyboard.release(Key["left"])
        keyboard.release(Key.cmd)

    elif direction == "horiztonal" or direction == "4":
        keyboard.press(Key.cmd)
        keyboard.press(Key["down"])
        keyboard.release(Key["down"])
        keyboard.release(Key.cmd)
        iterations = 1 if direction == "horiztonal" else 3
        for _ in range(iterations):
            time.sleep(1.5)
            os.system(
                nohup.format(
                    "cryptowatch"
                )
            )

    elif direction == "minimize":
        keyboard.press(Key.cmd)
        keyboard.press("h")
        keyboard.release("h")

    elif direction == "fullscreen":
        keyboard.press(Key.f11)
        keyboard.release(Key.f11)
        
    # Directional
    else:
        keyboard.press(Key.cmd)
        keyboard.press(Key[direction])
        keyboard.release(Key[direction])
        keyboard.release(Key.cmd)


# ────────────────────────────────────────────────────────────────────────────────
# ─── SEND KEYS HELPERS ──────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


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



# ────────────────────────────────────────────────────────────────────────────────
# ─── THEMES ─────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


def get_deepin_theme(choice):
    schemes = [
        "gruvbox dark",
        "monokai dark",
        "shel",
        "material",
        "tomorrow night eighties",
        "tomorrow night bright",
        "empathy",
        "tin",
        "dracula",
        "solarized dark",
        "pali",
        "flat",
        "breeze",
        "elio",
        "bim",
        "elic",
        "tin",
        "gruvbox dark",
        "monokai dark",
        "shel",
        "material",
        "tomorrow night dark",
        "tomorrow night blue",
        "jup",
        "nep",
        "sat",
        "hemisu light",
        "one light",
        "white wind",
        "gruvbox light",
        "solarized light",
        "mar",
        "tomorrow",
        "ura",
    ]

    theme = choice
    if theme == "default":
        if random.randint(0,4) > 1:
            theme = 'peppermint'
        else:
            theme = 'dracula'
    else:
        for _ in schemes:
            if choice == _:
                theme = _
                break

    return theme


def get_coin_theme(choice):
    schemes = [
        "crimson",
        "grayscale",
        "homebrew",
        "iceberg",
        "mars",
        "matrix",
        "synthwave",
        "system",
        "xray",
    ]

    theme = choice
    if theme == "default":
        if random.randint(0,4) > 1:
            theme = 'homebrew'
        else:
            theme = 'synthwave'
    else:
        for _ in schemes:
            if choice in _:
                theme = _
                break
        if theme == "default":
            for _ in schemes:
                if choice[0] or choice[1] in _:
                    theme = _
                    break 
        if theme == "default":
            theme = "homebrew"

    return theme


def switch_deepin_configs():
    if os.path.isfile("/home/bymyself/Desktop/python-scripts/coin-gui-deepin-config.conf"):
        os.system("sudo mv ~/.config/deepin/deepin-terminal/config.conf /home/bymyself/Desktop/python-scripts/")
        os.system("sudo mv /home/bymyself/Desktop/python-scripts/coin-gui-deepin-config.conf ~/.config/deepin/deepin-terminal/config.conf")



# ────────────────────────────────────────────────────────────────────────────────
# ─── OPTIONS ────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


def g_args():
    parser = argparse.ArgumentParser(prog="coin")

    # ────────────────────────────────────────────────────────────────── KRAKEN ─────

    parser.add_argument(
        "--kraken",
        "-k",
        help = "[k]raken web terminal with specified browser, dimensions, window #, & tiling",
        action = "store_true", 
        default = False
    )

    # ───────────────────────────────────────────────────────────── CRYPTOWATCH ─────

    parser.add_argument(
        "--cryptowatch",
        "-c",
        help = "[c]ryptowatch app fullscreen",
        action = "store_true", 
        default = False
    )


    # ───────────────────────────────────────────── KRAKEN AND CRYPTOWATCH COMBO ─────

    parser.add_argument(
        "-kcv",
        help = "[k]raken + [c]ryptowatch [v]ertical split",
        action = "store_true", 
        default = False
    )

    parser.add_argument(
        "-2kc",
        help = ".25 [k]raken x[2] + .5 [c]ryptowatch",
        action = "store_true", 
        default = False
    )

    parser.add_argument(
        "-kct",
        help = ".25 [k]raken + .5 [c]ryptowatch + .25 coin[t]op",
        action = "store_true", 
        default = False
    )

    # ───────────────────────────────────────────────────────────────── TERMINAL ─────

    # Cointop - Only Bottom Panel
    parser.add_argument(
        "-cbp",
        help="[c]ointop [b]ottom [p]anel",
        action="store_true", 
        default=False
    )

    # Cointop - Bottom and Left Minimal panels
    parser.add_argument(
        "-chu",
        help="[c]ointop [h]eads [u]p (left and bottom panels with transparent center)",
        action="store_true", 
        default=False
    )

    # Cointop + Coinmon Fullscreen Tiling 
    parser.add_argument(
        "-cf",
        help="[c]ointop and coinmon [f]ullscreen tiling",
        action="store_true", 
        default=False
    )

    # [ROTATED] Cointop + Coinmon Fullscreen Tiling 
    parser.add_argument(
        "-cfr",
        help="[c]ointop and coinmon [f]ullscreen tiling (*[r]otated)",
        action="store_true", 
        default=False
    )

    
    # ──────────────────────────────────────────────── KRAKEN AND TERMINAL COMBO ─────

    # 2 Chromium Kraken 1 Deepin Cointop
    parser.add_argument(
        "-k2c", 
        action="store_true", 
        default=False, 
        help=".5 Kraken Chromium | .25 Kraken Chromium | .25 Deepin Cointop"
    )

    # Left/Right Kraken + Terminal Bot Panel
    parser.add_argument(
        "-kvtb", 
        help="[k]raken [v]ertical split + coin[t]op [b]ottom panel",
        action="store_true", 
        default=False
    )

    # Left/Right Kraken + Full Heads-Up Cointop Terminal
    parser.add_argument(
        "-kvhu", 
        help="[k]raken [v]ertical split + cointop [h]eads [u]p (left and bottom panel)",
        action="store_true", 
        default=False
    )

    # Fullsreen Kraken + Terminal Bot Panel
    parser.add_argument(
        "-kftb", 
        help="[k]raken [f]ullscreen + coin[t]op [b]ottom panel",
        action="store_true", 
        default=False
    )

    # Fullsreen Kraken + Terminal Left Panel
    parser.add_argument(
        "-kftl", 
        help="[k]raken [f]ullscreen + coin[t]op [l]eft panel",
        action="store_true", 
        default=False
    )

    # Kraken/Termianl Vertical Split
    parser.add_argument(
        "-ktv",
        help="[k]raken + coin[t]op vertical 50/50 split",
        action= "store_true",
        default=False
    )

    # Kitchen Sink
    parser.add_argument(
        "--kitchen-sink",
        help="start everything possible",
        action="store_true", 
        default=False
    )

    # ────────────────────────────────────────────────────────────────────────────────

    # Main Currency(ies) Selection
    parser.add_argument("--coin1", nargs="?", default="DOGE", const="DOGE")
    parser.add_argument("--coin2", nargs="?", default="ETC", const="ETC")
    parser.add_argument("--coin3", nargs="?", default="XLM", const="XLM")
    parser.add_argument("--coin4", nargs="?", default="ADA", const="ADA")

    # Reference Currency Selection
    parser.add_argument(
        "--reference-currency", 
        "-r", 
         metavar=("COIN"),
        nargs="?", 
        default="BTC", 
        const="BTC"
    )

    # Browser Software
    parser.add_argument(
        "--browser",
        choices = ["chromium", "chrome", "firefox", "selenium", "edge", "default"],
        metavar=["chrome", "chromium", "firefox", "selenium", "edge", "default"], 
        nargs="?",
        default="chromium", 
        const="chromium"
    )

    # Direction / Type of Window Tiling
    parser.add_argument(
        "--tiling",
        "-t",
        choices = ["vertical", "horizontal", "minimize", "fullscreen", "4", "custom"],
        metavar= ["vertical", "horizontal", "minimize", "fullscreen", "4", "custom"], 
        nargs="?",
        default="fullscreen", 
        const="fullscreen"
    )

    # Window Dimensions
    parser.add_argument(
        "--dimensions",
        metavar=("WIDTH,HEIGHT"), 
        nargs="?",
        default="960,600", 
        const="960,600"
    )

    # Deepin Theme
    parser.add_argument(
        "--deepin-scheme",
        "-ds", 
        metavar=("color-scheme"),
        nargs="?", 
        default="dracula", 
        const="dracula"
    )

    # Cointop Color Scheme
    parser.add_argument(
        "--cointop-scheme",
        "-cs",
        metavar=("cointop-color-scheme"),
        nargs="?", 
        default="default", 
        const="default"
    )

    # ────────────────────────────────────────────────────────────────────────────────

    return parser.parse_args()


def get_screen_resolution():
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[0].split(b'x')
    return {'width': resolution[0], 'height': resolution[1]}



# ────────────────────────────────────────────────────────────────────────────────
# ─── MAIN ───────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────


def main():

    # ────────────────────────────────────────────────────────────────── OPTIONS ─────


    options = vars(g_args())

    # Main Currencies
    coin1, coin2, coin3, coin4 = options["coin1"], options["coin2"], options["coin3"], options["coin4"]

    # Deepin Theme
    theme = get_deepin_theme(
        options["deepin_scheme"]
    )

    # Cointop Color Scheme
    if options["cointop_scheme"] == "default":
        ctheme = False # Required to use multiple schemes as default
    else:
        ctheme = get_coin_theme(
            options["cointop_scheme"]
        )

    # Screen Resolution
    resolution = get_screen_resolution()


    # ────────────────────────────────────────────────────────────────── KRAKEN ──────


    if options["kraken"]:

        # Fullscreen by using Super+Up hotkey
        if options["tiling"] == "fullscreen":
            kraken(options["browser"], direction="up", coin=coin1, reference_currency=options["reference_currency"])

        # Minimize by using Super+Down hotkey
        elif options["tiling"] == "minimize":
            kraken(options["browser"], direction="h", coin=coin1, reference_currency=options["reference_currency"])

        # Custom Dimensions from 'dimensions' option
        elif options["tiling"] == "custom":
            res = str(options["dimensions"])
            kraken(options["browser"], direction="custom",dimensions=res, coin=coin1, reference_currency=options["reference_currency"])

        # Vertical split by using Super+Left|Right hotkeys
        elif options["tiling"] == "vertical":
            kraken(options["browser"], direction="left", coin=coin1, reference_currency=options["reference_currency"])
            time.sleep(1)
            kraken(options["browser"], direction="right", coin=coin2, reference_currency=options["reference_currency"])
        
        # Horizontal Split by using width of screen x half the height of screen
        elif options["tiling"] == "horizontal":
            half_height = "5000," + str(int(resolution["height"])//2)
            kraken(options["browser"], direction="custom", dimensions=half_height,  coin=coin1, reference_currency=options["reference_currency"])
            time.sleep(1)
            kraken(options["browser"], direction="custom", dimensions=half_height, coin=coin2, reference_currency=options["reference_currency"])

        # 4 Windows by using dimensions of .5 width by .5 height
        elif options["tiling"] == "4":
            quarter_dimensions = str(int(resolution["width"])//2) + "," + str(int(resolution["height"])//2)
            kraken(options["browser"], direction="custom", dimensions=quarter_dimensions,  coin=coin1, reference_currency=options["reference_currency"])
            time.sleep(1)
            kraken(options["browser"], direction="custom", dimensions=quarter_dimensions, coin=coin2, reference_currency=options["reference_currency"])
            time.sleep(1)
            kraken(options["browser"], direction="custom", dimensions=quarter_dimensions,  coin=coin3, reference_currency=options["reference_currency"])
            time.sleep(1)
            kraken(options["browser"], direction="custom", dimensions=quarter_dimensions, coin=coin4, reference_currency=options["reference_currency"])


    # ───────────────────────────────────────────────────────────── CRYPTOWATCH ──────


    elif options["cryptowatch"]:
        #cryptowatch(options["tiling"])
        cryptowatch("fullscreen")


    # ───────────────────────────────────────────── KRAKEN AND CRYPTOWATCH COMBO ─────


    elif options["kcv"]:
        cryptowatch("right")
        time.sleep(1)
        kraken(options["browser"], direction="left", coin=coin1, reference_currency=options["reference_currency"])

    elif options["2kc"]:
        cryptowatch("right")
        time.sleep(1)
        quarter_dimensions = str(int(resolution["width"])//2) + "," + str(int(resolution["height"])//2)
        kraken(options["browser"], direction="custom", dimensions=quarter_dimensions,  coin=coin1, reference_currency=options["reference_currency"])
        time.sleep(1)
        kraken(options["browser"], direction="custom", dimensions=quarter_dimensions, coin=coin2, reference_currency=options["reference_currency"])

    elif options["kct"]:
        cryptowatch("right")
        time.sleep(1)
        quarter_dimensions = str(int(resolution["width"])//2) + "," + str(int(resolution["height"])//2)
        kraken(options["browser"], direction="custom", dimensions=quarter_dimensions,  coin=coin1, reference_currency=options["reference_currency"])
        time.sleep(1)
        new_cointop(theme)


    # ───────────────────────────────────────────────────────────────── TERMINAL ─────


    # Cointop - Only Bottom Panel
    elif options["cbp"]:
        bottom_bar_term(theme, coin1, coin2, coin3, custom_coin_theme=ctheme)

    # Cointop - Bottom and Left Minimal panels
    elif options["chu"]:
        bottom_bar_term(theme, coin1, coin2, coin3, custom_coin_theme=ctheme)
        time.sleep(1.5)
        left_term_panel()

    # Cointop + Coinmon Fullscreen Tiling 
    elif options["cf"]:
        terminal_gui(theme, coin1, coin2, coin3, right=False, custom_coin_theme=ctheme)

    # [ROTATED] Cointop + Coinmon Fullscreen Tiling
    elif options["cfr"]:
        terminal_gui(theme, coin1, coin2, coin3, right=True, custom_coin_theme=ctheme)


    # ──────────────────────────────────────────────── KRAKEN AND TERMINAL COMBO ─────


    # 2 Chromium Kraken 1 Deepin Cointop
    elif options["k2c"]:
        new_cointop(theme)
        time.sleep(1.3)
        kraken("chromium", coin=coin1, direction="right", reference_currency=options["reference_currency"])
        time.sleep(.5)
        kraken("chromium", coin=coin2, direction="custom", reference_currency=options["reference_currency"])

    # Left/Right Kraken + Terminal Bot Panel
    elif options["kvtb"]:
        kraken(options["browser"], direction="left", coin=coin1, reference_currency=options["reference_currency"])
        time.sleep(1)
        kraken(options["browser"], direction="right", coin=coin2, reference_currency=options["reference_currency"])
        time.sleep(2)
        bottom_bar_term(theme, coin1, coin2, coin3, custom_coin_theme=ctheme)

    # Left/Right Kraken + Full Heads-Up Cointop Terminal
    elif options["kvhu"]:
        kraken(options["browser"], direction="left", coin=coin1, reference_currency=options["reference_currency"])
        time.sleep(1)
        kraken(options["browser"], direction="right", coin=coin2, reference_currency=options["reference_currency"])
        time.sleep(2)
        bottom_bar_term(theme, coin1, coin2, coin3, custom_coin_theme=ctheme)
        time.sleep(.25)
        left_term_panel()

    # Fullsreen Kraken + Terminal Bot|Left Panel
    elif options["kftb"] or options["kftl"]:
        kraken(options["browser"], direction="up", coin=coin1, reference_currency=options["reference_currency"])
        time.sleep(1)
        keyboard.press(Key.f11)
        keyboard.release(Key.f11)
        time.sleep(1.5)
        if options["kftb"]:
            bottom_bar_term(theme, coin1, coin2, coin3, custom_coin_theme=ctheme)
        elif options["kftl"]:
            time.sleep(.5)
            new_cointop(theme, screensize="fullscreen")
            time.sleep(.35)
            keyboard.press(Key.shift)
            time.sleep(.35)
            ctrl_letter("j")
            keyboard.release(Key.shift)
            time.sleep(1.5)
            left_term_panel()

    # Kraken/Termianl Vertical Split
    elif options["ktv"]:
        terminal_gui(theme, coin1, coin2, coin3, right=False, custom_coin_theme=ctheme)
        time.sleep(1.15)
        kraken(options["browser"], direction="right", coin=coin1, reference_currency=options["reference_currency"])

    # Kitchen Sink
    elif options["kitchen_sink"]:
        quarter_dimensions = str(int(resolution["height"])/2) + "," + str(int(resolution["width"])/2)
        kraken(options["browser"], direction="custom", dimensions=quarter_dimensions,  coin=coin1, reference_currency=options["reference_currency"])
        time.sleep(1)
        kraken(options["browser"], direction="custom", dimensions=quarter_dimensions, coin=coin2, reference_currency=options["reference_currency"])
        time.sleep(1)
        kraken(options["browser"], direction="custom", dimensions=quarter_dimensions,  coin=coin3, reference_currency=options["reference_currency"])
        time.sleep(1)
        kraken(options["browser"], direction="custom", dimensions=quarter_dimensions, coin=coin4, reference_currency=options["reference_currency"])
        time.sleep(2)
        new_cointop(theme)
        time.sleep(1.3)
        kraken("chromium", coin=coin1, direction="right", reference_currency=options["reference_currency"])
        time.sleep(.5)
        kraken("chromium", coin=coin2, direction="custom", reference_currency=options["reference_currency"])
        time.sleep(1)
        cryptowatch("fullscreen")

    # ────────────────────────────────────────────────────────────────── DEFAULT ─────


    else:
        cryptowatch("right")
        time.sleep(1)
        kraken(options["browser"], direction="left", coin=coin1, reference_currency=options["reference_currency"])


if __name__ == "__main__":
    main()