# Credits: @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import importlib
import logging
import sys
from pathlib import Path
from random import randint

import heroku3
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.contacts import UnblockRequest

from indomie import (
    BOT_TOKEN,
    BOTLOG_CHATID,
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    LOGS,
    bot,
)

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def autopilot():
    LOGS.info("TUNGGU SEBENTAR. SEDANG MEMBUAT GROUP LOG USERBOT UNTUK ANDA")
    desc = "Group Log untuk IndomieUserBot.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✦ Powered By ~ @IndomieProject ✦"
    try:
        grup = await bot(
            CreateChannelRequest(title="Userbot Log", about=desc, megagroup=True)
        )
        grup_id = grup.chats[0].id
    except Exception as e:
        LOGS.error(str(e))
        LOGS.warning(
            "var BOTLOG_CHATID kamu belum di isi. Buatlah grup telegram dan masukan bot @MissRose_bot lalu ketik /id Masukan id grup nya di var BOTLOG_CHATID"
        )
    if not str(grup_id).startswith("-100"):
        grup_id = int(f"-100{str(grup_id)}")
    heroku_var["BOTLOG_CHATID"] = grup_id


async def autobot():
    if BOT_TOKEN:
        return
    await bot.start()
    await asyncio.sleep(15)
    await bot.send_message(
        BOTLOG_CHATID, "**SEDANG MEMBUAT BOT TELEGRAM UNTUK ANDA DI @BotFather**"
    )
    who = await bot.get_me()
    name = who.first_name + " Assistant"
    if who.username:
        username = who.username + "_userbot"
    else:
        username = "Indomie" + (str(who.id))[5:] + "userbot"
    bf = "@BotFather"
    await bot(UnblockRequest(bf))
    await bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
        )
        sys.exit(1)
    await bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
            )
            sys.exit(1)
    await bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    await bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "Asisstant" + (str(who.id))[6:] + str(ran) + "userbot"
        await bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            await bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, "Search")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_file(bf, "indomie/utils/styles/asisstant.png")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"Managed With ☕️ By {who.first_name}")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(
                bf, f"✦ Owner ~ {who.first_name} ✦\n\n✦ Powered By ~ @IndomieProject ✦"
            )
            await bot.send_message(
                BOTLOG_CHATID,
                f"**BERHASIL MEMBUAT BOT TELEGRAM DENGAN USERNAME @{username}**",
            )
            LOGS.info(
                f"BERHASIL MEMBUAT BOT TELEGRAM DENGAN USERNAME @{username}")
            await bot.send_message(
                BOTLOG_CHATID,
                "**Tunggu Sebentar, Sedang Restart Heroku Untuk Menyimpan Perubahan.**",
            )
            heroku_var["BOT_TOKEN"] = token
            heroku_var["BOT_USERNAME"] = f"@{username}"
        else:
            LOGS.info(
                "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
            )
            sys.exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        await bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, "Search")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setuserpic")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_file(bf, "indomie/utils/styles/asisstant.png")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"Managed With ☕️ By {who.first_name}")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(
            bf, f"✦ Owner ~ {who.first_name} ✦\n\n✦ Powered By ~ @IndomieProject ✦"
        )
        await bot.send_message(
            BOTLOG_CHATID,
            f"**BERHASIL MEMBUAT BOT TELEGRAM DENGAN USERNAME @{username}**",
        )
        LOGS.info(f"BERHASIL MEMBUAT BOT TELEGRAM DENGAN USERNAME @{username}")
        await bot.send_message(
            BOTLOG_CHATID,
            "**Tunggu Sebentar, Sedang Restart Heroku Untuk Menyimpan Perubahan.**",
        )
        heroku_var["BOT_TOKEN"] = token
        heroku_var["BOT_USERNAME"] = f"@{username}"
    else:
        LOGS.info(
            "Silakan Hapus Beberapa Bot Telegram Anda di @Botfather atau Set Var BOT_TOKEN dengan token bot"
        )
        sys.exit(1)


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"indomie/modules/{shortname}.py")
        name = "indomie.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Successfully imported " + shortname)
    else:

        path = Path(f"indomie/modules/{shortname}.py")
        name = "indomie.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.CMD_HELP = CMD_HELP
        mod.logger = logging.getLogger(shortname)
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["indomie.modules." + shortname] = mod
        LOGS.info("Successfully imported " + shortname)


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"indomie/modules/assistant/{shortname}.py")
        name = "indomie.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Starting Your Assistant Bot.")
        LOGS.info("Assistant Sucessfully imported " + shortname)
    else:
        path = Path(f"indomie/modules/assistant/{shortname}.py")
        name = "indomie.modules.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules["indomie.modules.assistant" + shortname] = mod
        LOGS.info("Assistant Successfully imported" + shortname)


def remove_plugin(shortname):
    try:
        try:
            for i in CMD_HELP[shortname]:
                bot.remove_event_handler(i)
            del CMD_HELP[shortname]

        except BaseException:
            name = f"indomie.modules.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError


async def create_supergroup(group_name, client, botusername, descript):
    try:
        result = await client(
            functions.channels.CreateChannelRequest(
                title=group_name,
                about=descript,
                megagroup=True,
            )
        )
        created_chat_id = result.chats[0].id
        result = await client(
            functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            )
        )
        await client(
            functions.channels.InviteToChannelRequest(
                channel=created_chat_id,
                users=[botusername],
            )
        )
    except Exception as e:
        return "error", str(e)
    if not str(created_chat_id).startswith("-100"):
        created_chat_id = int("-100" + str(created_chat_id))
    return result, created_chat_id
