# dotfiles-desktop
My dotfiles managed by [yadm](https://yadm.io/).

Also contains a python based install script that has support for installing with snap and aptitude. As well as bootstrapping configurations into files.

Right now only support for ubuntu 20.04 since that is what is use.

## Getting started
1. Clone repo
1. Install yadm for your distribution
1. `yadm clone --bootstrap git@github.com:Wholteza/dotfiles-desktop.git`
1. Run installer `python3 ~/.config/wholteza/installer/install.py ubuntu`
