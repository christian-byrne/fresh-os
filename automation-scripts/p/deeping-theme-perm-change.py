

import os, sys


def change_theme():
    config_file = open("/home/bymyself/.config/deepin/deepin-terminal/config.conf", "r")
    lines = config_file.readlines()
    config_file.close()

    theme = sys.argv[1]

    config_file = open("/home/bymyself/.config/deepin/deepin-terminal/config.conf", "w")
    lines[1] = f"theme={theme}\n"

    for line in lines:
        config_file.write(line)

    config_file.close()


if __name__ == "__main__":
    change_theme()
