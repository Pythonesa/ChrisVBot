from _secrets import IRC_TOKEN
from twitchio.ext import commands

class ChatReader(commands.Bot):
    def __init__(self):
        super().__init__(
            token=IRC_TOKEN,
            prefix='!',
            initial_channels=['chrisvdev']
        )

    
    async def event_ready(self):
        print(f"Bot has connected to Twitch as {self.nick}")


def main():
    reader = ChatReader()
    reader.run()

if __name__ == "__main__":
    main()