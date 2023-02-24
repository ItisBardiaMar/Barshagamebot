import discord
from discord.ext import commands
from main import prefix, Developers
import os
import asyncio
from datetime import datetime
from discord.ext.commands import *
import traceback
import sys
import random
import time

cogsPath = os.path.dirname(__file__)

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client







    





    # Simple on_ready command, prints when the bot goes online.
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.client.get_channel(1013402404663865384)
        image = self.client.get_user(797534062721368135)
        time = str(datetime.now())
        embed = discord.Embed(title=f"Bot Is online!🟢", color=discord.Color.green())
        embed.set_footer(text=f"{time[:16]} (CST/Central Time)")
        await channel.send(embed=embed)
        print(f"Connected To Discord.com ....")
        print(f"Connected To DataBase ....")
        print(f"All Files Loaded Success")
        print(f"Bot Is Online")
        



        


    # Tells the user the bots prefix when the ping it.
    @commands.Cog.listener()
    async def on_message(self, message):
        mentions = ["BarshaGame Bot#0455", "<@1016294213735948348>", "<@!1016294213735948348>"]
        if message.content.startswith(">"):
            channel = self.client.get_channel(1013402404663865384)
            embed = discord.Embed(title=f"{message.author} has ran:", description=f"```\n{message.content}\n```")
            embed.set_footer(text=f"This message was sent from \"{message.guild}\" ({message.guild.id}) | Member Count: {message.guild.member_count}")
            await channel.send(embed=embed)
        if message.content in mentions:
            embed = discord.Embed(title=f"My prefix is: {prefix[0]}", description="*You may also mention me instead of using a prefix*", color=0x225c9a)
            await message.channel.send(embed=embed, delete_after=10)

    # SUPPORT SERVER STUFF
    # Sends a message in the channel I have specified, saying when someone has added Bot to their server
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.name != None:
            channel = self.client.get_channel(1013402404663865384)
            embed = discord.Embed(title=f"{guild.name} has added BarshaBot Bot to their server!", 
            description=f"{guild.name}'s Description: ```\n{guild.description}\n```", 
            color=0x225c9a)
            embed.set_thumbnail(url=guild.icon_url)
            invite = await guild.text_channels[0].create_invite(reason="Creating an invite for support server (discord.gg/G8XEhAkpnj)!")
            embed.set_footer(text=f"Member Count: {guild.member_count}, Owner: {guild.owner}\nServer Invite Link: {invite}")
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        if guild.name != None:
            channel = self.client.get_channel(907820281207353378)
            embed = discord.Embed(title=f"{guild.name} has removed BarshaBot from their server!", 
            description=f"{guild.name}'s Description: ```\n{guild.description}\n```", 
            color=0x225c9a)
            embed.set_thumbnail(url=guild.icon_url)
            embed.set_footer(text=f"Owner: {guild.owner}")
            await channel.send(embed=embed)

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     guild = member.guild
    #     MemberRole = discord.utils.get(member.guild.roles, name="Member")
    #     if guild.id == 900257936713076736:
    #         await member.add_roles(MemberRole, reason=f"Giving {member} the member role.")
    #         channel = self.client.get_channel(900257936713076739)
    #         message = await channel.send(member.mention)
    #         await message.delete()
    #         dev = self.client.get_user(448645983748882442)
    #         embed = discord.Embed(title=f"Welcome {member.name}!", description=f"If you need any help you can give **{dev.name}** a ping with your question!", color=0x225c9a)
    #         await channel.send(embed=embed)
    # SUPPORT SERVER STUFF ^
    
    # WARNING THIS EVENT REMOVES FULL TRACEBACKS FROM YOUR CONSOLE, AND WILL ONLY SHOW DISCORD PROVIDED ERRORS
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        errorCode = random.randint(0,1000000000)
        try:
            member = ctx.author
            guild = ctx.guild.name
        except:
            member = "`Can't find member`"
            guild = "`Can't find guild`"
        channel = self.client.get_channel(903065937312366653)
        embed =  discord.Embed(title=f"{member} from {guild} | Error Code: {errorCode}", description=f"```\n{error}\n```", color=discord.Color.red())   
        await channel.send(embed=embed)
        tracebacks = self.client.get_channel(926675821828120587)
        await tracebacks.send(f"Error Code: {errorCode}\n```{type(error)} {error} {error.__traceback__}```")
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        embed=discord.Embed(title=f"❌ Error!", description=f"`{error}`", color=0xFF0000)
        embed.set_footer(text="This message will delete after 1 minute.")
        try:
            message = await ctx.reply(embed=embed, mention_author=False, delete_after=60)
        except:
            try:
                message = await ctx.send(embed=embed, mention_author=False, delete_after=60)
            except:
                message = await ctx.author.send(embed=embed, mention_author=False, delete_after=60)
        await message.add_reaction("🗑️")
        await message.add_reaction("⚠️")
        def check(reaction, user):
            reactions = ["🗑️", "⚠️"]
            return user != self.client.user and str(reaction) in reactions
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            try:
                await message.delete()
            except:
                pass
        try:
            if str(reaction) == "🗑️":
                try:
                    await message.delete()
                except:
                    pass
            elif str(reaction) == "⚠️":
                embed=discord.Embed(title="⚠️ Bug Report ⚠️", color=0xFFF100)
                embed.add_field(name="Your command: ", value=f"> `{ctx.message.content}`")
                embed.add_field(name="Your Error: ", value=f"> `{error}`")
                message = await user.send("Would you like to report this error? If so please send: `yes`, and if you would like to provide a reson send: `yes, <reason>`", embed=embed)
                try:
                    message = await self.client.wait_for('message', timeout=60.0, check=lambda message: message.author == ctx.author)
                except asyncio.TimeoutError:
                    await user.send("Prompt Timed Out.")
                BugChannel = self.client.get_channel(913177475415175178)
                if message.content.lower().startswith("yes,"):
                    await user.send("Thank you for the feedback! This helps unwanted errors get sorted out :) If BardiaMsa#7913 sends you a friend request he is contacting you about the error!")
                    embed=discord.Embed(title="⚠️ Bug Report ⚠️", color=0xFFF100)
                    embed.add_field(name=f"{ctx.author}'s command: ", value=f"> `{ctx.message.content}`")
                    embed.add_field(name=f"{ctx.author}'s Error: ", value=f"> `{error}`")
                    embed.add_field(name="Their message: ", value=f"`{message.content}`")
                    embed.set_footer(text=f"From {ctx.guild.name}, ID: {ctx.guild.id}")
                    await BugChannel.send(embed=embed)
                elif message.content.lower().startswith("yes"):
                    await user.send("Thank you for the feedback! This helps unwanted errors get sorted out :) BardiaMsa#7913 sends you a friend request he is contacting you about the error!")
                    embed=discord.Embed(title="⚠️ Bug Report ⚠️", color=0xFFF100)
                    embed.add_field(name=f"{ctx.author}'s command: ", value=f"> `{ctx.message.content}`")
                    embed.add_field(name=f"{ctx.author}'s Error: ", value=f"> `{error}`")
                    embed.set_footer(text=f"From {ctx.guild.name}, ID: `{ctx.guild.id}`")
                    await BugChannel.send(embed=embed)
                else:
                    await user.send("Bug Report Canceled.")
        except:
            pass
            
class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ping","info","files"])
    async def stats(self, ctx):
        # Creates variables for the embed. (The bots users, amount of guilds the bot is in, and the guild names)
        guildAmt = len(self.client.guilds)
        guilds = []
        userCount = 0
        for guild in self.client.guilds:
            if guild.unavailable:
                continue
            userCount += guild.member_count
            guilds.append(f"**{guild.name}**: {guild.member_count}")
        guilds = (", ").join(guilds)

        cogsAmt = 1
        for filename in os.listdir(cogsPath):
            if filename.endswith(".py"):
                cogsAmt += 1
        
        python_icon="https://cdn.discordapp.com/emojis/925036468756443168.webp?size=64"
        file_icon="https://discord.com/assets/ecf869302151b7838aff2f2125920206.svg"









        embed = discord.Embed(title=f"📊 __**{self.client.user.name}'s Stats**__", color=0x225c9a)
        embed.add_field(name=f"Bot's Ping:", value=f"🤖 {round(self.client.latency * 1000)} ms", inline = False)
        embed.add_field(name=f"Servers:", value=f"🤝 {guildAmt}", inline = False)
        embed.add_field(name=f"Bot's Users:", value=f"👉 {userCount}", inline = False)
        embed.add_field(name=f"Discord.py Version:", value=f"👩‍💻 {discord.__version__}", inline = False)
        embed.add_field(name=f"File Amount: ", value=f"📁 {cogsAmt}", inline = False)
        embed.add_field(name=f"Command Amount:", value=f"📟 {len(self.client.commands)}")
        # Checks if the user is a dev, and if they are provides the guild names in the embed.
        if ctx.author.id in Developers:
            embed.add_field(name=f"Guilds:", value=f"> {guilds}", inline = False)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    # 60 second cooldoown, per user
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion=None):
        SuggestionChannel = self.client.get_channel(1018788883263143996)
        # If the user messes up the command, the cooldown isn't triggered.
        if suggestion == None:
            ctx.command.reset_cooldown(ctx)
            embed=discord.Embed(title=f"❌ You must enter a message to suggest to my developer!", description=f"`{prefix[0]}suggest <suggestion>`", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        await ctx.message.add_reaction("✅")
        embed=discord.Embed(title=f"Suggestion sent!", description=f"Your suggestion was sent! `{suggestion}`", color=0x225c9a)
        embed.set_footer(text=f"People may vote on your suggestion in Suggestion ! {prefix[0]}support")
        await ctx.reply(embed=embed, mention_author=False)
        devembed = discord.Embed(title=f"{ctx.author} made a suggestion!", description=f"```{suggestion}```", color=0x225c9a)
        devembed.set_thumbnail(url=ctx.author.avatar.url)
        message = await SuggestionChannel.send(embed=devembed, mention_author=False)
        await message.add_reaction("⬆️")
        await message.add_reaction("⬇️")

    # the cooldown for the "suggest" function
    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f"Command is on cooldown!",description=f"Try again in {error.retry_after:.2f}s.", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            print(error)

    # DMs the user all of the support links. (DMs so it doesn't advertise in a server that doesn't want it)
    @commands.command(aliases=["server", "bot", "invite", "website", "site", "vote"])
    async def support(self, ctx):
        embed = discord.Embed(title="Support🎧", color=0x225c9a)
        embed.add_field(name="BarshaGame Server Invite", value="> https://discord.gg/BnaH4nbdqQ", inline=False)
        embed.add_field(name="My invite link:", value="> https://discord.com/api/oauth2/authorize?client_id=1016294213735948348&permissions=8&scope=bot",
        inline=False)
        embed.set_footer(text="If you need to contact my developer, Write -developer To Contact")
        await ctx.message.add_reaction("✅")
        await ctx.author.send(embed=embed, mention_author=False)




def setup(client):
    client.add_cog(Events(client))
    client.add_cog(Commands(client))