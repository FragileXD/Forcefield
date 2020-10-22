import discord
import datetime
import time
import asyncio
import random
import json
from discord.ext import commands
from discord.utils import get


class Giveaways(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giveaway(self, ctx, mins: int = None, *, prize: str):
        roles = str(ctx.guild.roles)
        if mins == None:
            return True

        if "Giveaway Master" in roles:
            role = get(ctx.guild.roles, name="Giveaway Master")
            if role in ctx.author.roles:
                channels = str(ctx.guild.channels)
                if "giveaways" in channels:
                    channel = get(ctx.guild.channels, name="giveaways")
                    embed = discord.Embed(
                        title="Giveaway",
                        description=f"{ctx.author.mention} is hosting a giveaway!",
                        color=0x005275
                    )
                    end = datetime.datetime.utcnow() + datetime.timedelta(seconds=mins * 60)
                    tday = datetime.date.today()
                    embed.set_footer(
                        text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                    embed.add_field(name="Prize:", value=prize, inline=True)
                    embed.add_field(
                        name="Ends at:", value=f"{end} UTC ({mins} minutes from now)!", inline=True)
                    message = await channel.send("@everyone", embed=embed)

                    await message.add_reaction("🎉")
                    await asyncio.sleep(mins * 60)

                    with open("giveaways.json", "r") as f:
                        giveawayload = json.load(f)

                    giveawayload[str(ctx.message.id)] = prize

                    with open("giveaways.json", "w") as f:
                        json.dump(giveawayload, f, indent=4)

                    message2 = await channel.fetch_message(message.id)
                    users = await message2.reactions[0].users().flatten()
                    users.pop(users.index(self.client.user))

                    winner = random.choice(users)

                    wembed = discord.Embed(
                        title="Giveaway Winner",
                        description=f"🥳Congratulations {winner}! You just won {prize}!🥳",
                        color=0x005275
                    )
                    tday = datetime.date.today()
                    wembed.set_footer(
                        text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                    await channel.send(embed=wembed)

                    return True
                else:
                    guild = ctx.guild
                    await guild.create_text_channel(name="giveaways")
                    embed = discord.Embed(
                        title="Almost there!",
                        description=f"Hey, {ctx.author.mention}, you didnt have a giveaways channel, so we set one up for you!\nRun the same command to post your giveaway.",
                        color=0x005275
                    )
                    tday = datetime.date.today()
                    embed.set_footer(
                        text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                    await ctx.send(embed=embed)
                    return True

            else:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `Giveaway Master` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)
                return True
        else:
            guild = ctx.guild
            await guild.create_role(name="Giveaway Master")
            if not "Giveaway Master" in ctx.author.roles:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `Giveaway Master` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)
                return True

    @commands.command()
    async def reroll(self, ctx):
        roles = str(ctx.guild.roles)
        if "Giveaway Master" in roles:
            role = get(ctx.guild.roles, name="Giveaway Master")
            if role in ctx.author.roles:
                channels = str(ctx.guild.channels)
                if "giveaways" in channels:
                    channel = get(ctx.guild.channels, name="giveaways")
                    channel.send("test")
                    pass

    @commands.command()
    async def claim(self, ctx):
        pass


def setup(client):
    client.add_cog(Giveaways(client))
