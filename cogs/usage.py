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

class Usage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def usage(self, ctx, arg=None):
        if arg == None:
            embed = discord.Embed(
                title='Usage',
                description='Usage for `usage`: "-usage <command>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "help":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `help`: "-help"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "support":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `support`: "-support"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "test":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `test`: "-test"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "membercount":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `membercount`: "-membercount"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "userinfo":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `userinfo`: "-userinfo <user (optional)>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "poll":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `poll`: "-poll "<poll question>" <answer 1> <answer 2> <answer 3> <answer 4> <answer 5> <answer 6> <answer 7> <answer 8> <answer 9> <answer 10>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "say":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `say`: "-say <argument>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "8ball":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `8ball`: "-8ball <question>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "dice":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `dice`: "-dice <question (optional)>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "wouldyourather":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `wouldyourather`: "-wouldyourather"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "kick":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `kick`: "-kick <user> <reason (optional)>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "ban":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `ban`: "-ban <user> <reason (optional)>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "unban":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `unban`: "-unban <name+tag>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "mute":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `mute`: "-mute <user> <reason (optional)>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "unmute":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `unmute`: "-unmute <user>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "purge":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `purge`: "-purge <amount>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "createtextchannel":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `createtextchannel`: "-createtextchannel <name>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "createvoicechannel":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `createvoicechannel`: "-createvoicechannel <name>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "lockdown":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `lockdown`: "-lockdown <channel>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)
        elif arg == "setup":
            embed = discord.Embed(
                title='Usage',
                description='Usage for `setup`: "-setup <subcommand (see help command)>"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Usage(client))