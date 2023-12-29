#Tworzenie eventu
#Główny plik
@client.event
async def on_message(): #ta funkcja uruchamia się tylko w tedy kiedy ktokolwiek wyśle wiadomość na kanale 
    #KONTYNUACJA KODU

#W Wielu plikach w schemacie wiki
@commands.Cog.listener()
async def on_message(self):
    #KONTYNUACJA KODU

#praktyczne zastosowanie
    
@client.event()
async def on_message(message):
    print(message.content)

@commands.Cog.listener()
async def on_message(self, message):
    print(message.content)

#tą funkcje można wykorzystać do 
#liczenia wiadomości 
#ogranicza się tylko twoja wyobraznia