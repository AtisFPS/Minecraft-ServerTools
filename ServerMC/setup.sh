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
setup-bot-discord-ServerMC(){
    mkdir /bot-discord/
    cd /bot-discord/
    mkdir ./scripts
    wget -O ./scripts/cron-start.sh # LIEN GITHUB
    wget -O alim-system.py # LIEN GITHUB
    wget -O backup-server.py # LIEN GITHUB
    
}

update_system
install_dependance
install_python
setup-bot-discord-ServerMC