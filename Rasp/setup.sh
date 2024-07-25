#!/bin/bash

update_system(){
    apt update
    apt full-upgrade -y
    apt install sudo -y
}
install_dependance(){
    sudo apt install zip -y
    sudo apt install screen -y
}
install_python(){
    sudo apt install -y python3 python3-venv python3-pip
    python3 -m venv venv
    source venv/bin/activate
    pip install discord.py wakeonlan
}
RaspMC(){
    mkdir /bot-discord/
    cd /bot-discord/
    wget -o wol.py https://raw.githubusercontent.com/AtisFPS/Minecraft-ServerTools/main/Rasp/wol.py
    wget -o wol.sh https://raw.githubusercontent.com/AtisFPS/Minecraft-ServerTools/main/Rasp/wol.sh
}

update_system
install_dependance
install_python
RaspMC

clear
echo Modifié le wol.py par votre/vos ID et votre TOKEN discord
echo Dossier d'installation dans /bot-discord/
echo Script ecrit par @AtisFPS 
echo https://github.com/AtisFPS
