import discord
from discord.ext import commands as cmd
import streamlit as st
token=st.secrets["TOKEN"]
bot=cmd.Bot(command_prefix="/",intents=ds.Intents.all())
st.set_page_config(
    page_title="Pybot",
    page_icon ="🤖"
)
st.title("Discord Pybot")
@bot.event
async def on_ready():
    st.write(f'Logged in as {bot.user}')

@bot.command()
async def hi(ctx):
    st.write("Used /hi func")
    await ctx.send(f'Hi {ctx.author.mention}!')

bot.run(token)


