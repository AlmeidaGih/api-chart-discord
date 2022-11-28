import discord
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content == "oi":
            await message.channel.send("oiii")

client = discord.Client(intents=discord.Intents.default())

client.run('MTA0Njg2MTEwMTkwNTc1MjEwNQ.Ge9Qsc.-_8ky_m8tQpAlFi2CU5XR5dhxrNHqSHKyHHRUY')