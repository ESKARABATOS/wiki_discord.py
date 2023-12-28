import discord #importujemy biblioteke discorda
from discord.ext import commands #importujemy obsługiwanie komend

intents = discord.Intents.all() #Uprawniamy bota do wszystkich poleceń

client = commands.Bot(commands_prefix="NAZWA PREFIXU KOMEND", intents=intents) #tworzenie klienta bota

@client.event #tworzenie eventu
async def on_ready(): #tworzenie funkcji eventu on_ready czyli po uruchomieniu bota 
    print("Bot został uruchomiony")

client.run("TOKEN") #URUCHAMIAMY BOTA TOKEN ZNAJDZIESZ NA DISCORD DEVELOPER PORTAL