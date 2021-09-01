# Made with python3
# (C) @FayasNoushad
# (C) @BXBotz
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Translator-Bot-V2/blob/main/LICENCE

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from googletrans import Translator

Telegram = Client(
    "Translator Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
Hello {},

`Iam a Simple Google Translater Bot. Send Me Any Text & Select Desired Language`

**Made With ❤ By @BX_Botz**
"""
HELP_TEXT = """
✪ `Just send a text with language code`

✪ `And select a language for translating`

© [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz) 
"""
ABOUT_TEXT = """
🤖 **Bot** : **Gᴏᴏɢʟᴇ Tʀᴀɴsʟᴀᴛᴏʀ**

👨‍💻 **Dᴇᴠᴇʟᴏᴘᴇʀ** : [ᴍᴜꜰᴀᴢ 🇮🇳](https://telegram.me/Mufaz123)

📣 **Cʜᴀɴɴᴇʟ** : [BX Bᴏᴛᴢ](https://t.me/BX_Botz)

👥 **Gʀᴏᴜᴘ** : [ʙx sᴜᴘᴘᴏʀᴛ](https://t.me/BxSupport)

🌐 **Sᴏᴜʀᴄᴇ** : [Cʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/nokiyirunnoippokitum)

🎧 **Lᴀɴɢᴜᴀɢᴇ** : [Pʏᴛʜᴏɴ𝟹](https://python.org/)

📚 **Lɪʙʀᴀʀʏ** : [Pʏʀᴏɢʀᴀᴍ](https://pyrogram.org/)

📡 **Sᴇʀᴠᴇʀ** : [Hᴇʀᴏᴋᴜ](https://heroku.com/)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/BX_Botz'),
        InlineKeyboardButton('🎨 Support Group', url='https://telegram.me/BXSUPPORT')
        ],[
        InlineKeyboardButton('🛠️ Help', callback_data='help'),
        InlineKeyboardButton('🔮 About', callback_data='about')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data='home'),
        InlineKeyboardButton('♻️About', callback_data='about'),
        InlineKeyboardButton('Close 🔒', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data='home'),
        InlineKeyboardButton('🛠️Help', callback_data='help'),
        InlineKeyboardButton('Close 🔒', callback_data='close')
        ]]
    )
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Close 🔒', callback_data='close')
        ]]
    )
TRANSLATE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('♻️ Join Updates Channel ♻️', url='https://telegram.me/BX_Botz')
        ]]
    )
LANGUAGE_BUTTONS = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton("മലയാളം", callback_data="Malayalam"),
    InlineKeyboardButton("Tamil", callback_data="Tamil"),
    InlineKeyboardButton("Hindi", callback_data="Hindi")
    ],[
    InlineKeyboardButton("Kannada", callback_data="Kannada"),
    InlineKeyboardButton("Telugu", callback_data="Telugu"),
    InlineKeyboardButton("Marathi", callback_data="Marathi")
    ],[
    InlineKeyboardButton("Gujarati", callback_data="Gujarati"),
    InlineKeyboardButton("Odia", callback_data="Odia"),
    InlineKeyboardButton("Arabic", callback_data="arabic")
    ],[
    InlineKeyboardButton("Punjabi", callback_data="Punjabi"),
    InlineKeyboardButton("Persian", callback_data="Persian"),
    InlineKeyboardButton("English", callback_data="English")
    ],[
    InlineKeyboardButton("Spanish", callback_data="Spanish"),
    InlineKeyboardButton("French", callback_data="French"),
    InlineKeyboardButton("Russian", callback_data="Russian")
    ]]
)

@Telegram.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    elif update.data == "close":
        await update.message.delete()
    else:
        message = await update.message.edit_text("`🌐 Translating...`")
        text = update.message.reply_to_message.text
        language = update.data
        translator = Translator()
        try:
            translate = translator.translate(text, dest=language)
            translate_text = f"**Translated to {language}**"
            translate_text += f"\n\n`{translate.text}`"
            if len(translate_text) < 4096:
                translate_text += ""
                await message.edit_text(
                    text=translate_text,
                    disable_web_page_preview=True,
                    reply_markup=TRANSLATE_BUTTON
                )
            else:
                with BytesIO(str.encode(str(translate_text))) as translate_file:
                    translate_file.name = language + ".txt"
                    await update.reply_document(
                        document=translate_file,
                        caption="**Made With ❤ By @BX_Botz**",
                        reply_markup=TRANSLATE_BUTTON
                    )
                await message.delete()
        except Exception as error:
            print(error)
            await message.edit_text("Something wrong. Contact My Support Group\n\n☎️ @BXSupport")

@Telegram.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Telegram.on_message(filters.private & filters.text)
async def translate(bot, update):
    await update.reply_text(
        text="**Select You Desired Language**",
        disable_web_page_preview=True,
        reply_markup=LANGUAGE_BUTTONS,
        quote=True
    )
    
Telegram.run()
