import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.queue = {}
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self, ctx):
        if len(self.queue) > 0:
            self.is_playing = True
            #get the first url
            m_url = self.queue[ctx.guild.id][0]['source']
            #remove the first element as you are currently playing it
            self.queue[ctx.guild.id].pop(0)
            try:
                ctx.voice_client.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            except:
                ctx.voice_client.stop()
                ctx.voice_client.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self, ctx):
        if len(self.queue) > 0:
            self.is_playing = True

            m_url = self.queue[ctx.guild.id][0]['source']
            
            #try to connect to voice channel if you are not already connected
            state = ctx.author.voice
            if state == None:
                embed = discord.Embed(title="You must be in a VC to use this command!", color=0x225c9a)
                await ctx.reply(embed=embed, mention_author=False)
            else:
                channel = ctx.author.voice.channel
                if ctx.voice_client == None:
                    await channel.connect()
                else:
                    if channel == ctx.voice_client.channel:
                        pass
                    else:
                        embed = discord.Embed(title="I'm already in a different VC!", color=0x225c9a)
                        await ctx.reply(embed=embed, mention_author=False)
                        return
            
                #remove the first element as you are currently playing it
                self.queue[ctx.guild.id].pop(0)
                ctx.voice_client.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
        else:
            self.is_playing = False

    @commands.command(aliases=["p"])
    async def play(self, ctx, *args):
        query = " ".join(args)
        
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            #you need to be connected so that the bot knows where to go
            embed = discord.Embed(title="You must be in a VC to use this command!", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            song = self.search_yt(query)
            print(song)
            if type(song) == type(True):
                embed = discord.Embed(title="Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.", color=0x225c9a)
                await ctx.reply(embed=embed, mention_author=False)
            else:
                title = song["title"]
                url = song["source"]
                embed = discord.Embed(title=f"__{title}__ added to the queue!", description=f"[Music Url]({url})", color=0x225c9a)
                await ctx.reply(embed=embed, mention_author=False)
                try:
                    self.queue[ctx.guild.id].append(song)
                except:
                    self.queue[ctx.guild.id] = [song]
                if self.is_playing == False:
                    await self.play_music(ctx)

    @commands.command(aliases=["q", "que", "playlist"])
    async def queue(self, ctx):
        description = ""
        try:
            for song in enumerate(self.queue[ctx.guild.id]):
                description += f"**{song[0]+1}:** {song[1]['title']}\n"
        except:
            embed = discord.Embed(title="No songs in your queue!", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)
            return
        embed = discord.Embed(title="Your current queue:", description=f"{description}", color=0x225c9a)
        if description != "":
            await ctx.reply(embed=embed, mention_author=False)
        else:
            embed = discord.Embed(title="No songs in your queue!", color=0x225c9a)
            await ctx.reply(embed=embed, mention_author=False)

    """VERY BUGGY COMMAND, MUST FIX LATER"""
    '''
    @commands.command(name="skip", help="Skips the current song being played")
    async def skip(self, ctx):
        state = ctx.author.voice
        if state == None:
            embed = discord.Embed(title="You must be in a VC to use this command!", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
            return
        channel = ctx.author.voice.channel
        if ctx.voice_client == None:
            embed = discord.Embed(title="I must be in a VC to use this command! ", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
        elif ctx.voice_client.channel == channel:
            ctx.voice_client.stop()
            await self.play_music(ctx)
            embed = discord.Embed(title="Skipped", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
        elif ctx.voice_client != None and ctx.voice_client.channel != channel:
            embed = discord.Embed(title="You must be in the same VC as me to use this command!", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
    '''

    @commands.command(aliases=["dc"])
    async def disconnect(self, ctx):
        state = ctx.author.voice
        if state == None:
            embed = discord.Embed(title="You must be in a VC to use this command!", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
            return
        channel = ctx.author.voice.channel
        if ctx.voice_client == None:
            embed = discord.Embed(title="I must be in a VC to use this command! ", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
        elif ctx.voice_client.channel == channel:
            await ctx.voice_client.disconnect()
            embed = discord.Embed(title="Disconnected", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)
            self.is_playing = False
            self.queue[ctx.guild.id].clear()
            await ctx.voice_client.disconnect()
        elif ctx.voice_client != None and ctx.voice_client.channel != channel:
            embed = discord.Embed(title="You must be in the same VC as me to use this command!", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Music(client))