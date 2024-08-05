import streamlit as st
from discord.ext import commands as cmd
import discord as ds
token=st.seceret["TOKEN"]
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
async def hello(ctk):
    ctk.send(f"Hi {ctx.author.mention}")
    st.write("Used /hi func")
bot.run(token)
