import asyncio
import re
import random
import requests
from Barath import barath, MODULE
from pyrogram import filters   
import config
from config import OWNER_ID, HANDLER, BARATH, SOURCE

@barath.on_message(filters.command("cat", prefixes=HANDLER) & filters.me)
async def cat(_, message):
    api = requests.get("https://api.thecatapi.com/v1/images/search").json()
    url = api[0]["url"]
    if url.endswith(".gif"):
        await message.reply_animation(url)
    else:
        await message.reply_photo(url)

@barath.on_message(filters.regex("baka") & filters.me)
async def baka(_, message):
    reply = message.reply_to_message
    api = requests.get("https://nekos.best/api/v2/baka").json()
    url = api["results"][0]['url']
    anime = api["results"][0]["anime_name"]     
    if reply:
        user = reply.from_user
        name = user.first_name
        username = user.username
        user_profile_link = f"https://t.me/{username}" if username else ""
        user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
        await reply.reply_animation(url, caption="**• {}**\n**Baka! {}**".format(anime, user_hyperlink))
    else:
        await message.reply_animation(url, caption="**• {}**\n**Baka!**".format(anime))

@barath.on_message(filters.regex("hug") & filters.me)
async def hug(_, message):
    reply = message.reply_to_message
    api = requests.get("https://nekos.best/api/v2/hug").json()
    url = api["results"][0]['url']
    anime = api["results"][0]["anime_name"]     
    if reply:
        user = reply.from_user
        name = user.first_name
        username = user.username
        user_profile_link = f"https://t.me/{username}" if username else ""
        user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
        await reply.reply_animation(url, caption="**• {}**\n**Hugs! {}**".format(anime, user_hyperlink))
    else:
        await message.reply_animation(url, caption="**• {}**\n**Hugs!**".format(anime))

@barath.on_message(filters.command("in", prefixes=HANDLER) & filters.me)
async def insult(_, message):
    reply = message.reply_to_message
    try:
        insult = requests.get("https://insult.mattbas.org/api/insult").text
        if reply:
            user = reply.from_user
            name = user.first_name
            username = user.username
            user_profile_link = f"https://t.me/{username}" if username else ""
            user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
            string = insult.replace("You are", user_hyperlink)
            await message.reply(string)
        else:
            await message.reply(insult)
    except Exception as e:
        await message.reply(f"Error: {e}")

@barath.on_message(filters.command("ri", prefixes=HANDLER) & filters.me)
async def riddle(_, message):
    riddle = requests.get("https://riddles-api.vercel.app/random").json()
    question = riddle["riddle"]
    answer = riddle["answer"]
    msg = await message.reply(f"**• Riddle**:\n[ `{question}` ]\n\n[ `The Answer will show automatically 20 seconds after tell me your guess's!` ]")
    await asyncio.sleep(20)
    await msg.edit(f"**• Riddle**:\n[ `{question}` ]\n\n• **Answer**: [ `{answer}` ]")

@barath.on_message(filters.command("qu", prefixes=HANDLER) & filters.me)
async def quote(_, m):
    api = random.choice(requests.get("https://type.fit/api/quotes").json())
    string = api["text"]
    author = api["author"]
    await m.reply(
        f"**Quotes**:\n`{string}`\n\n"
        f"   ~ **{author}**")

@barath.on_message(filters.command("gt", prefixes=HANDLER) & filters.me)
async def google_it(_, message):
    file_id = "CAACAgUAAx0CXss_8QABB0iVY2ZDrB4YHzW6u1xRqKLuUX7b6sEAAhUAA-VDzTc4Ts7oOpk4nx4E"
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(sticker=file_id, reply_markup=None)
        await message.reply_to_message.reply_text("🔎 [Google](https://www.google.com/search?)", disable_web_page_preview=True)
    else:
        await message.reply_sticker(sticker=file_id, reply_markup=None)
        await message.reply_text("🔎 [Google](https://www.google.com/search?)", disable_web_page_preview=True)

# <=====================================================================================================>
hack_ani = [
    "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
    "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
    "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",
    "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'",
    "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
    "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
    "`Hacking... 84%\n█████████████████████▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**",
    "`Hacking... 100%\n█████████HACKED███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹Output: Generating.....",
    "`Targeted Account Hacked...\n\nPay 9965566$ To`Or Your GirlFriend Number To  My Master `To Remove this hack..`\n\nTERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked this Account From Telegram Database**\n\n\n🔹**Output:** Successful",
]


@barath.on_message(
    filters.command("hack", prefixes=HANDLER) & filters.me)
async def hack(_, m):
    reply = m.reply_to_message
    if not reply:
        await m.reply_text("ʀᴇᴘʟʏ ᴛᴏ sᴏᴍᴇᴏɴᴇ ʜᴀᴄᴋ!")
        return
    if reply:
        msg = await m.reply_text("ʜᴀᴄᴋ ʙᴇᴇɴ sᴛᴀʀᴛᴇᴅ...")
        for x in range(9):
            await msg.edit_text(hack_ani[x % 9])
            time.sleep(1)
        await msg.edit_text(
                f"**Sᴜᴄᴄᴇssғᴜʟʟʏ ʜᴀᴄᴋᴇᴅ!**\n[{reply.from_user.first_name}](tg://user?id={reply.from_user.id})"
            )



love_ani = [
    "1 ❤️ love story",
    "  😐             😕 \n/👕\         <👗\ \n 👖               /|",
    "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
    "  😚            😒 \n/👕\         <👗> \n  👖             /|",
    "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
    "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
    "  😘   😊 \n /👕\/👗\ \n   👖   /|",
    " 😳  😁 \n /|\ /👙\ \n /     / |",
    "😈    /😰\ \n<|\      👙 \n /🍆    / |",
    "😅 \n/(),✊😮 \n /\         _/\\/|",
    "😎 \n/\\_,__😫 \n  //    //       \\",
    "😖 \n/\\_,💦_😋  \n  //         //        \\",
    "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
]


@barath.on_message(filters.command("love", prefixes=HANDLER) & filters.me)

async def love(_, m):
    msg = await m.reply_text("💑")
    for x in range(13):
        await msg.edit_text(love_ani[x % 13])
        time.sleep(1)
    await msg.edit_text("**ᴛʜᴇ ᴇɴᴅ 😂💔😂**")


__mod_name__ = "FUN"  
    
__help__ = """  
- gt: ggl search
- in: insult someone
- hug: try self
- baka: try self
- cat: rndm cat img
- ri: rndm riddle
- qu: rndm quotes eng
- hack: to hack someone 
- love: love story 
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
