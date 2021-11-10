from discord.embeds import Embed
from discord.ext import commands
from discord import Member
from discord.utils import get
import random

class GameSelector(commands.Cog):
    available_games = []

    def __init__(self, bot) -> None:
        self._original_help_command = bot.help_command

        self.bot = bot
        self.bot.help_command.cog = self
        self.preload_games()
        self.available_games.sort()
    
    def preload_games(self) -> None:
        self.available_games += [
            "Terraria",
            "Minecraft",
            "Alien Swarm",
            "Icarus",
            "Monster Hunter: World",
            "Hunt: Showdown",
            "Bloons Tower Defense 6",
            "Factorio",
            "Halo",
            "Valheim",
            "Deep Rock Galactic"
        ]
    
    @commands.command("add-game")
    async def add_game(self, ctx, *, game: str):
        # Try to validate the spelling of the game????
        # probably non-trivial
        # Maybe try a regex. Definitely validate that it isn't a link...
        if game in self.available_games:
            await ctx.send(f"{game} is already in games!")
            return
            
        self.available_games.append(game)
        await ctx.send(f"Added {game} to the library of available games!")
        
        self.available_games.sort()

    @commands.command("random")
    async def random_game(self, ctx) -> None:
        if len(self.available_games) == 0:
            await ctx.send("There are no games to pick from!")
            return
        await ctx.send(f"You should play: {random.choice(self.available_games)}!")

    @commands.command("games")
    async def show_games(self, ctx) -> None:
        if len(self.available_games) == 0:
            await ctx.send("There are no games in the library!")
            return

        embed = Embed(title="Available Games:")
        games = [f"{c+1}. {v}" for c,v in enumerate(self.available_games)]
        embed.add_field(name="All Games", value="\n".join(games), inline=False)

        await ctx.send(embed=embed)

    @commands.command("remove-game")
    async def remove_game(self, ctx, *, game: str) -> None:
        if game in self.available_games:
            self.available_games.remove(game)
            await ctx.send(f"Removed {game} from the library")
            return
        await ctx.send(f"{game} isn't even in the library, dummy")
    
    @commands.command("help-brandon")
    async def help_brandon(self, ctx):
        await ctx.send(f"There is no helping {ctx.message.server.get_member(393153618217402379).mention}")
