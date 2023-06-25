import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ 𝐑ᴜɴɴɪɴɢ 𝐃ᴏᴡɴʟᴏᴀᴅ 𝐒ᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.download()
        m = m.edit("**⇆ 𝐑ᴜɴɴɪɴɢ 𝐔ᴩʟᴏᴀᴅ 𝐒ᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ 𝐒ʜᴀʀɪɴɢ 𝐒ᴩᴇᴇᴅᴛᴇsᴛ 𝐑ᴇsᴜʟᴛs...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 ᴛʀʏɪɴɢ ᴛᴏ ᴄʜᴇᴄᴋ ᴜᴩʟᴏᴀᴅ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **𝐒ᴩᴇᴇᴅᴛᴇsᴛ 𝐑ᴇsᴜʟᴛs** ✯
    
<u>**❥͜͡ᴄʟɪᴇɴᴛ :**</u>
**» __𝐈sᴩ :__** {result['client']['isp']}
**» __𝐂ᴏᴜɴᴛʀʏ :__** {result['client']['country']}
  
<u>**❥͜͡sᴇʀᴠᴇʀ :**</u>
**» __𝐍ᴀᴍᴇ :__** {result['server']['name']}
**» __𝐂ᴏᴜɴᴛʀʏ :__** {result['server']['country']}, {result['server']['cc']}
**» __𝐒ᴩᴏɴsᴏʀ :__** {result['server']['sponsor']}
**» __𝐋ᴀᴛᴇɴᴄʏ :__** {result['server']['latency']}  
**» __𝐏ɪɴɢ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
