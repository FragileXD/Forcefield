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

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=' '):
        embed = discord.Embed(
        title='Kick',
        description=f'{ctx.author.mention} has kicked {member.mention} for {reason}.',
        color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/759782905860980766/761938217876324352/Untitled_14.png')
        await member.kick(reason=reason)
        await ctx.send(embed=embed)
        
        dmembed = discord.Embed(
        title='Kick',
        description=f'{member.mention}, you have been kicked from {ctx.member.guild} for {reason}!\nTry to behave next time.',
        color=0x005275
        )
        tday = datetime.date.today()
        dmembed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        dmembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/759782905860980766/761938217876324352/Untitled_14.png')
        await member.send(embed=dmembed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=' '):
        embed = discord.Embed(
        title='Banned User',
        description=f'User, {member.mention} has been banned!',
        color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/759782905860980766/761938902579019796/Untitled_15.png')
        embed.add_field(name="Reason:", value=f"{reason}", inline=False)

        dmembed = discord.Embed(
        title='Banned!',
        description=f'You have been banned from {member.guild} for: {reason}!\nTry to behave next time.',
        color=0x005275
        )
        tday = datetime.date.today()
        dmembed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        dmembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/759782905860980766/761938902579019796/Untitled_15.png')
        await member.ban(reason=reason)
        await member.send(embed=dmembed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member : discord.Member):
        banned_users = await ctx.guild.bans()
        member_name, member_disciminator = member.split('-')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_disciminator):
                await ctx.guild.unban(user)
                return
        
    @commands.command(aliases=["m", 'mute'])
    @commands.has_permissions(manage_roles=True)
    async def _mute(self, ctx, member : discord.Member, *, reason=' '):
        roles = str(ctx.guild.roles)
        guild = ctx.guild
        if "Muted" in roles:
            role = discord.utils.get(guild.roles, name='Muted')
            await member.add_roles(role)

            embed = discord.Embed(
            title='Muted User',
            description=f'User, {member.mention} has been Muted for {reason}!',
            color=0x005275
            )

            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
            embed.add_field(name="Duration", value="Permanent")

            await ctx.send(embed=embed)
        else:
            guild = ctx.guild
            await guild.create_role(name='Muted', permissions=discord.Permissions(send_messages=False))

    @commands.command(aliases=['um', 'unm'])
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member : discord.Member):
        roles = str(ctx.guild.roles)
        if 'Muted' in roles:
            role = get(ctx.guild.roles, name='Muted')
            await member.remove_roles(role)
            await role.delete()
        else:
            await ctx.send(f"{member.mention} is NOT muted!")

    @commands.command(aliases=[''])
    @commands.has_permissions(manage_channels=True)
    async def createtextchannel(self, ctx, *, name):
        guild = ctx.guild
        channels = str(ctx.guild.channels)
        if name in channels:
            pass
        else:
            await guild.create_text_channel(name)
            await ctx.send(f'Created text channel {name}!')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def createvoicechannel(self, ctx, *, name):
        guild = ctx.guild
        channels = str(ctx.guild.channels)
        if name in channels:
            pass
        else:
            await guild.create_voice_channel(name)
            await ctx.send(f'Created voice channel {name}')

    @commands.command()
    async def purge(self, ctx, amount : int):
        embed = discord.Embed(
            title='Purge',
            description=f'{ctx.author.mention} has purged {amount} messages.',
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/753886478362476554/760172570376667176/Untitled_10.png')
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def report(self, ctx, member : discord.Member=None, subject=None, addition=None):
        if member == None:
            await ctx.send(f"Hey, {ctx.author.name}, please fill in a member to report!")
            return True
        if subject == None:
            await ctx.send(f"Hey, {ctx.author.name}, please fill in a subject!\nExamples: `raiding`, `spamming`, etc.")
            return True

        await ctx.send(f"You reported {member.name} for {subject} with the addition of {addition}.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            embed = discord.Embed(
                title="Lockdown",
                description=f"I have now put {channel.name} in lockdown.",
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(
                title="Lockdown",
                description=f"I have now put {channel.name} in lockdown.",
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(
                title="Lockdown",
                description=f"I have now removed {channel.name} from lockdown.",
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
            
    @commands.command()
    async def votekick(self, ctx, member : discord.Member=None, *, reason=' '):
        if member == None:
            embed = discord.Embed(
                title=":x: Error :x:",
                description=f"{ctx.author.mention}, please fill in a member to votekick.",
                color=0xFF0000
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
            return True
        elif member == ctx.author:
            embed = discord.Embed(
                title=":x: Error :x:",
                description=f"{ctx.author.mention}, you can not votekick yourself.",
                color=0xFF0000
            )
            tday = datetime.date.today()
            embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
            return True
            
        embed = discord.Embed(
            title="Votekick",
            description=f"{ctx.author.mention} wants to kick {member.mention} for {reason}",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.add_field(name=f"React with 👍 to votekick", value="5 votes are needed.")
        
        message = await ctx.send(embed=embed)
        await message.add_reaction("👍")
        
        message2 = await ctx.channel.fetch_message(message.id)
        users = await message2.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        
        if len(users) == 1:
            await member.kick(reason=reason)
        

def setup(client):
    client.add_cog(Moderation(client))

#MINI_DISCORD
