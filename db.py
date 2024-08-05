import streamlit as st
from discord.ext import commands as cmd
import discord as ds
token=st.secrets["TOKEN"]
bot=cmd.Bot(command_prefix="/",intents=ds.Intents.all())
st.set_page_config(
    page_title="Pybot",
    page_icon ="🤖"
)
st.title("Discord Pybot")
@bot.event
async def main():
    st.write(f"Logged as {bot.user}")
@bot.command()
async def hello():
    ctk.send(f"Hi")
    st.write("Used /hi func")
bot.run(token)
