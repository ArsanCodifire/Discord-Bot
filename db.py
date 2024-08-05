import discord
from discord.ext import commands
import streamlit as st
import threading
token=st.secrets["TOKEN"]
bot=cmd.Bot(command_prefix="/",intents=ds.Intents.all())
st.set_page_config(
    page_title="Pybot",
    page_icon ="🤖"
)
st.title("Discord Pybot")
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Hi {ctx.author.mention}!')

def run_bot():
    bot.run(token)

# Streamlit setup
def main():
    st.write("Starting the bot...")
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    st.write("Bot is running. Type /hi in your Discord server to test.")

if __name__ == "__main__":
    main()


