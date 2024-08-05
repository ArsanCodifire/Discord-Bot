import streamlit as st
from discord.ext import commands as cmd
import discord as ds
import threading
token=st.secrets["TOKEN"]
bot=cmd.Bot(command_prefix="/",intents=ds.Intents.all())
st.set_page_config(
    page_title="Pybot",
    page_icon ="🤖"
)
st.title("Discord Pybot")

@bot.command()
async def hi(ctx):
    await ctx.send(f'Hi {ctx.author.mention}!')
    st.write("Used /hi func")
def run():
    bot.run(token)
@bot.event
def main():
    st.write(f"Logged as {bot.user}")
    bott= threading.Thread(target=run).start() 
if __name__=="__main__":
    main()

