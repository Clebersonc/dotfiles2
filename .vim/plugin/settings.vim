
" Encoding
"

set encoding=UTF-8 " Default encoding. (vim-only)
scriptencoding UTF-8 " Default encoding for current script.
set fileformats=unix " Only use Unix end-of-line format.

" Shared Data
set viminfo=!,'100,<50,s10,h
execute printf('set viminfo+=n~/.vim/cache/share/%s', has('nvim') ? 'nviminfo' : 'viminfo')

" Colors
 set background=dark " Choose dark colors if available.
 colorscheme plain " Color scheme.
 set termguicolors " Enable True Color support.

" Behaviour
set backspace=indent,eol,start " Allow backspacing over everything in insert mode.
set belloff=all " Turn off the bell upon all events.
set breakindent " Wrapped lines will be indented with same amount of space.
set clipboard= " Disable using system clipboard.
set confirm " Seek for confirmation for certain commands instead of giving errors.
set display=lastline " As much as possible of the last line in a window will be displayed.
set keywordprg= " Disable definition search by default.
set modelines=1 " Maximum number of lines that is checked for set commands.
set nojoinspaces " Disable inserting two spaces after `.`, `?`, `!` with join command.
set nolangremap " Setting 'langmap' does not apply to characters resulting from a mapping.
set noruler " Disable showing line numbers in command line.
set noshowmatch " When a bracket is inserted, do not jump to the matching one.
set nostartofline " Prevent the cursor from changing the current column when jumping.
set nowrap " Prevent wrapping for long lines.
set nrformats=bin,hex " Only accept binary and hexadecimal numbers.
set pumheight=10 " Maximum number of items to show in the pop-up menu for completion.
set report=0 " Threshold for reporting number of lines changed.
set sessionoptions=blank,buffers,curdir,folds,help,localoptions,resize,tabpages,winsize " Options for `mksession` command.
set shellpipe=&> " Fix potentional screen flashing problems with not using `tee`.
set shortmess=filmnrwxoOstTIc " Use abbreviations and short messages in command menu line.
set sidescroll=5 " Columns to scroll horizontally when cursor is moved off the screen.
set sidescrolloff=5 " Minimum number of screen columns to keep to cursor right.
set synmaxcol=200 " Maximum column in which to search for syntax items.
set textwidth=0 " Prevent auto wrapping when using affecting keys.
set timeoutlen=500 " Mapping delays in milliseconds.
set ttimeoutlen=10 " Key code delays in milliseconds.
set ttyfast " More characters will be sent to the screen for redrawing in terminal. (vim-only)
set updatetime=2000 " If that milliseconds nothing is typed CursorHold event will trigger.
set visualbell " Use visual bell instead of beeping on errors.
set guicursor= " Disable change cursor shape among modes.
if has('nvim') | set inccommand=nosplit | endif " Show live substitution results as you type.

" Interface
set cursorline " Highdark the line background of the cursor.
set fillchars=vert:⏐ " Characters to fill the status lines and vertical separators.
set laststatus=2 " Always show the status line.
set linebreak " Wrap lines in 'breakat', rather than at the last character.
set listchars=tab:│\ ,nbsp:␣,extends:…,precedes:… " Strings to use when 'list' option set.
set number " Show line numbers alongside relative numbers.
set relativenumber " Show relative line numbers alongside numbers.
set signcolumn=yes " Always draw the sign column even there is no sign in it.
set title " Show title as in 'titlestring' in title bar of window.
set titlestring=%f " Format of the title used by 'title'.
set mousehide      " Hide the mouse cursor while typing

" Diff
set diffopt=filler,vertical,foldcolumn:0 " Option settings for diff mode.

" Formatting
set formatoptions=croqnj " General text formatting options used by many mechanics.
set formatprg=par\ -w80 " External formatter program that will be used with `gq` operator.

" Completion
set complete=.,w,b,k,t " Options for keyword completion.
set completeopt=noinsert,menuone,noselect " Options for insert mode completion.
set path=.,** " Use recursive file search.

" Indentation
set tabstop=4 " Length of a <Tab> character.
set shiftwidth=0 " Number of spaces to use for each step of auto indent operators.
set softtabstop=-1 " Number of spaces that a <Tab> counts.
set noexpandtab " Disable using spaces instead of tab characters.
set nosmarttab " Tab key always inserts blanks according to 'tabstop'.
set autoindent " Copy indent from current line when starting a new line.
set shiftround " Round indent to multiple of 'shiftwidth'. Applies to > and < commands.
set smartindent " Automatically inserts one extra level of indentation in some cases.

" Folding
set foldlevelstart=99 " Start editing with all folds open.
set foldmethod=indent " Use indent model for folding mechanism.

" Search
let &grepprg = 'ag' " Program to use for the :grep command.
set grepformat=%f:%l:%c:%m,%f:%l:%m " Format to recognize for the :grep command output.
set ignorecase " Make default search is not case sensitive.
set incsearch " Instantly show results when you start searching.
set nohlsearch " Disable highdark the matched search results by default.
set smartcase " If a uppercase character is entered, the search will be case sensitive.

" Backup
set backupdir=~/.vim/cache/backup// " The directory for backup files.
set directory=~/.vim/cache/swap// " The directory for swap files.
set undodir=~/.vim/cache/undo// " The directory for undo files.
set undofile " Undo tree to be saved to a file when exiting a buffer.
set undolevels=100000 " Maximum undo limit.
set updatecount=100 " Typing this many characters will create the swap file.
set viewdir=~/.vim/cache/view// " Name of the directory where to store files for :mkview.
set viewoptions=cursor,folds " Options used by `mkview` and `loadview` commands.

" Buffers, Windows, Tabs
set autoread " Read the file again if have been changed outside of Vim.
set hidden " Allows you to hide buffers with unsaved changes without being prompted.
set splitbelow " Splitting a window will put the new window below of the current one.
set splitright " Splitting a window will put the new window right of the current one.
set switchbuf=useopen " Jump to the first open window that contains the specified buffer.
set tabpagemax=50 " Maximum number of tab pages to be opened by the `tab all` command.

" Command Mode
set cmdwinheight=18 " Height of the command window size for commands like `q:` and `q/`.
set history=10000 " Define maximum command history size.
set noshowcmd " Disable displaying key presses at the right bottom.
set noshowmode " Disable native mode indicator.
set wildcharm=<C-z> " The key to start wildcard expansion inside macro.
set wildignorecase " Ignore case when completing in command menu.
set wildmenu " Command-line completion operates in an enhanced mode.
set wildmode=full " Wildmenu options.