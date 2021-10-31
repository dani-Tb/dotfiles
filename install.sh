!#/bin/env bash

echo "DANGER!! Do not use as is. Not tested. Reference purposes only."

exit 0

#yay 
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si PKGBUILD

# Login manager
sudo pacman -S lightdm

# Qtile and utils
sudo pacman -S qtile feh alacritty w3m picom lxsessions volumeicon NetworkManager zsh curl

# Zsh defaiñt shell
chsh -s /usr/bin/zsh

# Fonts
echo "install meslo manually from https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k"

#Oh my zsh 
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" 

# powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

echo "Manually set ZSH_THEME="powerlevel10k/powerlevel10k" in ~/.zshrc"

# pywal
sudo pacman -S python-pywal
#schemer
sudo pacman -S go
go get github.com/thefryscorer/schemer2
# haishoku
yay -S python-haishoku
# colorz
yay -S colorz
# colorthief
yay -S python-colorthief

# Vim 
sudo pacman -S vim
# vim airline 
mkdir -p ~/.vim/pack/airline/start/
git clone git@github.com:vim-airline/vim-airline.git ~/.vim/pack/airline/start/vim-airline
# Nerdtree
git clone https://github.com/preservim/nerdtree.git ~/.vim/pack/vendor/start/nerdtree
vim -u NONE -c "helptags ~/.vim/pack/vendor/start/nerdtree/doc" -c q
# vim css color
mkdir -p ~/.vim/pack/css-color/start/
git clone t@github.com:ap/vim-css-color.git ~/.vim/pack/airline/start/vim-css-color
# vim pywal
mkdir -p ~/.vim/pack/pywal/start/
git clone git@github.com:dylanaraps/wal.vim.git ~/.vim/pack/airline/start/wal.vim
# vim airline 
mkdir -p ~/.vim/pack/vim-devicons/start/
git clone git@github.com:ryanoasis/vim-devicons.git ~/.vim/pack/airline/start/vim-devicons


# Alacritty
sudo pacman -S alacritty

# term utils
sudo pacman -S lsd bat htop
yay -S ytop 
#colorscripts
sudo pacman -S nodejs
npm install --save colorscript

# term apps
sudo pacman -S ranger neofetch 
yay -S pfetch

# Vimix Cursor
git clone https://github.com/vinceliuice/Vimix-cursors.git 
cd Vimix-cursors
./install
cd .. && rm -rf Vimix-cursors

