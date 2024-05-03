from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PROFESSOR import app
from config import BOT_USERNAME

start_txt = """
𝗛𝗲𝗿𝗲 𝗶𝘀 𝗟𝗶𝘀𝘁 𝗼𝗳 𝗼𝘂𝗿 𝗙𝗮𝗺𝗶𝗹𝘆 𝗚𝗼𝗺𝗮
𝗣𝗲𝗮𝗰𝗵 𝗕𝗼𝘁𝘀 𝗪𝗵𝗶𝗰𝗵 𝗖𝗮𝗻 𝗣𝗹𝗮𝘆 𝗠𝘂𝘀𝗶𝗰
🎶 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽𝘀.

𝗖𝗵𝗲𝗰𝗸 𝗕𝗼𝘁𝘀 𝗦𝘁𝗮𝘁𝘂𝘀 𝗧𝗵𝗲𝘆 𝗮𝗿𝗲 𝗔𝗹𝗶𝘃𝗲 𝗼𝗿
𝗡𝗼𝘁 𝗮𝘁 @GomaPeach_Status
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ＡＤＤ ＭＥ ＢＡＢＹ", url=f"https://t.me/Professor_Sukoon_Bot?startgroup=True&admin=delete_messages+invite_users+pin_messages")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("ᴘʀᴏғᴇssᴏʀ", url="https://t.me/SOURABH_OWNER"),
          ],
               [
                InlineKeyboardButton("ᴘʀᴏғᴇssᴏʀ ɴᴇᴛᴡᴏʀᴋ", url="https://t.me/PROFESSOR_NETWORK"),

],
[
              InlineKeyboardButton("ᴍᴀɪɴ ʙᴏᴛ", url=f"https://t.me/Professor_Sukoon_Bot"),
              InlineKeyboardButton("︎ᴍʏ ʀᴇᴘᴏ ", url=f"https://github.com/PROFESSOR-SOURABH/PROFESSOR-MUSIC"),
       
    ],
    [
              InlineKeyboardButton("sᴛʀɪɴɢ ɢᴇɴ", url=f"https://t.me/String_Generate_op_bot"),
              InlineKeyboardButton("︎sᴛʀɪɴɢ ʜᴀᴄᴋ", url=f"https://t.me/ProfessorStringHackBot"),
       
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/5a179edc9786aa59737e2.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
