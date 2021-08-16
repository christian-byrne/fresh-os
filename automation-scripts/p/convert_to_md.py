import os, pyfiglet, argparse, sys
from termcolor import colored
from term_gui import make_header


def g_args():
    parser = argparse.ArgumentParser(prog="md_converter")

    # Positional
    parser.add_argument("text|file", nargs="?")
    # Table
    parser.add_argument("--table", "-t", action="store_true", default=False)
    # Inline Code
    parser.add_argument("--inline-code", "-c", nargs="?", metavar=("language"), type=str, default="shell", const="shell")
    # Output File
    parser.add_argument("--output", "-o", nargs="?", metavar=("path/name"), type=str, default="__FORMATTER-OUTPUT.txt", const="__FORMATTER-OUTPUT.txt")
    # Header Level
    parser.add_argument("--header-lvl", "-hl", nargs="?", metavar=("lvl#"), type=int, default=6, const=6)
    # No Rewrite
    parser.add_argument("--no-rewrite", action="store_true", default=False)

    return parser.parse_args()


def from_file(options):
    fi = open(options["text|file"], "r")
    lines = fi.readlines()
    fi.close()
    ret = []
    for _ in lines:
        ret.append(_.strip("\n"))
    return ret


def convert_inline(lines, language, header_lvl):
    ret = []
    for index, _ in enumerate(lines):

        # Header Line (not inline code)
        if len(_) > 1:
            if _[0] == "#" or _[1] == "#":
                ret.append( "\n" + "#" * header_lvl + " " +  _[1:] + "\n\n\n" )
                continue

        # Not Last Line
        if index != len(lines) - 1:
            
            # Blank Line Before Text
            if len(_) < 4 and len(lines[index-1]) > 4:
                if len(lines[index-1]) > 1:
                    if lines[index-1][0] != "#" and lines[index-1][1] != "#":
                        ret.append("\n```\n\n")


            # Text on Line but Next Line Blank
            if len(_) > 4 and len(lines[index+1]) < 4 and _[0] != "#":
                if _[0] != "#" and _[1] != "#":
                    ret.append("\n```" + language + "\n")

        # Last Line
        else:
            if len(_) > 4:
                ret.append("\n```" + language + "\n" + _ + "\n```\n")
                continue
        ret.append(_)
    
    ret = "".join(ret)

    return ret


def convert_table(lines):
    import re
    separated =re.split(' \| |\n',lines)

    maxLenLeft = maxLenRight = 0
    for _ in separated:
        if separated.index(_) % 2 == 0:
            if len(_) > maxLenLeft:
                maxLenLeft = len(_)
        else:
            actualLength = _.replace("   ", "")
            if len(actualLength) > maxLenRight:
                maxLenRight = len(actualLength)
                
    newTable = []
    for _ in separated:
        if separated.index(_) % 2 == 0:
            spacesNeeded = maxLenLeft - len(_)
            spaces = " "*spacesNeeded
            newTable.append("|`" + _ + spaces + "`|")
        else:
            newString = _.replace("   ", "")
            spacesNeeded = maxLenRight - len(newString)
            spaces = " "*spacesNeeded
            newTable.append(spaces + newString + "|\n")

    records = "".join(newTable)
    header = "| **Command**	  |	  **Function**  |\n"
    headerBar = "|:---------------:| ---------------:|\n"

    return heeader + headerBar + records


def md_converter():

    print(colored(
        make_header(60, "Converting to Markdown", tiers=2),
        "magenta")
    )

    options = vars(g_args())

    if os.path.isfile(options["text|file"]):
        raw = from_file(options)
        print(colored(
            make_header(50, "Getting input from text file", character="~", tiers=1),
            "magenta")
        )

    else:
        raw = options["text|file"].split("\n")
        print(colored(
            make_header(50, "Getting input from sys arg", character="~", tiers=1),
            "magenta")
        )

    if not options["table"]:
        final = convert_inline(raw, options["inline_code"], int(options["header_lvl"]))
        print(colored(
            make_header(30, "converting inline code", character="~", tiers=1),
            "cyan")
        )
    else:
        final = convert_table(raw)
        print(colored(
            make_header(30, "converting to md table", character="~", tiers=1),
            "cyan")
        )

    if os.path.isfile(options["text|file"]) and not options["no_rewrite"]:
        temp = options["text|file"]
        print(colored(
            make_header(30, "'no rewrite' specified", tiers=1),
            "grey")
        )
    else:
        temp = "temp_temp_temp.txt"
    
    fi = open(temp, "w")
    fi.write(final)
    fi.close()
    import time
    time.sleep(.2)

    os.system("cat " + temp + " | clipboard")
    os.system("rm " + temp)

    print(colored(
        make_header(50, "Below is now in clipboard", tiers=2),
        "blue"),
        final
    )

    if os.path.isfile(options["text|file"]) and not options["no_rewrite"]:
        os.system("touch " + temp)

    if options["output"] != "__FORMATTER-OUTPUT.txt":
        ofi = open(options["output"], "w")
        ofi.write(final)
        ofi.close()
        os.system("xdg-open " + options["text|file"])


if __name__ == "__main__":
    md_converter()