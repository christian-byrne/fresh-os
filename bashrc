# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# ----------------- Aliases ----------------------------

alias entities='xdg-open https://dev.w3.org/html5/html-author/charref'

alias docean-ip='echo -n "143.198.57.139" | clipboard'
alias docean='bash ~/a/b/docean.sh'

# getting path of thing in cd
alias ppath='bash /home/bymyself/a/b/ppath.sh'

alias gifv='bash ~/a/b/gif-viewer.sh'
alias d2l='nohup > /dev/null xdg-open https://github.com/trevor-reznik/guides/blob/master/school/ua-d2l.js & disown'

# Misc
alias cb='clipboard'
alias web-sync='python3 ~/d/a/p/open_synced_chrome_tabs.py'
alias l='sh /home/bymyself/a/b/ext_ls.sh'
alias q='~/a/b/quote_returner'
alias urlparse='cd ~/d/a/p; python3 urlparser.py'

# Guides / Notes / Markdown Formatters
alias gu='python3 ~/p/g/open_guide.py'
alias guide='~/a/b/openGlowGuides.sh'
alias notes='vim ~/d/notes'
alias juice='python3 ~/d/a/p/format-note*'
alias how='~/a/b/how'
alias emmet='python ~/a/p/emmet_and_css_selectors.py'

# Apps
alias py='python3'
alias termtheme='python3 ~/p/g/colors/palette-generator/theme_switcher.py'
alias deepin-config='vim ~/.config/deepin/deepin-terminal/config.conf'
alias web='~/a/b/web'
alias naut='~/a/b/open_file_explorer'
alias a1='~/a/b/nohup'
alias term='~/a/b/term'
alias retroterm='a1 cool-retro-term'

# References
alias figlet-fonts='python3 ~/d/a/p/sample_fig_fonts.py'

# Directories
alias bg='~/a/b/terminology_wallpaper_selector.sh'

# School
alias school='python3 ~/p/g/school/summer-21.py'

# Projects
alias dl-crop='cd ~/p/dl; python3 ~/p/dl/dl_crop_flaskapp.py'
alias bmplayer='~/a/b/bm_player*'
alias crypto-gogo='cd ~/p/cb; python3 ~/p/cb/three_conditions.py'
alias BYMY='cd ~/_BYMYself/; python3 autoRun.py; python3 DL_and_Trim.py'

# Trading
alias dpswitch='sudo mv ~/.config/deepin/deepin-terminal/config.conf /home/bymyself/d/a/p/coin-gui-deepin-config.conf; sudo mv /home/bymyself/d/python-scripts/config.conf ~/.config/deepin/deepin-terminal/'
alias coin='python3 ~/d/a/p/coin-gui.py'

# Python Workflow
alias pypractice='vim ~/d/practice.py'
alias f5='~/a/b/f5'
alias vimnew='vim ~/d/temp-notes/temp1.txt'
alias termfull='python3 ~/d/a/p/deep_term*'
alias comp='~/a/b/Compare_Script/compare'
alias term4='~/a/b/term4.sh'
alias writepy='~/a/b/python_editing_environment'
alias roughcutpy='~/a/b/copy_practicepy_and_rename'

# ----------------- Aliases ----------------------------

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

export gitpass="dfdgfd4343*76{]][dfdq23%^2342389fd@#\$DS"
export KRAK_KEY="7zbOvDL1ZSDh3wKFAy/NX9xvwm++IlH1MHKu5F/fijlZ+b401TQWDXdh"
export KRAK_SEC="3pAZySISnqQKJ1W81V2nniQvyu8L8sk73xY+XCdpTgNpTwPEDeh/AwvU3yJHqdGFkDAOZHa7QoPt3Pe2aK0e7Q=="

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# declares an array with the emojis we want to support
EMOJIS=(📼 🍀 😂 🤖 💣 🧸 🛍️ 🈹 🈴 🈯 🈚 🈂️ 📟 🖱️ 💻 🖥️ 🔌 🔋 📠 🖲️ 💾 🚬 🐶 🦧 🐺 🦊 🦝 🐈 🐅 🐆 🐷 🐖 🐗 🐏 🐪 🐘 🐼 🐨 🦇 🐔 🦃 🐓 🐥 🐧 🐦 🦅 🦆 🦉 🐸 🐻 🐼 🐨 🐯 🦁 🐮 🐷 🐽 🐸 🐵 🙈 🙉 🙊 🐒 🐔 🐧 🐦 🐤 🐣 🐥 🦆 🦅 🦉 🦇 🐺 🐗 🐴 🦄 🐝 🐛 🦋 🐌 🐞 🐜 🦟 🦗 🕷 🕸 🦂 🐢 🐍 🦎 🦖 🦕 🐙 🦑 🦐 🦞 🦀 🐡 🐠 🐟 🐬 🐳 🐋 🦈 🐊 🐅 🐆 🦓 🦍 🦧 🐘 🦛 🦏 🐪 🐫 🦒 🦘 🐃 🐂 🐄 🐎 🐖 🐏 🐑 🦙 🐐 🦌 🐕 🐩 🦮 🐕‍🦺 🐈 🐓 🦃 🦚 🦜 🦢 🦩 🕊 🐇 🦝 🦨 🦡 🦦 🦥 🐁 🐀 🐿 🦔 🐾 🐉 🐲 🌵 🎄 🌲 🌳 🌴 🌱 🌿 ☘️ 🍀 🎍 🎋 🍃 🍂 🍁 🍄 🐚 🌾 💐 🌷 🌹 🥀 🌺 🌸 🌼 🌻)

# 🇮🇪

STRINGS=("let everything happen to you" "beauty and terror" "no feeling is final" "just keep going" "all is folly except the sky" "less is more" "except the sky" "elegance is elimination" "midnight moves over metropolis" "rise" "they are of the world" "greater is he" "remember" "malice" "hide behind the money" "accept everything" "look inwards" "love|obsession" "the fire rises" "fashion fades|beauty is eternal" "my name is legion" "villain|flux" "life is self-deception" "odyssey of dark roads" "form follows function" "the night is deception" "it's graceless being a martyr" "the self at dusk" "here for the moment" "my disease happens to be the ideal" "my tragedy my masterpiece" "america's tortured brow" "writ large in life's libretto" "they had something she lacked" "the sould discharges it passions on false objects when the true ones fail it" "learn to die" "tragedy is upon you" "boredem>begging>forgotten" "then and thereafter" "6 shots" "INT. CASH, DAY" "style and substance" "righteous destiny" "hang up and try again" "night addict" "metropolis park" "we are not the same" "baby carriage for sale. unused" "take me to your skinner box" "celluloid dreams" "bad city, somewhere" "murder she spoke" "double indemnity" "rhythms resemble home" "bad things happen" "life is folly|signifying nothing" "south of heaven" "east of eden" "live means die" "bored by the 2nd bomb" "kiss kiss bang bang" "changing planes in paris" "some like it hot" "sparkle motion" "au revoir" "are you the devil" "once upon a time in delusion" "the sin of man" "rebirth requires death" "love is eastside" "order tends to disorder" "its alive" "shes a monster" "make them remember" "remember what they took" "thanks to the lord in advance" "live in silence" "dont make trouble for humans" "exist in silence" "dont take advice" "the end of the fu***** world" "sinister lone rider" "slightly funny ridiculously twisted" "silence beckons" "shockingly indifferent" "masked spider troupe" "picture of a man staring at a picture" "the show's over" "welcome to me" "remember" "halway to hell" "fluoride dreams" "stop thinking" "hang up and try again" "stop thinking" "stop thinking" "no feeling is final" "let my pipe bang" "alice in the wall" "myself" "andrew bolkonski" "i dont exist" "villain|flux" "villain|flux" "villain|flux" "villain|flux" "villain|flux" "villain|flux" "villain|flux" "villain|flux" "villain|flux" "cathy ames" "the wolf waits" "depths of the unconscious" "forget it jake" "terror is glory" "man is wolf to man" "honor no kings|reject the trinity" "they are overrated" "dashed hopes|good intentions" "half my attention" "you're still here?" "crash like thunder" "might as well live" "learn all things" "knowledge is purpose" "flux" "villain" "devil" "flux" "flux" "no warranty in mortals" "judge them" "morality is performance" "is=/=ought" "dont beleive their performance" "character is destiny" "action is character" "character is action" "excitement is not happiness" "a crowd is untruth" "perspective is destination" "gap between stimulus & response" "suffering is opportunity" "offer no resistance" "success should surprise you" "accept what you cant change" "things are not what they seem" "you are your only obstacle" "begin with doubts|end in certainties" "KFKD" "starve yourself of your thoughts" "thinking|rearranging prejudices" "follow fear" "fear is glory" "reasonable men adapt themselves" "rock bottom is a solid foundation" "the abyss stares back" "sit in judgment of self|others" "worst memories|biggest illusions" "12 glib little reasons" "find the extent of your ignorance" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "elegance is elimination" "villain|flux" "nothing is what it seems" "life is a game" "knowledge is the liberator" "suffer|create" "creation is redemption" "steal victory by laughing at defeat" "no one is looking for you" "man never steps in the same river twice" "homo homini lupus" "man|wolf|man" "everything is only for a day" "sleep is death" "if its a story|theres an audience" "what what a boy know of destiny" "separation is illusion" "they believe they are what they pretend to be" "make the darkness conscious" "man vs power|memory vs forgetting" "a cold winter's day" "afraid to be seen failing" "life's a walking shadow" "full of sound and fury|signifying nothing" "learn no names" )


RANDOM_EMOJI() {
  if [ $? -eq 0 ] ; then
    SELECTED_EMOJI=${EMOJIS[$RANDOM % ${#EMOJIS[@]}]};
    echo $SELECTED_EMOJI;
  else
    echo "😓";
  fi

}

RANDOM_STR() {
  SELECTED_STR=${STRINGS[$RANDOM % ${#STRINGS[@]}]};
  echo $SELECTED_STR;
}




# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"



# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
    # Uncomment for random mini-quote in every new command
    #export PS1="[\e[0;32m\!\e[m][\e[2;31m\$(RANDOM_STR)\e[m][\$(RANDOM_EMOJI)][\e[0;32m\w\e[m] "
    # Uncomment for random mini-quote that persists in current session
    export PS1="\[\033[38;2;135;95;135;48;2;216;230;208m\][\#]\[\e[m\]\[\033[48;2;135;123;216;38;2;72;235;137m\][$(RANDOM_STR)]\[\e[m\][\$(RANDOM_EMOJI)][\[\033[38;2;72;235;137m\]\w\[\e[m\]] "
fi




unset color_prompt force_color_prompt

export PS2="[$(RANDOM_EMOJI)] "

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
[ -r /home/bymyself/.byobu/prompt ] && . /home/bymyself/.byobu/prompt   #byobu-prompt#
