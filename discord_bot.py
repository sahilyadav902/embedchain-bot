import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from embedchain import App

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/embedchain ', intents=intents)

def initialize_chat_bot():
    global chat_bot
    chat_bot = App()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    initialize_chat_bot()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply("Invalid command. Please refer to the documentation for correct syntax.")
    else:
        print("Error occurred during command execution:", error)
        
@bot.command()
async def add(ctx, data_type: str, *, url_or_text: str):
    print(f"User: {ctx.author.name}, Data Type: {data_type}, URL/Text: {url_or_text}")
    try:
        chat_bot.add(data_type, url_or_text)
        await ctx.reply(f"Added {data_type} : {url_or_text}")
        # print(f"Added {data_type} : {url_or_text}")
    except Exception as e:
        await ctx.reply(f"Failed to add {data_type} : {url_or_text}")
        print("Error occurred during 'add' command:", e)

@bot.command()
async def query(ctx, *, question: str):
    print(f"User: {ctx.author.name}, Query: {question}")
    try:
        response = chat_bot.chat(question)
        await ctx.reply(response)
        print("Query answered successfully!")
    except Exception as e:
        await ctx.reply("An error occurred. Please try again!")
        print("Error occurred during 'query' command:", e)

bot.run(os.environ["DISCORD_BOT_TOKEN"])
