from os import getenv
from dotenv import load_dotenv
from discord.ext import commands

from game_selector import GameSelector
from help_command import AtlasBotHelp

class AtlasBot(commands.Bot):
    def __init__(self, command_prefix, help_command: commands.HelpCommand = AtlasBotHelp(), description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)

        self.add_cog(GameSelector(self))

    async def on_ready(self):
        print(f"Connected to {self.guilds[0]} as {self.user.name}")


def main():
    load_dotenv()
    TOKEN = getenv('DISCORD_TOKEN')

    bot = AtlasBot(command_prefix="!")
    bot.run(TOKEN)


if __name__ == "__main__":
    main()