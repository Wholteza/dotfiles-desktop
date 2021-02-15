#!/bin/bash

# Wireguard
alias wg-up-de='wg-quick up de'
alias wg-down-de='wg-quick down de'
alias wg-up-se='wg-quick up se'
alias wg-down-se='wg-quick down se'

# Nice to have
alias what-is-my-ip='host myip.opendns.com resolver1.opendns.com'

# Edit commands
alias edit-bashrc='vim ~/.bashrc && source ~/.bashrc'
alias edit-aliases='vim ~/.bash_aliases && source ~/.bashrc'
alias edit-prompt='vim ~/.bash_prompt && source ~/.bashrc'
alias edit-bash='vim ~/.bash_additions && source ~/.bashrc'
alias edit-awesome='vim ~/.config/awesome/rc.lua && source ~/.bashrc'
alias edit-gitsync='vim ~/.config/wholteza/gitsync/run.sh && source ~/.bashrc'
alias edit-vim='vim ~/.vimrc && source ~/.bashrc'
alias edit-tmux='vim ~/.tmux.conf && source ~/.bashrc'
alias edit-installer-apt='vim ~/.config/wholteza/installer/package-definitions/ubuntu-apt-packages'
alias edit-installer-snap='vim ~/.config/wholteza/installer/package-definitions/ubuntu-snap-packages'
alias run-installer='python3 ~/.config/wholteza/installer/install.py ubuntu'

# Screenshots
alias snip='scrot -s ~/Pictures/Screenshots/scrot-%Y-%m-%d-%H_%M.png'

# Custom commands
alias gitsync='~/.config/wholteza/gitsync/run.sh'
