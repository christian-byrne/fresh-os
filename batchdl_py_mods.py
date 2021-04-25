import sys, time, os, subprocess
from term_gui import term_gui, make_header


def install_module(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def module_choices():
    # ANACONDA
    modules = {
        "media tools": {
            "ffmpeg": "FFmpeg is a free and open-source software project consisting of a large suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the FFmpeg program itself, designed for command-line-based processing of video and audio files.",
            "youtube-dl": "youtube-dl is an open-source download manager for video and audio from YouTube and over 1000 other video hosting websites. It is released under the Unlicense software license. As of April 2021, youtube-dl is one of the most starred projects on GitHub, with over 93.7k stars",
            "moviepy": "MoviePy (full documentation) is a Python library for video editing: cutting, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects. See the gallery for some examples of use.MoviePy can read and write all the most common audio and video formats, including GIF, and runs on Windows/Mac/Linux, with Python 2.7+ and 3 (or only Python 3.4+ from v.1.0).",
            "pillow": "Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors. As of 2019, Pillow development is supported by Tidelift.",
            "opencv-python": "OpenCV, a.k.a Open Source Computer Vision is a python package for image processing. It monitors overall functions that are focused on instant computer vision. Although OpenCV has no proper documentation, according to many developers, it is one of the hardest libraries to learn. However, it does provide many inbuilt functions through which you learn Computer vision easily.",
            "theano": "Theano is a python library and a compiler for feasible computer programs – aka an optimizing compiler. It can analyze, describe, optimize, and influence different mathematical declarations at the same time. As Theano makes the best use of multi-dimensional arrays, you hardly have to worry about the perfection of your projects."
        },
        "automation": {
            "pynput": "This library allows you to control and monitor input devices.\nCurrently, mouse and keyboard input and monitoring are supported.",
            "selenium": "Python language bindings for Selenium WebDriver.",
            "howdoi": "Stuck on a coding problem? Wish to visit StackOverflow without leaving the terminal? With howdoi, you can do it!"
        },
        "web/network": {
            "requests": "Requests is a rich Python HTTP library. Released under Apache2.0 license, Requests is focused on making HTTP requests more responsive and user-friendly. This python library is a real blessing for beginners as it allows the use of most common methods of HTTP. You can easily customize, inspect, authorize, and configure HTTP requests using this library.",
            "urllib3": "urllib3 is a powerful, user-friendly HTTP client for Python. Much of the Python ecosystem already uses urllib3 and you should too. urllib3 brings many critical features that are missing from the Python standard libraries:",
            "Flask": "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.\n\nFlask offers suggestions, but doesn’t enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.",
            "Django": "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.",
            "mod-wsgi": "The mod_wsgi package provides an Apache module that implements a WSGI compliant interface for hosting Python based web applications on top of the Apache web server.",
            "pyquery": "pyquery allows you to make jquery queries on xml documents. The API is as much as possible the similar to jquery. pyquery uses lxml for fast xml and html manipulation."
        },
        "dev-tools-general": {
            "datetime": "date and time tools",
            "python-dateutil": "The dateutil module provides powerful extensions to the standard datetime module, available in Python.",
            "Delorean": "Delorean is a python library for enhancing DateTime. With Delorean, as the name suggests, you can easily organize the time for your python projects. All it needs is an authentic DateTime object (which should be Python-based) to work. Moreover, it can work quite well with other python DateTime libraries, as well.",
            "path.py": "path tools",
            "sh": "sh is a full-fledged subprocess replacement for Python 2.6 - 3.8, PyPy and PyPy3 that allows you to call any program as if it were a function: from sh import ifconfig\nprint(ifconfig('eth0'))",
            "psutil": "cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network) in Python.",
            "geopy": "geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources."
        },
        "gui-dev": {
            "wxPython": "wxPython is a GUI toolkit for python. It is a powerful wrapper for many computer software that can be implemented on a variety of digital platforms. Many professionals have found wxPython very effective as an alternative to Tkinter. It is applied as an extension module of Python.",
            "tkinter": " A GUI toolkit contains widgets that are used to create a graphical interface. Python includes a wide range of Interface implementations available, from TkInter (it comes with Python, ) to a variety of various cross-platform solutions, such as PyQt5, which is known for its more sophisticated widgets and sleek look.",
            "pyqt5": "Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development.\nPyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.\nPyQt5 may also be embedded in C++ based applications to allow users of those applications to configure or enhance the functionality of those applications.",
            "nltk": "NLTK a.k.a Natural language toolkit is one of the most popular python NLP libraries. It is a set of language processing libraries and other programs that cumulatively provide a numerical and symbolic language processing solution for English only. It is written in Python. With NLTK, natural language processing with python has become more standard and ideal.",
            "pygame": "PyGame is a wrapper module for Python. It is a set of python functions and classes dedicated to writing video games mainly. However, you can also write other multi-media applications with PyGame as well. These applications and games are highly consistent. PyGame is a community-driven project since 2000, and for beginners, it is really easy to learn.",
            "docopt": "docopt creates beautiful command-line interfaces",
            "emjoi": "Emojis have become a way to express and to enhance simple boring texts. Now, the same gems can be used in Python programs too. Yes, really! You now have the ultimate power to use emojis in your code. For this, emoji module is needed to be installed."
        },
        "database-dev": {
            "SQLAlchemy": "Our next one on the list is a Database Abstraction Library for Python. SQLAlchemy comes with astounding support for a broad range of databases and layouts as possible. It provides a professional level of consistent patterns, developed for efficiency. It is easy to understand; for beginners as well. And featured with a really adjustable system."
        },
        "os-dev": {
            "pycos": "asyncoro is a Python framework for asynchronous, concurrent, network, distributed programming and distributed computing, using generator functions, asynchronous completions and message passing. asyncoro can be used to create coroutines with generator functions, similar to the way threads are created with functions with Python’s threading module. Programs developed with asyncoro have same logic and structure as programs with threads, except for a few syntactic changes - mostly using yield with asynchronous completions that give control to asyncoro’s scheduler, which interleaves executions of generators, similar to the way an operating system executes multiple processes."
        },
        "parsing": {
            "flashtext": "FlashText is another python library that offers easy search and replacement of words from documents. All FlashText needs is a set of words and string. Then it identifies some words as keywords and replaces them from Text Data. It is a very effective library. People who are struggling with word replacement can choose it with confidence.",
            "beautifulsoup4": "BeautifulSoup is a great python library. It is used for parsing. It can parse different broken HTML and XML documents, as well. It offers an easy way for web scraping by extracting direct data from HTML. Many professionals are really happy with its amazing performance. It can save quite a lot of time on your day.",
            "textblob": "TextBlob is one of the most simplified Python NLP libraries – for textual data processing. It is available both in Python 2.0 and Python 3.0. We mentioned the word “simplified” because this natural language processing python library comes with a very simple API, which does the job of different NLP related tasks with full efficiency. Beginners will enjoy this simple API for the first time, so as the professionals.",
            "irlib": "I started writing this library as part of my `Information Retrieval and Natural Language Processing (IR and NLP)",
            "rdflib": "construct a triple store, load it from an RDF file, and search through it - easy to install, no dependencies that I know of, small and easy, haven't been able to figure out how to do much with it",
            "wikipedia": "As if howdoi wasn’t enough, we can now import the entire Wikipedia! Yes, We can now import Wikipedia in Python using Wikipedia module. Use the incessant flow of knowledge with Python for daily needs"
        },
        "data/ml": {
            "matplotlib": "Matplotlib is a Python library that uses Python Script to write 2-dimensional graphs and plots. Often mathematical or scientific applications require more than single axes in a representation. This library help_short us to build multiple plots at a time. You can, however, use Matplotlib to manipulate different characteristics of figures as well.",
            "scikit-learn": "Scikit learn is a simple and useful python machine learning library. It is written in python, cython, C, and C++. However, most of it is written in the Python programming language. It is a free machine learning library. It is a flexible python package that can work in complete harmony with other python libraries and packages such as Numpy and Scipy.",
            "pandas": "Pandas is a python software package. It is a must to learn for data-science and dedicatedly written for Python language. It is a fast, demonstrative, and adjustable platform that offers intuitive data-structures. You can easily manipulate any type of data such as – structured or time-series data with this amazing package.",
            "keras": "People who want to learn deep neural networks, Keras can be a real good choice for them. Keras is an open-source deep neural network library. It is written in Python. Keras provides an effective inspection policy over detailed networks. Developers who work with Keras are impressed with its user-friendly and modular structure.",
            "tensorflow": "TensorFlow is a free, open-source python machine learning library. It is very easy to learn and has a handful collection of useful tools. However, it is not limited to machine learning only; you can also use it for dataflow and programs that are differentiable. You can easily get to work with TensorFlow by installing Colab Notebooks in any browser you use.",
            "scipy": "Scipy is an open-source python library that is used for both scientific and technical computation. It is a free python library. And very suitable for machine learning. However, computation is not the only task that makes scipy special. It is also very popular for image manipulation, as well.",
            "torch": "PyTorch is an open-source python machine learning library. It is based on the Torch library and was initially developed by the A.I researcher group of facebook. The good thing about PyTorch is, it can be used for multi- variational applications like computer vision and NLP (natural language processing) as well.",
            "bokeh": "Bokeh is a data visualization library for python. It allows interactive data visualization. It is a special package, and it works quite differently than other data visualization libraries. This is because Bokeh uses HTML and JavaScript to provide its graphics, which makes it a reliable platform for contributing to dashboards and applications that are web-based.",
            "networkx": "NetworkX is another python package. It offers immense solutions for studying and diagnosing graphs of all levels. It also helps you to develop and influence the architecture, motion, and functionalities of high-quality networks. It is a free python package and released under the new BSD license."
        },
        "remember": {
            "pywin32": "Python extensions for Microsoft Windows Provides access to much of the Win32 API, the ability to create and use COM objects, and the Pythonwin environment.",
            "py2exe": "py2exe is a Python Distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a Python installation.Spice",
            "cryptography": "cryptography is a package which provides cryptographic recipes and primitives to Python developers. Our goal is for it to be your “cryptographic standard library”. It supports Python 3.6+ and PyPy3 7.2+.cryptography includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions. For example, to encrypt something with cryptography’s high level symmetric encryption recipe:"
        }
    }

    Terminal = term_gui()
    colors = Terminal.gui["all color"]*40
    hicolors = Terminal.gui["bright color"]*20
    lowcolors = ["cyan", "magenta", "blue"]*35
    from termcolor import colored
    from emoji import emojize

    for cindex, (category, contents) in enumerate(modules.items()):
        pallette = [
            Terminal.complement[hicolors[cindex]],
            hicolors[cindex+2],
            Terminal.complement[hicolors[cindex+2]],
        ]
        help_short = (
            colored(
                "\n[C]ategory DL", pallette[0]),
            colored(
                "[A]ll DL", pallette[1]),
            colored(
                "Prin[t] All Info", pallette[2]),
            colored(
                "[i#] Info on #", pallette[0]),
            colored(
                "[#],[#],... Skip #'s", pallette[1])
        )
        help_long = (
                colored("\n\n Download All in" +" [C]ategory", colors[cindex+1]),
                colored("\n Download" + " [A]ll (in all categories)",  colors[cindex+2]),
                colored("\n Prin" + "[t] Info on All\n",  colors[cindex+3]),
                colored("[i#] for more Info on a Module (eg 'i2' for module 2 info)\n", colors[cindex+4]),
                colored("[#],[#],[#],... to Skip Over (not download) those Numbers", colors[cindex+5]) 
        )

        print(colored(
            make_header(60, category.upper(), tiers=3),
            hicolors[cindex])
            )
        for index, mod in enumerate(contents.keys()):
            print(colored(
                str(index) + " = " + mod,
                hicolors[cindex])
            ) 
       
        print(*help_long)
        stdin = input("")
        buffer_length = 0

        while not stdin[0].isnumeric() and stdin.lower() not in ["c", "quit", "exit"]:

            # Verify DL [A]ll
            if stdin.lower() == "a":
                if "y" in input("\nDownload every module in all future categories? [y/n]\n").lower():
                    break
                else:
                    print("Enter a new command:"); stdin = ""

            # i[#] info
            elif "i" in stdin:
                try:
                    dindex = int(stdin[1:])
                except:
                    try:
                        dindex = int(stdin[2:])
                    except:
                        try:
                            dindex = int(stdin[-1])
                        except:
                            dindex = 1
                try:
                    descrip = (list(contents.keys()))[dindex]
                except:
                    try:
                        descrip = (list(contents.keys()))[
                            int(stdin[-2])+int(stdin[-1])]
                    except:
                        try:
                            descrip = (list(contents.keys()))[int(stdin[-1])]
                        except:
                            descrip = (list(contents.keys()))[-1]

                print(colored(
                        make_header(42, descrip.upper(), character="-", boxed=True, centered=True, tiers=3),
                        colors[buffer_length % 7+1]),
                    "\n", (contents[descrip]).strip().replace(". ", ".\n"), "\n", 
                    colored("[R]eshow commands", "grey"))
                buffer_length += len(contents[descrip]) + 80*6

            # Prin[t] all info
            elif stdin.lower() == "t":
                for index, title in enumerate(contents.keys()):
                    print(colored(
                            make_header(42, title.upper(), boxed=True, character="-", centered=True, tiers=3),
                            lowcolors[index]),
                        "\n", contents[title].strip().replace(". ", ".\n")
                    )
                time.sleep(1.2)

            elif stdin.lower() != "r":
                print("\nInvalid Command. Enter a new Command:\n")

            # [R]eshow commands / or if terminal full (80 characters/line x 24 lines)
            if stdin.lower() == "r" or buffer_length > 80*24 or stdin.lower() == "t":
                if buffer_length > 80*24:
                    time.sleep(1.2)
                print("\n")
                for index, pkg in enumerate(contents.keys()):
                    print(colored(
                        str(index) + " = " + pkg,
                        hicolors[cindex])
                    )
                print(*help_short)
                buffer_length = 0

            stdin = input("")

        # [#] [#] [#]
        if stdin[0].isnumeric():
            candidates = [ _ for _ in range( len(contents.keys()) ) ]
            elim_index = []
            for char in [" ", ","]:
                for _ in stdin.split(char):
                    try:
                        elim_index.append( int(_.strip()) )
                    except:
                        try:
                            elim_index.append( int(_[-1].strip()) )
                        except: pass
            queue = [ list(contents)[_] for _ in candidates if _ not in elim_index ]
            for i, _ in enumerate(queue):
                print(colored(
                        make_header(60, ("downloading " + _ + " . . ."), tiers=2),
                        lowcolors[i]))
                try:
                    print(emojize(":thumbs_up:"))
                except: pass
                print(); install_module(_)

        # [C]ategory
        elif stdin.lower() == "c":
            for i, _ in enumerate(contents.keys()):
                print(colored(
                        make_header(60, ("downloading " + _ + " . . ."), tiers=2),
                        lowcolors[i]))
                try:
                    print(emojize(":thumbs_up:"))
                except: pass
                install_module(_)

        # [A]ll
        elif stdin.lower() == "a":
            for section in modules.keys():
                for i, _ in enumerate(modules[section].keys()):
                    print(colored(
                            make_header(60, ("downloading " + _ + " . . ."), tiers=2),
                            lowcolors[i]))
                    try:
                        print(emojize(":thumbs_up:"))
                    except: pass
                    install_module(_)


def get_modules(fresh=True):
    if fresh:
        install_module("termcolor")
        install_module("emoji")
        install_module("fire")
    module_choices()


if __name__ == "__main__":
    get_modules()