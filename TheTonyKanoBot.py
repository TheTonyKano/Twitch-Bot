import irc.bot

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel, bot_user_id):
        self.client_id = client_id
        self.token = token
        self.channel = "#" + channel
        self.bot_user_id = bot_user_id
        self.running = True
        server = 'irc.chat.twitch.tv'
        port = 6667
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, f"oauth:{token}")], username, username)

    def on_welcome(self, connection, event):
            connection.join(self.channel)

    def on_pubmsg(self, connection, event):
        username = event.source.split('!')[0]
        message = event.arguments[0]

        if message == '!hello':
            connection.privmsg(self.channel, f'Hello, {username}!')

    def on_whisper(self, connection, event):
        username = event.source.split('!')[0]
        message = event.arguments[0]

        if message == '!hello':
            connection.privmsg(f'/w {username}', f'Hello, {username}!')

    def start_bot(self):
        self.running = True
        self.start()

    def stop_bot(self):
        self.running = False
        self.connection.disconnect()
    
