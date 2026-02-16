from dotenv import load_dotenv 
import discord
import os
from Output import Output 
import asyncio


load_dotenv()
out = Output()

async def send_message(channel_id, content):
  channel = client.get_channel(channel_id)
  await channel.send(content)

async def main():
  await client.wait_until_ready()

  while True:
      msg = input(">> ")
      await send_message(123456789012345678, msg)


class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.author == self.user:
      return
    guild = message.guild
    if guild:
      response = f"Channels in **{guild.name}**:\n"
      for channel in guild.channels:
        response += f"* **{channel.name}**: `{channel.id}`\n"
      out.outPrint(response)
    else:
      out.outPrint("Could not find the guild context.")

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True
intents.messages = True

client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))