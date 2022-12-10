import discord
import os
from keep_alive import keep_alive
client = discord.client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.cotent == "hi" or message.contest == "hello" or message.contest == "你好":
        await message.channel.send("你好")
client.run("MTA1MDcyNDE4NjQ5MTk5NDE1NA.Ghxv3p.UGmphFET8nTMunE_2yU6iJRstD2hnoSKpUoysY")
