#import vs_settings_init
#import batch_crx
#import batch_vs_extensions
from batchdl_py_mods import get_modules
import random, os
from term_gui import term_gui, make_header
from termcolor import colored
from emoji import emojize






def start_section(section):
    try:
        os.system("clear")
    except: 
        try:
            os.system("cls")
        except: pass
    print(colored(
            make_header(45, section, boxed=True, character="-", centered=True, tiers=3),
            ["cyan", "magenta", "blue"][random.randint(0,2)]),
            "\n\n",
            colored("[S]kip this section | [P]roceed")
    )
    choice = input("")
    while choice.lower() != "p":
        if choice.lower() == "s":
            if input("Skip this section? [y|n]\n").lower() == "y":
                return False
            else:
                print("[S]kip this section | [P]roceed")
        else:
            print("Invalid Comamnd")
        choice = input("")
    try:
        os.system("clear")
    except: 
        try:
            os.system("cls")
        except: pass
    return True


def sh(section, commands_only=False):

    commands = {
        "wallpapers" : [
            "cd",
            "mkdir .themes",
            "cd Pictures",
            "mkdir wallpapers",
            "cd"

        ],


        "icons" : [
            "mkdir .icons",
        ],


        # ─── PACKAGE MANAGERS ───────────────────────────────────────────────────────────

        "snap store" : [
            "sudo apt-get update", 
            "sudo apt-get install snapd",
            "systemctl enable --now snapd",
            'export PATH="$PATH:/snap/bin',
            'sudo export PATH="$PATH:/snap/bin"',
            "sudo apt-get install software-properties-common",
        ],
        "yum": [
            "cd",
            "mkdir yum-manager",
            "cd yum-manager",
            "git clone git://yum.baseurl.org/yum.git",
            "make",
            "cd"
        ],

        "npm" : [
            "curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -",
            "sudo apt update",
            "sudo apt install nodejs",
            "sudo apt install nodejs npm",
            "sudo apt install build-essential"
        ],


        # ─── APPS ───────────────────────────────────────────────────────────────────────

        "ngrok" : [
            "wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip",
            "unzip *ngrok*.zip",
            "ngrok authtoken 1rJVN0ZJBJfZHCECZ3ofPDq5hi5_6mructS1CnqvQ3Gcjnu1E"
        ],
        "chrome" : [
            "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
            "sudo apt install ./*chrome*.deb",
        ],
        "virtualbox" : [
            "sudo apt update",
            "sudo apt install virtualbox",
        ],
        "vscode" : [
            "sudo apt-get update",
            "sudo snap install --classic code",
            "sudo update-alternatives --set editor /usr/bin/code",
        ],
        "glow" : [
            "sudo snap install glow",
        ],
        "nordvpn" : [
            "wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb",
            "cd",
            "sudo apt-get update",
            "sudo apt-get install ./*dvpn*.deb",
            "sudo apt-get update",
            "sudo apt-get install nordvpn",
        ],
        "terminator" : [
            "sudo add-apt-repository ppa:mattrose/terminator -r",
            "sudo apt-get update --allow-unauthenticated",
            "sudo apt update",
            "sudo apt install terminator",
        ],
        "guake term" : [
            "sudo apt-get update",
            "sudo apt-get install guake",
        ],
        "qbittorrent" : [
            "sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-unstable -r",
            "sudo apt-get update --allow-unauthenticated",
            "sudo apt-get install qbittorrent", 
        ],
        "htop" : [
            "sudo apt update && sudo apt upgrade",
            "sudo apt-get update && sudo apt-get upgrade",
            "sudo apt-get install htop"
        ]


        # ─── APP PLUGINS ────────────────────────────────────────────────────────────────

        "vim plugins" : [
            "cd",
            "mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim",
            "git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim",
            "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
            "cd",
            "rm .vimrc"



        ],
        "gedit plugins" : [
            "cd",
            "mkdir .gnome2/gedit/styles",
            "mkdir .gnome2/gedit/plugins",
            "sudo apt-add-repository ppa:ubuntu-on-rails/ppa -r",
            "sudo apt-get update --allow-unauthenticated",
            "sudo apt-get install gedit-gmate",
            "mkdir quickhighlight_gedit",
            "cd quickhighlight_gedit",
            "git clone git://github.com/nagaozen/gedit-plugin-quickhighlightmode.git",
            "mv quickhighlightmode.gedit-plugin ~/.gnome2/gedit/plugins/",
            "mv quickhighlightmode ~/.gnome2/gedit/plugins/",
            "cd"
        ],
        "terminator plugins" : [
            "cd",
            "mkdir -p .config/terminator/plugins",
            'wget https://git.io/v5Zww -O ".config/terminator/plugins/terminator-themes.py"',
            "cd; ",

        ],





            "vim +PluginInstall +qall;",
            "vim +PluginUpdate +qall;",

        "misc" : [
            "pip install emoji --upgrade"
        ]


        }
    if commands_only:
        ret = ""
        for _ in commands[section]:
            ret += _ + "; \n"
        return ret

    result = bash_chain(commands[section])
    while not result:
        if "n" in input(colored("Try bash script again? [y|n]\n","magenta")).lower():
            return True
        result = bash_chain(commands[section])
    return True


def bash_chain(chain):
    for index, cmd in enumerate(chain):
        try:
            os.system(cmd)
        except:
            try:
                os.system(cmd.strip("\n").strip())
            except Exception as e:
                print("\n"); print(e)
                print("\n\nFull List of Commands:")
                for _ in range( len(chain)-1 ):
                    if _ == index:
                        print(colored("ERROR HERE","red"))
                        print(chain[_])
                        print(colored("ERROR HERE","red"))
                    else:
                        print(chain[_])
                return False
    return True


def make_mine():

    # ─── PYTHON MODULES ─────────────────────────────────────────────────────────────
    if start_section("modules"):
        try:
            get_modules(fresh=False)
        except:
            pass


    # ─── SH DL SCRIPTS ──────────────────────────────────────────────────────────────
    
    sections = ["snap store", "ngrok", "test"]
    
    for _ in sections:
        if start_section(_):
            if sh(_):
                continue




if __name__ == "__main__":
    make_mine()