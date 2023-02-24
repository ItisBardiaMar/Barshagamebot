import discord
from discord.ext import commands
from main import prefix, Developers
from datetime import datetime
from discord.ext.commands import *

class Dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx, server: int):
        me = self.client.get_user(741964585300656170)
        if ctx.author.id == me.id:
            server = self.client.get_guild(server)
            invite = await server.text_channels[0].create_invite(reason="Joining for support")
            await me.send(invite)

            if server != None:
                ctx.send("Please Provide Server Id")

    @commands.command()
    async def servers(self, ctx):
        me = self.client.get_user(741964585300656170)
        if ctx.author.id == me.id:
            servers = self.client.guilds
            embed = discord.Embed(title=f"__**My Servers:**__", color=0x225c9a)
            for server in servers:
                if server.unavailable:
                    embed.add_field(name=f"{server.name} (Error)" , value=f"> (ID: `{server.id}`)", inline=True)
                    continue
                embed.add_field(name=f"{server.name} (Members: {server.member_count})" , value=f"> (ID: `{server.id}`)", inline=True)
            await ctx.send(embed=embed)






    @commands.command()
    async def developer(self, ctx):
       await ctx.send("To Contact Developer : Open #📜┊𝗧𝗶𝗰𝗸𝗲𝘁 Or Dm BardiaMsa#7913 ")

def setup(client):
    client.add_cog(Dev(client))