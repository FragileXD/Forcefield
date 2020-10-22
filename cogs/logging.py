import discord
from discord import Embed as embed
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Cog as cog


class Logging(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog.listener()
    async def on_message_delete(self, message):
        channels = str(message.guild.channels)
        if "logs" in channels:
            channel = get(message.guild.channels, name="logs")
            embed = discord.Embed(
                title="Message Deleted",
                description=f'"{message.content}"',
                color=0x005275
            )
            embed.add_field(name="Channel:",
                            value=message.channel.mention, inline=False)
            embed.add_field(
                name="Author:", value=message.author.mention, inline=False)
            embed.add_field(name="Created at:",
                            value=message.created_at, inline=False)
            await channel.send(embed=embed)
        else:
            pass

    @cog.listener()
    async def on_member_join(self, member):
        channels = str(member.guild.channels)
        if "logs" in channels:
            channel = get(member.guild.channels, name="logs")
            embed = embed(
                title="Member Joined",
                description=f"{member.mention}, {member}",
                color=0x005275
            )
            embed.add_field(name="Account age:", value=member.crea)

            await channel.send(embed=embed)


def setup(client):
    client.add_cog(Logging(client))

# NOTES
