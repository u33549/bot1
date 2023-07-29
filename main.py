import discord
import discord.ext.commands
from discord.ext import commands
from discord.ext.commands import Bot
import time
import calcFuncs as cf

TOKEN = "MTEzMTY0NjYyODU5MjM1MzI5Mg.GJF-zI.37q6Dt6tV4ROWoopBgnEOGjdpERpNrc_pYXNG0"

bot = Bot(command_prefix=".",intents=discord.Intents.all())


@bot.event
async def on_ready():
    text="Noluyo lan he anasını satıyım"
    print(text)




@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, arg):
    print("siliyorum")
    print(arg)
    await ctx.channel.purge(limit=int(arg))

@bot.event
async def on_reaction_add(reaction, user):
    if user==bot.user:
        return
    channel = reaction.message.channel
    emoji = reaction.emoji
    message = reaction.message
    content = message.content
    user_id = message.author.id

    if(emoji=="🔃"):
        tag = f"<@{user_id}>"
        trMsg = cf.translate_text(content, message.author.roles,user.roles)

        if trMsg == "33549#translateCode#same":
            return
        elif trMsg == "33549#translateCode#uhnr":
            await channel.send(f"{tag} you are not have a lang role for translation ")
            return

        await message.reply(f"{tag} said: {trMsg} ")

        return
    await bot.process_commands(reaction, user)


@bot.event
async def on_message(message):
    msg=message.content.lower()
    tag=f"<@{message.author.id}>"
    if message.author == bot.user:
        return
    if cf.isInText(msg,"neden"):
        await message.channel.send(f"{tag} KAPLUMBAĞA DEDEN")
        time.sleep(0.2)
        await message.channel.send("HAHAHAHAHAHAHA")

    elif cf.isInText(msg,"anan"):
        await message.channel.send(f"{tag} baban")

    elif cf.isInText(msg,"hııı"):
        await message.channel.send(f"{tag} hıı dedin yarramı yedin")

    elif cf.isInText(msg,"cu"):
        await message.channel.send(f"{tag} ANANIN AMCUUU")

    elif cf.isInText(msg,"mıyala"):
        await message.channel.send(f"{tag} yarramı yala")
    else:
        emoji = "🔃"

        try:
            await message.add_reaction(emoji)
        except discord.Forbidden:
            print("Bot, mesaja tepki eklemeye izin vermiyor.")

    await bot.process_commands(message)

bot.run(TOKEN)
