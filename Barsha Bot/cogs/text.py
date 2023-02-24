import discord
from discord.ext import commands
from main import prefix

class Text(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Clap command, adds a clap in between every message.
    @commands.command()
    async def clap(self, ctx, *, message=None):
        if message == None:
            embed=discord.Embed(title=f"❌ You must enter a message!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        message = message.split()
        if len(message) > 1:
            await ctx.reply((" 👏 ").join(message), mention_author=False)
        else:
            await ctx.reply(f"👏 {message[0]} 👏", mention_author=False)

    # Updown command, flips a sentence upsidedown.
    @commands.command(aliases=["updown"])
    async def upsidedown(self, ctx, *, message=None):
        if message == None:
            embed=discord.Embed(title=f"❌ You must enter a message!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        letters = {
            "z": "z",
            "y": "ʎ",
            "x": "x",
            "w": "ʍ",
            "v": "ʌ",
            "u": "n",
            "t": "ʇ",
            "s": "s",
            "r": "ɹ",
            "q": "b",
            "p": "d",
            "o": "o",
            "n": "u",
            "m": "ɯ",
            "l": "l",
            "k": "ʞ",
            "j": "ɾ",
            "i": "ı",
            "h": "ɥ",
            "g": "ɓ",
            "f": "ɟ",
            "e": "ǝ",
            "d": "p",
            "c": "ɔ",
            "b": "q",
            "a": "ɐ",
            "?": "¿",
            "!": "¡",
            ".": "˙",
            '"': "„",
            "_": "‾",
            "&": "⅋",
            "'": ",",
            ",": "'",
        }
        message = message.lower()
        NewMessage = []
        for letter in message:
            if letter in letters:
                NewMessage.append(letters[letter])
            else:
                NewMessage.append(letter)
        await ctx.reply(("").join(reversed(NewMessage)), mention_author=False)

    # Mock command, makes every other letter in a sentence uppercase. You may also reply to a message to mock the message
    @commands.command()
    async def mock(self, ctx, *, message=None):
        if ctx.message.reference != None:
            message = await ctx.fetch_message(ctx.message.reference.message_id)
            NewMessage = ""
            for letter in enumerate(message.content):
                if letter[0] % 2 == 0:
                    NewMessage += letter[1].upper()
                else:
                    NewMessage += letter[1].lower()
            await message.reply(NewMessage, mention_author=False)
            return
        if message == None:
            embed=discord.Embed(title=f"❌ You must enter a message!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        NewMessage = ""
        for letter in enumerate(message):
            if letter[0] % 2 == 0:
                NewMessage += letter[1].upper()
            else:
                NewMessage += letter[1].lower()
        await ctx.reply(NewMessage, mention_author=False)

    # Sparkle command, adds sparkles to every letter hehe
    @commands.command(aliases=["sparkly", "sparkley"])
    async def sparkle(self, ctx, *, message=None):
        if message == None:
            embed=discord.Embed(title=f"❌ You must enter a message!", color=0xFF0000)
            await ctx.reply(embed=embed, mention_author=False)
            return
        letters = {
            "z": "z͓̽",
            "y": "y͓̽",
            "x": "x͓̽",
            "w": "w͓̽",
            "v": "v͓̽",
            "u": "u͓̽",
            "t": "t͓̽",
            "s": "s͓̽",
            "r": "r͓̽",
            "q": "q͓̽",
            "p": "p͓̽",
            "o": "o͓̽",
            "n": "n͓̽",
            "m": "m͓̽",
            "l": "l͓̽",
            "k": "k͓̽",
            "j": "j͓̽",
            "i": "i͓̽",
            "h": "h͓̽",
            "g": "g͓̽",
            "f": "f͓̽",
            "e": "e͓̽",
            "d": "d͓̽",
            "c": "c͓̽",
            "b": "b͓̽",
            "a": "a͓̽"
        }
        message = message.lower()
        NewMessage = ""
        for letter in message:
            if letter in letters:
                NewMessage += letters[letter]
            else:
                NewMessage += letter
        await ctx.reply(NewMessage, mention_author=False)



    
    # Fancy command, makes a sentence 𝒻𝒶𝒶𝒶𝒶𝒶𝓃𝒸𝓎
    @commands.command(aliases=["special","cursive", "italics"])
    async def fancy(self, ctx, *, message):
        letters = {
            "z": "𝓏",
            "y": "𝓎",
            "x": "𝓍",
            "w": "𝓌",
            "v": "𝓋",
            "u": "𝓊",
            "t": "𝓉",
            "s": "𝓈",
            "r": "𝓇",
            "q": "𝓆",
            "p": "𝓅",
            "o": "𝑜",
            "n": "𝓃",
            "m": "𝓂",
            "l": "𝓁",
            "k": "𝓀",
            "j": "𝒿",
            "i": "𝒾",
            "h": "𝒽",
            "g": "𝑔",
            "f": "𝒻",
            "e": "𝑒",
            "d": "𝒹",
            "c": "𝒸",
            "b": "𝒷",
            "a": "𝒶"
        }
        message = message.lower()
        NewMessage = ""
        for letter in message:
            if letter in letters:
                NewMessage += letters[letter]
            else:
                NewMessage += letter
        await ctx.reply(NewMessage, mention_author=False)



    # Fancy command, makes a sentence 𝒻𝒶𝒶𝒶𝒶𝒶𝓃𝒸𝓎
    @commands.command(aliases=["special1","cursive1", "italics1"])
    async def fancy1(self, ctx, *, message):
        letters = {
            "z": "𝘇",
            "y": "𝘆",
            "x": "𝘅",
            "w": "𝘄",
            "v": "𝘃",
            "u": "𝘂",
            "t": "𝘁",
            "s": "𝘀",
            "r": "𝗿",
            "q": "𝗾",
            "p": "𝗽",
            "o": "𝗼",
            "n": "𝗻",
            "m": "𝗺",
            "l": "𝗹",
            "k": "𝗸",  
            "j": "𝗷",
            "i": "𝗶",
            "h": "𝗵",
            "g": "𝗴",
            "f": "𝗳",
            "e": "𝗲",
            "d": "𝗱",
            "c": "𝗰",
            "b": "𝗯",
            "a": "𝗮"
        }
        message = message.lower()
        NewMessage = ""
        for letter in message:
            if letter in letters:
                NewMessage += letters[letter]
            else:
                NewMessage += letter
        await ctx.reply(NewMessage, mention_author=False)



def setup(client):
    client.add_cog(Text(client))
