#4 TWORZYMY PLIK Z KOMEDNĄ LUB EVENTEM 
#Powtarzamy importy intents oraz tworzenie clienta

import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)

#teraz stworzymy klase do obsługi plików aby zawartość działała poprawnie
class Komendy(commands.Cog): #Nazwe klasy najlepiej pisać z dużej litery aby pokazać że jest dominująca w () piszemy argumenty 
    def __init__(self, client):
        self.client = client

    @commands.command(name="pomoc") #w przypadku gdy piszemy nowe komendy nie piszemy client.command() tylko commands.command() 
    #należy otym pamiętać w argumentach wpisujemy nazwe komendy jak jest w tym przykładzie name="NAZWA KOMENDY"
    async def command_pomoc(self, ctx): #tutaj tworzymy nazwe funkcji nie komendy trzeba o tym pamiętać że to są dwie inne żeczy oraz argument self jest obowiązkowy bo bez niego
        #komenda nie będzie działać ctx jest to zmienna która powoduje że po wpisaniu np. czyli prefixu pomoc nazwa komendy zostaną zebrane informacje które w puźniejszym etapie nam się przydadzą
        await ctx.send("OTO TWOJA POMOC") #ctx.send wysyła wiadomość na kanale na którym została wywołana przez użytkownika

#teraz trzeba stworzyć setup
        
async def setup(client): #torzymy funkcje która automatycznie dodaje się do naszej obsługi plików
    await client.add_cog(Komendy(client)) #tutaj dodajemy naszą klase do obsługi plików

#5 PO STWORZENIU FUNKCJI
#Jeżeli stworzyłeś swoją komende to teraz musisz ją wywołać na discordzie
#aby ją wywołać wpisujesz swój prefix z pliku main np !pomoc oraz nazwe funkcji
#jak wszystko będzie działać to zobaczysz że bot napisze OTO TWOJA POMOC na kanale jako wiadomośc