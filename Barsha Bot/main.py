from pydoc import cli
import discord
import os
import asyncio
from discord.ext import commands
from discord.ext.commands.errors import *

Developers = {
    YOUR_ID : "YOUR_USERNAME"
}

# The bots settings
prefix = ["PREFIX", "YOUR_FULL_NAME_DISCORD"]
token = "YOUR_BOT_TOKEN"
cogsPath = os.path.dirname(__file__)+'/cogs'
client = commands.Bot(
    intents= discord.Intents.all(),
    command_prefix = prefix,
    help_command = None,
    case_insensitive=True
    
    )






# Loads the cog
@client.command()
async def load(ctx, extension=None):
    if extension != None:
        extension = extension.lower()
    if ctx.author.id in Developers:
        if extension == "all" or extension == "*" or extension == None:
            for file in os.listdir(cogsPath):
                if file.endswith(".py"):
                    try:
                        client.unload_extension(f"cogs.{file[:-3]}")
                    except ExtensionNotLoaded:
                        continue
            embed = discord.Embed(title=f"📥 **All cogs loaded!**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
            return
        try:
            client.load_extension(f"cogs.{extension}")
            embed = discord.Embed(title=f"📥 **{extension} loaded**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        except (ExtensionNotFound, ExtensionAlreadyLoaded):
            await ctx.reply("Extension not found/Is already loaded!", delete_after=5, mention_author=False)
            await asyncio.sleep(5)
            await ctx.message.delete()
    else:
        embed = discord.Embed(title=f"❌ You must be a **bot developer** to use this command!, To Contact Devs, write -developer", color=0x225c9a)
        await ctx.reply(embed=embed, delete_after=15, mention_author=False)

# Unloads the cog
@client.command()
async def unload(ctx, extension=None):
    if extension != None:
        extension = extension.lower()
    if ctx.author.id in Developers:
        if extension == "all" or extension == "*" or extension == None:
            for file in os.listdir(cogsPath):
                if file.endswith(".py"):
                    try:
                        client.unload_extension(f"cogs.{file[:-3]}")
                    except ExtensionNotLoaded:
                        continue
            embed = discord.Embed(title=f"📤 **All cogs unloaded!**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
            return
        try:
            client.unload_extension(f"cogs.{extension}")
            embed = discord.Embed(title=f"📤 **{extension} unloaded**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        except (ExtensionNotFound, ExtensionNotLoaded):
            await ctx.reply("Extension not found/Is already unloaded!", delete_after=5, mention_author=False)
            await asyncio.sleep(5)
            await ctx.message.delete()
    else:
        embed = discord.Embed(title=f"❌ You must be a **bot developer** to use this command!, To Contact Devs, write -developer", color=0x225c9a)
        await ctx.reply(embed=embed, delete_after=15, mention_author=False)

# Unloads the cog, then reloads it.
@client.command()
async def reload(ctx, extension=None):
    if extension != None:
        extension = extension.lower()
    if ctx.author.id in Developers:
        if extension == "all" or extension == "*" or extension == None:
            for file in os.listdir(cogsPath):
                if file.endswith(".py"):
                    try:
                        client.unload_extension(f"cogs.{file[:-3]}")
                        client.load_extension(f"cogs.{file[:-3]}")
                    except ExtensionNotLoaded:
                        client.load_extension(f"cogs.{file[:-3]}")
            embed = discord.Embed(title=f"🔄 **All cogs reloaded!**", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
            return
        try:
            try:
                client.unload_extension(f"cogs.{extension}")
                client.load_extension(f"cogs.{extension}")
                embed = discord.Embed(title=f"🔄 **{extension} reloaded**", color=0x225c9a)
                await ctx.reply(embed=embed, mention_author=False)
            except ExtensionNotLoaded:
                client.load_extension(f"cogs.{extension}")
                embed = discord.Embed(title=f"🔄 **{extension} reloaded**", color=0x225c9a)
                await ctx.reply(embed=embed, mention_author=False)
        except ExtensionNotFound:
            await ctx.reply("Extension not found!", delete_after=5, mention_author=False)
            await asyncio.sleep(5)
            await ctx.message.delete()
    else:
        embed = discord.Embed(title=f"❌ You must be a **bot developer** to use this command!, To Contact Devs, write -developer", color=0x225c9a)
        await ctx.reply(embed=embed, delete_after=15, mention_author=False)

# Loads all the cogs when the bot is run
for filename in os.listdir(cogsPath):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
