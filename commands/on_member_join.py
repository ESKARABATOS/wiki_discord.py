#Event działa tylko wtedy kiedy ktoś dołączy na serwer

#Główny plik
@client.event
async def on_member_join(): #tworzenie funkcji eventu
    #KONTYNUACJA KODU

#W Wielu plikach w schemacie wiki
@commands.Cog.listener()
async def on_member_join(self):
    #KONTYNUACJA KODU

#praktyczne zastosowanie

#Główny plik
@client.event()
async def on_member_join(message):
    #tworzymy zmienną channel która przechowuje nazwe kanału powitania
    channel = discord.utils.get(message.guild.channels, name="powitania")
    await channel.send(f"Witamy cię {message.mention} na serwerze {message.guild}") #wysyła wiadomość na kanał ze zmiennej channel

#W Wielu plikach w schemacie wiki
@commands.Cog.listener()
async def on_member_join(self, message):
    #tworzymy zmienną channel która przechowuje nazwe kanału powitania
    channel = discord.utils.get(message.guild.channels, name="powitania")
    await channel.send(f"Witamy cię {message.mention} na serwerze {message.guild}") #wysyła wiadomość na kanał ze zmiennej channel