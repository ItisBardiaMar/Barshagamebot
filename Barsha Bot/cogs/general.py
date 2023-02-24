import discord
from discord import client
from discord.ext import commands
from main import prefix
import asyncio

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Sends an embed, seperate the fields with a "/"
    @commands.command(aliases=["em"])
    async def embed(self, ctx, *,message=None):
        author = True
        if message.endswith("-a") is True:
            message = message[:-2]
            author = False
        if message == None:
            embed = discord.Embed(title="❌ You must enter a message to embed!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        try:
            title, description = message.split("-s")
        except:
            title = message
            description = ""
        embed = discord.Embed(title=f"{title}", description=f"{description}",color = ctx.author.color)
        if author is True:
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.message.delete()
        await ctx.send(embed=embed, mention_author=False)

    # Gets the avatar of a member
    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member:discord.Member=None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f"**__{member}'s Avatar__**",
        description=f"[Avatar Link (PNG)]({member.avatar_url})",
        color=member.color)
        embed.set_image(url=member.avatar_url)
        message = await ctx.reply(embed=embed, mention_author=False)

    # Gives information on the guild
    @commands.command(aliases=["guild", "serverinfo"])
    async def guildinfo(self, ctx):
        guild = ctx.guild
        # Title
        embed = discord.Embed(title=f"{guild.name} (ID: {guild.id})", color=0x225c9a)
        # Description
        embed.add_field(name="Guild Description:", value=f"> `{guild.description}`", inline=False)
        # Created At
        created_at = str(guild.created_at)
        embed.add_field(name="Guild Creation Date:", value=f"> `{created_at[:10]}` at `{created_at[11:16]}`")
        # Member Count
        embed.add_field(name="Member Count:", value=f"> `{guild.member_count}`/`{guild.max_members}`", inline=False)
        # Role Count
        RoleCount = 0
        for role in guild.roles:
            RoleCount += 1
        embed.add_field(name="Role Count:", value=f"> `{RoleCount}`", inline=False)
        # Channel Count
        ChannelCount = 0
        CatagoryCount = 0
        for channel in guild.channels:
            ChannelCount += 1
        for catagory in guild.categories:
            CatagoryCount += 1
        embed.add_field(name="Channel and Catagory Count:", value=f"> Catagories - `{CatagoryCount}`, Channels - `{ChannelCount}`", inline=False)
        # Boost level
        embed.add_field(name="Guild Level:", value=f"> `Level {guild.premium_tier}` with `{guild.premium_subscription_count} boosts`.", inline=False)
        # Emojis
        # Thumbnail/Footer
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=f"This guild is owned by: {guild.owner} (ID: {guild.owner.id})", icon_url=guild.owner.avatar_url)
        # Sending
        await ctx.message.reply(embed=embed, mention_author=False)


    # Gives information on a user
    @commands.command(aliases=["user"])
    async def userinfo(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        # Title
        message = f"{member} (ID: {member.id})"
        if member.bot == True:
            message = f"`BOT` {member} (ID: {member.id})"
        embed = discord.Embed(title=message, color=member.color)
        # Status
        if member.status != None:
            embed.add_field(name=f"Status:", value=f"> `{member.status}`")
        else:
            embed.add_field(name=f"Activity:", value=f"> `Can't get user's status.`", inline=False)
        # Activity
        activites = []
        for activity in member.activities:
            try:
                if activity.details != None:
                    activites.append(f"{activity.name} ({activity.details})")
                else:
                    activites.append(f"{activity.name}")
            except:
                activites.append(f"{activity.name}")
        activites = ("`,\n> `").join(activites)
        if member.activity != None:
            embed.add_field(name=f"Activity:", value=f"> `{activites}`", inline=False)
        else: 
            embed.add_field(name=f"Activity:", value=f"> `Isn't playing anything.`", inline=False)
        # Created At
        created_at = str(member.created_at)
        embed.add_field(name=f"Date of account creation:", value=f"> `{created_at[:10]}` at `{created_at[11:16]}`", inline=False)
        # Joined At
        joined_at = str(member.joined_at)
        embed.add_field(name=f"Date of server join:", value=f"> `{joined_at[:10]}` at `{joined_at[11:16]}`", inline=False)
        # Permissions
        MemberPerms = []
        AdminPermissions = [
            "kick_members", "ban_members", "administrator", "manage_channels", "manage_guild", "view_audit_log", "manage_messages",
            "mention_everyone", "mute_members", "deafen_members", "move_members", "manage_roles", "manage_emojis"
        ]
        admin = False
        for perm in member.guild_permissions:
            if perm[0] == "administrator" and perm[1] == True:
                admin = True
        if admin == True:
            MemberPerms = "`administrator` (every permission)"
        else:
            for perm in member.guild_permissions:
                if perm[0] in AdminPermissions and perm[1] == True:
                    MemberPerms.append(f"`{perm[0]}`")
            MemberPerms = (", ").join(MemberPerms)
        if MemberPerms == "":
            MemberPerms = "`No Admin Permissions`"
        embed.add_field(name=f"Key Permissions: ", value=f"> {MemberPerms}", inline=False)
        # Roles
        roles = []
        for role in reversed(member.roles):
            if role.name == "@everyone":
                roles.append("@everyone")
            else:
                roles.append(role.mention)
        roles = (", ").join(roles)
        embed.add_field(name=f"Roles: ", value=f"> {roles}", inline=False)
        # replying Message
        embed.set_thumbnail(url=member.avatar_url)
        main_message = await ctx.reply(embed=embed, mention_author=False)
        # Pins
        pinned_messages = ""
        for channel in ctx.guild.text_channels:
            for pin in await channel.pins():
                if pin.author == member:
                    pinned_messages += f"> {pin.channel.mention} | `{pin.content}` | [Message Link]({pin.jump_url})\n"
        if pinned_messages != "":
            embed.add_field(name="Pinned Messages:", value=f"{pinned_messages}")
            await main_message.edit(embed=embed)

def setup(client):
    client.add_cog(General(client))
