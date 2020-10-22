import discord
import random
import json
import asyncio
import os
import datetime
import PIL
from aiohttp import ClientSession
from itertools import cycle
from discord import Member, Embed
from discord.ext import commands, tasks
from discord.ext.commands import Bot, command, cooldown, BucketType, Cog
from discord.utils import get


class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        roles = str(ctx.guild.roles)
        if "calculator" in roles:
            role = get(ctx.guild.roles, name="calculator")
            if role in ctx.author.roles:
                embed = discord.Embed(
                    title="Add",
                    description=f"{ctx.author.mention}, this is my calculation:",
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.add_field(name="Calculation:",
                                value=f"{left} + {right}", inline=True)
                embed.add_field(name="Answer:", value=left +
                                right, inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)
        else:
            guild = ctx.guild
            await guild.create_role(name="calculator")
            role = get(ctx.guild.roles, name="calculator")
            if role in ctx.author.roles:
                embed = discord.Embed(
                    title="Add",
                    description=f"{ctx.author.mention}, this is my calculation:",
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.add_field(name="Calculation:",
                                value=f"{left} + {right}", inline=True)
                embed.add_field(name="Answer:", value=left +
                                right, inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)

    @commands.command()
    async def multiply(self, ctx, left: int, right: int):
        roles = str(ctx.guild.roles)
        if "calculator" in roles:
            role = get(ctx.guild.roles, name="calculator")
            if role in ctx.author.roles:
                embed = discord.Embed(
                    title="Multiply",
                    description=f"{ctx.author.mention}, this is my calculation:",
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.add_field(name="Calculation:",
                                value=f"{left} x {right}", inline=True)
                embed.add_field(name="Answer:", value=left *
                                right, inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)
        else:
            guild = ctx.guild
            await guild.create_role(name="calculator")
            role = get(ctx.guild.roles, name="calculator")
            if role in ctx.author.roles:
                embed = discord.Embed(
                    title="Multiply",
                    description=f"{ctx.author.mention}, this is my calculation:",
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.add_field(name="Calculation:",
                                value=f"{left} x {right}", inline=True)
                embed.add_field(name="Answer:", value=left *
                                right, inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)

    @commands.command()
    async def divide(self, ctx, left: int, right: int):
        if right == 0:
            embed = discord.Embed(
                title=":x: Error :x:",
                description=f"Hey, {ctx.author.mention}, you can not define by 0!",
                color=0xFF0000
            )
            tday = datetime.date.today()
            embed.set_footer(
                text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
        else:
            roles = str(ctx.guild.roles)
            if "calculator" in roles:
                role = get(ctx.guild.roles, name="calculator")
                if role in ctx.author.roles:
                    embed = discord.Embed(
                        title="Divide",
                        description=f"{ctx.author.mention}, this is my calculation:",
                        color=0x005275
                    )
                    tday = datetime.date.today()
                    embed.set_footer(
                        text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                    embed.add_field(name="Calculation:",
                                    value=f"{left} : {right}", inline=True)
                    embed.add_field(
                        name="Answer:", value=left // right, inline=True)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title=":x: Error :x:",
                        description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                        color=0xFF0000
                    )
                    tday = datetime.date.today()
                    embed.set_footer(
                        text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                    await ctx.send(embed=embed)
            else:
                guild = ctx.guild
                await guild.create_role(name="calculator")
                role = get(ctx.guild.roles, name="calculator")
                if role in ctx.author.roles:
                    embed = discord.Embed(
                        title="Divide",
                        description=f"{ctx.author.mention}, this is my calculation:",
                        color=0x005275
                    )
                    tday = datetime.date.today()
                    embed.set_footer(
                        text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                    embed.add_field(name="Calculation:",
                                    value=f"{left} : {right}", inline=True)
                    embed.add_field(
                        name="Answer:", value=left // right, inline=True)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title=":x: Error :x:",
                        description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                        color=0xFF0000
                    )
                    tday = datetime.date.today()
                    embed.set_footer(
                        text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                    await ctx.send(embed=embed)

    @commands.command()
    async def subtract(self, ctx, left: int, right: int):
        roles = str(ctx.guild.roles)
        if "calculator" in roles:
            role = get(ctx.guild.roles, name="calculator")
            if role in ctx.author.roles:
                embed = discord.Embed(
                    title="Subtract",
                    description=f"{ctx.author.mention}, this is my calculation:",
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.add_field(name="Calculation:",
                                value=f"{left} - {right}", inline=True)
                embed.add_field(name="Answer:", value=left -
                                right, inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)
        else:
            guild = ctx.guild
            await guild.create_role(name="calculator")
            role = get(ctx.guild.roles, name="calculator")
            if role in ctx.author.roles:
                embed = discord.Embed(
                    title="Subtract",
                    description=f"{ctx.author.mention}, this is my calculation:",
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.add_field(name="Calculation:",
                                value=f"{left} - {right}", inline=True)
                embed.add_field(name="Answer:", value=left -
                                right, inline=True)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: Error :x:",
                    description=f"Hey, {ctx.author.mention}, you do not have the `calculator` role!",
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)

    @commands.command()
    async def calculate(self, ctx, left: int, middle, right: int):
        if middle == "+":
            await ctx.send(left + right)
        elif middle == "-":
            await ctx.send(left - right)
        elif middle == "x":
            await ctx.send(left * right)
        elif middle == "/":
            await ctx.send(left // right)


def setup(client):
    client.add_cog(Calculator(client))
