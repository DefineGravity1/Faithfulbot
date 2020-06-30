import discord
from discord.ext import commands
import asyncio
import os
import json
# import youtube_dl
from discord.utils import get
# def get_prefix(bot, message):
#     if not message.guild:
#         return commands.when_mentioned_or(".")(bot,message)
#
#     with open("prefixes.json", 'r') as f:
#         prefixes = json.load(f)
#1
#     if str(messange.guild.id) not in prefixes:
#         return commands.when_mentioned_or(".")(bot,message)
#
#     prefix = prefixs[str(message.guild.id)]
#     return commands.when_mentioned_or(prefix)(bot,message)
#
# @command.command()
# async def prefix(ctx, *, pre):
#     with open(r"C:\bot\prefixs.json", 'r') as f:
#         prefixs = json.load(f)
#
#     prefixes[str(ctx.guild.id)] = pre
#     await ctx.send(f"new prefix is {pre}")
#
#     with open(r"C:\bot\prefixs.json", 'w') as f:
#         json.dump(prefixes, f, idnet=4)

bot = commands.Bot(command_prefix= '.')
bot.remove_command('help')



TOKEN = 'NzA0NDY4NTkxOTE5MTA0MDUx.XqdmBw.lD9Xai4eRQviCZmlN90oJcB0C84'

# @bot.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(bot))



@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
 
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


# @bot.command()
# async def apply(ctx):
#     embed = discord.Embed(
#         title = 'VatalityPvP Staff Application',
#         description = ('Currently we are a team of two (2) Staff Members, DefineGravity and Shoe who review all applications. Once we have reviewed your application, you will receive a private message from one of us letting you know the outcome of your application.'),
#         colour = discord.Colour.blue()
#     )
#
#     embed.set_image(url='https://cdn.discordapp.com/attachments/704502238986371174/704561755149565962/56423df94032f_thumb900.jpg')
#     embed.set_author(name='Apply now')
#     embed.add_field(name="Fill out an application here: [Click here](https://forms.gle/hRypAffCMJLvxNL19)", value='Apply Now', inline=False)
#
#     await ctx.send(embed=embed)

# @bot.command()
# async def purge(ctx, amount=5):
#     if amount <= 0:
#         embed = discord.Embed(
#             title = 'The amount needs to be over 0',
#             colour = discord.Colour.blue()
#         )
#         await ctx.send(embed=embed, delete_after=3)
#     else:
#         await ctx.channel.purge(limit=amount+1)
#         embed = discord.Embed(
#             title = f'{amount} messages purged',
#             colour = discord.Colour.blue()
#         )
#         await ctx.send(embed=embed, delete_after=3)
#

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
                welcome = discord.Embed(
                    title = 'INFORMATION',
                    color = discord.Colour.blue()
                )
                welcome.set_thumbnail(url='{}'.format(member.avatar_url))
                welcome.set_author(name=f'Welcome {member.display_name} to the VatalityPvP discord!',
                icon_url='{}'.format(member.avatar_url)),
                welcome.add_field(name=f'<:credit_card:721564764173762681> Store', value='https://buy.vatalitypvp.us/', inline=False)
                welcome.add_field(name='<:desktop:721566145215201390> Forums', value='https://www.vatalitypvp.us/', inline=False)
                welcome.add_field(name='<:video_game:721566125078478889> Ip', value='play.vatalitypvp.us', inline=False)
                await channel.send(embed=welcome)

@bot.command()
async def test(ctx, member : discord.Member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":
                welcome = discord.Embed(
                    description = f'{member.mention}Welcome to the VatalityPvP discord',
                    color = discord.Colour.blue()
                )
                welcome.set_thumbnail(url='{}'.format(member.avatar_url))
                welcome.set_author(name='VatalityPvP',
                icon_url='https://cdn.discordapp.com/attachments/277273483464146944/720388231568556084/server-icon.png'),
                welcome.add_field(name='Store', value='[Click here](https://buy.vatalitypvp.us/)', inline=False)
                welcome.add_field(name='Forums', value='[Click here](https://buy.vatalitypvp.us/)', inline=False)
                welcome.add_field(name='Ip', value='play.vatalitypvp.us', inline=False)
                await channel.send(embed=welcome)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have the Permission for that!")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This is not a command, check the spelling.")


# @bot.event
# async def on_reaction_add(reaction, user):
#     for channel in member.guild.channels:
#         if str(channel) == "tickets":




@bot.command()
async def help(ctx):
    # emoji = get(ctx.message.server.emojis, name="joy")
    help = discord.Embed(
        title = f'Help menu',
        description = 'Type .help [category]',
        colour = discord.Colour.blue()
    )
    await ctx.send(embed=help)


def setup(bot):
    bot.add_cog(help(bot))


















# @bot.command()
# async def matthew(ctx):
#     embed = discord.Embed(
#         title = 'Help menu',
#         description = ('Type .help [category]'),
#         colour = discord.Colour.blue()
#     )
#
#
#
#     embed.add_field(name="<:emoji1:704936882126979122>", value="<:emoji1:704936882126979122>", inline=False)
#
#     await ctx.send(embed=embed)
#
#
# def setup(bot):
#     bot.add_cog(Apply(bot))
    # help = discord.Embed(
    #     title = f'Help menu',
    #     description = 'Type .help [category]',
    #     colour = discord.Colour.blue()
    # )
    #
    # # help.add_field(name=f"<:emoji1:704936882126979122>")
    #
    #













# @bot.command()
# async def prefix(ctx, prefix):
#
#     if prefix == :
#         embed = discord.Embed(
#             title = f'The servers prefix is {globalprefix}',
#             colour = discord.Colour.blue()
#         )
#         await ctx.send(embed=embed)
#         pass
#     else:
#         globalprefix = prefix

# @bot.command()
# async def setprefix(ctx, prefix):
#     prefix == globalprefix
#     embed = discord.Embed(
#         title = f'The new server prefix is {globalprefix}',
#         colour = discord.Colour.blue()
#     )
#     await ctx.send(embed=embed)
#
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(TOKEN)
