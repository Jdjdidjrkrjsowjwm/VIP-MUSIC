from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from VIPMUSIC import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂❍",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="❍ 𝐇𝙴𝙻𝙿 ❍", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="❍ 𝐒ҽƚƚιɳɠ𝐒❍", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐘ᴏᴜʀ 𝐇ᴇʟᴘᴇʀ ❍", callback_data="settings_back_helper"),
        ],
        [
             InlineKeyboardButton(
                text="❍ ✰ 𝚳𝛍𝛈֟֠֩፝𝛈ᴧ ✰ ❍",
                url=f"https://t.me/MUNNA_KING_XD",
            ),
            InlineKeyboardButton(
                text="❍ UPDATE ❍",
                url=f"https://t.me/Love_dp_Sad_dp",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍  𝛅𝛖𝛒֟֠֩፝𝛒𝛐𝛄𝛕  ❍",
                url=f"https://t.me/+Vr47TRT5Vbw2YjA9",
            ),
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍✿︎ ᴀᴅᴅ ᴍᴇ ✿︎❍", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
                 
