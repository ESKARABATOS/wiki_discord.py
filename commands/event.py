#powtarzamy schemat ten sam co w przypadku komend 

import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)


class Event(commands.Cog): #Zmiana nazwy funkcji jest obowiązkowa jeżeli tego nie zrobimy będzie błąd
    def __init__(self, client):
        self.client = client
    #Piszemy EVENT aby to zrobić trzeba stworzyć event podobnie jak w main
    @commands.Cog.listener() #oto schemat tworzenia eventu
    async def on_message(self, message): #tworzymy event który po napisaniu wiadmomości coś zrobi
        #w tej funkcji stworzymy aby wiadomość wysłana pokazała się w konsoli
        #aby tego dokonać potrzebujemy zmiennej message w funkcji nazwa zmiennej zależy tylko od ciebie nie może być to ctx ponieważ ctx jest do komend
        #awięc muśimy zrobić print który pobierze naszą wiadomość oraz przez message musimy dać znak * aby zmienna zapisywała wszystkie argumenty po spacji
        print(message.content) #tworzymy funkcje print oraz wypisujemy zmienną message.content content jest to treśc zmiennej message

    #SPIS EVENTÓW
async def setup(client): 
    await client.add_cog(Event(client))