def main():
    print("python3 batch_git.py  [text file w/ link location OR links with no spaces between]  [DL location, default is cd]")
    import sys, os
    if len(sys.argv) == 1:
        try:
            g = os.getcwd()
            fi = open(g + "/" + "output.txt", "r")
            li = fi.readlines()
            fi.close()
        except:
            try:
                fi = open("/home/bymyself/Desktop/python-scripts/output.txt", "r")
                li = fi.readlines()
                fi.close()
            except:
                print("Can't find file called 'output.txt' in cd\nPass a file name as the first option when executing script")
                sys.exit()

    if len(sys.argv) > 1:
        if ".com" in sys.argv[1]:
            li = sys.argv[1]
        else:
            fi = open(sys.argv[1], "r")
            li = fi.readlines()
            fi.close()
            print("Can't find file called " + sys.argv[1] + " in cd\n")
            sys.exit()

    if len(sys.argv) == 3:
        try:
            os.chdir(sys.argv[2])
        except:
            print("Could not go to path " + sys.argv[2])
            print("Downlaoding to cd")
    else:
        g = os.getcwd()
        os.chdir(g)
    
    for _ in li:
        try:
            os.system("git clone " + _)
        except:
            print("Unable to git clone: " + _)
            continue


if __name__ == "__main__":
    main()