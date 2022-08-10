import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(intents=intents, command_prefix='?')
channel = client.get_channel(CHANNEL ID HERE)
guild = client.get_guild(SERVER ID HERE)

@client.command()
async def members(ctx):
    count = 0
    for guild in client.guilds:
        for member in guild.members:
            print(member)
            if "CHARACTERS HERE" in member.name:
                print("banned")
                await ctx.guild.ban(member, reason='YOUR REASON HERE')
                await ctx.channel.send(f'Banned {member.mention} for YOUR REASON. (Members left: {(len(guild.members))})')#
                count = count+1
    await ctx.channel.send(f'I successfully banned {count} accounts for YOUR REASON. The server is now at {(len(guild.members))} members. Awaiting new orders...')

client.run("YOUR TOKEN HERE")
