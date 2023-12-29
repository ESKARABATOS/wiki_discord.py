#1 WPROWADZENIE

#Plik Main.py lub app.py 
#ten plik służy do uruchamiana naszego bota oraz przypisywania do niego poleceń które nie działają pomiędzy plikami

#2 START

#Aby zacząć programowanie discord bota najpierw trzeba zaimportować biblioteke discorda oraz ją zainstalować
#Aby ją zainstalować wpisujemy w cmd pip install discord.py lub pip install discord

#IMPORTY
import discord #Importowanie biblioteki discorda
import os
from discord.ext import commands #z biblioteki discorda zaimportujemy obsługiwanie komend

#następnie tworzymy uprawnienie do polecen i ogólnie wszystkiego
intents = discord.Intents.all() #zmienna do uprawnien

#teraz ztworzymy klienta bota
client = commands.Bot(command_prefix="!", intents=intents)# w '' USTALAMY PREFIX POLECEŃ BOTA NP. ! oraz dodajemy do klienta uprawnienia poprzez intents=intents

#teraz musimy połączyć główny plik z innymi plikami aby bot obsługiwał pliki poboczne np. Polecenia lub Eventy

#tworzymy klase Main
class Main():
    def __init__(self):
        pass
        #tutaj możemy przypisać zmienne klasowe jeżeli potrzebujemy do rozwinięća naszego systemu do plików

    #zaczynamy tworzyć funkcje do plików
    async def commands_func(self):
        #tworzymy pętle for która będzie wyświetlać wszystkie pliki z folderu podanego w ''
        #oraz aby obsługiwać pliki musimy zaimportować biblioteke wbudowaną os poprzez import os
        for i in os.listdir(f'./commands'): #folder commands musi zostać przez ciebie stworzony lub napisz kod który tworzy folder jeżeli nie jest stoworzny
            #treaz sprawdzimy czy plik jest z rozszerzeniem .py
            if i.endswith('.py'):
                #oraz załadujemy pliki
                await client.load_extension(f'commands.{i[:-3]}') #nazwa w tej linijce jest commands która też jest w 34 linijce jest to obowiązkowe nazwy muszą być takie same
                #to tyle w tej funkcji 

#teraz stworzymy aby funkcja z klasy byłą ogólno dostępna dla skryptu w tym pliku
#nazwa funkcji dowolna 
obj = Main() #po = nazwa musi być taka sama jak nazwa klasy

#następnie stworzymy event (wydarzenie) które wywoła nam funkcje po włączeniu bota 

@client.event #tworzenie eventu (wydarzenia)
async def on_ready(): #tworzenie funkcji on_ready (po włączeniu)
    print("Bot został uruchomiony") #funkcja print z angielskiego jest to drukowanie na ekranie w naszym przypadku jest to drukowanie w konsoli treści zawartej w ''
    await obj.commands_func() #wywołanie funkcji do plików z linijki 31

#Tworzenie komendy w głównym pliku bota
@client.command() #tworzenie komendy
async def test(ctx): #tworzenie nazwy funkcji czyli nazwy komendy 
    ctx.send("TESTOWA KOMENDA") #wysyłanie wiadomości na kanał na którym została wywołana komenda

#teraz stworzymy funkcje która uruchamia bota
    
client.run('') #Możemy dodać config który będziemy zmieniać w pliku config aby to zrobić trzeba stworzyć plik config.py oraz stworzyć słownik w pliku konfiguracyjnym gdzie przypiszemy token i inne funkcje które potrzebujemy

#3 TWORZENIE BOTA NA STRONIE
#token bota uzyskasz na tej stronie https://discord.com/developers/docs/intro
#aby zrobić poprawnie bota trzeba wejść na strone powyrzej oraz w zakładce Bot zaznaczyć 3 funkcje PRESENCE INTENT, SERVER MEMBERS INTENT, oraz MESSAGE CONTENT INTENT 
#jeżeli to jest gotowe to wchodzimy w OAuth2 
#Następnie w URL GENERATOR
#wybieramy w SCOPES bot
#wybieramy w BOT PERMISSIONS ADMINISTRATOR 
#Kopjujemy link i wklejamy na waszym discordzie i zapraszamy bota

#jeżeli wszystko zadziała w konsoli bota ukarze się informacja którą wpisaliśmy w lini 49

