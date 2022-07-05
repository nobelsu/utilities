import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import asyncio
import time

intents = discord.Intents(messages=True, guilds=True, members=True)

prefixs = '?'
bot = commands.Bot(command_prefix=prefixs, intents=intents)


@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}!")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="for empty servers!"))


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if f"<@!{bot.user.id}>" in ctx.content:
        global prefixs
        embed = discord.Embed(title=f"My current prefix is `{prefixs}`",
                              color=0x1597BB)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

@bot.command()
async def prefix(ctx, arg1=None):
    global prefixs
    embed20 = discord.Embed(title="You must be the owner to use this command!",
                            color=0x1597BB)
    embed20.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed20.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)
    embed = discord.Embed(title=f"My current prefix is `{prefixs}`",
                          color=0x1597BB)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

    if arg1 == None:
        await ctx.channel.send(embed=embed)
    else:
        prefixs = arg1
        embed2 = discord.Embed(title=f"My prefix has been set to `{prefixs}`",
                               color=0x1597BB)
        embed2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed2)
        bot.command_prefix = prefixs


@bot.command()
async def setup(ctx):
    #main embeds
    embed = discord.Embed(
        title=f"Hi,  {ctx.author.display_name}",
        description="How many **categories** would you like to create?",
        colour=0x1597BB)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(
        name="Requirements",
        value=
        "1. Select a number between `0 and 50`\n2. The number should be sent in `numerals`",
        inline=True)

    embed2 = discord.Embed(title=f"You must be the owner to use this command!",
                           color=0x1597BB)
    embed2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed2.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed3 = discord.Embed(title=f"Sorry, you didn't reply in time!",
                           colour=0x1597BB)
    embed3.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed3.add_field(name="Please respond within `30 seconds`.",
                     value="The process has been `terminated`.",
                     inline=True)

    embed5 = discord.Embed(
        title=
        "Your category name is too long! It must be less than `100 characters` long!",
        colour=0x1597BB)
    embed5.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed5.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed6 = discord.Embed(
        title="I told you! I don't like the blank character :rofl:",
        colour=0x1597BB)
    embed6.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed6.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed8 = discord.Embed(title="Please input a valid integer!",
                           colour=0x1597BB)
    embed8.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed8.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed9 = discord.Embed(
        title=
        "That's too many categories! The maximum number of categories is `50`!",
        colour=0x1597BB)
    embed9.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed9.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed10 = discord.Embed(title="You have more than `500` channels!",
                            colour=0x1597BB)
    embed10.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed10.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    embed14 = discord.Embed(
        title=
        "Your channel name is too long! It must be less than `100 characters` long!",
        colour=0x1597BB)
    embed14.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed14.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    embed15 = discord.Embed(
        title=f"Hi,  {ctx.author.display_name}",
        description="Are you sure you want to remake your server?",
        colour=0x1597BB)
    embed15.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed15.add_field(
        name="Requirements",
        value="1. Respond with `y` for Yes\n2. Respond with `n` for No",
        inline=True)

    embed16 = discord.Embed(title="You cancelled the process!",
                            colour=0x1597BB)
    embed16.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed16.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    embed17 = discord.Embed(title="Please input `y` or `n`!", colour=0x1597BB)
    embed17.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed17.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    if ctx.author.id != "":
        await ctx.channel.send(embed=embed2)
        return
    else:
        categories = []
        channels = {}
        categid = {}
        vchannels = {}

        await ctx.channel.send(embed=embed)

        def check(msg):
            return (msg.author == ctx.author) and (msg.channel == ctx.channel)

        try:
            msgc = await bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=embed3)
            return
        msgd = msgc.content
        print(msgd.isdigit())
        if msgd.isdigit() == False:
            await ctx.channel.send(embed=embed8)
            return

        if int(msgd) <= 0:
            await ctx.channel.send(embed=embed8)
            return

        if int(msgd) > 50:
            await ctx.channel.send(embed=embed9)
            return

        for l in range(int(msgd)):
            embed4 = discord.Embed(
                title=f"Please input the name of Category {l + 1}!",
                colour=0x1597BB)
            embed4.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed4.add_field(
                name="Requirements",
                value=
                "1. The number of characters in the name of the category must be between `0 and 100`\n2. Do not try to use the blank space character :joy:",
                inline=True)

            await ctx.channel.send(embed=embed4)
            try:
                category1 = await bot.wait_for("message",
                                               check=check,
                                               timeout=30)
            except asyncio.TimeoutError:
                await ctx.channel.send(embed=embed3)
                return

            category = category1.content
            if len(category) >= 100:
                await ctx.channel.send(embed=embed5)
                return

            for character in category:
                print(ord(character))
                if ord(character) == 12644:
                    await ctx.channel.send(embed=embed6)
                    return

            categories.append(category)
            channels[category] = []
            vchannels[category] = []
            categid[category] = category1
        channelsumm = 0
        for tcategory in categories:
            embed7 = discord.Embed(
                title=
                f"Please input the numer of text channels you would like to create in {tcategory}!",
                colour=0x1597BB)
            embed7.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed7.add_field(
                name="Requirements",
                value="1. The total number of channels must be less than `500`."
            )
            await ctx.channel.send(embed=embed7)
            try:
                channelno1 = await bot.wait_for("message",
                                                check=check,
                                                timeout=30)
            except asyncio.TimeoutError:
                await ctx.channel.send(embed=embed3)
                return
            channelno = channelno1.content
            if channelno.isnumeric() == False:
                await ctx.channel.send(embed=embed8)
                return

            channelsumm += int(channelno)

            if channelsumm > 500:
                await ctx.channel.send(embed=embed10)
                return

            for s in range(int(channelno)):
                embed11 = discord.Embed(
                    title=
                    f"Please input the name of Text Channel {s + 1} in {tcategory}!",
                    colour=0x1597BB)
                embed11.set_author(name=ctx.author,
                                   icon_url=ctx.author.avatar_url)
                embed11.add_field(
                    name="Requirements",
                    value=
                    "1. The number of characters in the name of the channel must be between `0 and 100`\n2. Do not try to use the blank space character :joy:"
                )

                await ctx.channel.send(embed=embed11)
                try:
                    channelname = await bot.wait_for("message",
                                                     check=check,
                                                     timeout=30)
                except asyncio.TimeoutError:
                    await ctx.channel.send(embed=embed3)
                    return
                if len(channelname.content) >= 100:
                    await ctx.channel.send(embed=embed14)
                    return
                for characters in channelname.content:
                    if ord(characters) == 12644:
                        await ctx.channel.send(embed=embed6)
                        return
                channels[tcategory].append(channelname.content)

        for xcategory in categories:
            embed12 = discord.Embed(
                title=
                f"Please input the numer of voice channels you would like to create in {xcategory}!",
                colour=0x1597BB)
            embed12.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed12.add_field(
                name="Requirements",
                value="1. The total number of channels must be less than `500`."
            )
            await ctx.channel.send(embed=embed12)
            try:
                channelno2 = await bot.wait_for("message",
                                                check=check,
                                                timeout=30)
            except asyncio.TimeoutError:
                await ctx.channel.send(embed=embed3)
                return
            channelno3 = channelno2.content
            if channelno3.isnumeric() == False:
                await ctx.channel.send(embed=embed8)
                return

            channelsumm += int(channelno3)

            if channelsumm > 500:
                await ctx.channel.send(embed=embed10)
                return

            for g in range(int(channelno3)):
                embed13 = discord.Embed(
                    title=
                    f"Please input the name of Voice Channel {g+ 1} in {tcategory}!",
                    colour=0x1597BB)
                embed13.set_author(name=ctx.author,
                                   icon_url=ctx.author.avatar_url)
                embed13.add_field(
                    name="Requirements",
                    value=
                    "1. The number of characters in the name of the channel must be between `0 and 100`\n2. Do not try to use the blank space character :joy:"
                )
                await ctx.channel.send(embed=embed13)
                try:
                    vchannelname = await bot.wait_for("message",
                                                      check=check,
                                                      timeout=30)
                except asyncio.TimeoutError:
                    await ctx.channel.send(embed=embed3)
                    return
                if len(vchannelname.content) >= 100:
                    await ctx.channel.send(embed=embed14)
                    return
                for characters in vchannelname.content:
                    if ord(characters) == 12644:
                        await ctx.channel.send(embed=embed6)
                        return
                vchannels[xcategory].append(vchannelname.content)

        await ctx.channel.send(embed=embed15)

        try:
            response1 = await bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=embed3)
            return
        response = response1.content.lower()
        if response not in ["y", "n"]:
            await ctx.channel.send(embed=embed17)
            return
        elif response == "y":
            for channel in ctx.guild.channels:
                await channel.delete()
            for categoryn in categories:
                await ctx.guild.create_category(categoryn)
                category11 = discord.utils.get(ctx.guild.categories,
                                               name=categoryn)
                for catechannel in channels[categoryn]:
                    await ctx.guild.create_text_channel(f"{catechannel}",
                                                        category=category11)

                for vochannel in vchannels[categoryn]:
                    await ctx.guild.create_voice_channel(f"{vochannel}",
                                                         category=category11)
        else:
            await ctx.channel.send(embed=embed16)
            return


@bot.command()
async def txtsetup(ctx, arg1=None):
    embed20 = discord.Embed(
        title=f"You must be the owner to use this command!", color=0x1597BB)
    embed20.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed20.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    if ctx.author.id != "":
        await ctx.channel.send(embed=embed20)
        return

    embed15 = discord.Embed(
        title=f"Hi,  {ctx.author.display_name}",
        description="Are you sure you want to remake your server?",
        colour=0x1597BB)
    embed15.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed15.add_field(
        name="Requirements",
        value="1. Respond with `y` for Yes\n2. Respond with `n` for No",
        inline=True)

    embed3 = discord.Embed(title=f"Sorry, you didn't reply in time!",
                           colour=0x1597BB)
    embed3.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed3.add_field(name="Please respond within `30 seconds`.",
                     value="The process has been `terminated`.",
                     inline=True)

    embed16 = discord.Embed(title="You cancelled the process!",
                            colour=0x1597BB)
    embed16.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed16.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    embed17 = discord.Embed(title="Please input `y` or `n`!", colour=0x1597BB)
    embed17.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed17.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    embed1 = discord.Embed(title="Please check your .txt file!",
                           colour=0x1597BB)
    embed1.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed1.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed18 = discord.Embed(title="Usage: ;txtsetup [separator]",
                            colour=0x1597BB)
    embed18.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed18.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    embed = discord.Embed(title="Please send a .txt file in this channel.",
                          colour=0x1597BB)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(
        name="Requirements",
        value=
        "1. You must have less than `50` categories and `500` channels\n2. The number of characters in the name of your channels and category must be less than `100`\n3. Don't use the blank space :rotl:",
        inline=True)

    if arg1 == None:
        await ctx.channel.send(embed=embed18)
        return

    def check(msg):
        return (msg.author == ctx.author) and (msg.channel == ctx.channel)

    await ctx.channel.send(embed=embed)
    try:
        message = await bot.wait_for("message", check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.channel.send(embed=embed3)
        return
    try:
        if str(message.attachments) == "[]":
            return
        else:
            split_v1 = str(message.attachments).split("filename='")[1]
            filename = str(split_v1).split("' ")[0]
            print(filename)
            if filename.endswith(".txt"):
                await message.attachments[0].save(
                    fp="Files/{}".format(filename))
                os.rename(f"Files/{filename}", f"Files/{ctx.guild.id}.txt")
            else:
                await ctx.channel.send(embed=embed1)
                return

        with open(f'Files/{ctx.guild.id}.txt', 'r+') as file:
            categories = []
            channels = {}
            stop = True
            line1 = file.readline().strip()
            sep = str(arg1)
            checking = line1.split(" " + sep + " ")
            if checking != ["Category", "Text Channels", "Voice Channels"]:
                raise Exception("The file doesn't have correct titles")
            while stop:
                newline = file.readline().strip()
                if newline == "":
                    stop = False
                    break
                toadd = newline.split(sep)
                categories.append(toadd[0])
                channels[toadd[0]] = {
                    "TC": toadd[1].split(","),
                    "VC": toadd[2].split(",")
                }
        file.close()
        os.remove(f"Files/{ctx.guild.id}.txt")
        print(categories)
        print(channels)
        await ctx.channel.send(embed=embed15)
        try:
            response1 = await bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=embed3)
            return
        response = response1.content
        if response not in ["y", "n"]:
            await ctx.channel.send(embed=embed17)
            return
        elif response == "y":
            for channel in ctx.guild.channels:
                await channel.delete()
            for categoryn in categories:
                cat = await ctx.guild.create_category(categoryn)
                for catechannel in channels[categoryn]["TC"]:
                    if catechannel.strip() != "":
                        await ctx.guild.create_text_channel(f"{catechannel}",
                                                            category=cat)
                for vchannel in channels[categoryn]["VC"]:
                    if vchannel.strip() != "":
                        await ctx.guild.create_voice_channel(f"{vchannel}",
                                                             category=cat)
            return
        else:
            await ctx.channel.send(embed=embed16)
            return
    except:
        await ctx.channel.send(embed=embed1)
        return


@bot.command()
async def roles(ctx):
    embed20 = discord.Embed(
        title=f"You must be the owner to use this command!", color=0x1597BB)
    embed20.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed20.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    if ctx.author.id != "":
        await ctx.channel.send(embed=embed20)
        return

    def check(msg):
        return (msg.author == ctx.author) and (msg.channel == ctx.channel)

    embed = discord.Embed(
        title=f"Hi,  {ctx.author.display_name}",
        description="How many **roles** would you like to create?",
        colour=0x1597BB)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(
        name="Requirements",
        value=
        "1. Select a number between `0 and 250`\n2. The number should be sent in `numerals`",
        inline=True)

    embed2 = discord.Embed(title="Are you sure you want to add these roles?",
                           colour=0x1597BB)
    embed2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed2.add_field(
        name="Requirements",
        value="1. Respond with `y` for Yes\n2. Respond with `n` for No",
        inline=True)

    embed3 = discord.Embed(
        title=
        "Are you sure you want to add these roles and remove previous roles?",
        colour=0x1597BB)
    embed3.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed3.add_field(
        name="Requirements",
        value="1. Respond with `y` for Yes\n2. Respond with `n` for No",
        inline=True)

    embed4 = discord.Embed(title=f"Sorry, you didn't reply in time!",
                           colour=0x1597BB)
    embed4.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed4.add_field(name="Please respond within `30 seconds`.",
                     value="The process has been `terminated`.",
                     inline=True)

    embed5 = discord.Embed(title="Please input a valid integer!",
                           colour=0x1597BB)
    embed5.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed5.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed6 = discord.Embed(
        title="That's too little roles! The minimum number of roles is `1`!",
        colour=0x1597BB)
    embed6.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed6.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed7 = discord.Embed(
        title="That's too many roles! The maximum number of roles is `250`!",
        colour=0x1597BB)
    embed7.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed7.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed8 = discord.Embed(
        title="I told you! I don't like the blank character :rofl:",
        colour=0x1597BB)
    embed8.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed8.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed9 = discord.Embed(
        title=
        "Your role name is too long! It must be less than `40 characters` long!",
        colour=0x1597BB)
    embed9.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed9.add_field(name="An error occured",
                     value="The process has been `terminated`.",
                     inline=True)

    embed10 = discord.Embed(
        title="Would you like to remove previous roles as well?",
        colour=0x1597BB)
    embed10.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed10.add_field(
        name="Requirements",
        value="1. Respond with `y` for Yes\n2. Respond with `n` for No",
        inline=True)

    embed11 = discord.Embed(title="Please input `y` or `n`!", colour=0x1597BB)
    embed11.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed11.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    embed12 = discord.Embed(title="Roles created!", colour=0x1597BB)
    embed12.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed12.add_field(name="Success",
                      value="All roles have been created.",
                      inline=True)
    embed13 = discord.Embed(title="You cancelled the process!",
                            colour=0x1597BB)
    embed13.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed13.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)

    await ctx.channel.send(embed=embed)

    try:
        response1 = await bot.wait_for("message", check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.channel.send(embed=embed4)
        return
    response = response1.content

    if response.isnumeric() == False:
        await ctx.channel.send(embed=embed5)
        return

    if int(response) <= 0:
        await ctx.channel.send(embed=embed6)
        return

    if int(response) > 250:
        await ctx.channel.send(embed=embed6)
        return

    rolelist = []
    response = int(response)

    for x in range(response):
        embed8 = discord.Embed(title=f"Please input the name of Role {x + 1}",
                               colour=0x1597BB)
        embed8.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed8.add_field(
            name="Requirements",
            value=
            "1. The number of characters in the name of the role must be between `0 and 40`\n2. Do not try to use the blank space character :joy:",
            inline=True)

        await ctx.channel.send(embed=embed8)
        try:
            rname = await bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=embed4)
            return

        role = rname.content

        if len(role) > 40:
            await ctx.channel.send(embed=embed9)
            return

        for characters in role:
            if ord(characters) == 12644:
                await ctx.channel.send(embed=embed8)
                return

        rolelist.append(role)

    await ctx.channel.send(embed=embed10)
    try:
        response1 = await bot.wait_for("message", check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.channel.send(embed=embed4)
        return
    response = response1.content
    if response not in ["y", "n"]:
        await ctx.channel.send(embed=embed11)
        return
    elif response == "y":
        await ctx.channel.send(embed=embed3)
        try:
            response1 = await bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=embed4)
            return
        response = response1.content
        if response not in ["y", "n"]:
            await ctx.channel.send(embed=embed11)
            return
        elif response == "y":
            for rolename in ctx.guild.roles:
                role_object = discord.utils.get(ctx.message.guild.roles,
                                                name=rolename)
                await role_object.delete()
            for roleno in rolelist:
                await ctx.guild.create_role(name=roleno)

            await ctx.channel.send(embed=embed12)
            return
        else:
            await ctx.channel.send(embed=embed13)
    else:
        await ctx.channel.send(embed=embed2)
        try:
            response1 = await bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.channel.send(embed=embed4)
            return
        response = response1.content
        if response not in ["y", "n"]:
            await ctx.channel.send(embed=embed11)
            return
        elif response == "y":
            for roleno in rolelist:
                await ctx.guild.create_role(name=roleno)
            await ctx.channel.send(embed=embed12)
            return
        else:
            await ctx.channel.send(embed=embed13)


@bot.command()
@has_permissions(administrator=True)
async def clear(ctx, arg1=None):
    global prefixs
    embed20 = discord.Embed(title=f"You have deleted {arg1} messages!",
                            color=0x1597BB)
    embed20.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed21 = discord.Embed(title=f"Usage: {prefixs}clear `integer`",
                            color=0x1597BB)
    embed21.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed21.add_field(name="An error occured",
                      value="The process has been `terminated`.",
                      inline=True)
    try:
        if arg1 == None or int(arg1) == 0:
            await ctx.channel.send(embed=embed21)
            return
        await ctx.channel.purge(limit=int(arg1) + 1)
        message = await ctx.channel.send(embed=embed20)
        time.sleep(3)
        await message.delete()
    except:
        await ctx.channel.send(embed=embed21)


@clear.error
async def clearerror(ctx, error):
    if isinstance(error, CheckFailure):
        embed21 = discord.Embed(
            title=f"You must be an admin to use this command!", color=0x1597BB)
        embed21.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed21.add_field(name="An error occured",
                          value="The process has been `terminated`.",
                          inline=True)
        await ctx.channel.send(embed=embed21)
    else:
        return

bot.run(os.getenv('token'))
