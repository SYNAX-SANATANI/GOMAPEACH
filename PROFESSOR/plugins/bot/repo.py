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
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 1 ]", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 2 ]", url="https://t.me/SOURABH_OWNER"),
          ],
        [
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 3 ]", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 4 ]", url="https://t.me/SOURABH_OWNER"),
          ],
               [
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 5 ]", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 6 ]", url="https://t.me/SOURABH_OWNER"),
          ],
[
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 7 ]", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 8 ]", url="https://t.me/SOURABH_OWNER"),
          ],          
    [
              InlineKeyboardButton("𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 9 ]", url=f"https://t.me/String_Generate_op_bot"),
              InlineKeyboardButton("︎𝗚𝗼𝗺𝗮 𝗣𝗲𝗮𝗰𝗵 [ 10 ]", url=f"https://t.me/ProfessorStringHackBot"),
       
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/5a179edc9786aa59737e2.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
