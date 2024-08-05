import discord as ds
from discord.ext import commands as cmd
import streamlit as st
import threading

token = st.secrets["TOKEN"]
bot = cmd.Bot(command_prefix="/", intents=ds.Intents.all())

st.set_page_config(
    page_title="Pybot",
    page_icon="🤖"
)

st.title("Discord Pybot")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')  # Use print instead of st.write here

@bot.command()
async def hi(ctx):
    if ctx.author != bot.user:
        await ctx.send(f'Hi {ctx.author.mention}!')
        print("Used /hi func")  # Use print instead of st.write here

def run_bot():
    bot.run(token)

# Streamlit setup
if st.button("Start Bot"):
    st.write("Starting the bot...")
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

st.write("Bot is running. Type /hi in your Discord server to test.")
