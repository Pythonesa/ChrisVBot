from _secrets import IRC_TOKEN
from twitchio.ext import commands
import bot_commands.bot_commands as bc

class ChatReader(commands.Bot):
    def __init__(self):
        super().__init__(
            token=IRC_TOKEN,
            prefix='!',
            initial_channels=['chrisvdev']
        )

        self.add_command(bc.commands)

    
    async def event_ready(self):
        print(f"Bot has connected to Twitch as {self.nick}")


def main():
    reader = ChatReader()
    reader.run()

if __name__ == "__main__":
    main()