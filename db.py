import discord as ds
from discord.ext import commands as cmd
import streamlit as st
import multiprocessing

# Token setup
token = st.secrets["TOKEN"]
bot = cmd.Bot(command_prefix="/", intents=ds.Intents.all())

# Streamlit page configuration
st.set_page_config(
    page_title="Pybot",
    page_icon="🤖"
)

st.title("Discord Pybot")

# Discord bot events and commands
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')  # Print to console instead of st.write

@bot.command()
async def hi(ctx):
    if ctx.author != bot.user:
        await ctx.send(f'Hi {ctx.author.mention}!')
        print("Used /hi func")  # Print to console instead of st.write

def run_bot():
    bot.run(token)

# Start the bot process
if __name__ == "__main__":
    bot_process = multiprocessing.Process(target=run_bot)
    bot_process.start()

    st.write("Pybot is running.")

