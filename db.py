import discord as ds
from discord.ext import commands as cmd
import streamlit as st
import asyncio

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
        st.write("Used /hi func")  # Print to console instead of st.write

# Function to run the bot using asyncio
async def run_bot():
    await bot.start(token)

# Streamlit interface
async def main():
    st.write("Pybot is running.")
    await run_bot()

# Run the main function using asyncio's event loop
if __name__ == "__main__":
    asyncio.run(main())
    

