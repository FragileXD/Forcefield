import discord
import random
import json
import asyncio
import os
import datetime
import time
from discord import Embed
from itertools import cycle
from discord import Member, Embed
from discord.ext import commands, tasks
from discord.ext.commands import Cog
from discord.ext.commands import Bot, command, cooldown, BucketType
from discord.utils import get


class Information(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_guild_join(self, guild):
        channel = await guild.create_text_channel('forcefield')
        embed = discord.Embed(
            title='Thanks!',
            description='Thank you for adding me! Use `-help` for all my commands',
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        await channel.send(embed=embed)

    @Cog.listener()
    async def on_member_remove(self, member):
        channel = get(member.guild.channels, name='member-logs')
        messages = ['Bye Bye',
                    'See ya later, alligator',
                    'why you bully us',
                    "you don't like jazz :(",
                    'didnt bring the pizza',
                    'bruv',
                    'went "Aight imma head out" on us',
                    'is a scammer (like OrangeBeatle123(so true(yes he actually is(yeah(yup(agreed(stop this please(no u(what the hell Wik(no u Lax(shut(no(yes(ok))))))))))))))',
                    'said, "Bye, losers!"',
                    'wow, you didnt have to do us like that',
                    'suit urself',
                    'is VERY unpog']

        embed = discord.Embed(
            title='Goodbye...',
            description=f'{member}, {random.choice(messages)}...',
            color=0x005275
        )
        embed.add_field(
            name='New member count:',
            value=member.guild.member_count,
            inline=False
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
        await channel.send(embed=embed)

    @Cog.listener()
    async def on_member_join(self, member):
        channel = get(member.guild.channels, name='member-logs')
        messages = ['Hope ya brang pizza',
                    'Welcome to the server!',
                    'Diamonds for YOU!',
                    'Hope you brang some pizza because we like that pizza you know',
                    'Good Human',
                    'Have fun',
                    'Good server choice',
                    'Thank you for choosing us',
                    ':)'
                    'Pretty neat',
                    'ez',
                    'ye boiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',
                    'I was gonna say summit, but I forgot.',
                    'Have a good stay',
                    'MINE DIAAAMONDSSSSSSSSSSSS',
                    'ya like jazz ~Bee Movie',
                    'likes to eat Pizza!',
                    'got THICC muscles',
                    'is pog for joining!',
                    'POGGERS',
                    'Thank you for taking the time out of your sweet century to join the marvellous server. Lots of love <3 from the Devs :)']

        embed = discord.Embed(
            title="Welcome!",
            description=f"{member.mention}, {random.choice(messages)}!",
            color=0x005275
        )
        embed.add_field(
            name='New member count:',
            value=member.guild.member_count,
            inline=False
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
        await channel.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description="My commands:",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/759782905860980766/761937275034533928/Untitled_12.png')
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')

        # FORCEFIELD
        embed.add_field(name='Forcefield',
                        value='`help`, `support`, `servers`, `creators`,\n`prefix <set <prefix>> / <reset>`', inline=False)
        # INFORMATION
        embed.add_field(
            name='Information', value='`usage`, `membercount`, `avatar`, `userinfo`, `channelinfo`', inline=False)
        # MISC
        embed.add_field(
            name='Misc', value='`ping`, `test`, `poll`, `say`, `embed`', inline=False)
        # GAMES
        embed.add_field(
            name='Games', value='`8ball`, `dice`, `wouldyourather`, `joke`, `wikipedia`', inline=False)
        # RPG
        embed.add_field(
            name="RPG", value="`rpginfo (WIP)`, `start (WIP)`", inline=False)
        # CALCULATOR
        embed.add_field(name='Calculator',
                        value='`add`, `subtract`, `multiply`, `divide`, `calculate`', inline=False)
        # GIVEAWAYS
        embed.add_field(
            name="Giveaways", value="`giveaway (WIP)`, `reroll (WIP)`, `claim (WIP)`", inline=False)
        # MODERATION
        embed.add_field(
            name='Moderation', value='`report (WIP)`, `kick`, `ban`, `unban`, `mute`, `unmute`,\n`purge`, `createtextchannel`, `createvoicechannel`, `lockdown`', inline=False)
        # SETUP
        embed.add_field(name='Setup (SUBCOMMANDS)',
                        value='`logs`, `memberlogs`, `rules`, `status`, `leveling`', inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['support'])
    async def invite(self, ctx):
        embed = discord.Embed(
            title='Support',
            description=f'{ctx.author.mention}, Support Forcefield™ here:',
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/759782905860980766/761937644413386752/Untitled_13.png')
        embed.add_field(name='Support server:',
                        value='[Click Here](https://discord.gg/TSE5gvJ)')
        embed.add_field(name='Invite Forcefield™:',
                        value='[Click Here](https://discord.com/api/oauth2/authorize?client_id=759474291267600402&permissions=8&scope=bot)')

        await ctx.send(embed=embed)

    @commands.command(aliases=['count'])
    async def membercount(self, ctx):
        if ctx.guild.member_count > 2:
            embed = discord.Embed(
                title="Member Count",
                description=f"The member count of your server is: {ctx.guild.member_count}!",
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(
                text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Member Count",
                description=f"{ctx.author.mention}, you should invite some friends xD",
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(
                text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)

    @commands.command()
    async def test(self, ctx):
        embed = discord.Embed(
            title='Test',
            description=f'{ctx.author.mention}, Test Test 123. Its working!',
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['userinfo', 'whois', 'info'])
    async def ui(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        roles = [role for role in member.roles]

        embed = discord.Embed(
            title='User Info',
            decription=f"{member.mention}'s info:",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(url=member.avatar_url)

        embed.add_field(name='Server Name:',
                        value=member.display_name, inline=True),
        embed.add_field(name='Created Account At:', value=member.created_at.strftime(
            '%a, %#d %B %Y, %I:%M %p UTC'), inline=True),
        embed.add_field(name='Joined Server At:', value=member.joined_at.strftime(
            '%a, %#d %B %Y, %I:%M %p UTC'), inline=True),
        embed.add_field(name=f'Roles ({len(roles)})', value=' '.join(
            [role.mention for role in roles]), inline=True),
        embed.add_field(name='Top Role:',
                        value=member.top_role.mention, inline=True),
        embed.add_field(name='ID:', value=member.id, inline=True),
        embed.add_field(name='Bot?', value=member.bot, inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['ci'])
    async def channelinfo(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(
            title=f"Channel Info",
            description=f"{channel.mention}'s info:",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.add_field(name="Channel Guild",
                        value=ctx.guild.name, inline=True)
        embed.add_field(name="Channel Id", value=channel.id, inline=True)
        embed.add_field(name="Channel Category",
                        value=f"{channel.category.name if channel.category else 'This channel is not in a category.'}", inline=True)
        embed.add_field(name="Channel Topic",
                        value=f"{channel.topic if channel.topic else 'This channel does not have a topic.'}", inline=True)
        embed.add_field(name="Channel Position",
                        value=channel.position, inline=True)
        embed.add_field(name="Channel Slowmode Delay",
                        value=channel.slowmode_delay, inline=True)
        embed.add_field(name="Channel Creation Time",
                        value=channel.created_at, inline=True)
        embed.add_field(name="Channel Permissions Synced",
                        value=channel.permissions_synced, inline=True)
        embed.add_field(name="NSFW?", value=channel.is_nsfw(), inline=True)
        embed.add_field(name="Announcements?",
                        value=channel.is_news(), inline=True)

        await ctx.send(embed=embed)

    @commands.command(aliases=["si"])
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title="Server Info",
            description=f"Info about {ctx.guild.name}",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.add_field(name="Name:", value=ctx.guild.name, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Ping",
            description=f"The Bots Ping Is: {round(self.client.latency * 1000)}MS Right Now.",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        await ctx.send(embed=embed)

    @commands.command()
    async def creators(self, ctx):
        embed = discord.Embed(
            title="Creators",
            description="<@338999581474029578> and <@533617333244133386> made Forcefield™!",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        await ctx.send(embed=embed)

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        embed = discord.Embed(
            title="Avatar",
            description=f"{member.mention}'s avatar:",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["s"])
    async def servers(self, ctx):
        embed = discord.Embed(
            title="Servers",
            description="I am in " +
            str(len(self.client.guilds)) + " servers!",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')

        await ctx.send(embed=embed)

    @commands.command(aliases=["nickname"])
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member = None, *, nickname=None):
        if member == None:
            member = ctx.author

        if nickname == None:
            nickname = member.name

        await member.edit(nick=nickname)


def setup(client):
    client.add_cog(Information(client))

# NOTES
