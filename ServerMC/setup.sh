#!/bin/sh 

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
    sudo apt install -y python3 python3-pip python3-venv python python-pip python-venv
    sudo apt install python3-discord -y
}
ServerMC(){
    mkdir /bot-discord/
    cd /bot-discord/
    mkdir ./scripts
    wget -O ./scripts/cron-start.sh https://raw.githubusercontent.com/AtisFPS/Minecraft-ServerTools/main/ServerMC/scripts/cron-start.sh
    wget -O alim-system.py https://raw.githubusercontent.com/AtisFPS/Minecraft-ServerTools/main/ServerMC/alim-system.py
    wget -O backup.py https://raw.githubusercontent.com/AtisFPS/Minecraft-ServerTools/main/ServerMC/backup.py
    
}

update_system
install_dependance
install_python
ServerMC

clear
echo Modifié les fichiers en .py par vos ID et votre TOKEN discord
echo Dossier d'installation dans /bot-discord/
echo Script ecris par @AtisFPS 
echo https://github.com/AtisFPS