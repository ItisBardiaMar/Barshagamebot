import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
import requests
import random
import html
import asyncio
import string
import asyncpraw
import json
import os
import enchant
import datetime

pointsPath = os.path.dirname(__file__)+'/points.json'

async def redEmoji(letter):
    red_letters = {
        "A": "<:A_:937168734932598785>",
        "H": "<:H_:937168735414919168>",
        "J": "<:J_:937168735473647676>",
        "B": "<:B_:937168735628832809>",
        "L": "<:L_:937168735674982420>",
        "G": "<:G_:937168735968567327>",
        "X": "<:X_:937168736039870485>",
        "R": "<:R_:937168736039882854>",
        "U": "<:U_:937168736081809449>",
        "T": "<:T_:937168736140542072>",
        "C": "<:C_:937168736228610159>",
        "Y": "<:Y_:937168736228614175>",
        "E": "<:E_:937168736287330344>",
        "O": "<:O_:937168736287354942>",
        "I": "<:I_:937168736320905288>",
        "F": "<:F_:937168736350253168>",
        "M": "<:M_:937168736354463784>",
        "W": "<:W_:937168736354463814>",
        "V": "<:V_:937168736367046676>",
        "Q": "<:Q_:937168736379613194>",
        "P": "<:P_:937168736379625543>",
        "N": "<:N_:937168736421548112>",
        "S": "<:S_:937168736442531840>",
        "D": "<:D_:937168736442535987>",
        "K": "<:K_:937168736572567613>",
        "Z": "<:Z_:937168736882950174>"
    }
    return red_letters[letter]
async def yellowEmoji(letter):
    yellow_letters = {
        "C": "<:C_:938957147994193961>",
        "B": "<:B_:938957148220694570>",
        "A": "<:A_:938957148300394496>",
        "F": "<:F_:938957148312965170>",
        "G": "<:G_:938957148354908200>",
        "I": "<:I_:938957148388483092>",
        "J": "<:J_:938957148392656947>",
        "T": "<:T_:938957148493348896>",
        "D": "<:D_:938957148711444611>",
        "P": "<:P_:938957148732403714>",
        "S": "<:S_:938957148740792321>",
        "V": "<:V_:938957148862435378>",
        "E": "<:E_:938957148950507570>",
        "Z": "<:Z_:938957148971487232>",
        "Y": "<:Y_:938957148979867668>",
        "R": "<:R_:938957148984053780>",
        "N": "<:N_:938957148988264518>",
        "W": "<:W_:938957149013418064>",
        "U": "<:U_:938957149051166770>",
        "K": "<:K_:938957149067968545>",
        "L": "<:L_:938957149076328519>",
        "Q": "<:Q_:938957149122478150>",
        "X": "<:X_:938957149139251230>",
        "O": "<:O_:938957149156020244>",
        "H": "<:H_:938957149156028466>",
        "M": "<:M_:938957149281857616>"
    }
    return yellow_letters[letter]
async def greenEmoji(letter):
    green_letters = {
    "A": "<:A_:938957023113011200>",
    "B": "<:B_:938957023381426247>",
    "F": "<:F_:938957023385632799>",
    "H": "<:H_:938957023494684792>",
    "L": "<:L_:938957023570173972>",
    "R": "<:R_:938957023654084730>",
    "J": "<:J_:938957023721173093>",
    "M": "<:M_:938957023809261589>",
    "P": "<:P_:938957023977029672>",
    "D": "<:D_:938957023981211678>",
    "N": "<:N_:938957023981219860>",
    "Y": "<:Y_:938957023985418241>",
    "Q": "<:Q_:938957023998005379>",
    "Z": "<:Z_:938957024002195506>",
    "O": "<:O_:938957024014778398>",
    "E": "<:E_:938957024018989076>",
    "I": "<:I_:938957024023171193>",
    "S": "<:S_:938957024044134450>",
    "K": "<:K_:938957024073494528>",
    "C": "<:C_:938957024073498694>",
    "V": "<:V_:938957024090263602>",
    "U": "<:U_:938957024090279946>",
    "W": "<:W_:938957024123818004>",
    "T": "<:T_:938957024140591114>",
    "G": "<:G_:938957024253837393>",
    "X": "<:X_:938957024350335006>"
    }
    return green_letters[letter]
async def blueEmoji(letter):
    blue_letters = {
        "G": "<:G_:937168634374160445>",
        "A": "<:A_:937168634470617108>",
        "F": "<:F_:937168634621620285>",
        "E": "<:E_:937168634705481738>",
        "I": "<:I_:937168634936184862>",
        "B": "<:B_:937168634944569344>",
        "J": "<:J_:937168635062018088>",
        "L": "<:L_:937168635150106704>",
        "P": "<:P_:937168635443683378>",
        "D": "<:D_:937168635691167856>",
        "S": "<:S_:937168635695341608>",
        "T": "<:T_:937168635699540048>",
        "Q": "<:Q_:937168635728896032>",
        "U": "<:U_:937168635737296947>",
        "W": "<:W_:937168635842142209>",
        "C": "<:C_:937168635905077269>",
        "H": "<:H_:937168636009922590>",
        "N": "<:N_:937168636014100600>",
        "O": "<:O_:937168636030906428>",
        "V": "<:V_:937168636102201414>",
        "K": "<:K_:937168636123172904>",
        "X": "<:X_:937168636190277642>",
        "Z": "<:Z_:937168636215427082>",
        "Y": "<:Y_:937168636236410920>",
        "R": "<:R_:937168636244803624>",
        "M": "<:M_:937168636265783356>"
    }
    return blue_letters[letter]
async def greyEmoji(letter):
    grey_letters = {
        "E": "<:E_:938957094688788543>",
        "J": "<:J_:938957094818832446>",
        "A": "<:A_:938957094835597402>",
        "B": "<:B_:938957094839779368>",
        "D": "<:D_:938957094843977728>",
        "F": "<:F_:938957094864973854>",
        "C": "<:C_:938957094902706236>",
        "V": "<:V_:938957094982406185>",
        "I": "<:I_:938957095124992090>",
        "T": "<:T_:938957095200501841>",
        "P": "<:P_:938957095263408148>",
        "R": "<:R_:938957095317934101>",
        "U": "<:U_:938957095322144818>",
        "S": "<:S_:938957095376678983>",
        "N": "<:N_:938957095385063485>",
        "M": "<:M_:938957095418601493>",
        "Z": "<:Z_:938957095426981950>",
        "H": "<:H_:938957095531843624>",
        "K": "<:K_:938957095531860038>",
        "O": "<:O_:938957095590568026>",
        "L": "<:L_:938957095594766337>",
        "G": "<:G_:938957095653474334>",
        "Q": "<:Q_:938957095695433808>",
        "W": "<:W_:938957095712206858>",
        "X": "<:X_:938957095804485643>",
        "Y": "<:Y_:938957095888384030>",
    }
    return grey_letters[letter]
async def darkGreyEmoji(letter):
    grey_letters = {
        "A": "<:A_:942506346186674206>",
        "D": "<:D_:942506346341888062>",
        "E": "<:E_:942506346413178910>",
        "G": "<:G_:942506346534830100>",
        "I": "<:I_:942506346698383370>",
        "J": "<:J_:942506346727755806>",
        "L": "<:L_:942506346769690624>",
        "B": "<:B_:942506346803261511>",
        "K": "<:K_:942506346924875876>",
        "P": "<:P_:942506346996170832>",
        "M": "<:M_:942506347029758032>",
        "S": "<:S_:942506347168145488>",
        "T": "<:T_:942506347239456819>",
        "V": "<:V_:942506347298164757>",
        "Y": "<:Y_:942506347327533057>",
        "O": "<:O_:942506347386269746>",
        "W": "<:W_:942506347419807774>",
        "C": "<:C_:942506347449167983>",
        "F": "<:F_:942506347516264470>",
        "Z": "<:Z_:942506347595960380>",
        "Q": "<:Q_:942506347629531136>",
        "U": "<:U_:942506347650482196>",
        "H": "<:H_:942506347663081582>",
        "N": "<:N_:942506347705040926>",
        "X": "<:X_:942506347717595136>",
        "R": "<:R_:942506347780530236>",
    }
    return grey_letters[letter]

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def trivia(self, ctx, category_choice=None, difficulty=None, question_type=None):
        await open_account(ctx.author)
        # Checks if they selected easy, medium, or hard
        valid_difficulties = ["easy", "medium", "hard"]
        if difficulty not in valid_difficulties:
            difficulty = random.choice(["easy", "medium", "hard"])
        # Checks if they selected boolean or multiple
        valid_question_types = ["boolean", "multiple"]
        if question_type not in valid_question_types:
            question_type = random.choice(["multiple", "boolean"])
        # Selects a random category, if an invalid one is entered
        if category_choice == None:
            category_choice = random.choice(["General_Knowledge", "Books", "Film", "Music", "Musicals", "Television", "Video_Games", "Board_Games", "Science", 
            "Computers", "Mathematics", "Mythology", "Sports", "Geography", "History", "Politics", "Art", "Celebrities", "Animals", "Vehicles", "Comics", "Gadgets", 
            "Anime", "Cartoon"])
        #Getting Data
        request = requests.get("https://opentdb.com/api_category.php")
        categories = request.json()
        # Replaces the _'s in their category choice with spaces
        for index, letter in enumerate(category_choice):
            if letter == "_":
                category_choice = category_choice[:index] + " " + category_choice[index+1:]
        # Fetches a question
        category_id = None
        category_name = None
        for index, category in enumerate(categories['trivia_categories']):
            if category_choice.lower() in category['name'].lower():
                category_id = categories['trivia_categories'][index]['id']
                category_name = categories['trivia_categories'][index]['name']
        question_request = requests.get(f"https://opentdb.com/api.php?amount=1&category={category_id}&difficulty={difficulty}&type={question_type}")
        question_json = question_request.json()
        # Reponse code 0 means there was no error
        if question_json['response_code'] == 0:
            results = question_json['results'][0]
            question = html.unescape(results['question'])
            correct_answer = html.unescape(results['correct_answer'])
            incorrect_answers = results['incorrect_answers']
            for index, incorrect_answer in enumerate(incorrect_answers):
                uncoded_text = html.unescape(incorrect_answer)
                incorrect_answers[index] = uncoded_text
            answers = incorrect_answers
            position = random.randint(0, len(answers))
            answers.insert(position, correct_answer)
            possible_answers = ""
            letter_conversion = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}
            for index, answer in enumerate(answers):
                possible_answers += f"**{letter_conversion[index]}:** {answer}\n"
            embed = discord.Embed(title=f"Question: `{question}`", description=f"{possible_answers}")
            embed.set_footer(text=f"Difficulty: {difficulty} | Category: {category_name} | 30 Seconds to answer!")
            message = await ctx.reply(embed=embed, mention_author=False)
            try:
                message = await self.client.wait_for('message', timeout=30.0, check=lambda message: message.author == ctx.author)
            except asyncio.TimeoutError:
                embed = discord.Embed(title=f"Question timed out! Run the command again for another question.")
                await message.edit(content=None, embed=embed)
                return
            if message.content.lower() == correct_answer.lower() or message.content.lower() == letter_conversion[position].lower():
                await update_points(ctx.author, 1, "trivia")
                await message.reply("Correct!", mention_author=False)
            else:
                await message.reply(f"Incorrect, correct answer: **{letter_conversion[position]}** / **{correct_answer}**", mention_author=False)
        # If there was a response code of anything other than 0 it will throw the error
        else:
            errors = {"0": "Returned results successfully.", 
            "1": "No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.",
            "2": "Invalid Parameter, make sure you have everything spelled correctly.",
            "3": "Token Not Found Session Token does not exist.",
            "4": "Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary."}
            embed = discord.Embed(title="Error! Please try again later.", description=f"`{errors[str(question_json['response_code'])]}`", color=discord.Color.red())
            await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=["c4", "connectfour"])
    async def connect4(self, ctx, member:discord.Member=None):
        game = None
        if member == None:
            embed = discord.Embed(title=f"Who would you like to play?", color=0x225c9a)
            game = await ctx.reply(embed=embed, mention_author=False)
            try:
                message = await self.client.wait_for('message', timeout=30.0, check=lambda message: message.author == ctx.author)
            except asyncio.TimeoutError:
                embed = discord.Embed(title=f"Game timed out! To try again send `>c4 (member)`", color=0x225c9a)
                await game.edit(content=None, embed=embed)
                return
            try:
                converter = MemberConverter()
                member = await converter.convert(ctx, message.content)
            except:
                embed = discord.Embed(title=f"Invalid member! To try again send `>c4 (member)`", color=0x225c9a)
                await game.edit(content=None, embed=embed)
        grid = [
            ["🔳","🔳","🔳","🔳","🔳","🔳","🔳"],
            ["🔳","🔳","🔳","🔳","🔳","🔳","🔳"],
            ["🔳","🔳","🔳","🔳","🔳","🔳","🔳"],
            ["🔳","🔳","🔳","🔳","🔳","🔳","🔳"],
            ["🔳","🔳","🔳","🔳","🔳","🔳","🔳"],
            ["🔳","🔳","🔳","🔳","🔳","🔳","🔳"]
        ]
        embed = discord.Embed(title=f"Connect Four! 🔴 `{ctx.author.name}` against `{member.name}` 🟡", color=0x225c9a)
        embed.add_field(name=f"{member.name}'s Turn:",
        value=f"🟦{''.join(grid[0])}🟦\
              \n🟦{''.join(grid[1])}🟦\
              \n🟦{''.join(grid[2])}🟦\
              \n🟦{''.join(grid[3])}🟦\
              \n🟦{''.join(grid[4])}🟦\
              \n🟦{''.join(grid[5])}🟦\
              \n🟦1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣🟦")
        game = await ctx.reply(f"{member.mention}", embed=embed, mention_author=False)
        await game.add_reaction("1️⃣")
        await game.add_reaction("2️⃣")
        await game.add_reaction("3️⃣")
        await game.add_reaction("4️⃣")
        await game.add_reaction("5️⃣")
        await game.add_reaction("6️⃣")
        await game.add_reaction("7️⃣")
        VALID_RESPONSES = {"1️⃣": 0,"2️⃣": 1,"3️⃣": 2,"4️⃣": 3,"5️⃣": 4,"6️⃣": 5,"7️⃣": 6}
        turn = "yellow"
        TURNS = {"red": {"user": ctx.author, "piece": "🔴"}, 
                "yellow": {"user": member, "piece": "🟡"}}
        round = 0
        while True:
            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=lambda reaction, user: user == member)
            except:
                embed = discord.Embed(title=f"Game timed out! To try again send `>c4 (member)`", color=0x225c9a)
                await game.edit(content=None, embed=embed)
                return
            if str(reaction) in VALID_RESPONSES:
                row = 5
                while True:
                    if grid[row][VALID_RESPONSES[str(reaction)]] == "🔳":
                        grid[row][VALID_RESPONSES[str(reaction)]] = TURNS[turn]["piece"]
                        break
                    else:
                        row -= 1
                    if row == -1:
                        await ctx.send("That row is full!")
                        break
                if row == -1:
                    continue
                if turn == "yellow":
                    turn = "red"
                else:
                    turn = "yellow"
                embed = discord.Embed(title=f"Connect Four! 🔴 `{ctx.author.name}` against `{member.name}` 🟡", color=0x225c9a)
                embed.add_field(name=f"{member.name}'s Turn:",
                value=f"🟦{''.join(grid[0])}🟦\
                      \n🟦{''.join(grid[1])}🟦\
                      \n🟦{''.join(grid[2])}🟦\
                      \n🟦{''.join(grid[3])}🟦\
                      \n🟦{''.join(grid[4])}🟦\
                      \n🟦{''.join(grid[5])}🟦\
                      \n🟦1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣🟦")
                await game.edit(content=TURNS[turn]["user"].mention, embed=embed)
                await game.remove_reaction(reaction, user)
                if round > 7:
                    LeftRight = 0
                    UpDown = 0
                    for i in range(4):
                        if grid[row][VALID_RESPONSES[str(reaction)]-i] == TURNS[turn]["piece"]:
                            LeftRight += 1
                        else:
                            break
                    for i in range(4):
                        if grid[row][VALID_RESPONSES[str(reaction)]+i] == TURNS[turn]["piece"]:
                            LeftRight += 1
                        else:
                            break
                    for i in range(4):
                        if grid[row-i][VALID_RESPONSES[str(reaction)]] == TURNS[turn]["piece"]:
                            UpDown += 1
                        else:
                            break
                    for i in range(4):
                        if grid[row+i][VALID_RESPONSES[str(reaction)]+i] == TURNS[turn]["piece"]:
                            UpDown += 1
                        else:
                            break
                    if LeftRight >= 4 or UpDown >= 4:
                        await ctx.send(TURNS[turn]["piece"] + " " + TURNS[turn]["user"] + " wins! " + TURNS[turn]["piece"])
                        break

                round += 1 

    @commands.command(aliases=["tt", "typing"])
    async def typingtest(self, ctx):
        US_DICT = enchant.Dict("en_US")
        SENTENCE_LENGTH = random.randint(30, 40)
        LETTER_MAPPING = {
            "z": "𝐳",
            "y": "𝐲",
            "x": "𝐱",
            "w": "𝐰",
            "v": "𝐯",
            "u": "𝐮",
            "t": "𝐭",
            "s": "𝐬",
            "r": "𝐫",
            "q": "𝐪",
            "p": "𝐩",
            "o": "𝐨",
            "n": "𝐧",
            "m": "𝐦",
            "l": "𝐥",
            "k": "𝐤",
            "j": "𝐣",
            "i": "𝐢",
            "h": "𝐡",
            "g": "𝐠",
            "f": "𝐟",
            "e": "𝐞",
            "d": "𝐝",
            "c": "𝐜",
            "b": "𝐛",
            "a": "𝐚"
        }
        sentence = ""
        mapped_sentence = ""
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        words = response.content.splitlines()
        for i in range(SENTENCE_LENGTH):
            while True:
                word = random.choice(words).decode()
                if US_DICT.check(word) == True and len(word) > 3:
                    sentence += word + " "
                    break
        for letter in sentence:
            if letter in LETTER_MAPPING:
                mapped_letter = LETTER_MAPPING[letter]
                mapped_sentence += mapped_letter
            else:
                mapped_sentence += letter
        await ctx.send(mapped_sentence)
        FIRST_TIME = datetime.datetime.now()
        try:
            user_message = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=480.0)
        except:
            await ctx.send("Your time to respond has expired!")
        SECOND_TIME = datetime.datetime.now()
        ELAPSED_TIME_SECONDS = (SECOND_TIME - FIRST_TIME).seconds
        ELAPSED_TIME_MINUTES = ELAPSED_TIME_SECONDS/60
        word_mistakes = 0
        letter_mistakes = 0
        USER_WORDS = user_message.content.split()
        SENTENCE_WORDS = sentence.split()
        for index1, word in enumerate(USER_WORDS):
            for index2, letter in enumerate(word):
                if SENTENCE_WORDS[index1][index2] == letter:
                    continue
                else:
                    mistakes += 1
                    break
        for index, letter in enumerate(user_message.content):
            if sentence[index] == letter:
                continue
            else:
                mistakes += 1
        AVERAGE_WORD_LEN = None
        letter_amt = 0
        for index, letter in enumerate(sentence):
            if letter != " ":
                letter_amt += 1
        CORRECT_WORDS = len(SENTENCE_WORDS) - word_mistakes
        CORRECT_LETTERS = len(sentence) - letter_mistakes
        WORD_ACCURACY = CORRECT_WORDS/len(SENTENCE_WORDS)
        LETTER_ACCURACY = CORRECT_LETTERS/len(sentence)
        WPM = CORRECT_WORDS/ELAPSED_TIME_MINUTES
        LPM = CORRECT_LETTERS/ELAPSED_TIME_MINUTES
        await ctx.send(WPM)
        await ctx.send(LPM/(letter_amt/len(USER_WORDS)))


    @commands.command(aliases=["word"])
    async def wordle(self, ctx, difficulty=None):
        US_DICT = enchant.Dict("en_US")
        await open_account(ctx.author)
        ALPHABET = list(string.ascii_uppercase)
        ROW_AMT = 6
        ROW_SIZE = 5
        WORD_BLACKLIST = ["sperm", "whore", "penis", "pussy", "horny", "boobs"]
        current_word = None
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        words = response.content.splitlines()
        if difficulty == None:
            difficulty = "medium"
        if difficulty.lower() == "easy":
            ROW_AMT = 7
            ROW_SIZE = 4
            while True:
                word = random.choice(words).decode()
                if len(word) == ROW_SIZE and word.lower() not in WORD_BLACKLIST:
                    current_word = word.upper()
                    break
        elif difficulty.lower() == "medium":
            ROW_AMT = 6
            ROW_SIZE = 5
            while True:
                word = random.choice(words).decode()
                if len(word) == ROW_SIZE and US_DICT.check(word) == True:
                    current_word = word.upper()
                    break
        elif difficulty.lower() == "hard":
            ROW_AMT = 5
            ROW_SIZE = 6
            while True:
                word = random.choice(words).decode()
                if len(word) == ROW_SIZE:
                    current_word = word.upper()
                    break
        keyboard = {}
        locations = {}
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            keyboard[letter] = await greyEmoji(letter)
        for index, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            locations[letter] = index 
        grid = ["<:EmptySquare:942267094114926643> "*ROW_SIZE + "\n"]*ROW_AMT
        visual = ("").join(grid)
        print(current_word)
        greenA = await greenEmoji('A')
        yellowA = await yellowEmoji('A')
        greyA = await greyEmoji('A')
        embed = discord.Embed(title=f"Reply to this message with your guess!\n> {greenA} Correct Letter and Location\n> {yellowA} Correct Letter, Incorrect Location\n> {greyA} Incorect Letter and Location\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_",
        description=visual + f"\n{''.join(keyboard.values())}", color=discord.Color.dark_gray())
        embed.set_author(name="🔤 Wordle!")
        embed.set_footer(text="This game will end if you do not respond in 5 minutes between turns!")
        game = await ctx.reply(embed=embed, mention_author=False)
        round = 0
        while True:
            if round > ROW_AMT-1:
                embed = discord.Embed(title=f"> Ran out of guesses! Your word was: `{current_word}`\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_",
                description=("").join(grid) + f"\n{''.join(keyboard.values())}", color=discord.Color.dark_gray())
                embed.set_author(name="🔤 Wordle!")
                await game.edit(embed=embed)
                break
            try:
                original_message = await self.client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=600.0)
            except:
                embed = discord.Embed(title=f"**🔤 Wordle! 🔤**\n> Your time has expired! Your word was: `{current_word}`\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_",
                description=("").join(grid) + f"\n{''.join(keyboard.values())}", color=discord.Color.dark_gray())
                await game.edit(embed=embed)
                break
            if original_message.reference:
                if original_message.reference.message_id == game.id:
                    message = list(original_message.content.strip().upper())
                    if len(message) == ROW_SIZE:
                        if US_DICT.check("".join(message)) == True:
                            row = ""
                            total_right = 0
                            stop = False
                            for index, letter in enumerate(message):
                                letter = letter.upper()
                                if letter not in string.ascii_uppercase:
                                    stop = True
                            if stop == True:
                                await ctx.send("Word must only contain letters!")
                                continue
                            else:
                                if "".join(message).lower() == "adieu":
                                    await original_message.reply("lame word...but I'll take it...", mention_author=False)
                                for index, letter in enumerate(message):
                                    letter = letter.upper()
                                    if letter not in string.ascii_uppercase:
                                        stop = True
                                    else:
                                        if letter in current_word:
                                            if current_word[index] == letter:
                                                green = await greenEmoji(letter)
                                                row += green + " "
                                                keyboard[letter] = green
                                                total_right += 1
                                            else:
                                                yellow = await yellowEmoji(letter)
                                                row += yellow + " "
                                                keyboard[letter] = yellow
                                        else:
                                            grey = await greyEmoji(letter)
                                            darkGrey = await darkGreyEmoji(letter)
                                            row += grey + " "
                                            keyboard[letter] = darkGrey

                            grid[round] = row + "\n"        
                            if total_right == ROW_SIZE:
                                embed = discord.Embed(title=f"> Correct! Your word was: `{current_word}`\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_",
                                description=("").join(grid) + f"\n{''.join(keyboard.values())}", color=discord.Color.dark_gray())
                                embed.set_author(name="🔤 Wordle!")
                                await game.edit(embed=embed)
                                await original_message.add_reaction("✅")
                                await update_points(ctx.author, 1, "wordle")
                                break
                            embed = discord.Embed(title=f"Reply to this message with your guess!\n> {greenA} Correct Letter and Location\n> {yellowA} Correct Letter, Incorrect Location\n> {greyA} Incorect Letter and Location\n\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_",
                            description=("").join(grid) + f"\n{''.join(keyboard.values())}", color=discord.Color.dark_gray())
                            embed.set_author(name="🔤 Wordle!")
                            embed.set_footer(text="This game will end if you do not respond in 10 minutes between turns!")
                            await game.edit(embed=embed)
                            round += 1
                        else:
                            await ctx.send("Must be a real word!")
                    else:
                        await original_message.reply(f"Word must be **{ROW_SIZE}** letters long!", mention_author=False)

    @commands.command(aliases=["category"])
    async def categories(self, ctx):
        categories = ["General_Knowledge",
                        "Books",
                        "Film",
                        "Music",
                        "Musicals**/**Theatres",
                        "Television",
                        "Video_Games",
                        "Board_Games",
                        "Science**/**Nature",
                        "Computers",
                        "Mathematics",
                        "Mythology",
                        "Sports",
                        "Geography",
                        "History",
                        "Politics",
                        "Art",
                        "Celebrities",
                        "Animals",
                        "Vehicles",
                        "Comics",
                        "Gadgets",
                        "Anime**/**Manga",
                        "Cartoon**/**Animations"]
        text = ""
        for category in categories:
            text += category + "\n"
        embed=discord.Embed(title="Trivia Categories!", description=text, color=0x225c9a)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def joke(self, ctx):
        request = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")
        items = request.json()
        embed = discord.Embed(title="Here's a joke!", description="*" + items["joke"] + "*", color=0x225c9a)
        embed.set_footer(text="Joke Category: " + items["category"])
        await ctx.reply(embed=embed, mention_author=False)

  

    @commands.command()
    async def emojis(self, ctx):
        if ctx.author.id == 448645983748882442:
            emojis = ctx.guild.emojis
            for emoji in emojis:
                letter = str(emoji)[2:3]
                await ctx.send(f"\"{letter}\": \"\<:{emoji.name}:{emoji.id}>\",", mention_author=False)

    # @commands.command(aliases = ["lb"])
    # async def leaderboard(self, ctx):
    #     await open_account(ctx.author)
    #     users = await get_points()
    #     wordle_leaderboard = {}
    #     trivia_leaderboard = {}
    #     for user in users:
    #         wordle_leaderboard[int(user)] = users[user]["wordle"]
    #         trivia_leaderboard[int(user)] = users[user]["trivia"]
    #     wordle_total = sorted(wordle_leaderboard.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    #     trivia_total = sorted(trivia_leaderboard.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    #     embed = discord.Embed(title = f"__Global Leaderboard__", color=0x45d5d5)
    #     print(wordle_total)
    #     print(trivia_total)
    #     wordle_field = ""
    #     trivia_field = ""
    #     for index, user in enumerate(wordle_total):
    #         amt = wordle_leaderboard[user[0]]
    #         member = await self.client.fetch_user(user[0])
    #         wordle_field += f"**{index+1}.** `{member}` - **{amt}** points\n"
    #         if index == 9:
    #             break
    #     for index, user in enumerate(trivia_total):
    #         amt = trivia_leaderboard[user[0]]
    #         member = await self.client.fetch_user(user[0])
    #         trivia_field += f"**{index+1}.** `{member}` - **{amt}** points\n"
    #         if index == 9:
    #             break
    #     embed.add_field(name="Wordle Leaderboard", value=wordle_field)
    #     embed.add_field(name="Trivia Leaderboard", value=trivia_field)
    #     points = await update_points(ctx.author, 0, "wordle")
    #     embed.set_footer(text=f"Your wordle points: {points[0]}\nYour trivia points: {points[1]}")
    #     await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def points(self, ctx):
        await open_account(ctx.author)
        points = await update_points(ctx.author, 0)
        embed=discord.Embed(title=f"`{ctx.author}`'s Points", description=f"Wordle points: **{points[0]}**\nTrivia points: **{points[1]}**")
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Fun(client))

async def open_account(user):
    users = await get_points()
    if str(user.id) in users:
        users[str(user.id)]["name"] = user.name
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["name"] = user.name
        users[str(user.id)]["wordle"] = 0
        users[str(user.id)]["trivia"] = 0
    with open(pointsPath,"w") as f:
        json.dump(users,f)
    return True
async def get_points():
    with open(pointsPath,"r") as f:
        users = json.load(f)
    return users
async def update_points(user,change = 0,mode = "wordle"):
    users = await get_points()
    users[str(user.id)][mode] += change
    with open(pointsPath,"w") as f:
        json.dump(users,f)
    total = [users[str(user.id)]["wordle"],users[str(user.id)]["trivia"]]
    return total