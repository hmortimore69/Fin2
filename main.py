import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client=discord.Client()
noPermissionMessage = "You do not have permission to use this command."

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  prefix = db["prefix"]
  msg = message.content

  if msg.startswith(prefix + "help"):
    helpMenuEmbed = discord.Embed(title="Help Menu", description="Sus Bot Help Menu", color=0xb53636)
    helpMenuEmbed.add_field(name="{}settings".format(prefix), value="Requires the 'Administrator' permission. ", inline=False)
    helpMenuEmbed.add_field(name="{}play [Song]".format(prefix), value="No permission required. (Doesn't work yet)", inline=False)
    helpMenuEmbed.set_footer(text="Built by Harvey#6969. Please note command permissions can be changed in settings.")
    await message.channel.send(embed=helpMenuEmbed)
  
  if msg.startswith(prefix + ""):
    

  if msg.startswith(prefix + "settings"):
    if (message.author.guild_permissions.administrator) == True: 
      print(msg)
      settingsInput = msg.split(' ')
      print(settingsInput)
      if len(settingsInput) >= 2:
        if settingsInput[1].lower() == "prefix":
          if len(settingsInput) >= 3:
            if len(settingsInput[2])>1:
              await message.channel.send("The prefix " + settingsInput[2] + " is too large. Please use a single character for the bot's prefix.")
            else:
              db["prefix"] = settingsInput[2]           
              await message.channel.send("You have successfully changed the prefix to " + db["prefix"])
              prefix = db["prefix"]
          else:
            settingsMenuEmbed = discord.Embed(title="Settings", decsription="Edit the bot's settings.", color=0x2366cc)
            settingsMenuEmbed.add_field(name="{}settings prefix [Value]".format(prefix), value="Change the prefix of the bot.", inline=False)
            await message.channel.send(embed=settingsMenuEmbed)         
        else:
          settingsMenuEmbed = discord.Embed(title="Settings", decsription="Edit the bot's settings.", color=0x2366cc)
          settingsMenuEmbed.add_field(name="{}settings prefix [Value]".format(prefix), value="Change the prefix of the bot.", inline=False)
          await message.channel.send(embed=settingsMenuEmbed)
      else:
        settingsMenuEmbed = discord.Embed(title="Settings", decsription="Edit the bot's settings.", color=0x2366cc)
        settingsMenuEmbed.add_field(name="{}settings prefix [Value]".format(prefix), value="Change the prefix of the bot.", inline=False)
        await message.channel.send(embed=settingsMenuEmbed)
    else:
      await message.channel.send(noPermissionMessage)

keep_alive()
client.run(os.getenv("TOKEN")) 