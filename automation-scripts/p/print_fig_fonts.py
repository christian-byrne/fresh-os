

def print_fonts():
    import os
    path = os.path.expanduser("~")
    path += "/../../usr/share/figlet"
    try:
        fonts = os.listdir(path)
    except:
        try:
            path = ("/../../usr/share/figlet")
            fonts = os.listdir(path)
        except:
            try:
                path = (os.path.expanduser("~") + "/../../usr/share/figlet/fonts")
                fonts = os.listdir(path)
            except:
                try:
                    path = ("/../../usr/share/figlet/figlet-fonts")
                    fonts = os.listdir(path)
                except:
                    try:
                        path = ("/../../usr/bin/figlet")
                        fonts = os.listdir(path)
                    except:
                        try:
                            path = (os.path.expanduser("C:\\") + "\\..\\..\\usr\\share\\figlet")
                            fonts = os.listdir(path)
                        except:
                            try:
                                path = (os.path.expanduser("C:\\") + "\\usr\\share\\figlet")
                                fonts = os.listdir(path)
                            except:
                                os.system("ls " + input("Can't locate figlet folder. Enter manually:\n"))
    
    print(str(len(fonts)) +  " Fonts in Total")
    try:
        if sys.argv[1] == "--list":
            for _ in fonts:
                print((_.strip())[:-4])
        exit()
    except:
        pass
    print(path)
    try:
        temp = os.getcwd()
        os.system("cd")
        os.system("ls -G --color=tty " + path)
        os.chdir(temp)
    except:
        try:
            for _ in fonts:
                print((_.strip())[:-4])
        except:
            print(fonts)


if __name__ == "__main__":
    print_fonts()