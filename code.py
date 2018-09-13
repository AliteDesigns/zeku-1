import discord
from discord.ext import commands
import random
import asyncio

TOKEN = 'NDg4MjMyNzM1MDY5MDQ0NzU2.Dns8uw.ASrrvH3lIf3gjFsBUcvS6Q5FE-s'

client = commands.Bot(command_prefix='z!')

client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is online and ready to go!')
    await client.change_presence(game=discord.Game(name=f"z!help for help!"))
    
@client.command()
async def youtube():
     embed=discord.Embed(color=0x36393E)
     embed.title = '**__aQuiVeRs Youtube channel!__**'
     embed.url = 'http://youtube.com/aquiveraq'
     await client.say(embed=embed)
     
@client.command()
async def invite():
    embed=discord.Embed(color=0x36393E)
    embed.title = 'Invite Zeku to your server!'
    embed.url = 'https://discordapp.com/oauth2/authorize?client_id=488232735069044756&scope=bot&permissions=2146958847'
    await client.say(embed=embed)

@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please specify a user you want me to avatar!', inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name='Bam!', value='**{}s** avatar'.format(user.name), inline=True)
        embed.set_image(url=user.avatar_url)
        await client.say(embed=embed)

@client.command()
async def greet():
     embed=discord.Embed(color=0x36393E)
     embed.title = 'Hello! :wave:'
     await client.say(embed=embed)

@client.command()
async def help():
     embed=discord.Embed(color=0x36393E)
     embed.title = '**Commands Terminal**'
     embed.add_field(name='help1', value='Moderation commands', inline=False)
     embed.add_field(name='help2', value='Fun commands', inline=False)
     embed.add_field(name='help3', value='Bot features', inline=False)
     embed.add_field(name='help4', value='Other commands', inline=False)

     await client.say(embed=embed)
     
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content.upper() == "kdslkfjskldjlsjkdfjkd":
        await client.send_message(message.author, "Interesting")
    elif 'fuck' in message.content.lower():
        await client.send_message(message.author, "Please dont say any bad languages, thank you.")
        await client.delete_message(message)
    if message.content.upper() == "kdslkfjskldjlsjkdfjkd":
        await client.send_message(message.author, "Interesting")
    elif 'shit' in message.content.lower():
        await client.send_message(message.author, "Please dont say any bad languages, thank you.")
        await client.delete_message(message)
    if message.content.upper() == "kdslkfjskldjlsjkdfjkd":
        await client.send_message(message.author, "Interesting")
    elif 'sht' in message.content.lower():
        await client.send_message(message.author, "Please dont say any bad languages, thank you.")
        await client.delete_message(message)
    if message.content.upper() == "kdslkfjskldjlsjkdfjkd":
        await client.send_message(message.author, "Interesting")
    elif 'fck' in message.content.lower():
        await client.send_message(message.author, "Please dont say any bad languages, thank you.")
        await client.delete_message(message)

@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please specify a user you want me to slap!', inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name='Oof!', value='**{}** got slapped! :raised_back_of_hand: '.format(user.name), inline=True)
        embed.set_image(url='https://cdn.discordapp.com/attachments/488233832315617283/489204828199714817/Screenshot_2018-09-12_at_07.43.00.png')
        await client.say(embed=embed)

@client.command()
async def server():
    embed=discord.Embed(color=0x36393E)
    embed.title = '**Join Zeku Discord server here!**'
    embed.url = 'https://discord.gg/PCESZQ6'
    await client.say(embed=embed)

@client.command()
async def updatelogs():
     embed=discord.Embed(color=0x36393E)
     embed.title = '**Update logs**'
     embed.add_field(name='2018.9.9', value='Started making the bot', inline=False)
     embed.add_field(name='2018.9.10', value='Setted up the bot', inline=False)
     embed.add_field(name='2018.9.11', value='Added some commands. Slap, Server and clear', inline=False)
     embed.add_field(name='2018.9.12', value='Added a command, info, autorole system, new ping / botinfo display. Also new help display, and some moderation commands.', inline=False)
     await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await client.say("**The username is:** `{}`".format(user.name))
    await client.say("**The user ID is:** `{}`".format(user.id))
    await client.say("**The user status is:** `{}`".format(user.status))
    await client.say("**The users highest role is:** `{}`".format(user.top_role))
    await client.say("**The user joined at:** `{}`".format(user.joined_at))

@client.command()
async def botinfo():
    embed = discord.Embed(
        title = '**Bot info**',
        description = 'The bot was made by aQuiVeR using Python. The bot can mainly do auto roles, slapping, chat filters and more!',
        color = discord.Color.blue()
    )

    embed.set_footer(text='Note: If you like the bot, please invite Zeku by typing "z!invite"!')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/489241752557846528/489358705259708426/ZEKU2.png')
    embed.add_field(name='**Credits**', value='Thanks to SaVaGe;_; for helping me make the bot.', inline=False)

    await client.say(embed=embed)

@client.command()
async def ping():
    embed = discord.Embed(
        description = ':ping_pong: **Pong!**',
        color = discord.Color.blue()
    )

    await client.say(embed=embed)
 
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Members')
    await client.add_roles(member, role)

@client.command(pass_context=True)
async def kick(ctx, user: discord.User):
    if ctx.message.author.server_permissions.kick_members:
        await client.kick(user)
        await client.say ('**Kicked the user successfully** :white_check_mark:')
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You dont have permmision to do that!', inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ban(ctx, user: discord.User):
    if ctx.message.author.server_permissions.kick_members:
        await client.ban(user)
        await client.say ('**Banned the user successfully** :white_check_mark:')
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You dont have permmision to do that!', inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    if ctx.message.author.server_permissions.manage_messages:
        channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

@client.command()
async def help1():
    embed = discord.Embed(
        description = '**Moderation commands:** kick | ban | clear',
        color = discord.Color.blue()
    )

    await client.say(embed=embed)

@client.command()
async def help2():
    embed = discord.Embed(
        description = '**Fun commands:** slap | avatar',
        color = discord.Color.blue()
    )

    await client.say(embed=embed)

@client.command()
async def help3():
    embed = discord.Embed(
        description = '**Bot features:** Auto role (requires role "Member" in the server) | Chat filter (fck / sht)',
        color = discord.Color.blue()
    )

    await client.say(embed=embed)

@client.command()
async def help4():
    embed = discord.Embed(
        description = '**Other commands:** invite | server | youtube | botinfo | updatelogs | ping',
        color = discord.Color.blue()
    )

@client.command(pass_context=True)
async def mute(ctx, user: discord.User):
    if ctx.message.author.server_permissions.administrator:
        user = ctx.message.author
        role = discord.utils.get(ctx.message.server.roles, name="zekuMuted")
        await client.add_roles(user, role)
        await client.say ('**Muted the user successfully!** :white_check_mark:')
    else:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You dont have permmision to do that! Please check if you have admin permission!', inline=False)
        await client.say(embed=embed)
        
client.run(TOKEN)
