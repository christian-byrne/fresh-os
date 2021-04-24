import batch_crx
from batch_crx import dl_crx
from batch_vs_extensions import batch_vs
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
        "repo" : [
            "cd",
            "mkdir temp_clone",
            "cd temp_clone",
            "git clone https://github.com/trevor-reznik/fresh-os.git",
            "cd"
        ],

        "themes" : [
            "cd",
            "mkdir .themes",
            "mkdir .icons"
            "mkdir Pictures",
            "cd Pictures",
            "mkdir wallpapers",
            "cd",
            "mv ~/temp_clone/fresh-os/wallpapers/* ~/Pictures/wallpapers",
            "sudo mv ~/temp_clone/fresh-os/icons/* ~/.icons",
            "sudo mv ~/temp_clone/fresh-os/themes/* ~/.themes",
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
        ],


        # ─── APP PLUGINS ────────────────────────────────────────────────────────────────

        "vim plugins" : [
            "cd",
            "mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim",
            "git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim",
            "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
            "cd",
            "sudo mv ~/temp_clone/fresh-os/vimrc /.vimrc",
            "vim +PluginInstall +qall;",
            "vim +PluginUpdate +qall;"
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
            "cd",
        ],


        # ─── CONFIG FILES ─────────────────────────────────────────────────────────────────


        "config files" : [
            "pip3 install emoji --upgrade"
            "sudo mv ~/temp_clone/fresh-os/autostart ~/.config/",
            "sudo mv ~/temp_clone/fresh-os/plank ~/.config/",

            "sudo mv ~/temp_clone/fresh-os/terminator ~/.config/",
            "sudo mv ~/temp_clone/fresh-os/gedit ~/.config/",
            "sudo mv ~/temp_clone/fresh-os/terminology ~/.config/",
            "sudo mv ~/temp_clone/fresh-os/qBittorrent ~/.config/",
            "sudo mv ~/temp_clone/fresh-os/nordvpn ~/.config/",
            "sudo mv ~/temp_clone/fresh-os/guake ~/.config/",

            "sudo mv ~/temp_clone/fresh-os/gedit-plugins ~/temp_clone/fresh-os/plugins",
            "sudo mv ~/temp_clone/fresh-os/plugins ~/.gnome2/gedit/",
            "sudo mv ~/temp_clone/fresh-os/gedit-styles ~/temp_clone/fresh-os/styles",
            "sudo mv ~/temp_clone/fresh-os/styles ~/.gnome2/gedit/",

            "sudo mv ~/temp_clone/fresh-os/settings.json /.config/Code/User/"
        ],

        "Windows" : [
            "sudo mv ~/temp_clone/fresh-os/settings.json $HOME/Library/Application Support/Code/User/settings.json"
        ],

        "Mac" : [
            "sudo mv ~/temp_clone/fresh-os/settings.json %APPDATA%\\Code\\User\\settings.json"
        ],

        "bash scripts/aliases" : [
            "cd",
            "sudo mv ~/temp_clone/fresh-os/bash-scripts .",
            "sudo chmod +x ~/bash-scripts/f5*",
            "sudo chmod +x ~/bash-scripts/nohup*",
            "echo 'alias pypractice=\"vim ~/Desktop/practice.py\"' >> ~/.bashrc"
            "echo \"alias f5='~/bash_scripts/f5'\" >> ~/.bashrc"
            "echo \"alias setalias='nano ~/.bashrc'\" >> ~/.bashrc"
            "echo \"alias a1='~/bash_scripts/nohup'\" >> ~/.bashrc"
        ],

        "cleanup" : [
            "cd",
            "rm *.deb",
            "rm *.zip",
            "cd Downloads",
            "rm *.deb",
            "rm *.zip",
            "cd",
            "sudo ln -s /var/lib/snapd/desktop/applications /usr/share/applications/snapd",
            "xfce4-panel -r",
            "sudo rm quickhighlight_gedit -r",
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


def guided_sections():
    modules = {
        "appearance" : """    ---------------------------
    |       <Appearance>       |
    ---------------------------

    | Theme "Appearance"
    | Hide desktop icons
    | Icons
    | Cursor (Theme and Size)
    | 	(Change in Mouse and Touchpad Settings)
	| Wallpapers in terminology config files (set as source folder)""",

    "tweaks" :"""    ---------------------------
    |         <Tweaks>         |
    ---------------------------


    <w Dialog Windows_________ >
    |
    |    __Search for___________
    |    [1] Settings Editor
    |    [2] Settings (xfce window)
    |    [3] Window Manager Tweaks
    		 No Window Snapping""",
    "startup commands" :"""    <w Startup Command Chain_________ >
    |
    |  xrandr --size 1680x1050; terminator;""",
    
    "shortcuts" : """<!=================================================================!>

    <w Shortcuts_________ >
    |
    |	 ______________________________________
    |    [+]__Add_____
    |	 [A] Keyboard -> Settings Editor -> xfce4-keyboard-shortcuts
    |    [1] Super_L		:		xfce4-popup-whiskermenu
    |    [2] <Alt>h	  		:		hide window
    |    [3] <Alt>7	  		:		move window
    |    [4] <Alt>8	  		:		resize window
    |    [5] <Alt>11		:		fullscreen
    |	 [B] Keyboard -> Application Shortcuts
    |    [1] terminator 	: 		Alt+Return
    |    [2] appfinder  	: 		Alt+'
    |    [3] whisker-popup  : 		Super L
    |    [4] screenshot clipboard regions	:	Super s
    
<!=================================================================!>"""
    }



    for title, text, color in zip(modules.keys(), modules.values(), \
        ["blue", "magenta", "cyan","blue", "magenta", "cyan"]):
        print(colored(
            make_header(60, title, character="~", tiers=1),
            "red")
            )
        print(colored(
            text,
            color)
            )
        nxt = input("\n\n[P]roceed\n")
        while nxt.lower() != "p":
            nxt = input("")


def make_mine():

    # ─── PYTHON MODULES ─────────────────────────────────────────────────────────────
    if start_section("python modules"):
        try:
            get_modules(fresh=False)
        except:
            pass


    # ─── SH DL SCRIPTS ──────────────────────────────────────────────────────────────
    sections = [
        "repo", "themes", "snap store", "yum", "npm", "ngrok", "chrome", "virtualbox",
        "vscode", "glow", "nordvpn", "terminator", "guake term", "qbittorrent", "htop",
        "vim plugins", "gedit plugins", "terminator plugins", "config files",
        "bash scripts/aliases", "cleanup"
    ]
    for _ in sections:
        if start_section(_):
            if sh(_):
                continue


    # ─── TUTORIAL FROM TXT ───────────────────────────────────────────────────────────
    if start_section("guided settings changes"):
        guided_sections()


    # ─── BATCH VSCODE EXTENSIONS ────────────────────────────────────────────────────
    batch_vs()


    # ─── CHROME EXTENSIONS ──────────────────────────────────────────────────────────
    dl_crx()


    # ─── CLEANUP ────────────────────────────────────────────────────────────────────
    cleanup = [
        "cp ~/temp_clones/fresh-os/Computer_Usage ~/Desktop/"
        "sudo rm -r ~/temp_clone"
    ]
    for _ in cleanup:
        os.system(_)
    print("\n\n\nFINISHED\n\n\n")


if __name__ == "__main__":
    make_mine()