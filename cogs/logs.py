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

class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    
def setup(client):
    client.add_cog(Logs(client))