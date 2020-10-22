import discord
import random
import json
import asyncio
import os
import datetime
import PIL
import wikipedia
from aiohttp import ClientSession
from itertools import cycle
from discord import Member, Embed
from discord.ext import commands, tasks
from discord.ext.commands import Bot, command, cooldown, BucketType, Cog
from discord.utils import get

numbers = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣",
           "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟")


def wiki_summary(arg):
    definition = wikipedia.summary(
        arg, sentences=3,
        chars=1000,
        auto_suggest=True,
        redirect=True)
    return definition


class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dice(self, ctx, *, question=' '):
        responses = random.randrange(101)

        embed = discord.Embed(
            title='Dice',
            description=f'{ctx.author.mention} rolled a dice.',
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/759782905860980766/761935699745570836/Untitled_11.png')
        embed.add_field(
            name=f'Question: {question}', value=f'By {ctx.author.mention}', inline=False)
        embed.add_field(name=f'Answer: {responses}',
                        value='By Forcefield™', inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['8ball', '8b'])
    async def _8ball(self, ctx, *, question):
        responses = responses = ['It is certain.',
                                 'It is decidedly so.',
                                 'Without a doubt.',
                                 'Yes - definitely.',
                                 'You may rely on it.',
                                 'As I see it, yes.',
                                 'Most likely.',
                                 'Outlook good.',
                                 'Yes.',
                                 'Signs point to yes.',
                                 'Better not tell you now.',
                                 'Dont count on it.',
                                 'My reply is no.',
                                 'My sources say no.',
                                 'Outlook not so good.',
                                 'Very doubtful.']
        embed = discord.Embed(
            title='8ball',
            description=f'{ctx.author.mention} asked something to "Magic 8ball"',
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/759782905860980766/761935296089817088/tmeightball.png')
        embed.add_field(
            name=f'Question: {question}', value=f'By {ctx.author.mention}.', inline=False)
        embed.add_field(
            name=f'Answer: {random.choice(responses)}', value='By Forcefield™', inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, question, *options):
        if len(options) > 10:
            embed = discord.Embed(
                title=":x: Error :x:",
                description=f"{ctx.author.mention}, you can only have 10 options!",
                color=0xFF0000
            )
            tday = datetime.date.today()
            embed.set_footer(
                text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Poll',
                description=f'"{question}"',
                color=0x005275
            )
            tday = datetime.date.today()
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/759782905860980766/761935989471051806/tmcpolls.png')
            embed.set_footer(
                text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')

            embed.add_field(name='Options', value='\n'.join(
                [f'{numbers[idx]} {option}' for idx, option in enumerate(options)]), inline=False)
            message = await ctx.send(embed=embed)

            for emoji in numbers[:len(options)]:
                await message.add_reaction(emoji)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, sentence):
        await ctx.send(sentence)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx, title=None, description=None):
        if title == None:
            await ctx.send(f"Hey, {ctx.author.name}, please add a title to your embed!")
            return True
        if description == None:
            await ctx.send(f"Hey, {ctx.author.name}, please add a description to your embed!")
            return True

        embed = discord.Embed(
            title=title,
            description=description,
            color=ctx.author.color
        )
        embed.add_field(name='Sent by:',
                        value=ctx.author.mention, inline=False)
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['wouldyourather'])
    async def wyr(self, ctx):
        responses1 = ['Become a Muffin',
                      'Bulldoze your own house and get a mansion instead',
                      "Have a Cat and Dog that don't get A-long",
                      'Lose the Ability to Read',
                      'Have a Golden Voice',
                      'Be covered in Fur',
                      'Be in Jail for a Year']

        responses2 = ['eat a Muffin',
                      'get 1 Million Dollars',
                      'be a Cupcake',
                      'have a Party Every Day',
                      'lose the Ability to Speak',
                      'have a Silver Tongue',
                      'lose Half a Year of Your Life']

        embed = discord.Embed(
            title='Would you Rather?',
            description=f'{ctx.author.mention} is playing!',
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/762707483126792193/762710558851072000/tmwyr.png')
        embed.add_field(name=f'{random.choice(responses1)},',
                        value='To vote for this, react with the :one: emoji', inline=False)
        embed.add_field(name=f'Or {random.choice(responses2)}',
                        value='To vote for this, react with the :two: emoji', inline=False)
        message = await ctx.send(embed=embed)

        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")

    @commands.command(aliases=["wikipedia", 'google'])
    async def define(self, message, *, arg):
        embed = discord.Embed(
            title='Definition',
            description=wiki_summary(arg),
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        await message.channel.send(content=None, embed=embed)

    @commands.command(aliases=['joke', 'j'])
    async def _joke(self, ctx):

        jokes = [
            'During a job interview at the 99 Cents store, my son was asked, “Where do you see yourself in five years?” My son’s reply: “At the Dollar Store.” He got the job.',
            'Two guys stole a calendar. They got six months each.',
            'Since the coronavirus outbreak, my 47-year-old son has been washing his hands religiously. In fact, he said, “I’ve been washing my hands so much, I found the answers to an old eighth-grade math quiz.”',
            '“I make mistakes; I’ll be the second to admit it.”',
            'My father liked to say, “I’m bald because a good man always comes out on top.” Dad loved to make people laugh. At his funeral, the preacher said, “In his lifetime, this man told thousands of jokes, but they were always the same one.”',
        ]

        embed = discord.Embed(
            title="Joke",
            description=f"Requested by: {ctx.author.mention}",
            color=0x005275
        )
        tday = datetime.date.today()
        embed.set_footer(
            text=f'Forcefield™  •  {tday.month}/{tday.day}/{tday.year}')
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/762707483126792193/766997539568222218/Untitled_19.png')
        embed.set_author(name="Source: [click here]",
                         url='https://www.rd.com/jokes/')
        embed.add_field(name=random.choice(jokes),
                        value=f"What do you think, {ctx.author.mention}?")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Games(client))

# NOTES
