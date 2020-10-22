import discord
import random
import json
import asyncio
import os
from itertools import cycle
from discord import Member, Embed
from discord.ext import commands, tasks
from discord.ext.commands import Bot, command, cooldown, BucketType
from discord.utils import get

client = commands.Bot(command_prefix = '-', case_insensitive=True)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        title=':x: Error :x:',
        description=f'{ctx.author.mention}, The Server prefix is `/`.',
        color=0xFF0000
        )
        embed.set_footer(text='Forcefield')
        embed.add_field(name='Please fill in all required arguments!', value='Use the `help` command for a list of commands.', inline=False)
        await ctx.message.add_reaction('👎')
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
        title=':x: Error :x:',
        description=f'{ctx.author.mention}, The Server prefix is `/`.',
        color=0xFF0000
        )
        embed.set_footer(text='Forcefield')
        embed.add_field(name='That is not a command', value='Use the `help` command for a list of commands.', inline=False)
        await ctx.message.add_reaction('👎')
        await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
        title=':x: Error :x:',
        description=f'{ctx.author.mention}, The Server prefix is `/`.',
        color=0xFF0000
        )
        embed.set_footer(text='Forcefield')
        embed.add_field(name='Object not found!', value='Use the `help` command for a list of commands.', inline=False)
        await ctx.message.add_reaction('👎')
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
        title=':x: Error :x:',
        description=f'{ctx.author.mention}, The Server prefix is `/`.',
        color=0xFF0000
        )
        embed.set_footer(text='Forcefield')
        embed.add_field(name='You do not have permission to use this command!', value='Use the `help` command for a list of commands.', inline=False)
        await ctx.message.add_reaction('👎')
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
        title=':x: Error :x:',
        description=f'{ctx.author.mention}, The Server prefix is `/`.',
        color=0xFF0000
        )
        embed.set_footer(text='Forcefield')
        embed.add_field(name=f'You are on cooldown for this command! Try again in {error.retry_after//60:,.1f} minutes.', value='Use the `help` command for a list of commands.', inline=False)
        await ctx.message.add_reaction('👎')
        await ctx.send(embed=embed)

@client.event
async def on_command_erro(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
        title=':x: Error :x:',
        description=f'{ctx.author.mention}, An error occured!',
        color=0xFF0000
        )
        embed.set_footer(text='Forcefield')
        embed.add_field(name=f'You are on cooldown for this command! Try again in {error.retry_after//60:,.2f} minutes.', value='Use the `help` command for a list of commands.', inline=False)
        await ctx.message.add_reaction('👎')
        await ctx.send(embed=embed)
