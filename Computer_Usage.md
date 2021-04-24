
-----------------------------------
	   <RUNNING_HEAD >
-----------------------------------
	
<!-- ________Recently Learned________ -->


	<!-- ABRIDGED -->


	grep --exclude=GLOB
	
	xdg-open $URL$
	
	--prefix=sudo
	
	&   &&
	
	
	
	tail
	
	setvtrgb 
	
	unsigned repositories: sudo apt-add-repository -r
						   sudo apt-get update --allow-unauthenticated
						   
						   
	<!-- HIGHLY USEFUL -->
	
	 sudo apt-add-repository ppa:ubuntu-on-rails/ppa --allow-unauthenticated

	_____________________________________________
	[4.22] sudo !! and !sudo
	
		   [1] sudo !! 
		   	   execute the last command taken from 
		   	   the history with sudo in the beginning.
		   [2] !sudo 
		       execute the last command in the history
		       that started with sudo.

	_____________________________________________
	[4.22] CTRL-A
	 
	brings you at the beginning of the line in a 
	linux terminal and CTRL-E to the end.


	_____________________________________________
	[4.22] Finding applications to solve problems
		   (when you know the problem but don't know what apps exist for it)
	
		   apt-cache search $keyword for related applications$
		   info apt-cache
		   
		   Example:
		   apt-cache search clipboard 
		   (trying to find a prorgam that allows redirecting to clipboard)
	
	_____________________________________________
	[4.22] Finding built-in programs/functions to solve problems
	
		   man -k $keyword$
		   
		   info | grep $keyword$
		   
		   help | grep $keyword$
		   
	_____________________________________________
	[4.22] Redirecting to clipboard
		   cat [file] | cb 
		   (cb is alias for clipboard)
		   
		   Examples:
		   info wget --where | xargs zcat | grep URL --exclude=K -A 4 | clipboard



	<!-- MODERATELY USEFUL -->
	
	
	_____________________________________________
	[5] ^ caret

		find and replace sequence from previous command
		replace 1st occurrence of ?restart? w/ ?status? -> run
	

	_____________________________________________
	[7] >,<,>>,<< (redirect)

		> redirect output
		$echo "hello" > file.txt
		
		< redirect input
		$ cat < file.txt
		
		>> append lines
		> empty and overwrite the file
		

	_____________________________________________
	[4.22] Copying man pages
	
		   append to a text file:
		   info [function] --where | xargs zcat >> ~/Desktop/Guides/Computer_U*
					  
		   pipe to clipboard
		   info wget --where | xargs zcat | grep URL --exclude=K -A 4 | clipboard
	
	_____________________________________________
	[4.22] listing all bash commands and searching for functinoality
		   info coreutils
		   info coreutils | grep $keyword$
		   
	_____________________________________________
	[1] xdg-open $any file$
	
		opens a file or URL in the user's preferred application
	
		xdg-open {file | URL}
		xdg-open {--help | --manual | --version}
	
	
	<!-- SOMEWHAT USEFUL -->
					    
	_____________________________________________
	[4.22] grep before and after
		
		  grep $keyword$ -A $number of lines$
	
		  Output control:
		  -m, --max-count=NUM       stop after NUM selected lines
		  -b, --byte-offset         print the byte offset with output lines
		  -n, --line-number         print line number with output lines
			  --line-buffered       flush output on every line
		  -H, --with-filename       print file name with output lines
		  -h, --no-filename         suppress the file name prefix on output
			  --label=LABEL         use LABEL as the standard input file name prefix
		  -o, --only-matching       show only nonempty parts of lines that match
		  -q, --quiet, --silent     suppress all normal output
			  --binary-files=TYPE   assume that binary files are TYPE;
				                    TYPE is 'binary', 'text', or 'without-match'
		  -a, --text                equivalent to --binary-files=text
		  -I                        equivalent to --binary-files=without-match
		  -d, --directories=ACTION  how to handle directories;
				                    ACTION is 'read', 'recurse', or 'skip'
		  -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
				                    ACTION is 'read' or 'skip'
		  -r, --recursive           like --directories=recurse
		  -R, --dereference-recursive  likewise, but follow all symlinks
			  --include=GLOB        search only files that match GLOB (a file pattern)
			  --exclude=GLOB        skip files that match GLOB
			  --exclude-from=FILE   skip files that match any file pattern from FILE
			  --exclude-dir=GLOB    skip directories that match GLOB
		  -L, --files-without-match  print only names of FILEs with no selected lines
		  -l, --files-with-matches  print only names of FILEs with selected lines
		  -c, --count               print only a count of selected lines per FILE
		  -T, --initial-tab         make tabs line up (if needed)
		  -Z, --null                print 0 byte after FILE name

		Context control:
		  -B, --before-context=NUM  print NUM lines of leading context
		  -A, --after-context=NUM   print NUM lines of trailing context
		  -C, --context=NUM         print NUM lines of output context
		  -NUM                      same as --context=NUM
			  --color[=WHEN],

	





	<!-- VERY USEFUL ON RARE OCCASIONS -->
	
	_____________________________________________
	[2] Find syntax errors in file:
	
		cd /etc/apache2
		Then:
		apache2ctl configtest
	
	
	<!-- SOMEWHAT USEFUL ON RARE OCCASIONS -->
	_____________________________________________
	[3] Display Dir Size
	
		sudo du -sh /$path$
	
		s - Display only total size of the specified directory
			(do not display file size totals for subdirectories)
		h - Print sizes in a human-readable format (h).

	_____________________________________________
	[4] figlet -f [font] string 




	
	_____________________________________________
	[6] systemctl
	
		sudo systemctl restart httpd

		Unit Commands:
		  list-units [PATTERN...]             List units currently in memory
		  list-sockets [PATTERN...]           List socket units currently in memory,
				                              ordered by address
		  list-timers [PATTERN...]            List timer units currently in memory,
				                              ordered by next elapse
		  start UNIT...                       Start (activate) one or more units
		  stop UNIT...                        Stop (deactivate) one or more units
		  reload UNIT...                      Reload one or more units
		  restart UNIT...                     Start or restart one or more units
		  try-restart UNIT...                 Restart one or more units if active
		  reload-or-restart UNIT...           Reload one or more units if possible,
				                              otherwise start or restart
		  try-reload-or-restart UNIT...       If active, reload one or more units,
				                              if supported, otherwise restart
		  isolate UNIT                        Start one unit and stop all others
		  kill UNIT...                        Send signal to processes of a unit
		  clean UNIT...                       Clean runtime, cache, state, logs or
				                              configuration of unit
		  is-active PATTERN...                Check whether units are active
		  is-failed PATTERN...                Check whether units are failed
		  status [PATTERN...|PID...]          Show runtime status of one or more units
		  show [PATTERN...|JOB...]            Show properties of one or more
				                              units/jobs or the manager
		  cat PATTERN...                      Show files and drop-ins of specified units
		  set-property UNIT PROPERTY=VALUE... Sets one or more properties of a unit
		  help PATTERN...|PID...              Show manual for one or more units
		  reset-failed [PATTERN...]           Reset failed state for all, one, or more
				                              units
		  list-dependencies [UNIT...]         Recursively show units which are required
				                              or wanted by the units or by which those
				                              units are required or wanted
	
	
	
<!-- ________Recently Used________ -->

	
	info [add-apt-repository] [apt-get] [wget]

	info apt-secure
	(trying to fix signing of repository)
	
	info wget
	(learning about wget)
	
	
	
		
<!-- ________Learning Journal________ -->



	______________________________________________________________________
	<u Learning how to unzip .gz files>
		[1] man -k gz
			>> uz
		[2] uz ~/*.gz
	
	______________________________________________________________________
	<u Trying to find out how to copy man pages for wget to my notes>
	
		[1] man -k copy
		[2] info cp
		[3] info wget --where
				(show location of man page for wget)
				>> /usr/share/info/wget.info.gz
		[4] man -k zip
				(finding the function for cat-ing a gz file)
		[5] man -k zip | grep print
		[6] man -k zip | grep page
				(filtering zip related commands for cat-like function)
		[7] info | grep zip
				(using info + grep because can't find the function)
				>> zmore: (gzip)Overview
		[8] zmore ../../usr/share/info/wget.info.gz
				(more'ing the man page to check if correct)
		[9] (release zmore will not be good for piping output)
		[1]	man -k gzip
				(searching for a cat function for zipped fileS)
		[2] info zcat
				(trying "zmore" but replacing more with cat)
				>> it exists
		[3] zcat ../../usr/share/info/wget.info.gz
				(works)
		[4] zcat ../../usr/share/info/wget.info.gz > temp.txt; gedit temp.txt
				(cat the zipped file, redirect to temp.txt, open temp.txt)
	


	______________________________________________________________________
	<u How can I redirect to my clipboard? >
	
		[1] man -k clipboard
			>> xclipboard
		[2] man xclipboard
			>> it is a program with a GUI
		[3] info xclipboard
			>> xclipboard [ -toolkitoption ... ] [ -w ] [ -nw ]
		[4] info xclipboard | grep SEE ALSO
			>> only printed the line that the word occurred
		[5] grep --help
			(finding how to control lines before/after)
		[6] info xclipboard | grep SEE ALSO -A 3
			(print three lines after) 
			>> X(7), xcutsel(1), xterm(1), 
			   individual client documentation for how to make 
			   a selection and send it to the CLIPBOARD.
		[7] man xcutsel
		[8] Better to Google this, found clipboard-cli program
		[9] it says it is installed through npm
		[1] apt-cache search clipboard
		[2] apt-cahce search clipboard | grep GTK --exclude=xfce
			(excluding for xfce desktops)
		[3] Just going to use npm
			info npm
			npm --help
			npm install -g clipboard-cli
		[4] forget permissions
			sudo npm install -g clipboard-cli
		[5] cd; nano .bashrc -> alias cb=clipboard
			
		
-----------------------------------
	   		<MANUALS>
-----------------------------------


	
<!-- _____info_____ -->

	
	Usage: info [OPTION]... [MENU-ITEM...]


	info coreutils
	
	_______________________________________
	<! Options !>
	Frequently-used options:
	  -a, --all                    use all matching manuals
	  -k, --apropos=STRING         look up STRING in all indices of all manuals
	  -d, --directory=DIR          add DIR to INFOPATH
	  -f, --file=MANUAL            specify Info manual to visit
	  -h, --help                   display this help and exit
		  --index-search=STRING    go to node pointed by index entry STRING
	  -n, --node=NODENAME          specify nodes in first visited Info file
	  -o, --output=FILE            output selected nodes to FILE
	  -O, --show-options, --usage  go to command-line options node
		  --subnodes               recursively output menu items
	  -v, --variable VAR=VALUE     assign VALUE to Info variable VAR
		  --version                display version information and exit
	  -w, --where, --location      print physical location of Info file

	The first non-option argument, if present, is the menu entry to start from;
	it is searched for in all 'dir' files along INFOPATH.
	If it is not present, info merges all 'dir' files and shows the result.
	Any remaining arguments are treated as the names of menu
	items relative to the initial node visited.


	_______________________________________
	<! BROWSE MANUAL THROUGH CHAPTER/SECTION INDEX !>
	[1] info -> H -> scroll through and select chapters
		such as invoking info, cursor commands, scrolling commands,
		index commands, xref commands, window commands, printing nodes,
		mescellaneous commands, variables, colors and styles,
		custom key bindings
		
		
	_______________________________________
	<! BROWSE MANUAL BY PAGE !>
	[1] info
		more all commands by category 
		(compression, basics, emacs, editors, development, etc.)

	[2] info bash
		list of options that can be appended to most bash function calls
		general info about the shell commands and bash functions
	

	_______________________________________
	<! info [function/program] | grep [keyword] !>
	[1] info | grep editor
		show all editor cli functions/tools
	_______________________________________
	[2] info | grep zip
		list of all zip file related functions 
		(gunzip, gzexe: compress executables, 
		zcat (decmopress to sdout), zdiff, 
		zforce (force .gz extension), 
		zgrep (search compressed files), 
		zmore (decompress by page))
 
 
	_______________________________________
	<! Examples !>
	  info                         		show top-level dir menu
	  info info-stnd               		show the manual for this Info program
	  info emacs                   		start at emacs node from top-level dir
	  info emacs buffers           		select buffers menu entry in emacs manual
	  info emacs -n Files          		start at Files node within emacs manual
	  info '(emacs)Files'          		alternative way to start at Files node
	  info --show-options emacs    		start at node with emacs' command line options
	  info --subnodes -o out.txt emacs	dump entire emacs manual to out.txt
	  info -f ./foo.info           		show file ./foo.info, not searching dir




<!-- _____help_____ -->

	_______________________________________
    Options:
      -d	output short description for each topic
      -m	display usage in pseudo-manpage format
      -s	output only a short usage synopsis for each topic matching
    		PATTERN
	_______________________________________
	[1] help
		List of common commands
		Defined internally
	_______________________________________
	[2] help help
		help options
	_______________________________________
	<! help [Pattern specifying a help topic] !>
	[1] help printf
		show the manual, options, usage, examples for the prinf command

	[2] [program] --help | grep [keyword related to thign you want info on]
	[3] grep --help | grep buffer 
		(search all commands related to "buffer" in grep manual)
	[4] ls --help | grep recursive
		(search for the recursive commands of ls)



<!-- _____man______ -->



	Usage: man [OPTION...] [SECTION] PAGE...
		   man man
	_______________________________________
	<! man -k !>
	[1] ____man -k enable
		list of all functinos related to the world "enable"
	_______________________________________
	[2] ____man -k print
		list of all functinos related to printing / that involve printing
	_______________________________________
	[3] ____man -k ssh
		all ssh functions and all functions related to ssh stuff 
		(e.g., ztelnet, zssh, XtIsShell)
	_______________________________________
	[4] man -k status
		functions and tools related to showing status of things


	_______________________________________
	<! OPTIONS !>

	(Mandatory or optional arguments to long options are also mandatory or optional
	for any corresponding short options.)

	  -C, --config-file=FILE     use this user configuration file
	  -d, --debug                emit debugging messages
	  -D, --default              reset all options to their default values
		  --warnings[=WARNINGS]  enable warnings from groff

	 ______ <! Main modes of operation !> ______________________________
	  -f, --whatis               equivalent to whatis
	  -k, --apropos              equivalent to apropos
	  -K, --global-apropos       search for text in all pages
	  -l, --local-file           interpret PAGE argument(s) as local filename(s)
	  -w, --where, --path, --location
		                         print physical location of man page(s)
	  -W, --where-cat, --location-cat
		                         print physical location of cat file(s)

	  -c, --catman               used by catman to reformat out of date cat pages
	  -R, --recode=ENCODING      output source page encoded in ENCODING

	 ______ <! Finding manual pages !> ____________________________________
	  -L, --locale=LOCALE        define the locale for this particular man search
	  -m, --systems=SYSTEM       use manual pages from other systems
	  -M, --manpath=PATH         set search path for manual pages to PATH

	  -S, -s, --sections=LIST    use colon separated section list

	  -e, --extension=EXTENSION  limit search to extension type EXTENSION

	  -i, --ignore-case          look for pages case-insensitively (default)
	  -I, --match-case           look for pages case-sensitively

		  --regex                show all pages matching regex
		  --wildcard             show all pages matching wildcard

		  --names-only           make --regex and --wildcard match page names only,
		                         not descriptions

	  -a, --all                  find all matching manual pages
	  -u, --update               force a cache consistency check

		  --no-subpages          don't try subpages, e.g. 'man foo bar' => 'man
		                         foo-bar'

	 ______ <! Controlling formatted output !> ______________________________
	  -P, --pager=PAGER          use program PAGER to display output
	  -r, --prompt=STRING        provide the `less' pager with a prompt

	  -7, --ascii                display ASCII translation of certain latin1 chars
	  -E, --encoding=ENCODING    use selected output encoding
		  --no-hyphenation, --nh turn off hyphenation
		  --no-justification,                              --nj   turn off justification
	  -p, --preprocessor=STRING  STRING indicates which preprocessors to run:
		                         e - [n]eqn, p - pic, t - tbl, g - grap, 
		                         r - refer, v - vgrind

	  -t, --troff                use groff to format pages
	  -T, --troff-device[=DEVICE]   use groff with selected device

	  -H, --html[=BROWSER]       use www-browser or BROWSER to display HTML output
	  -X, --gxditview[=RESOLUTION]   use groff and display through gxditview
		                         (X11):
		                         -X = -TX75, -X100 = -TX100, -X100-12 = -TX100-12
	  -Z, --ditroff              use groff and force it to produce ditroff

	  -?, --help                 give this help list
		  --usage                give a short usage message
	  -V, --version              print program version



	_______________________________________
	<! EXAMPLES !>
	   _______________________________________________________
       [1] man ls
           Display the manual page for the item (program) ls.

	   _______________________________________________________
       [2] man man.7
           Display the manual page for macro package man from section 7.  
           (This is an alternative spelling of "man 7man".)

	   _______________________________________________________
       [3] man 'man(7)'
           Display the manual page for macro package man from section 7.  
           (This is another alternative  spelling  of
           "man  7 man".  It may be more convenient when copying and 
           pasting cross-references to manual pages.  Note
           that the parentheses must normally be quoted to protect them
           from the shell.)

	   _______________________________________________________
       [4] man -a intro
           Display, in succession, all of the available intro 
           manual pages contained within the manual.  It is  pos‐
           sible to quit between successive displays or skip any of them.

	   _______________________________________________________
       [5] man -t bash | lpr -Pps
           Format  the  manual page for bash into the default troff
           or groff format and pipe it to the printer named
           ps.  The default output for groff is usually PostScript.
           man --help should advise as to which  processor
           is bound to the -t option.

	   _______________________________________________________
       [6] man -l -Tdvi ./foo.1x.gz > ./foo.1x.dvi
           This  command  will decompress and format the nroff source 
           manual page ./foo.1x.gz into a device indepen‐
           dent (dvi) file.  The redirection is necessary as 
           the -T flag causes output to be directed to stdout with
           no  pager.   The  output could be viewed with a program
           such as xdvi or further processed into PostScript
           using a program such as dvips.






-----------------------------------
	   		<wget>
-----------------------------------


<!-- Recently Used -->

	info add-apt-repository
	info apt-get
	info apt-secure
	info wget
	
	

<!-- _____Simple Usage_____ -->


   • Say you want to download a URL.  Just type:

          wget http://fly.srk.fer.hr/

   • But what will happen if the connection is slow, and the file is
     lengthy?  The connection will probably fail before the whole file
     is retrieved, more than once.  In this case, Wget will try getting
     the file until it either gets the whole of it, or exceeds the
     default number of retries (this being 20).  It is easy to change
     the number of tries to 45, to insure that the whole file will
     arrive safely:

          wget --tries=45 http://fly.srk.fer.hr/jpg/flyweb.jpg

   • Now let’s leave Wget to work in the background, and write its
     progress to log file ‘log’.  It is tiring to type ‘--tries’, so we
     shall use ‘-t’.

          wget -t 45 -o log http://fly.srk.fer.hr/jpg/flyweb.jpg &

     The ampersand at the end of the line makes sure that Wget works in
     the background.  To unlimit the number of retries, use ‘-t inf’.


   • But what will happen if the connection is slow, and the file is
     lengthy?  The connection will probably fail before the whole file
     is retrieved, more than once.  In this case, Wget will try getting
     the file until it either gets the whole of it, or exceeds the
     default number of retries (this being 20).  It is easy to change
     the number of tries to 45, to insure that the whole file will
     arrive safely:

          wget --tries=45 http://fly.srk.fer.hr/jpg/flyweb.jpg

   • Now let’s leave Wget to work in the background, and write its
     progress to log file ‘log’.  It is tiring to type ‘--tries’, so we
     shall use ‘-t’.

          wget -t 45 -o log http://fly.srk.fer.hr/jpg/flyweb.jpg &

     The ampersand at the end of the line makes sure that Wget works in
     the background.  To unlimit the number of retries, use ‘-t inf’.

   • The usage of FTP is as simple.  Wget will take care of login and
     password.

          wget ftp://gnjilux.srk.fer.hr/welcome.msg

   • If you specify a directory, Wget will retrieve the directory
     listing, parse it and convert it to HTML.  Try:

          wget ftp://ftp.gnu.org/pub/gnu/
          links index.html


7.2 Advanced Usage
==================

   • You have a file that contains the URLs you want to download?  Use
     the ‘-i’ switch:

          wget -i FILE

     If you specify ‘-’ as file name, the URLs will be read from
     standard input.

   • Create a five levels deep mirror image of the GNU web site, with
     the same directory structure the original has, with only one try
     per document, saving the log of the activities to ‘gnulog’:

          wget -r https://www.gnu.org/ -o gnulog

   • The same as the above, but convert the links in the downloaded
     files to point to local files, so you can view the documents
     off-line:

          wget --convert-links -r https://www.gnu.org/ -o gnulog

   • Retrieve only one HTML page, but make sure that all the elements
     needed for the page to be displayed, such as inline images and
     external style sheets, are also downloaded.  Also make sure the
     downloaded page references the downloaded links.


	_______________________________________
	<! Options !>
	
	

======================
# FINESSES



	=================================================
	(1) read content | find first 5 lines with regex match
	(2) pipe to figlet
	-------------------------------------------------
	$ cat README.md | grep $regular-expression$ -m 5 | figlet


	=================================================
	(1) list directory, show first result with keyword
	(3) pipe to xargs to find location of result
	(4) find first location path that matches keyword
	-------------------------------------------------
	ls | grep *$destination-keyword$* -m 1 | xargs find | grep $destination-keyword$ -m 1
	-------------------------------------------------
	(5) go to the result, lsit directory
	(6) show the first markdown file in the directory
	(7) pipe result to xargs and open MD file with glow
	-------------------------------------------------
	cd $previous-result$; ls | grep -m 1 .md | xargs glow

	
	=================================================
	(1) Search recursively in cd for filenames that match
	(2) show only 10 results with sub or same keyword
	(3) redirect output to temp.txt and overwrite existing text
	-------------------------------------------------
	ls -R *$node-app-keyword$* | grep -m 10 $keyword$ > temp.txt
	-------------------------------------------------
	
	
	
	=================================================

	find . -type f -path '*SCHEDULE*/*' -name '*.xls'




======================
# whereis 
# find


	'whereis [file/folder]'

	find . -type f -path '*SCHEDULE*/*' -name '*.xls'


======================
# xargs 


	grep -r "TWL" --exclude=*.csv* | xargs -I '{}' cp '{}' ~/data/lidar/tmp-ajp2/

	normally if you use xargs, it will put the output after the command

	With the placeholder, you can choose the location where 
	it is inserted, even multiple times.


======================
# glow



	`glow -> /`

	glow README.md



======================
# more


	more [file] (for sneak-peaking a preview of a file instead of cat the whole file)
	more command is used to diaplay a file with pausing. Answer: cat command will dump the entire content of a file on the screen whereas more command will display content that would fit your screen and you can press enter to see rest of the content line by line.

======================
# SCP



	scp <source> <destination>


	To copy a file from B to A while logged into B:

	scp /home/bymyself/Pictures/Wallpapers/1z.jpg legion@10.0.2.255:/legion


	To copy a file from B to A while logged into A:

	scp bymyself@127.0.0.1:/home/bymyself/Pictures/Wallpapers/1z.jpg /legion



======================
# rysnc



	$ rsync <option> <source_user>@<source_host>:<file> <destination_user>@<destination_host>:<file>

	For example, in order to transfer files from a local host to a remote machine, you would run the following command

	$ rsync file user@192.168.178.27:file

	Similarly, to copy files from your remote host to your local machine, you would run

	$ rsync user@192.168.178.27:file file


	With rsync, you can also transfer complete directories from a local host to a remote one.

	You just have to append the ?-r? option to your current syntax


	Progress Bar:
	 rsync --progress <source_user>@<source_host>:<file> <destination_user>@<destination_host>:<file>
 
 
 
======================
# ifconfig



	https://www.tecmint.com/ifconfig-command-examples/



======================
# KILLING APPS/PROCESSES



	man 7 signal (complete list of kill signals)
	ps aux | grep chrome
	ps aux [a = show proccesses for all users]
		   [u = display the process's user/owner]
		   [x = also show processes not attached to terminal]
		   
	______________________		   
	## Get Application ID
	----------------------
	ps -ef | grep [application]



	kill [process ID]
	killall [process by name]
		  -l [list args]
		  1 (hangup)
		  9 (kill signal)
		  15 (termination signal)
		  17 (stop process)
	type / to find file by name after opening glow


======================
# CUSTOM COMMANDS



| Command |Purpose | 
|:-------:|:------- |
vimnew				|new notepad on dekstop
xikinew				|xiki
nautilus [file]		|open with default program
notes 				|notes file in vim
glow [md file]		|markdown reading
f5					|run practice.py
comp [desktopfile]	|wait for pase -> diff	
writepy [f]			|editing env [fullscreen]
functions			|built-in python functions
roughcutpy [name]	|pract as [name] to desktop
q [#]				|random quote with number


======================
# FOLDERS/NAVIGATION COMMANDS



| Command |Purpose | 
|:-------:|:------- |
a1 [program]		|nohup without writing log file
guide | open guides in glow
guides				|guides folder
guide				|MD guides in glow
desktop				|open desktop folder
how [guide name]	|open guide
pypractice			|practice.py in vim



======================
# SETTINGS SHORTCUTS



| Command |Purpose | 
|:-------:|:------- |
naut [file]			|nautilus ~\[location]
vim ~/.imwheelrc	| change mouse scroll settings
setalias			|open bash.rc
scripts				|open scripts folder
vimrc |open vim config file



======================
# APP SHORTCUTS



| Command |Purpose | 
|:-------:|:------- |
naut 				|explorer
web					|open firefox
deepin-config		|deepin config file
term4 [f]			|4 window term [fullscreen]
term				|open custom term 



======================
# CUSTOMIZATION COMMANDS



| Change Highlight Color | 
(1) open dconf-editor 
(2) go to path: org => gnome => desktop => interface
(3) gtk-color-scheme
(4) edit this part: selected_bg_color:#023C88
(5) IN CHROME: use "color highlight" chrome extension

| Command |Purpose | 
|:-------:|:------- |
wallpapers			|terminal_wallpapers
loops				|loops folder
megashots			|megashots folder
dconf-editor 		|-> /org/gnome/desktop/interface/
bg [pic/loop/vid]	|set terminology bg
gnome-tweaks 		|open tweaks
plank --preferences |plank taskbar settings
./config/autostart	|choose onstart apps
conky | (use theme manager)
komerabi(1) | create wallpaper
komerabi(2)| sudo cp -r [newbg] /System/Resources/Komorebi
komerabi(3)| cd /System/Resources/Komorebi; 
komerabi(4)|cd [wallpaper folder]; sudo mv thumb.jpg wallpaper.jpg



======================
# GENERAL COMMANDS



| Command | Args | Purpose | 
|:-------:|:----:|:------- | 
cd | .. | go up one directory
cd | ../../.. | go up three directories
htop | | system monitor
unzip 	| [file]			|		unzips file in cd
youtube-dl | [url] |dl audio or video
gallery-dl |[url] | dl  pictures
python3 -m http.server | [port #] | start http local server
sudo ufw | [disable] or [enable] | firewall
netstats | -l | network stats



======================
# MULTI-PURPOSE COMMANDS



======================

`cp`


Arg | Purpose | 
:----:|:------- | 
[file] [file] 	| 		copy file in cd
[file(s)] [dir]		|		cp multiple files to dir
[file(s)] \~\ [dir] |		when dir is not in cd
-p					|		preserver attributes
*.filetype			|		wildcard
-R *				|		copy recursively
-i					|		prompt on overwrite


======================

`cat`


Arg | Purpose | 
:----:|:------- | 
[file(s)]			|show contents 
[new file]			|create file-> type -> ctrl d
[file(s)] > [file]  |redir stdout of file1 -> file2 
[file] | [file]		|appends
< [file]			|use as input for a cmd
-n					|show line numbers


test test1 test2 | sort > test3
(sort output)


======================

`mv`


Arg | Purpose | 
:----:|:------- |
[file] [file]	|		rename file
[file(s)] [loc]	|		(cut and paste)
*.txt			|		glob



(mv works with directors)


======================

`ls`


Arg | Purpose | 
:----:|:------- |
ls --help			|		see ls options
ls -3 |



======================

`figlet`

TO GET WORD IN ALL FONTS:
"showfigfonts" first arg instead of "figlet"
"showfigfonts [word]"

Arg | Purpose | 
:----:|:------- |
-f [fontfile]			|		select font file
-d [fontdirectory] | change defaault font directory
-c | justify center
-l | justify left
-r | justify right
-t | set output to terminal width
-w | set output width to given integer
-p | paragraph mode
-C | control file
-N | clear control file
-S or -s | smush characters
-k | space between characters
-m [integer 1-63] | layout mode
3 | print selected font
4 | print output width
5 | print supported fonts


======================

# HOTKEYS

| **Command**	  |	  **Function**  |
|:--------------- | ---------------:|
|`  ctrl shift x `|       save screenshot  |
|`  windows M    `|notification tray toggle|
|`  [ctrl shift s] `|       screenshot 2 clip|
` windows arrow`|    snap focused program|
|`  alt return   `|           open terminal|
|`  alt F7       `|   select window to move|
|`  windows L    `|             lock screen|
|`  alt space    `|     menu of focused app|
|`  windows D    `|           show desktop |
|`  windows H    `|         minimize window|
|`  windows A    `|           applications |
|`  ctrl H       `|      see hidden folders|
|`  ctrl L       `|      select address bar|


======================

# OS OPTIMIZATIONS

`CNTRL L` 
> ctrl c -> path in naut or url in browser in clipboard

`SHELL PROMPT` 
> export PS1='\[\e[1;32m\][\u@\h \W]\$\[\e[0m\] '

`VIM DIFF`
> vim -d [file1] [file2]

`MASS CHANGE EXT`
> for f in *.md; do mv "$f" "${f%.md}"; done; for f in *; do mv "$f" "$f.md"; done


---------------------------------

# PYTHON SCRIPTS

## Get all URLS from website
1. nordvpn c;
2. urlparse [-h] [-m MAX_URLS] url

https://www.thepythoncode.com/code/extract-all-website-links-python


---------------------------------

# RESEARCH

https://github.com/awesome-lists/awesome-bash
https://www.quora.com/What-is-the-most-useful-bash-script-that-you-have-ever-written
https://opensource.com/article/20/1/bash-scripts-aliases
https://linuxhint.com/30_bash_script_examples/
https://ostechnix.com/collection-useful-bash-scripts-heavy-commandline-users/
https://dev.to/aviaryan/some-helpful-bash-scripts-i-use-daily-40bd
https://www.8base.com/blog/the-simplest-productivity-hack-using-a-bash-script

https://sass-lang.com/guide
https://documentcloud.github.io/visualsearch/docs/hotkeys.html
https://wangchujiang.com/hotkeys/
https://react-cn.github.io/react/downloads.html

## htop
https://lifehacker.com/control-your-system-with-the-top-command-5445302
https://opensource.com/business/15/5/midnight-commander
https://hackr.io/blog/best-javascript-ide-source-code-editors


---------------------------------

# GENERAL COMMANDS


| Command | Purpose | 
|:-------:|:----:|
cntrl+shift+~		|		open Terminus
bymyself			|		School Material
vim					|		Open vim
money				|		bank,btc,coinbase,sessionbuddy
log					|		log in commands
soft				|		soft login start
wqchrome			|		save session in session buddy and exit chrome
chromesesh			|		open last session from chrome
anime				|		open latest crunchyroll page
gmails.py			|		All Emails
wgetsong			|		quick youtube-dl current URL with no args
coolors				|		coolors saved templates
school.py			|		All School Websites
gmails.py			|		All Emails
chromehistory.py	|		Open chrome -> history
sessionbuddy.py		|		open sessionbuddy
roshes.py			|		roshes  playlissts  w/ chrome ext
run1.py				|		porn hub + xvideos login
run.py				|		porn super log in
resources |
stackitup |
progress |
movies |
mesocycles |
fashion |
diet |
biohacking |



