# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import requests
import os
import json
import random
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram.errors import MessageNotModified
from chatgpt.module.what import *
from config import OPENAI_API 

@ren.on_message(filters.command("ask") & filters.private | filters.group)
@ratelimiter
async def chatbot(c, m):
    if len(m.command) == 1:
        return await kirimPesan(m, f"Gunakan perintah <code>/{m.command[0]} [pertanyaan]</code> untuk menanyakan pertanyaan menggunakan AI.")
    pertanyaan = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": pertanyaan,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await kirimPesan(m, "Wait a moment looking for your answer..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await editPesan(msg, response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await editPesan(msg, "Yahh, sorry i can't get your answer.")
