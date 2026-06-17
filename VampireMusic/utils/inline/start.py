from pyrogram.types import InlineKeyboardButton

import config
from VampireMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], url=config.SUPPORT_CHAT
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_10"], callback_data="Kanha_Anu"
            ),
            InlineKeyboardButton(
                text="💌 ʏᴛ-ᴀᴘɪ", callback_data="api_status"
            ),
        ],
        [
            InlineKeyboardButton(
                text=" ⚜️ ʟᴧɴɢᴜᴧɢᴇ", callback_data="LG"
            ),
            InlineKeyboardButton(
                text="🛡️ ᴘʀɪᴠᴧᴄʏ",
                url="https://graph.org/KanhaMusic-04-18",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"], callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons