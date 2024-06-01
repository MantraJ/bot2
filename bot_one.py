import discord
import time
import random

random_Messages = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ",
 "diowahoirdiowahoirdiowahoirdiowahoirdiowahoirdiowahoirdiowahoirdiowahoirdiowahoir",
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        if message.content == "RUN KRJA EXPERTHWK":
            while True:
                arbitrary = random.randint(0, 2)
                arbitrary_message = random.randint(0,2)
                time.sleep(arbitrary)
                await message.channel.send(random_Messages[arbitrary_message])


client = MyClient()
client.run("NzM1OTAwMDYwMzk0NDU1MDgy.GIO7JB.B-Wu1YUYb__RbIn3Vd_nvlJ2Ja2UuHkhzQwW7g")