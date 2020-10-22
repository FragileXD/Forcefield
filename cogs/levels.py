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


class Levels(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open("users.json", 'r') as f:
            self.users = json.load(f)

        self.client.loop.create_task(self.save_users())

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open('users.json', 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(20)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 0
            self.users[author_id]['exp'] = 0

        self.users[author_id]['exp'] += 1

        if self.lvl_up(author_id):
            channels = str(message.guild.channels)
            embed = discord.Embed(
                title='Level Up!',
                description=f'{message.author.mention}, You have now leveled up to level {self.users[author_id]["level"]}',
                color=0x005275
            )
            if "leveling" in channels:
                channel = get(message.guild.channels, name="leveling")
                await channel.send(embed=embed)
            else:
                await message.channel.send(embed=embed)

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send('This member is not ranked yet.')
        else:
            embed = discord.Embed(
                title='Level',
                description=f"{member.mention}'s ranks:",
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_footer(
                text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            embed.add_field(
                name='Level:',
                value=self.users[member_id]['level'],
                inline=True
            )
            embed.add_field(
                name='XP:',
                value=self.users[member_id]['exp'],
                inline=True
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Levels(client))
