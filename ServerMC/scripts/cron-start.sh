#!/bin/sh
sleep 5
cd /bot-discord/
# Activate the virtual environment and run the bot
screen -dmS MC-system python3 alim-system.py
screen -dmS MC-backup python3 backup.py