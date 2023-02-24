import discord
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
import datetime

guilds = {
        # Our Network
        876067421948100658: {
            "transcriptions_channel": 1000848265660604536,
            "help_channel": 1000848265660604536,
            "open_tickets": 1000852477417107516, 
            "closed_tickets": 1000851547237908591,
            "staff_roles": [1000849438023094312]
        },
        
    }

async def getTranscriptionsChannel(guild):
    return get(guild.channels, id=guilds[guild.id]["transcriptions_channel"])
async def getHelpChannel(guild):
    return get(guild.channels, id=guilds[guild.id]["help_channel"])
async def getOpenTickets(guild):
    return get(guild.categories, id=guilds[guild.id]["open_tickets"])
async def getClosedTickets(guild):
    return get(guild.categories, id=guilds[guild.id]["closed_tickets"])
async def getStaffRole(guild):
    staff_roles = []
    for id_ in guilds[guild.id]["staff_roles"]:
        role = get(guild.roles, id=id_)
        staff_roles.append(role)
    return staff_roles

class Tickets(commands.Cog):
    def __init__(self, client, guilds):
        self.client = client
        self.guilds = guilds
        
    @tasks.loop(seconds=43200.0)
    async def auto_close_tickets(self):
        open_tickets = await getOpenTickets(self.client.get_guild(793628209345724416))
        staff_commands = open_tickets.guild.get_channel(793683518282399774)
        for channel in open_tickets:
            current_time = datetime.datetime.now()
            last_message = channel.last_message.created_at
            await staff_commands.send(((last_message-current_time).seconds)//60)

    @commands.command()
    async def ticket(self, ctx):
        # Set to your staff role
        staff = await getStaffRole(ctx.guild)
        for role in staff:
            if role in ctx.author.roles:
                embed=discord.Embed(title=f"__**{ctx.guild.name}** Tickets__", 
                description=f"If you need help with anything on *{ctx.guild.name}* open a ticket to discuss it with the staff team!", 
                color=discord.Color.dark_teal())
                embed.set_footer(text="To open a ticket click the ticket emoji!", 
                icon_url="https://media.discordapp.net/attachments/738120642414772347/920806716591988776/Ticket.png?width=671&height=671")
                message = await ctx.send(embed=embed)
                await message.add_reaction("🎟️")

    @commands.command()
    async def close(self, ctx):
        # Set to your staff role
        staff = await getStaffRole(ctx.guild)
        for role in staff:
            if role in ctx.author.roles or str(ctx.author.id) in ctx.channel.topic:
                # Set to your open tickets category
                opened_tickets = await getOpenTickets(ctx.guild)
                if ctx.channel.category_id == opened_tickets.id:
                    await ctx.send("Are you sure you would like to close this ticket? Type `confirm` to close this ticket.")
                    message = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                    if "confirm" in message.content.lower():
                        closing = await ctx.send("Closing ticket in 5...")
                        for i in range(4, 0, -1):
                            await asyncio.sleep(1)
                            await closing.edit(content=f"Closing ticket in {i}...")
                        # Set to your closed tickets category
                        closed_tickets = await getClosedTickets(ctx.guild)
                        await ctx.channel.edit(category=closed_tickets, sync_permissions=True)
                        await ctx.send("If you would like to re-open this channel Type `>open` to re-open it.\
                        If you would like to delete the ticket entirely type `>delete`.")
                        transcriptions_channel = await getTranscriptionsChannel(ctx.guild)
                        transcribing = await ctx.send("Transcribing ticket...")
                        file = open("transcriptions.txt","w")
                        file.write("")
                        file.close()
                        file = open("transcriptions.txt","a")
                        messages = await ctx.channel.history(limit=None).flatten()
                        messages.reverse()
                        for message in messages:
                            print(message.content)
                            if len(message.embeds) > 0:
                                embeds = str(len(message.embeds))
                                file.write(f"{message.author} (Has Embeds: {embeds}): {message.content}\n")
                            else:
                                file.write(f"{message.author}: {message.content}\n")
                        file.close()
                        with open("transcriptions.txt", "rb") as file:
                            await transcriptions_channel.send(f"Transcription of {ctx.channel.name}", file=discord.File(file, "transcriptions.txt"))
                        file = open("transcriptions.txt","w")
                        file.write("")
                        file.close()
                        await transcribing.edit(content=f"Transcribed <#{ctx.channel.id}>")


    @commands.command()
    async def messages(self, ctx):
        count = 0
        async for message in ctx.channel.history(limit=None):
            count += 1
        await ctx.send(count)

    @commands.command()
    async def open(self, ctx):
        # Set to your staff role
        staff = await getStaffRole(ctx.guild)
        try:
            topic = ctx.channel.topic
            userID = topic.split("'")
            user = self.client.get_user(int(userID[0]))
            for role in staff:
                if role in ctx.author.roles or str(ctx.author.id) == userID[0]:
                    # Set to your closed tickets category
                    closed_tickets = await getClosedTickets(ctx.guild)
                    if ctx.channel.category_id == closed_tickets.id:
                        await ctx.send("Are you sure you would like to re-open this ticket? Type `confirm` to re-open this ticket.")
                        message = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                        if "confirm" in message.content.lower():
                            closing = await ctx.send("Re-Opening ticket in 5...")
                            for i in range(4, 0, -1):
                                await asyncio.sleep(1)
                                await closing.edit(content=f"Re-Opening ticket in {i}...")
                            # Set the ID to your open tickets category
                            open_tickets = await getOpenTickets(ctx.guild)
                            overwrites = {user: discord.PermissionOverwrite(read_messages=True), 
                            message.guild.default_role: discord.PermissionOverwrite(read_messages=False)}
                            for staffRole in staff:
                                overwrites[staffRole] = discord.PermissionOverwrite(read_messages=True)
                            await ctx.channel.edit(category=open_tickets, sync_permissions=False, overwrites=overwrites)
        except:
            return

    @commands.command()
    async def delete(self, ctx):
        # Set to your staff role
        staff = await getStaffRole(ctx.guild)
        try:
            staff = await getStaffRole(ctx.guild)
            for role in staff:
                if role in ctx.author.roles:
                    # Set to your closed tickets category
                    closed_tickets = await getClosedTickets(ctx.guild)
                    if ctx.channel.category_id == closed_tickets.id:
                        await ctx.send("Are you sure you would like to delete this ticket? Type `confirm` to completely delete this ticket (This is completely ireversable).")
                        message = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                        if "confirm" in message.content.lower():
                            closing = await ctx.send("Deleting ticket in 5...")
                            for i in range(4, 0, -1):
                                await asyncio.sleep(1)
                                await closing.edit(content=f"Deleting ticket in {i}...")
                            await ctx.channel.delete(reason=f"Deleting ticket - Deleted by {ctx.author.name}#{ctx.author.discriminator}")
        except:
            return

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message = await self.client.get_channel(payload.channel_id).fetch_message(payload.message_id)
        reaction = discord.utils.get(message.reactions)
        user = payload.member
        if user.id is not self.client.user.id:
            if str(reaction.emoji) == "🎟️":
                # Set this to your help channel (the channel where you click the reaction to open the ticket)
                help_channel = await getHelpChannel(message.guild)
                channel = reaction.message.channel
                if channel.id == help_channel.id:
                    await reaction.remove(user)
                    guild = reaction.message.guild
                    # Set to your open tickets category
                    open_tickets = await getOpenTickets(message.guild)
                    for channel in open_tickets.channels:
                        if str(user.id) in channel.topic:
                            await user.send("You may only have 1 ticket open at once!")
                            return
                    # Set to your staff role
                    staff = await getStaffRole(message.guild)
                    overwrites = {user: discord.PermissionOverwrite(read_messages=True), 
                    message.guild.default_role: discord.PermissionOverwrite(read_messages=False)}
                    staff_mentions = []
                    for role in staff:
                        staff_mentions.append(f"<@&{role.id}>")
                        overwrites[role] = discord.PermissionOverwrite(read_messages=True)
                    staff_mentions = ", ".join(staff_mentions)
                    ticket = await guild.create_text_channel(f"{user.name[:22]}'s Ticket", 
                    category=open_tickets, 
                    reason="Opening a ticket", 
                    topic=f"{user.id}'s Ticket. ({user.name})",
                    overwrites=overwrites)
                    embed=discord.Embed(title=f"Welcome **{user.name}**!", description="Please send what you need in the chat!\n\
                    We may take some time to respond so please be patient!",
                    color=discord.Color.blurple())
                    embed.set_footer(text="To close the ticket send '>close'")

                    await ticket.send(f"{user.mention}{staff_mentions}", embed=embed)

def setup(client):
    client.add_cog(Tickets(client, guilds))