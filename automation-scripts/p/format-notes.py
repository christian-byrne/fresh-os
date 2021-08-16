

import os, pyfiglet, argparse, random
from termcolor import colored
from pyfiglet import Figlet


def g_args():

    """""""""""""""
    |               # max space = 80, always one extra padding line, quotation quote # algorithm
    |                   
    |  add_argumnet()   
    |                   
    |
    |___________________________________________________________________________________________________ 
    |  [-]----------------------------------------------------------------------------------------------| 
    |  [1] name or flags :  Either a name or a list of option strings, e.g. foo or -f, --foo            |
    |  [+]______________________________________________________________________________________________| 
    |  [2] action        :  Basic type of action to be taken when this argument is encountered at       |
    |  [+]                  the command line                                                            |
    |  [+]______________________________________________________________________________________________| 
    |  [3] nargs         :  The number of command-line arguments that should be consumed                |
    |  [+]______________________________________________________________________________________________| 
    |  [4] const         :  A constant value required by some action and nargs selections               |
    |  [+]______________________________________________________________________________________________| 
    |  [5] default       :  The value produced if the argument is absent from the command line an       |
    |  [+]                  if it is absent from the namespace object                                   |
    |  [+]                  the argument is absentm the namespace object                                |
    |  [+]______________________________________________________________________________________________| 
    |  [6] type          :  The type to which the command-line argument should be converted             | 
    |  [+]______________________________________________________________________________________________| 
    |  [7] choices       :  A container of the allowable values for the argument                        |
    |  [+]______________________________________________________________________________________________| 
    |  [8] required      :  Whether or not the command-line option may be omitted (optionals only       |
    |  [+]______________________________________________________________________________________________| 
    |  [9] help          :  A brief description of what the argument does                               |
    |  [+]______________________________________________________________________________________________| 
    |  [a] metavar       :  A name for the argument in usage messages                                   |
    |  [+]______________________________________________________________________________________________| 
    |  [b] dest          :  The name of the attribute to be added to the object returned by parse_args()|
    |  [+]______________________________________________________________________________________________| 
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    parser = argparse.ArgumentParser(prog="juice")

    # Positional
    parser.add_argument("path", nargs="?")
    # Adjustments
    parser.add_argument("--downscale", "-d", nargs="?", const=1, type=int, default=0, metavar=("increment"))
    parser.add_argument("--title","-t", nargs="?", metavar=("title/header string"), default="none")
    # Output
    parser.add_argument("--rewrite","-r", action="store_true", default=False)
    parser.add_argument("--no-backup", action="store_true", default=False)
    parser.add_argument("--output", "-o", nargs="?", metavar=("path/name"), type=str, default="__FORMATTER-OUTPUT.txt", const="__FORMATTER-OUTPUT.txt")
    parser.add_argument("--open", nargs="?", type=str, choices=["gedit","vim", "nano", "office","cat", "notepad", "notepad++", "vscode", "sublime", "geany", "emacs", "docviewer", "browser", "pdf", "meld", "diff", "$filetype$"], metavar=("program|filetype"), default="gedit", const="gedit")
    # Figlet Choices
    parser.add_argument("-fonts","-f", nargs=4, default=["auto", "auto", "auto", "auto"], metavar=("[header]", "[section-titles]", "[special]", "[table-titles]"))
    parser.add_argument("--title-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--section-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--special-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    parser.add_argument("--table-title-font", nargs="?", type=str, default="auto", const="auto", metavar=("random|none|fontname"))
    # Additional Help Dialogs
    parser.add_argument("--show-fonts", action="store_true", default=False)

    return parser.parse_args()


# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

fonts = {
    "all" : ['britebi', 'octal', 'fair_mea', 'smisome1', 'hades___', 'banner3', 'maxfour', 'relief2', 'pawp', 'ts1_____', 'linux', 'eftipiti', 'fuzzy', 'unarmed_', '5lineoblique', 'yie_ar_k', 'clb8x8', 'triad_st', 'clb6x10', 'xsans', 'tecrvs__', 'charact3', 'kgames_i', 'ucf_fan_', 'runic', 'rally_s2', 'clr8x8', 'spc_demo', 'gradient', 'xhelvb', 'tsn_base', 'future_6', 'beer_pub', 'broadway', 'alligator2', 'c_ascii_', 'mad_nurs', 'timesofl', 'pebbles', 'war_of_w', 'star_war', 'hollywood', 'threepoint', 'nipples', 'ebbs_1__', 'thin', 'poison', 'rounded', 'wavy', 'rad_phan', '3x5', 'krak_out', 'magic_ma', 'assalt_m', 'twopoint', 'charact2', 'stencil2', 'cyberlarge', 't__of_ap', 'top_duck', 'isometric3', 'sblood', 'joust___', 'sketch_s', 'mirror', 'fbr12___', 'future_3', 'xsbookbi', 'couri', 'druid___', 'odel_lak', 'aquaplan', 'rastan__', 'hex', 'jerusalem', 'graffiti', 'rok_____', 'bigchief', 'mayhem_d', 'char2___', 'bubble', 'helv', 'xbritei', 'diamond', 'rectangles', 'xhelvi', 'baz__bil', 'sansbi', 'xttyb', 'contessa', 'pacos_pe', 'roman', 'xsbooki', 'clr7x8', 'small', 'trashman', 'xhelv', 'mike', 'xbriteb', 'ntgreek', 'house_of', 'future_1', 'zig_zag_', 'sansi', 'subteran', 'battlesh', 'fraktur', '5x7', 'convoy__', 'charact5', 'modern__', 'lexible_', 'rad_____', 'smtengwar', 'chunky', 'sbookb', 'cursive', 'asc_____', 'ticks', 'script__', 'type_set', 'eftiwall', 'char1___', 'ascii___', 'banner', 'lockergnome', 'tomahawk', 'pyramid', 'advenger', 'rci_____', 'grand_pr', 'greek', 'inc_raw_', 'space_op', 'rainbow_', 'ghost_bo', 'ebbs_2__', 'xbritebi', 'mnemonic', 'rockbox_', 'sbookbi', 'c_consen', 'barbwire', 'jazmine', 'ivrit', 'ugalympi', 'raw_recu', 'npn_____', 'rev', 'ti_pan__', 'future_5', 'decimal', 'bubble__', 'atc_gran', 'script', 'ticksslant', 'z-pilot_', 'pawn_ins', 'com_sen_', 'madrid', 'usaflag', 'cricket', 'battle_s', 'fp2_____', 'sm______', 'shimrod', 'pepper', 'smscript', 'isometric2', 'cosmike', 'letters', 'rowancap', 'atc_____', 'taxi____', 'dcs_bfmo', 'sbook', 'dotmatrix', 'peaks', 'etcrvs__', 'catwalk', 'utopiabi', 'eftifont', 'xtty', 'ripper!_', 'straight', 'relief', 'char3___', 'characte', 'slscript', '3-d', 'xtimes', 'puffy', 'twin_cob', 'katakana', 'f15_____', 'caus_in_', 'charact1', 'skate_ro', 'street_s', 'mcg_____', 'brite', 'crawford', 'alphabet', 'smkeyboard', 'term', 'd_dragon', 'fireing_', 'cosmic', 'xsansb', 'xsansbi', 'runyc', 'nancyj-fancy', 'banner3-D', 'future_8', 'outrun__', 'tty', 'ogre', 'defleppard', 'c1______', 'courbi', '6x10', 'kik_star', '5x8', '4x4_offr', 'nancyj-underlined', 'radical_', 'sbooki', 'banner4', 'marquee', 'basic', 'stacey', 'flyn_sh', 'bubble_b', 'doom', 'funky_dr', 'rally_sp', '64f1____', 'mshebrew210', 'platoon2', 'invita', 'univers', 'stencil1', 'larry3d', 'roman___', 'deep_str', 'short', 'xcour', '6x9', 'xsansi', 'skateroc', 'eca_____', 'sans', 'starwars', 'isometric1', 'slant', 'whimsy', 'acrobatic', 'fourtops', 'fender', 'helvb', 'rot13', 'xchartr', 'os2', 'hills___', 'tiles', 'usa_pq__', 'letter_w', 'tubular', 'tengwar', 'italics_', 'demo_1__', 'future_7', 'charact4', 'future_4', 'ok_beer_', 'asslt__m', 'a_zooloo', 'usa_____', 'tec1____', 'platoon_', 'stampatello', 'arrows', 'times', 'notie_ca', 'chartri', 'heroboti', 'shadow', 'dwhistled', 'fbr1____', 'helvi', 'fp1_____', 'caligraphy', 'clb8x10', 'eftichess', 'kban', 'char4___', 'eftirobot', 'c2______', 'coil_cop', 'lcd', 'tsalagi', 'speed', 'phonix__', 'road_rai', 'utopiab', 'future_2', 'block', 'demo_m__', 'eftiwater', 'rozzo', 'contrast', 'drpepper', 'new_asci', 'finalass', 'xcourb', 'tsm_____', '1943____', 'charact6', 'clr4x6', 'cli8x8', 'clr8x10', 'super_te', 'morse', 'clr6x6', 'mini', 'helvbi', 'letterw3', 'sansb', 'b_m__200', 'stellar', 'nvscript', 'stop', 'fbr_tilt', 'demo_2__', 'e__fist_', 'coinstak', 'eftitalic', 'italic', 'rampage_', 'double', 'xbrite', 'gauntlet', 'tav1____', 'xsbook', 'cybersmall', 'lazy_jon', 'serifcap', 'heavy_me', 'panther_', 'faces_of', 'tanja', 'computer', 'home_pak', 'chartr', 'gothic__', 'courb', 'yie-ar__', 'fbr_stri', 'epic', 'tec_7000', 'fantasy_', 'pod_____', 'xsbookb', 'colossal', 'clr5x10', 'binary', 'vortron_', 'xhelvbi', 'ttyb', 'standard', 'clr5x6', 'p_s_h_m_', 'lean', 'bell', 'p_skateb', 'xcourbi', 'cour', 'thick', 'o8', 'isometric4', 'skateord', 'smslant', 'fairligh', 'devilish', 'doh', 'nancyj', 'hyper___', 'high_noo', 'weird', 'moscow', 'fbr2____', 'calgphy2', 'mig_ally', 'avatar', 'clr6x10', 'master_o', 'trek', 'gothic', 'r2-d2___', 'hypa_bal', 'smshadow', 'nfi1____', 'green_be', 'goofy', 'charset_', 'tinker-toy', 'alligator', 'big', 'utopia', 'clr6x8', 'digital', 'slide', 'utopiai', 'xchartri', 'clr7x10', 'cybermedium', 'xcouri', 'tombstone', 'briteb', 'clr5x8', 'bulbhead', 'zone7___', 'graceful', 'stealth_', 'britei'],
    "xxl" : ["doh", "rev", "relief", "banner3-D", "calgphy2", "caligraphy"],
    "xl" : ["doh", "3-d", 'banner3', "alligator", "banner", "alligator2", "banner2", "banner4", "barbwire"],
    "l" : ["basic", "larry3d", "isometric1", "isometric2", "isometric3", "isometric4", "big", "coinstalk", "colossal"],
    "m"   : ["avatar", "epic", "bell"," block", "chunky"],
    "small" : ["doom", "bulbhead", "starwars", "o8", "ntgreek", "maxfour", "letters","elevator"],
    "xs" : ["bubble","contessa", "cybersmall", "digital", ]
}

# ────────────────────────────────────────────────────────────────────────────────

tier = [
    {#TITLE#
        "SEP" : "\n\n\n",
        "BAR" : "<!{}!>\n",
        "offset" : 4,
        "FILL"  : "=",
        "TXT" : " | {}\n"
    },
    {##1
        "SEP" : "\n\n\n",
        "BAR" : "<!--{}-->\n",
        "offset" : 8,
        "FILL"  : "=",
        "TXT" : " | {}\n"
    },
    {##2
        "BAR" : "    -{}-\n",
        "offset" : 2,
        "FILL"  : "-",
        "T"  :"    |{}|\n",
        "SEP" : "\n\n",
        "TXT" : "    | {}\n",
        "PAD" : "    |\n"
    },
    {##3
        "T"  : "    <{} {}_________ >\n",
        "BAR"   : "_{}_",
        "offset" : 2,
        "FILL"  : "_",
        "PAD" : "    |\n",
        "SEP" : "\n\n",
        "TXT" : "    |  {}\n"
    },
    {##4
        "FILL"  : "_",
        "BAR"  : "_{}_",
        "offset" : 2,
        "T"   :"    |    __{}_____________________\n",
        "TXT" : "    |    {}\n",
        "SEP" : "    |\n",
    },
    {##5
        "T"   :"    |    [+]__{}\n",
        "FILL"  : "'",
        "BAR"  : "|{}",
        "offset" : 1,
        "TXT" : "    |    {}\n",
        "SEP" : "    |\n",

    }
]

# ────────────────────────────────────────────────────────────────────────────────

fm = {
    "title" : {
        "BAR" : "================================================================\n"
    },
    "bars" : {
        "H1BAR" : "<!--=========================================================-->\n",
        "H2BAR" : "    -{}-\n"
    },
    "special" : {
        "SPECIAL" : "    |    <!_ {} _!>\n",
        "SPECIALBAR" : "{}<!{}!>\n"
    },
    "indents" : {
        "H1TXT" : " | {}\n",
        "H2TXT" : "    | {}\n",
        "H3TXT" : "    |  {}\n",
        "H4TXT" : "    |    {}\n",
        "H3PAD" : "    |\n"
    },
    "table" : {
        "iter" : "[{}] "
    }
}

# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────

MAXHEIGHT = 40
FALLBACK = "doom"

def display_fonts():
    try:
        sys.path.append(os.getcwd())
        import print_fig_fonts
    except:
        try:
            import sys
            sys.path.append(os.getcwd())
            import print_fig_fonts
        except:
            print(figl)


def val_path(path):
    try:
        home = os.path.expanduser("~")
    except:
        try:
            from pathlib import Path
            home = Path.home()
        except: home = ""
    if "~" in path:
        path = path.replace("~", home)
    path = "/" + path.strip("/")
    if not os.path.isfile(path):
        try:
            temp_path = os.getcwd()
            os.system("cd")
        except Exception as e: print(e)
        if not os.path.isfile(path):
            path = str(path.split("/")[-1:])
            while not os.path.isfile(path):
                path = input(colored("[-] File Not Found. Try Again Please.\n[:]","red"))
                path = path.replace("~", home)
                path = "/" + path.strip("/")
                try: os.chdir(temp_path)
                except: pass
    return path


def txt_files(start_path):
    in_file = open(start_path,"r")
    lines = in_file.readlines()
    in_file.close()
    try:
        backup_log = open(os.path.expanduser("~") + "/BACKUP.txt", "a")
    except: backup_log = open("BACKUP.txt", "a")
    return [lines, backup_log]


def append_backup(backup_lines, log):
    try:
        from datetime import datetime
        log.write("\n"*5 + "="*130 + "\n" + datetime.now().strftime("%H:%M:%S") + "\n" + "="*130 + "\n"*2)
        print(colored("__________________________________________","blue"))
        print(colored("______Backup Appended to 'BACKUP.txt'_____\n\n\n", "grey"))
    except: log.write("\n"*5 + "="*130 + "\n"*2)
    log.write("\n".join(backup_lines).replace(",\n",""))


def val_font(font):
    if font.lower() == "none":
        return False
    elif "rando" in font.lower():
        font = fonts["all"][random.randint(0, len(fonts["all"])-1)]
    elif font not in fonts["all"]:
        try:
            import difflib
            font = difflib.get_close_matches(font, fonts["all"], n=1, cutoff=0.6)
        except:
            font = fonts["all"][random.randint(0, len(fonts["all"])-1)]
    try:
        return Figlet(font=font)
    except:
        return Figlet(font=AUTO)

   
def auto_font(text, get_max_width=False):
    if len(text) < 5:
        # < 5 characters only chooses from xxl fronts
        f = Figlet(font=(fonts["xxl"][random.randint(0, len(fonts["xxl"])-1)]))
    else:
        i = 0
        max_height = 12 if len(text) < 18 else 16 if len(text) < 24 else 20 if len(text) < 50 else MAXHEIGHT
        # Max lines of rendered figlet. short phrases should not be split across 
        # multiple lines but should still be able to choose big fonts if appropriate.
        # long phrases can have more lines but shouldn't be using big fonts

        f = Figlet(font=(fonts["all"][random.randint(0, len(fonts["all"])-1)]))
        candidate = f.renderText(text)
        width = [len(_) for _ in (candidate.split("\n"))]
    
        while max(width) > 80 or max(width) < 50 or len(width) > max_height:
            f = Figlet(font=(fonts["all"][random.randint(0, len(fonts["all"])-1)]))
            candidate = f.renderText(text)
            width = [len(_) for _ in (candidate.split("\n"))]
            i += 1
            if i > 10000:
                f = Figlet(font=FALLBACK)
                break

    return f.renderText(text) if not get_max_width else [f.renderText(text), max(width)]


def max_fig_width(rendered_text):
    width = [len(_) for _ in (rendered_text.split("\n"))]
    return max(width)


def fig_header(options, title, output_file, lvl, top_bar=False,bot_bar=False):
    opt_types = ["title_font", "section_font", "special_font", "table_title_font"]

    # If auto font is specified by leaving both args empty/default
    if options["fonts"][lvl] == "auto" and options[opt_types[lvl]] == "auto":
        [txt, length] = auto_font(title, get_max_width=True)

    # If a specific font (or random) is specified
    else:
        # Pass whichever is not left as default (auto)
        if options["fonts"][lvl] == "auto":
            f = val_font(options[opt_types[lvl]])
        else:
            f = val_font(options["fonts"][lvl])
        txt = f.renderText(title)
        length = max_fig_width(txt)
    

    length = length - tier[lvl]["offset"]
    fill = tier[lvl]["FILL"] * length
    bar = tier[lvl]["BAR"].format(fill)

    if top_bar:
        output_file.write(bar)
    output_file.write(txt)
    if bot_bar:
        output_file.write(bar)
    return output_file


def new_format(options, lines, output):

    maxes = {"h1" : None, "chunk_ct" : None, "h2" : None, "h3" : None, "h4" : None, "h5" : None}
    maxes["h1"] = get_max(lines, 1, and_count=True)[0]
    maxes["chunk_ct"] = get_max(lines, 1, and_count=True)[1]

    # ────────────────────────────────────────────────────────────────────────────────
    # ─── BY BLOCK SEPARATED BY H1 HEADERS ───────────────────────────────────────────
    # ────────────────────────────────────────────────────────────────────────────────

    for _ in range(maxes["chunk_ct"]+1):

        # Current block
        cur = nxt_chunk(lines, _+1)

        # Number of header types in this block
        maxes["h2"] = get_max(cur, 2) + 10
        maxes["h3"] = get_max(cur, 3) - 4
        maxes["h4"] = get_max(cur, 4) - 4
        maxes["h5"] = get_max(cur, 5) - 4
        curr_lvl = 1; char = "w"

        # ────────────────────────────────────────────────────────────────────────────
        # ─── ITERATE THROUGH CURRENT BLOCK ──────────────────────────────────────────

        iterator = 1; sub1 = 1; sub2 = 1

        iter_indent = [iterator, sub1, sub2, "+", "*", "[']"]
        iter_level = 0
        alphabet = ["1234567890", "abcdefghijklmnopqrstuvwxyz", "io^%@!io^%@!io^%@!io^%@!"]

        for index, line in enumerate(cur):


            # Don't write blank lines
            if not line:
                continue

            line = line.strip("\n")
            # Check for bullets/numbered lists
            if "[#]" in line:

                # Same indent level?
                if iter_indent[0] > 1:
                    prev = (cur[index-1]).index("[")
                    current = (cur[index]).index("[")

                    if current > prev:
                        iter_level += 1
                    if prev < current:
                        iter_level -= 1

                    if iter_level < 3:
                        line = line.replace("[#]", ("[{}]".format(alphabet[iter_level])))
                        iter_indent[iter_level] += 1
                    else:
                        try:
                            line = line.replace("[#]", ("[{}]".format(iter_indent[iter_level])))
                        except:
                            line = line.replace("[#]", ("[+]"))
                else:
                    line = line.replace("[#]", "[1]")
                    iter_indent[0] += 1

            # If the ordered list is over AND there's a new header
            elif "[#]" not in line and "##" in line:
                iter_indent[0] = 1; iter_indent[1] = 1; iter_indent[2] = 1 

            # ────────────────────────────────────────────────────────────────────────
            # ─── #HEADER# ───────────────────────────────────────────────────────────

            if "#HEADER#" in line:
                curr_lvl = 1
                output.write(tier[0]["SEP"])
                output = fig_header(options, line.replace("#HEADER# ", "").strip("\n"),\
                 output, 0, top_bar=False, bot_bar=True)
                
            # ────────────────────────────────────────────────────────────────────────
            # ─── ##1 ────────────────────────────────────────────────────────────────

            elif "##1" in line:
                curr_lvl = 1
                char = (line.replace("##1 ", ""))[1]
                output.write(tier[1]["SEP"])
                output = fig_header(options, line.replace("##1 ", "").strip("\n"),\
                 output, 1, top_bar=True, bot_bar=True)
                try:
                    if "##2" not in cur[index+1]:
                        output.write("\n\n")
                except:
                    output.write("\n\n")

            # ────────────────────────────────────────────────────────────────────────
            # ─── ##2 ────────────────────────────────────────────────────────────────

            elif "##2" in line:
                curr_lvl = 2
                output.write(tier[2]["SEP"])
                output.write(tier[2]["BAR"].format((maxes["h2"]+1)*"-"))
                extra = ((maxes["h2"] - len(line.replace("##2 ", ""))) // 2) * " "
                x = extra + "<" + line.replace("##2 ", "").replace(" ", "_") + ">" + extra
                if (maxes["h2"] - len(line.replace("##2 ", ""))) % 2 != 0:
                    x += " "
                output.write(tier[2]["T"].format(x))
                output.write(tier[2]["BAR"].format((maxes["h2"]+1)*"-") + "\n\n")

            # ────────────────────────────────────────────────────────────────────────
            # ─── ##3 ────────────────────────────────────────────────────────────────

            elif "##3" in line:
                curr_lvl = 3
                output.write(tier[3]["SEP"])
                output.write(tier[3]["T"].format(char, line.replace("##3 ", "")))
                if "##" not in cur[index+1]:
                    output.write(tier[2]["PAD"])

            # ────────────────────────────────────────────────────────────────────────
            # ─── ##4 ────────────────────────────────────────────────────────────────

            elif "##4" in line:
                curr_lvl = 4
                output.write(tier[4]["SEP"])
                output.write(tier[4]["T"].format(line.replace("##4 ","")))

            # ────────────────────────────────────────────────────────────────────────
            # ─── ##5 ────────────────────────────────────────────────────────────────

            elif "##5" in line:
                curr_lvl = 5
                output.write(tier[5]["SEP"])
                output.write(tier[5]["T"].format(line.replace("##5 ","")))

            # ────────────────────────────────────────────────────────────────────────
            # ─── #NONE# ─────────────────────────────────────────────────────────────

            elif "#NONE#" in line:
                output.write(line + "\n")

            else:

                # ────────────────────────────────────────────────────────────────────────
                # ─── Normal Text ────────────────────────────────────────────────────────

                if len(line) > (65 - curr_lvl * 5):
                    output.write(tier[curr_lvl]["TXT"].format(line[:(65 - curr_lvl * 5)]))
                    if len(line[(65 - curr_lvl * 5):]) > (65 - curr_lvl * 5):
                        output.write(tier[curr_lvl]["TXT"].format(line[(65 - curr_lvl * 5):(65 - curr_lvl * 5)*2].strip()))
                    else:
                        output.write(tier[curr_lvl]["TXT"].format(line[(65 - curr_lvl * 5):].strip()))
                else:
                    output.write(tier[curr_lvl]["TXT"].format(line.strip()))

    output.write("\n"*5)
    output.close()


def nxt_chunk(lines, chunk_num):
    i = start = 0
    count = 0
    while count <= int(chunk_num) and i < len(lines):
        if "##1" in lines[i]:
            count += 1
        i += 1
        if count <= int(chunk_num) - 1:
            start += 1
    return lines[start+1:i]


def get_max(lines, lvl, and_count=False):
    ret = ct = 0
    lvl = str(lvl).strip("##")
    for _ in lines:
        if "##" + lvl in _:
            if len(_) > ret:
                ret = len(_)
            if and_count:
                ct += 1
    return ret if not and_count else [ret, ct]


def juicer():

    temp_path = os.getcwd()
    options = vars(g_args())
    if options["show_fonts"]:
        display_fonts(); exit()
    input_path = val_path(options["path"])
    [lines, backup_log] = txt_files(input_path)
    if not options["no_backup"]:
        append_backup(lines, backup_log)
    
    if not options["rewrite"]: 
        readtype = "a"
        if os.path.isfile(options["output"]):
            if options["output"] == "__FORMATTER-OUTPUT.txt":
                readtype = "w"
            elif "o" in (input(colored("Specified output file already exists.\n[a]ppend or [o]verwrite?\n", "red"))).lower():
                readtype = "w"
        o = open(options["output"], readtype)
    else:
        o = open(options["path"], "w")
    
    for _ in range(options["downscale"]):
        tier.pop(1)
    
    # Format page header if specified
    if options["fonts"][0] != "none" and options["title_font"] != "none":
        # If no title specified, use first line and pop it from list
        if options["title"] == "none":
            o = fig_header(options, lines[0], o, 0, top_bar=True, bot_bar=True)
            lines.pop(0)
        else:
            o = fig_header(options, options["title"], o, 0)

    new_format(options, lines, o)


    if "." == options["open"][0]:
        try:
            cmd = "xdg-open " + options["output"]
            os.system(cmd)
        except:
            cmd = "start " + options["output"] + " ." 
            os.system(cmd)
            try:
                cmd = "start " + options["open"] + " " + options["output"]
                os.system(cmd) 
            except:
                try:
                    cmd = "xdg-open " + options["output"]
                    os.system(cmd)
                except:
                    cmd = "start " + options["output"] + " ." 
                    os.system(cmd)
                finally:
                    os.system(". " + options["output"])
    else:
        try:
            cmd = options["open"] + " " + options["output"]
            os.system(cmd)
        except:
            try:
                cmd = "start " + options["open"] + " " + options["output"]
                os.system(cmd) 
            except:
                try:
                    cmd = "xdg-open " + options["output"]
                    os.system(cmd)
                except:
                    cmd = "start " + options["output"] + " ." 
                    os.system(cmd)
                finally:
                    os.system(". " + options["output"])


    os.chdir(temp_path)


if __name__ == "__main__":
    juicer()