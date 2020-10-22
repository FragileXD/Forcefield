import discord
import random
import json
import asyncio
import os
import datetime
import time
from itertools import cycle
from discord import Member, Embed
from discord.ext import commands, tasks
from discord.ext.commands import Bot, command, cooldown, BucketType
from discord.utils import get


class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def setup(self, ctx, arg=None):
        if arg == None:
            await ctx.send(':no_entry: You can do: logs, member-logs or memberlogs, rules and giveaways! :no_entry:')
        elif arg == "logs":
            guild = ctx.guild
            channels = str(ctx.guild.channels)
            if 'logs' in channels:
                embed = discord.Embed(
                    title=':x: Error :x:',
                    description=f'{ctx.author.mention}, You have already set up logs\nOr you already have a channel called logs (Forcefield will use that channel instead.)',
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
                await ctx.send(embed=embed)
            else:
                await guild.create_text_channel('logs')
                embed = discord.Embed(
                    title='Logs',
                    description=f'{ctx.author.mention}, logs are now activated!',
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
                await ctx.send(embed=embed)
        elif arg == "memberlogs":
            guild = ctx.guild
            channels = str(ctx.guild.channels)
            if 'member-logs' in channels:
                embed = discord.Embed(
                    title=':x: Error :x:',
                    description=f'{ctx.author.mention}, You have already set up memberlogs\nOr you already have a channel called member-logs (Forcefield will use that channel instead.)',
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
                await ctx.send(embed=embed)
            else:
                await guild.create_text_channel('member-logs')
                embed = discord.Embed(
                    title='Member Logs',
                    description=f'{ctx.author.mention}, member-logs are now activated!',
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
                await ctx.send(embed=embed)
        elif arg == "rules":
            guild = ctx.guild
            channels = str(ctx.guild.channels)
            if 'rules' in channels:
                embed = discord.Embed(
                    title=':x: Error :x:',
                    description=f'{ctx.author.mention}, you have already set up rules\nOr you already have a channel called rules (Forcefield will use that channel instead.)',
                    color=0xFF0000
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)
            else:
                await guild.create_text_channel('rules')
                embed = discord.Embed(
                    title='Set Up Rules! :partying_face:',
                    description=f'{ctx.author.mention}, you now set up your rules channel!',
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')

                ruleembed = discord.Embed(
                    title=f'Rules',
                    description=f'Rules made by Forcefield™\n(This message is optional! Feel free to delete.)',
                    color=0x005275
                )
                tday = datetime.date.today()
                ruleembed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                ruleembed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/753886478362476554/760905614435418142/tmrules.png')

                # FIELDS
                ruleembed.add_field(
                    name='Swearing', value='Please do not swear in this server. We try to keep it as PG as possible', inline=True)
                ruleembed.add_field(
                    name='DMing', value="Please don't DM Members of this Discord! (If this happens to you, please ignore the message and DON'T CLICK ANY LINKS!)", inline=True)
                ruleembed.add_field(
                    name='Spamming', value="Please don't spam in the Channels. It will result in a WARNING/MUTE/KICK!", inline=True)
                ruleembed.add_field(
                    name='Raiding', value="Please don't encourage raiding in this server! This will annoy people and may get you kicked or banned.", inline=True)
                ruleembed.add_field(
                    name="Innapropriate PFP's", value='Your profile picture should not contain any explicit content! If someone does have an innapropriate GIF/IMG please PING or DM a Staff Member.', inline=True)
                ruleembed.add_field(
                    name='Pinging', value="Please don't randomly ping staff/members without reason! This will result in a WARNING/MUTE!", inline=True)
                ruleembed.add_field(
                    name='Nicknames', value='Please DO NOT change your nickname to anything not Family Friendly/PG.', inline=True)
                ruleembed.add_field(
                    name='Respect', value='Please treat the other members with respect. Stay cool!', inline=True)
                ruleembed.add_field(
                    name='Help Staff', value='Remind other people of the rules when they break them. Also keep an eye on your own messages! >:(', inline=True)
                ruleembed.add_field(
                    name='Mini-Helpers', value='Please DO NOT MINI-MOD/MINI-HELPER in this server. Staff will take care of the situation. (The least you can do is PING a staff member.)', inline=True)
                ruleembed.add_field(
                    name='Have fun', value='The most important rule is to OF COURSE Have Fun! Or not.', inline=True)
                ruleembed.add_field(
                    name='THANKS!', value='Thank you for choosing Forcefield™ as your prefered Bot! It makes us (The Developers) very happy :D', inline=True)

                channel = get(ctx.guild.channels, name='rules')
                await ctx.send(embed=embed)
                await channel.send(embed=ruleembed)
        elif arg == "status":
            guild = ctx.guild
            channels = str(ctx.guild.channels)
            if 'forcefield-status' in channels:
                pass
            else:
                await guild.create_text_channel('forcefield-status')
                channel = get(ctx.guild.channels, name='forcefield-status')
                embed = discord.Embed(
                    title='Set Up Status! :partying_face:',
                    description=f'{ctx.author.mention}, you now set up your status channel!',
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)

                sembed = discord.Embed(
                    title=f'Status',
                    description='Status info by Forcefield™\n(This message is optional! Feel free to delete.)',
                    color=0x005275
                )
                tday = datetime.date.today()
                sembed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await channel.send(embed=sembed)
        elif arg == "leveling":
            guild = ctx.guild
            channels = str(ctx.guild.channels)
            if 'leveling' in channels:
                pass
            else:
                await guild.create_text_channel('leveling')
                embed = discord.Embed(
                    title='Set Up Leveling! :partying_face:',
                    description=f'{ctx.author.mention}, you now set up your Leveling Channel!',
                    color=0x005275
                )
                tday = datetime.date.today()
                embed.set_footer(
                    text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Setup(client))

# NOTES
