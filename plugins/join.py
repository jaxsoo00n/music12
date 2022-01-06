# Credit DaisyXMusic, Changes By Blaze, Improve Code By Decode

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from Client.callsmusic import client as USER
from config import SUDO_USERS


@Client.on_message(filters.command(["userbotjoin", "انضم"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>أضفني كمسؤول في مجموعتك أولاً</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "@ee_rr_0"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"<b>{user.first_name} انضم الحساب المساعد إلى محادثتك🎧</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🚨خطأ بسبب كثرة الطلبات 🚨\n{user.first_name} الحساب المساعد تعذر الانضمام إلى مجموعتك بسبب كثرة طلبات الانضمام للحساب المساعد تأكد من عدم حظر الحساب المساعد في المجموعة."
            "\n\nأو أضف يدويًا @{ee_rr_0} إلى مجموعتك وحاول مرة أخرى.</b>",
        )
        return
    await message.reply_text(
        f"<b>{user.first_name} 🎧تم انضمام الحساب المساعد بنجاح 🎧</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave", "غادر"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "<b>لا يمكن للحساب المساعد مغادره المجموعه قد يكون بسبب الضغط .\n\nانتظر او قم بطردي يدويا من جروبك</b>"
        )

        return


@Client.on_message(filters.command(["userbotleaveall", "غادرالجميع"]))
async def bye(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🚨الحساب المساعد غادر جميع الدردشات🚨")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"الحساب المساعد غادر... Left: {left} الدردشه. Failed: {failed} الدردشه."
            )
        except:
            failed += 1
            await lol.edit(
                f"الحساب المساعد غادر... Left: {left} الدردشه. Failed: {failed} الدردشه."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"Left {left} الدردشه. Failed {failed} الدردشه."
    )

