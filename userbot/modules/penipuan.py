# Port By @VckyouuBitch From Geez-Projects
# Copyright (C) 2021 Geez-Project
from userbot.events import register
from userbot import CMD_HELP
import asyncio

# Languange en to id from Linux-Userbot
# Thanks Vicky


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai Pengetikan Palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai rekaman audio palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Memulai perekaman video palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Perintah salah`")
    await event.edit(f"`Mulai Bermain Game Palsu Untuk {t} detik.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)

CMD_HELP.update(
    {
        "penipuan": "**° Modul :** `penipuan`\
        \n\n  •  **Perintah :** `.ftyping` | `.faudio` | `.fvideo` | `.fgame` <jumlah text>\
        \n  •  **Function :** Fake typing ini Berfungsi dalam group\
    "
    }
)
