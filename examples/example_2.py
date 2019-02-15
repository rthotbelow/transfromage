import transfromage

client = transfromage.Client()

@client.event
def on_ready():
    client.setCommunity('EN')
    client.login("Username", "Password", "Room name")

@client.event
def on_logged():
    print('Logged in! '+client.player.name)

@client.event
def on_room_message(message):
    if message.content == '!look':
        client.sendRoomMessage(message.author.name+', '+message.author.look)


client.start('api-id', 'token') 
 
