import discord
from discord.ext import commands
from main import prefix, Developers

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    #  Help command, if the user enters a valid category, gives information on all the commands in a category
    @commands.command()
    async def help(self, ctx, *, category=None):
        dev = self.client.get_user(448645983748882442)
        # Default embed
        MainEmbed = discord.Embed(title="❔ Help Menu!", description=f"Valid Prefixs: `{prefix[0]}`, `@BarshaGame Bot#0455`, `<@1016294213735948348-`\
        \nTo get more information on any command, run `{prefix[0]}help <category-`", color = 0x225c9a)
        MainEmbed.add_field(name="⚔️ Moderation", value=f"- `-ban <member- (reason)`\n- `-unban <member- (reason)`\n- `-bans`\n- `-muterole`\
        \n- `mute <member- (reason)`\n- `-unmute <member-`\n- `-kick <member- (reason)`\n- `-log <amount-`\n- `-purge <amount-`")
        MainEmbed.add_field(name="🖨️ Text", value=f"- `-clap <sentence-`\n- `-mock <sentence-`\n- `-upsidedown <sentence-`\n- `-sparkle <sentence-`\
        \n- `fancy <sentence-`\n- `Fancy1 <sentence>`")
        MainEmbed.add_field(name="🤖 Bot Info", value=f"- `-stats`\n- `-support`\n- `-suggest (suggestions for the bot)`")
        MainEmbed.add_field(name="📚 General Commands", value=f"- `-userinfo <member-`\n- `-serverinfo`\n- `-avatar <member-`\n- `-embed <title- (-s description) (-a)`")
        MainEmbed.add_field(name="🎮 Game Commands", value=f"- `-leaderboard`\n- `-trivia (category) (easy/medium/hard) (boolean/mutliple)`\n- `-categrories`\n- `-wordle (easy/medium/hard)`")
        MainEmbed.add_field(name="🖼️ Images", value=f"- `-gif`")
        dev_icon="https://cdn.discordapp.com/emojis/965663387109437480.webp?size=64"
        MainEmbed.add_field(name=f"{dev_icon} To Get Developer Contact", value=f"- `-developer`")
        if ctx.author.id in Developers:
            MainEmbed.add_field(name="🔧 Developer Commands", value=f"- `-servers`\n- `-join <server-`")
        MainEmbed.set_footer(text=f"This bot was coded in Python!\nand was developed by BardiaMsa ❤️",
        icon_url="https://cdn.discordapp.com/emojis/898009300646105089.png?size=128")
        MainEmbed.set_author(name=f"Get more information on any command, run '{prefix[0]}help <category-'")

        if category != None:
            category = category.lower()

            # Checks if the category is "mod"
            if category.startswith("mod"):
                embed = discord.Embed(title="⚔️ Moderation", color = 0x225c9a)
                embed.add_field(name=f"`-ban <member- (reason)`", value="- *Bans a member, and logs the reason in the audit logs if provided.*")
                embed.add_field(name=f"`-unban <member-`", value="- *Unbans a user, you must enter the user in this format: `Username#Numbers`*")
                embed.add_field(name=f"`-bans`", value="- *Gives a list of banned user in your current server*")
                embed.add_field(name=f"`-mute <member- (reason)`", value=f"- *Mutes a member, if you do not have a mute role create one using `{prefix[0]}muterole`*")
                embed.add_field(name=f"`-muterole`", value=f"- *Creates a mute role, the role must remain named `Muted` or it will not work!*")
                embed.add_field(name=f"`-kick <member- (reason)`", value=f"- *Kicks a member, and logs the reason in audit logs if provided.*")
                embed.add_field(name=f"`-log <amount-`", value=f"- *Logs messages in a channel and puts them into a file*")
                embed.add_field(name=f"`-purge <amount-`", value=f"- *Clears the specified amount of messages from the channel*")
                embed.set_footer(text="the items in '<-'s are required, the items in '()'s are optional.")
                await ctx.reply(embed=embed, mention_author=False)
            # Checks if the category is "text"
            elif category.startswith("text"):
                embed = discord.Embed(title=f"🖨️ Text", color = 0x225c9a)
                embed.add_field(name=f"`-clap <sentence-`", value=f"- *Adds the 👏 emoji in-between every word: This 👏 is 👏 an 👏 example*")
                embed.add_field(name=f"`-mock <sentence-`", value=f"- *Sends a message with every other capitals: ThIs Is An ExAmPlE*\
                    \n- *You may also reply to someone else message to mock their message.*")
                embed.add_field(name=f"`-upsidedown <sentence-`", value=f"- *Flips a sentence upsidedown: ǝldɯɐxǝ uɐ sı sıɥʇ*")
                embed.add_field(name=f"`-sparkle <sentence-`", value=f"- *Adds sparkles to to a sentence: t͓̽h͓̽i͓̽s͓̽ i͓̽s͓̽ a͓̽n͓̽ e͓̽x͓̽a͓̽m͓̽p͓̽l͓̽e͓̽*")
                embed.add_field(name=f"`-fancy <sentence-`", value=f"- *Makes a sentence faaancy: 𝓉𝒽𝒾𝓈 𝒾𝓈 𝒶𝓃 𝑒𝓍𝒶𝓂𝓅𝓁𝑒*")
                await ctx.reply(embed=embed, mention_author=False)
            # Checks if the category is "bot info"
            elif category.startswith("bot"):
                embed= discord.Embed(title=f"🤖 Bot Info", color = 0x225c9a)
                embed.add_field(name=f"`-suggest <suggestion-`", value=f"- *Makes a suggestion for this bot, you may vote on suggestions in my support server (`{prefix[0]}support`)*")
                embed.add_field(name=f"`-stats`", value=f"- *Shows the stats of this bot*")
                embed.add_field(name=f"`-support`", value=f"- *DMs the user support links*")
                embed.set_footer(text="the items in '<-'s are required, the items in '()'s are optional.")
                await ctx.reply(embed=embed, mention_author=False)
            # Checks if the category is "general"
            elif category.startswith("gen"):
                embed = discord.Embed(title=f"📚 General Commands", color = 0x225c9a)
                embed.add_field(name=f"`-embed <title- (-s description) (-a)`", value=f"- *Sends an embed based on the args provided. You may add a description by adding a '-s' to seperate the two fields, and a '-a' at the very end to remove the author field*")
                embed.add_field(name=f"`-userinfo (member)`", value=f"- *Sends all info on the user provided, or the author if no user is provided*")
                embed.add_field(name=f"`-serverinfo`", value=f"- *Sends all info on the current guild you're in*")
                embed.add_field(name=f"`-avatar (member)`", value=f"- *Sends the avatar of the user provided, or the author if no user is provided*")
                embed.set_footer(text="the items in '<-'s are required, the items in '()'s are optional.")
                await ctx.reply(embed=embed, mention_author=False)
            elif category.startswith("ima") or category.startswith("pic") or category.startswith("img"):
                embed = discord.Embed(title=f"🖼️ Image Commands", color = 0x225c9a)
                embed.add_field(name=f"`-joke`", value=f"- *Sends A Random Joke*")
                await ctx.reply(embed=embed, mention_author=False)
            elif category.startswith("dev"):
                if ctx.author.id in Developers:
                    embed = discord.Embed(title=f"🔧 Developer Commands", color = 0x225c9a)
                    embed.add_field(name=f"`-servers`", value=f"- *Lists all the servers that the bot is in*")
                    embed.add_field(name=f"`-join <server ID-`", value=f"- *Sends an invite to a server that the bot is in to the author*")
                    embed.set_footer(text="the items in '<-'s are required, the items in '()'s are optional.")
                    await ctx.reply(embed=embed, mention_author=False)    
            elif category.startswith("gam"):
                embed = discord.Embed(title=f"🎮 Game Commands", color = 0x225c9a)
                embed.add_field(name=f"`-leaderboard`", value=f"- *Shows the leaderboard for Wordle and trivia*")
                embed.add_field(name=f"`-trivia (category) (easy/medium/hard) (boolean/mutliple)`", value=f"- *Gives you a trivia question, you can change the category, the difficulty and the type (boolean is true/false, multiple is multiple choice)*")
                embed.add_field(name=f"`-categories`", value=f"- *Shows all the available trivia categories.*")
                embed.add_field(name=f"`-wordle (easy/medium/hard)`", value=f"- *Starts a Wordle game!*")
                embed.set_footer(text="the items in '<-'s are required, the items in '()'s are optional.")
                await ctx.reply(embed=embed, mention_author=False)
            else:
                # If no valid category is provided, sends the default embed
                await ctx.reply(embed=MainEmbed, mention_author=False)
        # If no category is provided, sends the default embed
        else:
            await ctx.reply(embed=MainEmbed, mention_author=False)
        
def setup(client):
    client.add_cog(Help(client))