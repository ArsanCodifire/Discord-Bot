import discord as ds
from discord.ext import commands as cmd
import streamlit as st
# Token setup
token = st.secrets["TOKEN"]
bot = cmd.Bot(command_prefix="/", intents=ds.Intents.all())
# Discord bot events and commands
@bot.event
async def on_ready():
    log1=(f'Logged in as {bot.user}')  # Print to console instead of st.write

@bot.command()
async def hi(ctx):
    if ctx.author != bot.user:
        await ctx.send(f'Hi {ctx.author.mention}!')
        log2=("Used /hi func")  # Print to console instead of st.write

# Streamlit interface
async def main():
    log3=("Pybot is running.")
    await run_bot()

# Run the main function using asyncio's event loop
bot.run(token)
    

