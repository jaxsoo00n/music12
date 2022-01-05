from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2, command
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(command(["start"]) & other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**مرحبا بك عزيزي, انا {bn} 🎧
⌁ ⁞  بوت تشغيل الاغاني  في المكالمه ' الجماعيه وبحث /song +اسم الاغنيه
⌁ ⁞ قم برفع البوت مشرف مع صلاحيه اضافه مستخدمين عبر الرابط
لمعرفه الأوامر اضغط /help 
⌁ ⁞   Developed By [『ＪａｘＳｏｎ』 𖡨](https://t.me/J_X_S1)!**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔮ⓜⓤⓢⓘⓒ🔮", url="https://t.me/RehaaMusic")
                  ],[
                  InlineKeyboardButton(
                        "『ＪａｘＳｏｎ』 𖡨", url="https://t.me/J_X_S1")
                  ],[
                    InlineKeyboardButton(
                       "𝐒𝐎𝐔𝐑𝐂𝐄🌀", url="https://t.me/J_X_S3"
                    ),
                    InlineKeyboardButton(
                        "🚨ⒷⒶⓇ🚨", url="https://t.me/J_X_S9"
                    )
                ],[
                    InlineKeyboardButton(
                        "🎧اضافه البوت اللي مجموعتك🎧",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(command(["help"]) & other_filters2)
async def help(_, message: Message):
    await message.reply_text(
        f"""{bn}• الاوامر 

- /play <اسم الأغنية> 
ـ تشغيل الأغنية التي طلبتها. 

- /playlist 
ـ عرض قائمة التشغيل الآن. 

- /song <اسم الاغنيه>
ـ تنزيل الأغاني التي تريدها بسرعة. 

- /search <اسم الاغنيه> 
ـ البحث في اليوتيوب مع التفاصيل. 

- /vsong <اسم الاغنيه>
ـ تنزيل مقاطع الفيديو التي تريدها بسرعة

- /lyric <اسم الاغنيه>
ـ إحضار كلمات الاغنيه. 

• الاوامر الخاصه بِ المشرفين فقط . 
 
- /player  
ـ فتح لوحة إعدادات مشغل الموسيقى

- /pause 
ـ وقف تشغيل الاغنيه الحاليه. 

- /resume
ـ استئناف تشغيل الأغنية. 

- /skip 
ـ التقدم للأغنية التالية

- /end 
ـ إيقاف تشغيل الموسيقى. 

- /musicplayer on 
ـ لتعطيل مشغل الموسيقى في مجموعتك. 

- /musicplayer off 
- لتمكين مشغل الموسيقى في مجموعتك. 

- /userbotjoin 
- دعوة المساعد إلى الدردشه الحاليه 

- /userbotleave 
- إزالة المساعد من الدردشة الحالية. 

- /reload 
- تحديث قائمة الإدارة. 

- /uptime 
- التحقق من وقت تشغيل البوت

- /ping 
- تحقق من حالة البوت 

• الاوامر الخاصه بالمطورين

- /pmpermit on | off  
ـ قفل/فتح الدردشه ف الخاص. 

- /userbotleaveall 
- اطلب من المساعد مغادرة جميع المجموعات

- /gcast 
- عمل إذاعه

• الشات الخاص بالبوت المساعد 

- .yes 
- الموافقة على إرسال رسالة إلى المساعد في الخاص. 

- .no 
- رفض إرسال رسالة إلى المساعد في الخاص.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚨ⒷⒶⓇ🚨", url=f"https://t.me/J_X_S9"
                    ),
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄🌀", url=f"https://t.me/J_X_S3"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "『ＪａｘＳｏｎ』 𖡨", url=f"https://t.me/J_X_S1"
                    )
                ]
            ]
        )
    )