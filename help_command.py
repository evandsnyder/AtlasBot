from discord.ext import commands
from discord import Embed

class AtlasBotHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return f"{self.clean_prefix}{command.qualified_name} {command.signature}"

    async def send_bot_help(self, mapping):
        embed = Embed(title="Help")
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)
        
        channel = self.get_destination()
        await channel.send(embed=embed)
       
   # !help <command>
    async def send_command_help(self, command):
        embed = Embed(title=self.get_command_signature(command))
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)
    
    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = Embed(title="Error", description=str(error))
            await ctx.send(embed=embed)
        else:
            raise error