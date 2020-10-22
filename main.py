import discord
import random
import json
import asyncio
import os
import datetime
from itertools import cycle
from discord import Member, Embed
from discord.ext import commands, tasks
from discord.ext.commands import Bot, command, cooldown, BucketType
from discord.utils import get


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
client.remove_command('help')
# region TOKEN

# endregion
status = cycle(['My default prefix is -', 'Use -help for a list of commands!'])


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_connect():
    print("Forcefield has connected to Discord! ;)")


@client.event
async def on_ready():
    change_status.start()
    print('Logged in as: ' + TOKEN)
    print("Forcefield is ready for takeoff!\n\n")


@client.event
async def on_task_start():
    print('Task started.')


@client.command()
async def stop(ctx):
    author = ctx.message.author
    authorid = ctx.author.id
    if authorid == 338999581474029578 or 533617333244133386:
        print(f'{author} stopped Forcefield')

        embed = discord.Embed(
            title='Stop',
            description="See you! :cry:",
            color=0x005275
        )

        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')

        await ctx.send(embed=embed)
        await client.logout()
        await client.close()
    else:
        pass

# COGS


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 338999581474029578 or 533617333244133386:
        client.load_extension(f'cogs.{extension}')
        await ctx.send('done')
        print(f'loaded {extension}')
    else:
        pass


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 338999581474029578 or 533617333244133386:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send('done')
        print(f'reloaded {extension}')
    else:
        pass


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 338999581474029578 or 533617333244133386:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send('done')
        print(f'unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# region PREFIXES


@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "-"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.command(aliases=["pre"])
@commands.has_permissions(manage_guild=True)
async def prefix(ctx, arg, *, prefix="-"):
    if arg == "set":
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        embed = discord.Embed(
            title="Prefix (set)",
            description="",
            color=0x005275
        )

    elif arg == "reset":
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = "-"

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        embed = discord.Embed(
            title="Prefix (reset)",
            description=f"{ctx.author.mention}, your server prefix has been reset!",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')

        await ctx.send(embed=embed)
# endregion

client.run(TOKEN)

# MINI_DISCORD
