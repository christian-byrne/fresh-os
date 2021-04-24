import os, time, sys, webbrowser
from termcolor import colored, cprint
from pynput.keyboard import Key, Controller
keyboard = Controller()

from term_gui import term_gui, make_header

def ctrl_letter(char):
    char = str(char)
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


def press_tab():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)


def press_arrow_keys(list_arrows):
    for direction in list_arrows:
        keyboard.press(Key[direction])
        keyboard.release(Key[direction])


def exit_program():
    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)


def open_links(gui):
    num_extensions = 0
    extensions = {
        "core" : ["https://chrome.google.com/webstore/detail/imagus/immpkjjlgappgfkkfieppnmlhakdmaab",\
                  "https://chrome.google.com/webstore/detail/session-buddy/edacconmaakjimmfgnblocblbcdcpbko"],
        "cookie cleaners" : [
                  "https://chrome.google.com/webstore/detail/i-dont-care-about-cookies/fihnjjcciajhdojfnbdddfaoknhalnja",\
                  "https://chrome.google.com/webstore/detail/cookie-autodelete/fhcgjolkccmbidfldomjliifgaodjagh"],
        "UI preferences" : [
                  "https://chrome.google.com/webstore/detail/old-reddit-redirect/dneaehbmnbhcippjikoajpoabadpodje",\
                  "https://chrome.google.com/webstore/detail/hacker-vision/fommidcneendjonelhhhkmoekeicedej"],
        "URL cleaners" : [ "https://chrome.google.com/webstore/detail/clearurls/lckanjgmijmafbedllaakclkaicjfmnk"],
        "dev tools" : ["https://chrome.google.com/webstore/detail/crx-extractordownloader/ajkhmmldknmfjnmeedkbkkojgobmljda?hl=en-US"],
        "basic privacy" : ["https://chrome.google.com/webstore/detail/duckduckgo-privacy-essent/bkdgflcldnnnapblkhphbgpggdiikppg",\
                  "https://chrome.google.com/webstore/detail/https-everywhere/gcbommkclmclpchllfjekcdonpmejbdp",\
                  "https://chrome.google.com/webstore/detail/privacy-badger/pkehgijcmpdhfbdbbnkijodmdjhbjlgp",\
                  "https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm",\
                  "https://chrome.google.com/webstore/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj",\
                  "https://chrome.google.com/webstore/detail/localcdn/njdfdhgcmkocbgbhcioffdbicglldapd",\
                  "https://chrome.google.com/webstore/detail/privacy-settings/ijadljdlbkfhdoblhaedfgepliodmomj",\
                  "https://chrome.google.com/webstore/detail/blend-in-and-spoof-most-p/pmhjnoimpcanemmhpkoakibmjhdenffk",\
                  "https://chrome.google.com/webstore/detail/incognito-homepage/lobiipjnbhchdplbbfcndkjinfcdnehb?hl=en"],
        "anti fingerprint" : [
                  "https://chrome.google.com/webstore/detail/url-tracking-stripper-red/flnagcobkfofedknnnmofijmmkbgfamf",\
                  "https://chrome.google.com/webstore/detail/canvas-blocker-fingerprin/nomnklagbgmgghhjidfhnoelnjfndfpd/related",\
                  "https://chrome.google.com/webstore/detail/css-exfil-protection/ibeemfhcbbikonfajhamlkdgedmekifo",\
                  "https://chrome.google.com/webstore/detail/ping-blocker/jkpocifanmihboebfhigkjcdihgfcdnb",\
                  "https://chrome.google.com/webstore/detail/cydec-platform-anti-finge/becfjfjckdhngmmpkhakoknnkgpgfelk",\
                  "https://chrome.google.com/webstore/detail/font-fingerprint-defender/fhkphphbadjkepgfljndicmgdlndmoke",\
                  "https://chrome.google.com/webstore/detail/redirect-amp-to-html/kifkmmpiicbcnkjaliilaoeaojlldonl",\
                  "https://chrome.google.com/webstore/detail/tracking-token-stripper/kcpnkledgcbobhkgimpbmejgockkplob",\
                  "https://chrome.google.com/webstore/detail/audiocontext-fingerprint/pcbjiidheaempljdefbdplebgdgpjcbe"],
        "extreme privacy" : [
                  "https://chrome.google.com/webstore/detail/site-bleacher/mlcfcepfmnjphcdkfbfgokkjodlkmemo",\
                  "https://chrome.google.com/webstore/detail/privacy-redirect/pmcmeagblkinmogikoikkdjiligflglb"]
    }

    for color, category in zip((gui["cool color"])*4, extensions.keys()):

        if "y" in input(colored(f"\nInstall {category} Extensions? [y/n]\n", color)).lower():
            num_extensions += len(extensions[category])
            for link in extensions[category]:
                webbrowser.open(link, autoraise=False)
            try:
                keyboard.press(Key.alt)
                time.sleep(.2)
                keyboard.press(Key.tab)
                time.sleep(.1)
                keyboard.release(Key.alt)
                keyboard.release(Key.tab)
            except:
                continue
    return num_extensions


def send_keys(n):
    keyboard.press(Key.alt)
    time.sleep(.2)
    keyboard.press(Key.tab)
    time.sleep(.1)
    keyboard.release(Key.alt)
    keyboard.release(Key.tab)
    for _ in range(n):
        time.sleep(.2)
        for _ in range(4):
            time.sleep(.2)
            keyboard.press(Key.tab)
            time.sleep(.1)
            keyboard.release(Key.tab)
            time.sleep(.1)
        time.sleep(.3)
        keyboard.press(Key.enter)
        time.sleep(.2)
        keyboard.release(Key.enter)
        time.sleep(.1)

        # dialog
        time.sleep(.3)
        keyboard.press(Key.tab)
        time.sleep(.2)
        keyboard.release(Key.tab)
        time.sleep(.3)
        keyboard.press(Key.enter)
        time.sleep(.2)
        keyboard.release(Key.enter)
        time.sleep(.1)

        # close tab
        time.sleep(.1)
        ctrl_letter("w")
        time.sleep(.5)


def dl_crx():
    Terminal = term_gui()
    num_extensions = open_links(Terminal.gui)
    if "n" in input(colored("\n\nAutomate Download Clicks by Sending Keystrokes? [y/n]\n", "cyan")).lower():
        if "y" in input(colored("\nAre you sure? [y/n]\n","red")).lower():
            return None
    send_keys(num_extensions)


if __name__ == "__main__":
    dl_crx()
