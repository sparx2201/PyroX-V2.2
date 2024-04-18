import config 
import requests

from Barath import barath 
from Barath import MODULE, bot, INFO as GET_INFO
from Barath.helpers.help_func import spacebin
from pyrogram import filters
from Barath.plugins.alive import alive
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto,
)
from itertools import zip_longest

@bot.on_inline_query(filters.regex("help"))
async def help_cmds(_, inline_query):
    user_id = (await GET_INFO.barath()).id
    if not inline_query.from_user.id == user_id:
        return

    buttons = [
        [InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")]
        for x in MODULE
    ]

    # Check if buttons list is empty
    if not buttons:
        await inline_query.answer(text="No help available at the moment.")
        return

    num_buttons_per_column = (len(buttons) + 1) // 2
    buttons_column1, buttons_column2 = zip_longest(*[iter(buttons)] * num_buttons_per_column, fillvalue=None)
    
    # Initialize InlineKeyboardMarkup with the custom layout
    inline_keyboard = InlineKeyboardMarkup(
        [
            *buttons_column1,
            *buttons_column2,
        ]
    )

    await bot.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                "🆘 HELP COMMANDS",
                InputTextMessageContent(message_text="[`HELP COMMANDS`]"),
                thumb_url="https://graph.org/file/b136511bda43b1d8db7d2.jpg",
                reply_markup=inline_keyboard
            )
        ]
    )

@bot.on_inline_query(filters.regex("test"))
async def test(_, inline_query):
    user_id = (await GET_INFO.barath()).id
    if not inline_query.from_user.id == user_id:
       return 
    string = "This is a test message."  # Ensure string is a string literal
    await bot.answer_inline_query(
       inline_query.id,
       cache_time=0,
       results=[
          InlineQueryResultArticle(
             "Test Inline Query",
             InputTextMessageContent(message_text=string, disable_web_page_preview=True),
             thumb_url="https://graph.org/file/4f71af878a085505e8faf.jpg"
          )
       ]
    )

@bot.on_inline_query(filters.regex("alive"))
async def alive_inline(_, inline_query):
    user_id = (await GET_INFO.barath()).id
    if not inline_query.from_user.id == user_id:
        return
     
    ALIVE_TEXT, photo_url = await alive()

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💫 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/botupdatex"),
            ],
            [
                InlineKeyboardButton("🌝 𝗗𝗘𝗩'𝗦", url="https://t.me/Sexy_Dark"),
                InlineKeyboardButton("🌝 𝗗𝗘𝗩'𝗦", url="https://t.me/Siamkira"),
            ],
            [
                InlineKeyboardButton("❄️ 𝗢𝗪𝗡𝗘𝗥", url="https://t.me/tobiix"),
            ],
        ]
    )
 
    await bot.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultPhoto(
                title="🤖 Bot Status",
                caption=ALIVE_TEXT,  # Use caption for text content
                photo_url=photo_url,
                thumb_url="https://graph.org/file/b136511bda43b1d8db7d2.jpg",
                reply_markup=buttons,
            )
        ]
    )
