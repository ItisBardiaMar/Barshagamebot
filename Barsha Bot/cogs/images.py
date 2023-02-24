import discord
from discord.ext import commands
from discord.ext.commands import *
import random

class Images(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx):
        gif = [
            "https://media1.giphy.com/media/q1zPWOcKgN0n2Gef7Q/giphy.mp4?cid=73b8f7b13307525281e89fad121061caf79d612213cb3db1&rid=giphy.mp4&ct=g",
            "https://media.discordapp.net/attachments/632195896096063488/1016659304243265597/2812192B-BD9A-4C30-8084-0279C31F0971.gif",
            "https://media.discordapp.net/attachments/819298405532696616/1013709884660912210/fun.gif",
            "https://tenor.com/view/pishro-gif-24534041",
            "https://media.discordapp.net/attachments/854672200480718868/854673332229767178/1623840385062.gif",
            "https://media.discordapp.net/attachments/1000785565836382379/1013725527720337478/20220125_110511.gif",
            "https://media.giphy.com/media/WwJfWxvfCUJjKIqBoz/giphy.gif",
            "https://tenor.com/view/star-wars-cat-vs-dog-jedi-cat-jedi-lightsaber-gif-16455709",
            "https://imgur.com/gallery/pmSuXlo",
            "https://media.discordapp.net/attachments/940737081372733480/975661091369672764/ezgif.com-gif-maker-7.gif"
        ]
        message = ["💨", "Hehe Boy!", "💩"]
        await ctx.send(f"{random.choice(message)}, {random.choice(gif)}")
    

def setup(client):
    client.add_cog(Images(client))