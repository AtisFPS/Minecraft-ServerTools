import discord
from discord.ext import tasks
from wakeonlan import send_magic_packet
import os

# Remplacez par votre token Discord
TOKEN = ''
# Adresse MAC et IP de votre serveur minecraft pour le status et le wake on lan
MAC_ADDRESS = ''
IP_ADDRESS = ''

# ID des utilisateurs pouvant démarrer votre serveur
AUTHORIZED_USERS = []

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

def ping_server(ip):
    response = os.system(f'ping -c 1 -W 1 {ip}')
    return response == 0

@bot.event
async def on_ready():
    update_status.start()

# Mise a jour de l'activité du bot en fonction de l'etat du ping 
@tasks.loop(seconds=1)
async def update_status():
    if ping_server(IP_ADDRESS):
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="status : ON"))
    else:
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="status : OFF"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == '!start':
        if message.author.id in AUTHORIZED_USERS:
            try:
                send_magic_packet(MAC_ADDRESS)
                embed = discord.Embed(
                    title="Rasp 1 - Wake On Lan",
                    description="Démarrage du serveur, le status du bot changera lorsque la machine est démarrée.",
                    color=discord.Color.blue()
                )
            except Exception as e:
                embed = discord.Embed(title="Rasp 1 - Erreur", description=f"Erreur lors du démarrage via le Wake On Lan : {e}", color=discord.Color.red())
                await message.channel.send(embed=embed)
                return
        else:
            embed = discord.Embed(title="Rasp 1 - Erreur", description="Vous n'êtes pas autorisé à utiliser cette commande.", color=discord.Color.red())
        await message.channel.send(embed=embed)
        return

bot.run(TOKEN)