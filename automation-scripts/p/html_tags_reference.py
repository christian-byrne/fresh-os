
def get_html_tags(with_tags=None):
    tags = ['<base>', '<head>', '<link>', '<meta>', '<style>', '<title>', '<body>', '<address>', '<article>', '<aside>', '<footer>', '<header>', '<h1>, <h2>, <h3, <h4>, <h5>, <h6>', '<main>', '<nav>', '<section>', '<blockquote>', '<dd>', '<div>', '<dl>', '<dt>', '<figcaption>', '<figure>', '<hr>', '<li>' '<o>', '<ol>', '<p>', '<pre>', '<ul>', '<a>', '<abbr>', '<b>', '<bdi>', '<bdo>', '<br>', '<cite>', '<code>', '<data>', '<dfn>', '<em>', '<i>', '<kbd>','<k>' '<mark>', '<q>', '<rb>', '<rp>', '<rt>', '<rtc>', '<ruby>', '<s>', '<samp>', '<small>', '<span>', '<strong>', '<sub>', '<sup>', '<time>', '<u>', '<wb<var>', '<wbr>', '<area>', '<audio>', '<img>', '<map>', '<track>', '<video>', '<embed>', '<iframe>', '<object>', '<param>', '<picture>', '<portal>', '<source>', '<svg>', '<math>', '<canvas>', '<noscript>', '<script>', '<del>', '<ins>', '<caption>', '<col>', '<colgroup>', '<table>', '<tbody>','<td>', '<tfoot>', '<th>', '<thead>', '<tr>', '<button>', '<datalist>', '<fieldset>', '<form>', '<input>', '<label>', '<legend>', '<meter>', '<optgroup>', '<option>', '<output>', '<progress>', '<select>', '<textarea>', '<details>', '<dialog>', '<menu>', '<summary>', '<slot>', '<template>', '<acronym>', '<applet>', '<basefont>', '<bgsound>', '<big>', '<blink>', '<center>', '<content>', '<dir>', '<font>', '<frame>', '<frameset>', '<hgroup>', '<image>', '<isindex>', '<keygen>', '<listing>', '<marquee>', '<menuitem>', '<multicol>', '<nextid>', '<nobr>', '<noembed>', '<noframes>', '<pla>' '<sintext>', '<rb>', '<rtc>', '<shadow>', '<spacer>']

    if with_tags:
        if with_tags == "start" or with_tags == "open" or with_tags == "<":
            ret = []
            for _ in tags:
                ret.append(_.strip(">"))
        if with_tags == "start" or with_tags == "close" or with_tags == ">" or with_tags == "closed":
            ret = []
            for _ in tags:
                ret.append(_.strip("<"))
        else:
            return tags
    if not with_tags:
        ret = []
        for _ in tags:
            ret.append(_.strip("<").strip(">"))
    return ret
