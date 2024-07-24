import discord
from discord.ext import commands
import subprocess

# Token de votre bot Discord
TOKEN = ''

# ID utilisateur pouvant gerer votre systeme
AUTHORIZED_IDS = []

intents = discord.Intents.default()
intents.messages = True  
intents.guilds = True  
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.event
async def on_disconnect():
    print('Connexion perdu , tentative de reconnexion ')

@bot.command(name='stop')
async def stop_machine(ctx):
    if ctx.author.id not in AUTHORIZED_IDS:
        embed = discord.Embed(title="Permissions", description=f"Vous n\'êtes pas autorisé à exécuter cette commande.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="Status de la machine", description=f"Arrêt de la machine en cours...", color=discord.Color.red())
    await ctx.send(embed=embed)
    try:
        subprocess.run(['/sbin/poweroff'])
    except Exception as e:
        embed = discord.Embed(title="Erreur", description=f"Une erreur s\'est produite lors de l\'arrêt de la machine.", color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command(name='reboot')
async def reboot_machine(ctx):
    if ctx.author.id not in AUTHORIZED_IDS:
        embed = discord.Embed(title="Permissions", description=f"Vous n\'êtes pas autorisé à exécuter cette commande.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    embed = discord.Embed(title="Status de la machine", description=f"La machine redemarre", color=discord.Color.red())
    await ctx.send(embed=embed)
    try:
        subprocess.run(['/sbin/reboot'])
    except Exception as e:
        embed = discord.Embed(title="Erreur", description=f"Une erreur s\'est produite lors de l\'arrêt de la machine.", color=discord.Color.red())
        await ctx.send(embed=embed)

bot.run(TOKEN)