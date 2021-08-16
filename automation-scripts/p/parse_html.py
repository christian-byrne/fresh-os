def get_path():
    import sys
    from pathlib import Path
    candidates = []
    home = str(Path.home()) + "/"

    if len(sys.argv) == 2:
        html_file = sys.argv[1]
        if ".html" not in html_file:
            html_file += ".html"
    else:
        import glob    
        for name in glob.glob(home + "*.html"):
            candidates.append(name)
        html_file = candidates[0]
    
    try:
        ret = open(home + html_file.strip(),"r")
    except:
        try:
            ret = open(home + "Desktop/" + html_file.strip(),"r")
        except:
            try:
                ret = open(home + "Documents/" + html_file.strip(),"r")
            except:
                if candidates:
                    for index, fi in enumerate(candidates):
                        try:
                            ret = open(home + fi,"r")
                        except:
                            try:
                                ret = open(home + "Desktop/" + glob.glob(home + "Desktop/" + "*.html")[index], "r")
                            except:
                                continue
    return ret


def parse_tag_name(html, tag="table"):
    """
    parses html file looking for lines that contain the 
    given tag name. tries to validate similar tag names.
    Returns a dict following format of 'line' : 'tag'
    """
    # Split into list with separator "</"
    raw = html.readlines()
    lines = []
    for l in raw:
        _ = l.split("</")
        lines += _

    # Backup tags for correction. Else just use the passed arg as searched tag
    tags = {
        "table": ["table", "tabel", "tab", "th", "tr", "td", "tl"],
        "image": ["img", "picture", "icon", "pic"],
        "link": ["url", "href", "hyperlink", "hyper","address"],
        "video": ["vid", "iframe", "src", "embed", "object"]
    }
    if tag not in tags.keys():
        if tag in ["table", "tabel", "tab", "th", "tr", "td", "tl"]:
            tag = "table"
        else:
            for p, z in zip(tags.values(), tags.keys()):
                for _ in p:
                    if tag == _:
                        tag = z

    # Find matches      
    line_hits = {}; ret = {}
    for candidate in tags[tag]:
        for line in lines:
            # Don't include the lines that are just tag> (as result of split separator)
            # Don't include tags that are part of the innerHTML but not between <>
            if "<" + candidate + ">" in line:
                # Don't include lines that are just <tag> or </tag>
                if len(line) > ( len(candidate) + 2 ):
                    line_hits[line] = candidate

    from html_tags_reference import get_html_tags
    tag_ref = get_html_tags()
    for keys, values, in zip(line_hits.keys(), line_hits.values()):
        _ = keys.split("<")
        _.reverse()
        x = _[0].split()
        if x[0] in tag_ref and len(x) > 1:
            z = "".join(x[1:])
        else:
            z = "".join(x)
        r = z.strip(">").strip("<").split(">")
        if len(r) > 1:
            _ = "".join(r[1:])
        else:
            _ = str(r[0])
        ret[_] = values
    if ret:
        return ret

###
### DON'T USE THIS FUNCTION UNLESS YOU ARE GETTING FORMATTING PROBLEMS WITHOUT IT
###
def get_inner_html(lines):
    """
    Accepts dict following format of 'line' : 'tag'.
    Parses the text data from between the given tags.
    Returns list of the text data separated by 
    occurrence in html file.
    """
    ret = []
    for line, tag in zip(lines.keys(), lines.values()):
        for index, character in enumerate(line):
            if character == "<":
                start_index = index + 1
                hit = True
                for t_char in tag:
                    if t_char != line[start_index]:
                        hit = False
                    start_index += 1
                if hit:
                    end_index = start_index + len(tag)
                    try:
                        while line[end_index] != "<" and line[end_index+len(tag)+1] != ">":
                            end_index += 1
                        ret.append(line[start_index:end_index]) 
                    except:
                        ret.append(line[start_index:])
    return ret     


def stdout_ret(usr_dict, printf=None):
    """
    return list of values and optionally
    print to stdout by line for purpose of batch usage
    """
    if printf:
        for value, key in zip(usr_dict.values(), usr_dict.keys()):
            print("____TAG NAME: " + value + "\n")
            for _ in key:
                print(key)
            print("\n----------------------------------\n")

    ret = []
    for key in usr_dict.keys():
        ret.append(key)
    return ret


def cntrl_f(string_list, expression):
    ret = []
    for _ in string_list:
        if expression in _ and "demo" not in _:
            ret.append(_)
    return ret


def parse_html():
    html = get_path()
    hits = parse_tag_name(html)
    re = stdout_ret(hits)
    import sys
    if len(sys.argv) == 3:
        search_expression = sys.argv[2]
        re = cntrl_f(re, search_expression)
    if len(sys.argv) == 4:
        search_expression = sys.argv[3]
        re = cntrl_f(re, search_expression)

    out = open("HTML_parse_output.txt", "w")
    for _ in re:
        print(_)
        out.write(_ + "\n")
    out.close()


if __name__ == "__main__":
    print("python3 parse_html.py $file_name$ [search_expression] [search_expression] \n\n\
        If HTML file not in Desktop or Login Directory,\n\
            include the absolute path in the file name\n\
                Prints to stdout and to text file in python_scripts folder\n\n\n")
    parse_html()