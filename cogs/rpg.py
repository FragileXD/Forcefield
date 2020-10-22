import discord
import random
import json
from discord.ext import commands
from discord.ext.commands import Cog

# PLAYER
player = {'heal': 16, 'health': 250}

# HELPERS
butterfly = {'name': 'Butterfly', 'heal': random.randint(2, 15), 'health': 5}
sniper = {'name': 'Sniper', 'attack': 1000, 'chance': 1}
# SNIPER HAS A 50% CHANCE OF HITTING AN ENEMY. WHEN HE HAS SHOT CHANCE = 0
golem = {'name': 'Golem', 'attack': 40, 'health': 120}

# ENEMIES
fiend = {'name': 'Fiend', 'attack': 5, 'health': 20}
adult_fiend = {'name': 'Adult Fiend', 'attack': 10, 'health': 40}
badass_fiend = {'name': 'Badass Fiend',
                'attack': random.randint(35, 40), 'health': 100}
goblin = {'name': 'Goblin', 'attack': random.randint(20, 25), 'health': 20}
troll = {'name': 'Troll', 'dmg': random.randint(3, 6), 'health': 27}

# WEAPONS
# GUNS:
ak = {'name': 'AK47', 'dmg': random.randint(10, 14)}
smg = {'name': 'SMG', 'dmg': random.randint(5, 10)}
rpg = {'name': 'RPG', 'dmg': random.randint(45, 55)}
laser_gun = {'name': 'Laser Gun', 'dmg': random.randint(15, 20)}
# MEELEE:
fists = {'name': 'Fists', 'dmg': random.randint(3, 7)}
knife = {'name': 'Knife', 'dmg': random.randint(8, 16)}
sword = {'name': 'Sword', 'dmg': random.randint(12, 21)}
flail = {'name': 'Flail', 'dmg': random.randint(23, 39)}
halberd = {'name': 'Halberd', 'dmg': random.randint(25, 31)}


class Rpg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx):
        channel = ctx.channel
        await channel.send("Say hello!")

        def check(m):
            return m.content == "hello" and m.channel == channel

        msg = await self.client.wait_for("message", check=check)
        if msg.author == ctx.author:
            await channel.send("Hello {.author.mention}!".format(msg))
        elif not msg.author == ctx.author:
            await channel.send("no")
            return False


def setup(client):
    client.add_cog(Rpg(client))

# NOTES


'''heellloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'''
