#!/bin/bash
#TEST
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
