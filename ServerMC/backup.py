# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import os
from datetime import datetime
import subprocess
import paramiko
from scp import SCPClient
import asyncio
import shutil

# Token de votre bot minecraft
TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

# ID utilisateur pouvant gerer votre system
ALLOWED_USER_IDS = []

def is_authorized(ctx):
    return ctx.author.id in ALLOWED_USER_IDS

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.event
async def on_disconnect():
    print('Connexion perdu , tentative de reconnexion ')

@bot.command()
@commands.check(is_authorized)
async def bkp(ctx):
    await asyncio.sleep(1)
    embed = discord.Embed(title="Sauvegarde - ServerMC", description="La sauvegarde des fichiers du serveur Minecraft a démarré", color=discord.Color.green())
    await ctx.send(embed=embed)
    
    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y - %H:%M")
    
    archive_name = f"{now.strftime('%d-%m-%Y_%H-%M')}.zip"
    archive_path = f"./{archive_name}"
    
    #Mot de passe que vous souhaitez donner a l'archive
    password = ""
    
    # Chemin du dossier de votre minecraft
    folder_to_backup = ""
    tmp_backup_folder = f"/tmp/Server-Minecraft-Temporaire/"
    
    if not os.path.exists(folder_to_backup):
        embed = discord.Embed(title="Erreur de sauvegarde", description=f"Le dossier à sauvegarder n'existe pas : {folder_to_backup}", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    try:
        if os.path.exists(tmp_backup_folder):
            shutil.rmtree(tmp_backup_folder)
        shutil.copytree(folder_to_backup, tmp_backup_folder)
    except Exception as copy_error:
        embed = discord.Embed(title="Erreur de sauvegarde", description=f"Une erreur est survenue lors de la copie du dossier : {copy_error}", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    command = [
        "zip",
        "-r",  
        "-P", password,
        archive_path,
        tmp_backup_folder
    ]
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        if os.path.exists(archive_path):
            print(f"Archive créée avec succès: {archive_path}")
        else:
            print(f"L'archive n'a pas été créée. Vérifiez les permissions et l'espace disque.")
        
        download_link = f"VOTRE-SITE/{archive_name}"

        embed.add_field(name="Sauvegarde ServerMinecraft ", value=f"La sauvegarde est terminée. [Lien de téléchargement]({download_link})", inline=False)
        
    except subprocess.CalledProcessError as e:
        embed = discord.Embed(title="Erreur de sauvegarde", description=f"Une erreur est survenue lors de la création de l'archive : {str(e)}", color=discord.Color.red())
    except FileNotFoundError:
        embed = discord.Embed(title="Erreur de sauvegarde", description="La commande `zip` n'a pas été trouvée sur le système.", color=discord.Color.red())
    
    await ctx.send(embed=embed)
bot.run(TOKEN)
