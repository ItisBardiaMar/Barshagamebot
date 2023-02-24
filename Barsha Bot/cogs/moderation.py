import discord
import datetime
import asyncio
from discord.ext import commands
from main import prefix

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Bans a member
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member=None, *, reason=None):
        time = str(datetime.datetime.now())
        if member == None:
            embed = discord.Embed(title="❌ You must enter a valid member to ban!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        elif member.top_role >= ctx.author.top_role:
            embed = discord.Embed(title="❌ You cannot ban someone who is a higher or same rank as you!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        else:
            await ctx.guild.ban(member, reason=reason, delete_message_days=0)
            embed = discord.Embed(title=f"**{member}** was banned by: **{ctx.author}**", color=0xFF0000)
            embed.set_footer(text=f"{member} was banned for: {reason}, At: {time[:16]} EST", icon_url=member.avatar.url)
            await ctx.reply(embed=embed, mention_author=False)

    # Unbans a member
    @commands.command(aliases=["pardon", "un-ban"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member=None):
        if member == None:
            embed = discord.Embed(title="❌ Member not found! To unban someone you must enter their username this format: `<name>#<discriminator/numbers>`", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        time = str(datetime.datetime.now())
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title=f"**{member}** was unbanned by: **{ctx.author}**", color=0x225c9a)
                embed.set_footer(text=f"{member} was unbanned at: {time[:16]} EST", icon_url=user.avatar.url)
                await ctx.reply(embed=embed, mention_author=False)
            else:
                embed = discord.Embed(title="❌ Member not found! To unban someone you must enter their username this format: `<name>#<discriminator/numbers>`", color=0xFF0000)
                await ctx.reply(embed=embed, mention_author=False)
                return
    
    # Checks the ban list of a guild
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def bans(self, ctx):
        page = 1
        bans = await ctx.guild.bans()
        def check(reaction, user):
            return user != self.client.user
        message = None
        
        while True:
            header = f"'s Banned Users (Page - {page}):"
            embed = discord.Embed(title=f"{ctx.guild.name}{header}", color=0x225c9a)
            for ban_entry in bans[(page-1)*10:page*10]:
                embed.add_field(name=f"**{ban_entry.user}**", value=f"> Reason: *{ban_entry.reason}*")
            if message == None:        
                message = await ctx.reply(embed=embed, mention_author=False)
            else:
                await message.edit(embed=embed)
            if len(bans) > 10 and not page*10 - len(bans) <= 10:
                await message.add_reaction("◀️")
                await message.add_reaction("▶️")
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    await message.clear_reaction("◀️")
                    await message.clear_reaction("▶️")
                    break
                if str(reaction) == "▶️":
                    page += 1
                elif str(reaction) == "◀️" and page > 1:
                    page -= 1
                else:
                    print("none of the reactions")
            else:
                break

    # Kicks a member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, reason=None):
        time = str(datetime.datetime.now())
        if member == None:
            embed = discord.Embed(title="❌ You must enter a valid member to ban!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        elif member.top_role >= ctx.author.top_role:    
            embed = discord.Embed(title="❌ You cannot kick someone who is a higher or same rank as you!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        else:
            await ctx.guild.ban(member, reason=reason, delete_message_days=0)
            embed = discord.Embed(title=f"**{member}** was kicked by: **{ctx.author}**", color=0x225c9a)
            embed.set_footer(text=f"{member} was kicked for: {reason}, At: {time[:16]} EST", icon_url=member.avatar.url)
            await ctx.reply(embed=embed, mention_author=False)

    # Mutes a member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None, reason=None):
        if member == None:
            embed=discord.Embed(title="❌ You must enter a member to mute!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        elif member.top_role >= ctx.author.top_role:
            embed=discord.Embed(title="❌ You cannot mute someone who is a higher or same rank as you!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return

        MuteRole = discord.utils.get(ctx.guild.roles, name='Muted')
        if MuteRole != None:
            MemberRoles = member.roles
            for role in MemberRoles:
                if str(role) == str(MuteRole):
                    embed=discord.Embed(title=f"**❌ {member}** is already muted!", color=0xFF0000)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
            await member.add_roles(MuteRole, reason=f"{ctx.author} muted {member}!")
            embed=discord.Embed(title=f"**{ctx.author}** muted **{member}**!", description=f"{member} was muted for: {reason}", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            embed=discord.Embed(title=f"❌ You do not have a mute role! Use `{prefix[0]}muterole` to create one.", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)

    # Creates a "Muted" role
    @commands.command(aliases=["createdmuterole", "createmute", "crm"])
    @commands.has_permissions(kick_members=True)
    async def muterole(self, ctx, member: discord.Member=None):
        MuteRole = discord.utils.get(ctx.guild.roles, name='Muted')
        guildClient = ctx.guild.get_member(797534062721368135)
        if MuteRole == None:
            RolePos = guildClient.top_role.position

            embed=discord.Embed(title="Creating a mute role...", color=0x225c9a)
            message = await ctx.reply(embed=embed, mention_author=False)
            MuteRole = await ctx.guild.create_role(name="Muted", reason=f"Creating a mute role for {self.client.user}.")
            await MuteRole.edit(position=RolePos)
            for channel in ctx.guild.channels:
                await channel.set_permissions(MuteRole, send_messages=False, add_reactions=False)
            embed=discord.Embed(title="Mute role created!", color=0x225c9a)
            embed.set_footer(text="Note: this role will only work if it is higher than the member role, and the channel doesn't have overrides that lets the member send messages.")
            await message.edit(embed=embed)
        else:
            embed=discord.Embed(title="❌ You already have a mute role!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)

    # Unmutes a member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member=None):
        if member == None:
            embed=discord.Embed(title="❌ You must enter a member to unmute!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        elif member.top_role >= ctx.author.top_role:
            embed=discord.Embed(title="❌ You cannot unmute someone who is a higher or same rank as you!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        MuteRole = discord.utils.get(ctx.guild.roles, name='Muted')
        if MuteRole != None:
            MemberRoles = member.roles
            for role in MemberRoles:
                if str(role) == str(MuteRole):
                    await member.remove_roles(MuteRole, reason=f"{ctx.author} is unmuting {member}")
                    embed=discord.Embed(title=f"**{ctx.author}** unmuted **{member}**!", color=0x225c9a)
                    await ctx.reply(embed=embed, mention_author=False)
                    return
            embed=discord.Embed(title=f"❌ **{member}** isn't muted!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            embed=discord.Embed(title=f"❌ You do not have a mute role! Use `{prefix[0]}muterole` to create one.", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)

    # Kicks a member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, reason=None):
        if member == None:
            embed=discord.Embed(title="❌ You must enter a member to kick!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        elif member.top_role >= ctx.author.top_role:
            embed=discord.Embed(title="❌ You cannot kick someone who is a higher or same rank as you!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        await member.kick(reason=f"{ctx.author} is unmuting {member}")
        embed=discord.Embed(title=f"**{ctx.author}** kicked **{member}**!", description=f"{member} was kicked for: {reason}", color=0x225c9a)
        await ctx.reply(embed=embed, mention_author=False)
        return

    # Purges a specified amount of messages
    @commands.command(aliases=["clear", "clearmessages", "purgemessages"])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=10):
        if amount > 100:
            embed=discord.Embed(title="❌ You cannot purge more than 100 messages!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        elif amount < 1:
            embed=discord.Embed(title="❌ You cannot purge less than 1 message!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        await ctx.channel.purge(limit=(amount+1))
        embed=discord.Embed(title=f"Bulk Deleted **{amount}** messages!", color=0x225c9a)
        await ctx.send(embed=embed, delete_after=4, mention_author=False)
        
    @commands.command(aliases=["save","channellog","channelsave"])
    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def log(self, ctx, amount=50):
        if amount > 200:
            ctx.command.reset_cooldown(ctx)
            embed=discord.Embed(title="❌ You cannot log more than 200 messages!", color=0xFF0000)
            embed.set_footer(text="*This is because save messages takes up a lot of the bots resources, so can't be used often")
            await ctx.reply(embed=embed, mention_author=False)
        elif amount < 10:
            ctx.command.reset_cooldown(ctx)
            embed=discord.Embed(title="❌ You cannot log less than 10 messages!", color=0xFF0000)
            embed.set_footer(text="*This is because save messages takes up a lot of the bots resources, so can't be used often")
            await ctx.reply(embed=embed, mention_author=False)
        else:
            file = open("log.txt","w")
            file.write("")
            file.close()
            file = open("log.txt","a")
            messages = await ctx.channel.history(limit=amount).flatten()
            messages.reverse()
            for message in messages:
                if len(message.embeds) > 0:
                    embeds = str(len(message.embeds))
                    file.write(f"{message.author} (Has Embed): {message.content}\n")
                else:
                    file.write(f"{message.author}: {message.content}\n")
            file.close()
            with open("log.txt", "rb") as file:
                await ctx.author.send("Here is your file (It reads top to bottom, top being the oldest):", file=discord.File(file, "log.txt"))
            file = open("log.txt","w")
            file.write("")
            file.close()
        await ctx.message.add_reaction("✅")
            





    @log.error
    async def log_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f"Command is on cooldown!",description=f"Try again in {error.retry_after:.2f}s.", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            print(error)

def setup(client):
    client.add_cog(Moderation(client))
