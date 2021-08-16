set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
" call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" Keep Plugin commands between vundle#begin/end.

" Fugitive - Git
Plugin 'tpope/vim-fugitive'

" Vim Notes + Helper Script Loader
Plugin 'xolox/vim-misc'
Plugin 'xolox/vim-notes'

" Color Scheme Collections
Plugin 'rafi/awesome-vim-colorschemes'
Plugin 'rainglow/vim'
Plugin 'mswift42/vim-themes'
" Plugin 'chriskempson/base16-vim'
Plugin 'patstockwell/vim-monokai-tasty'
Plugin 'connorholyday/vim-snazzy'
Plugin 'ghifarit53/daycula-vim'
Plugin 'jdsimcoe/panic.vim'
Plugin 'kjakapat/eva-theme'
Plugin 'gosukiwi/vim-atom-dark'
Plugin 'ghifarit53/tokyonight-vim'
Plugin 'nightsense/seabird'
Plugin 'capaldo/boogiewoogie'
Plugin 'dhruvasagar/vim-table-mode'
" Colorscheme Switcher
Plugin 'xolox/vim-colorscheme-switcher'


" how to dl Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'

" how to dl git repos on your local machine (i.e. when working on your own plugin)
" Plugin 'file:///home/gmarik/path/to/plugin'

" The sparkup vim script is in a subdirectory of this repo called vim.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}

" Emmet = adding tags efficiently
Plugin 'mattn/emmet-vim'

" See Indentation Level with vertical lines on the side (if using spaces)
" Plugin 'Yggdroot/indentLine'

" color preview
Plugin 'gko/vim-coloresque'

" Enable to use the auto-completion and language support plugin
" need to access server
" Plugin 'neoclide/coc.nvim', {'branch': 'release'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
" filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" Pathon Plugin Manager
execute pathogen#infect()
syntax on
filetype plugin indent on

" Python Mode
call plug#begin('~/.vim/plugged')
Plugin 'python-mode/python-mode', { 'for': 'python', 'branch': 'develop' }
call plug#end()

" Enable column view in pymode
let g:pymode_options_colorcolumn = 1
" Set Max line length for pymode plugin
let g:pymode_options_max_line_length = 120

" Change Tab Characters -- https://vim.fandom.com/wiki/Highlight_unwanted_spaces
" ---------------------
" Show Tabs
:set list lcs=tab:\|\ 

" Tabs and shift-tab (>) to 4 spaces
set tabstop=4
set shiftwidth=4
set expandtab

" << Highlight tabs as errors. >>
" https://vi.stackexchange.com/a/9353/3168
match Error /\t/

" End of Line
:set listchars=eol:↓

" << Some Presets >>
" set listchars=tab:→\ ,eol:↲,nbsp:␣,trail:•,extends:⟩,precedes:⟨

" →→
" :set tab:\ \ ┊,trail:●,extends:…,precedes:…,space:·
" :set listchars=tab:__,trail:_,extends:>,precedes:<,nbsp:~
" :set listchars=tab:__,trail:●,extends:>,precedes:<,nbsp:~
" :set listchars=tab:__,trail:●,extends:…,precedes:…,space:·
:set listchars=tab:__

" define highlights groups like "ExtraWhitespace" using :help
" :match ExtraWhitespace /[^\t]\zs\t\+/
" << Add trailing spaces to tabs >>
" set showbreak=↪\
"
" The :match command specifies the name of a highlight group and a pattern. Any text matching the pattern will be displayed in the foreground and background colors defined by the highlight group. :help :match :help :2match

 

" -----------------------

" bottom of page for collections of schemes: https://github.com/rafi/awesome-vim-colorschemes

" Color code system used by Vim/Xterm: https://vim.fandom.com/wiki/Xterm256_color_names_for_console_Vim

" Change Color Scheme ------
" colorscheme vim-monokai-tasty
" See all installed schemes: ls -l /usr/share/vim/vim*/colors/
" Some schemes: pablo, murphy, morning, shine, slate, ron, torte, zellner
" You can change color schemes at anytime in vi by typing colorscheme followed by
" space and the name of the color scheme. For more color schemes, you can browse
" this library on the vim website. You can enable or disable colors by simply
" typing 'syntax on' or 'syntax off' in vi.

" Highlight conceal color with your colorscheme instead of default (grey)
" let g:indentLine_setColors = 0
" let g:indentLine_setColors = 060
" use the set color for special keys for the indentLine vertical bars
" let g:indentLine_defaultGroup = 'SpecialKey'

" Change background color of indent vertical bars
" let g:indentLine_bgcolor_term = 202

"  Change indent Character
" let g:indentLine_char = 'c'

