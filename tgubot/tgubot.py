from telethon import events
#import subprocess
from subprocess import Popen as SSSU, PIPE, STDOUT
#from os import getcwd as CWD
from threading import Thread
from html import escape as FIX
from telethon import TelegramClient
from telethon.sessions import StringSession
from logging import INFO, basicConfig, getLogger
import asyncio
import datetime
#from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps, ImageEnhance
from io import BytesIO as BIO
from uuid import uuid4 as UID
#from traceback import format_exc as ERR
import textwrap
import requests
#import pyfiglet
import random
from time import time
from time import sleep
#from moviepy import VideoFileClip, ImageSequenceClip
#from telethon.tl.types import MessageEntityBlockquote as MEB
from telethon.extensions.markdown import DEFAULT_DELIMITERS as DEF
from telethon.tl import types
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import GetStickersRequest
#from telethon.extensions.markdown import ParseMode
#from telethon.tl.types import InputStickerSetShortName
from telethon.errors import StickersetInvalidError, FloodWaitError
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest, EditPhotoRequest, GetParticipantRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights, ChatBannedRights
from telethon import types
import traceback
#import speedtest
import glob
import json
#from bs4 import BeautifulSoup
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
#import datetime
from gtts import gTTS
from openai import OpenAI
import shutil
#import ollama
from google import genai as geminiai
#from pdf2image import convert_from_path
#import convertapi
from shutil import rmtree
#import wikipedia
import base64
import unicodedata
import string
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
import emoji
#import textwrap
import urllib
#import logging
#import random
#import json
import os
import re
#from htmlwebshot import WebShot



"""Logging"""
basicConfig(format="%(message)s", level=INFO)
LOGS = getLogger(__name__)

"""Account Vars"""
API_KEY = "26626311"
API_HASH = "3e3c1d58c4fc67286624369cb6c404ff"
STRING_SESSION = "1BVtsOLUBu0WN1RlvU5bnJPUckGC9DQD0Ed_MtIrfsEMDoG1Fv-xa7ho1IWb5Uwl6nI1nWvqdOa1p0UOzdzXaMsgNZzsteFAbEX0kwI49pk8nzRYuBnEth9TvGyVnjdbGntpAEY9H5oUleSzyRGXwuscXA2_GS9yU98B80mWM-QRsU77O6s6m3VTk6TeQTCvdEmae0mzipMKOi0hTb3zlP83Ue4eeDAVHD29Qcsu0iac1-lYALdykDzL0MT9N1c1t5S6tY-q3nmYXKJl5Qn30lj_K5XTMgqpkI7ohxbWSRrwuBzRl7_hCTRwLrTTmxzWW0b5JU9Eam52NCq8tePcdmcVzJNZjdXY="
default_group_link = "https://t.me/+JMnt71kRXcU3ODQ1" #for forward to save message u want with /sav
gay_channel_link = "https://t.me/gaylisttokilll"
ai_ml_api_key = "21b2d1030cbd484cba8e412824536743"
openrouter_api = "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"
gemini_ai_api_key = "AIzaSyBxB9BMjR4wZDDRwQJIQACeZj1yrOPh1uk"
MY_USER_ID = 6214704050
MY_USER_NAME = "@SothDev"
SS_API = "WJN257X-CD44T8D-K2NDM2B-J2J3H1C"

"""Define & Start Client"""
bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
bot.start()

"""Lovely Vars"""
SHELL_PATH = '/data/data/com.termux/files/usr/bin/bash'
CORE = {
    'SUDO': './tgbot/saved/sudo',
    'ISUDO': './tgbot/saved/isudo',
    'DMUTE': './tgbot/saved/dmute'
}
PENDING = {}

"""Spy For Triggers"""
def SPY(**a):
    p = a.get('p', None)
    if p: a['pattern'] = '(?i)' + p
    def d(f):
        async def w(c):
            try: await f(c)
            except KeyboardInterrupt: pass
        bot.add_event_handler(w, events.MessageEdited(**a))
        bot.add_event_handler(w, events.NewMessage(**a))
        return w
    return d

"""Triggers"""
SU_TRIG = r"\."
WHAT_TRIG = r"!!id$"
DUMP_TRIG = r"!!dump$"
ADD_SUDO_TRIG = r"!!TAKE SUDO$"
NUKE_SUDO_TRIG = r"!!NUKE SUDO$"
ADD_ISUDO_TRIG = r"!!TAKE ISUDO$"
NUKE_ISUDO_TRIG = r"!!NUKE ISUDO$"
ADD_DMUTE_TRIG = r"!!TAKE DMUTE$"
NUKE_DMUTE_TRIG = r"!!NUKE DMUTE$"
SUDO_YES_TRIG = r"/y$"
NUKE_TRIG = r"/dd$"
UPLOAD_TRIG = r"!!push"
DOWNLOAD_TRIG = r"!!steal"
ABORT_TRIG = r"\^C"
HTML_TRIG = r"!!html"
MEME_TRIG = r'!!meme'



"""Strings"""
AFTER_DMUTE = "Now I may shut you up when I can, {}"
AFTER_DMUTE_NUKE = "I will stop trying to shut you up, {}"
AFTER_SUDO = "Now you have a protected access to my shell, {}"
AFTER_SUDO_NUKE = "You no longer have a protected access to my shell, {}"
AFTER_ISUDO = "Now you have full access to my shell, {}"
AFTER_ISUDO_NUKE = "You no longer have full access to my shell, {}"
NOT_THERE = "This user's not there anyway"
ALREADY_THERE = "This user's already there"

"""Fix Missing Files"""
[open(CORE[f], 'a').close() for f in CORE]

"""Get, Edit, Inspect & Send Messages"""
async def GR(E,b=0): m = await E.get_reply_message(); return (m,T(m)) if b and m else m if m else (None,None)
async def ED(E,t):
    try: return await E.edit(t, parse_mode='HTML')
    except Exception as ex:
        if "not modified" in str(ex): pass
        else: return await SM(E.chat_id if hasattr(E, 'chat_id') else E.peer_id.channel_id, t)
async def SM(id,t): return await bot.send_message(id,t, parse_mode='HTML')
def T(E):
    return E.text if hasattr(E, 'text') else E.message.text

"""Obtain ID, User, Entity & Info"""
async def EN(id): return await bot.get_entity(int(id))
def U(EN,i=0): return EN.username if not i else (EN.username, EN.first_name)
def ID(E): return E.sender_id
"""Shell Toggle"""
Shell_ON_T = False 
"""last id"""
LAST_MSG_ID = 0
LAST_CHAT_ID = 0
"""Execute & Get SUDO"""
def SSU(C, **kw):
    return SSSU([SHELL_PATH, '-c', C], stdout=PIPE, stderr=STDOUT, text=True, **kw)
def SU(C):
    try: o = FIX(SSU(C).stdout.read())
    except Exception as e: o = F(FIX(0),'blockquote')+f"{e}"+F(None,'blockquote')
    if len(o)+len(C) >= 4000: o = f"{M(o[:4000-len(C)])}{F(0,'blockquote')}\n{Q(M('[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'))}{F([],'blockquote')}"
    return Q(M('$ ')+M(C)+M('\n'+o if o else ''))
def GS(): return EYE('SUDO')
def GIS(): return EYE('ISUDO')
def GDM(): return EYE('DMUTE')

"""Markdown"""
def F(t,u): return f"<{u}>{t}</{u}>" if t else f"</{u}><{u}>" if t == 0 else f"</{u}>"
def Q(t): return F(t,'blockquote')
def M(t): return F(t,'code')
def P(t): return F(t,'pre')

"""Read, Write & Append"""
def PIN(n,t):
    with open(CORE[n],'w') as f: f.write(t)
def PEN(n,t):
    with open(CORE[n],'a') as f: f.write(t)
def EYE(n):
    with open(CORE[n]) as f: return f.read().strip().split('\n')

"""Message Dump"""
#outgoing=True,
@SPY(outgoing=True, pattern=DUMP_TRIG)
async def dump(E):
    await ED(E, Q(P(str((await GR(E)) if E.is_reply else E))))

"""ID Identifier"""
@SPY(outgoing=True, pattern=WHAT_TRIG)
async def what(E):
    id = ID(E if not E.is_reply else await GR(E))
    if E.is_reply: await ED(E, Q(M(id)))
    else: await E.reply(Q(M(id)), parse_mode='HTML')

"""Add SUDO"""
@SPY(outgoing=True, pattern=ADD_SUDO_TRIG)
async def add_sudo(E):
    if not E.is_reply: return
    id = ID(await GR(E))
    if str(id) in GS(): await ED(E, Q(M(ALREADY_THERE))); return
    PEN('SUDO', '\n'+str(id))
    await ED(E, Q(M(AFTER_SUDO.format(U(await EN(id))))))

"""Nuke SUDO"""
@SPY(outgoing=True, pattern=NUKE_SUDO_TRIG)
async def nuke_sudo(E):
    if not E.is_reply: return
    id = ID(await GR(E))
    if str(id) not in GS(): await ED(E, Q(M(NOT_THERE))); return
    old = GS()
    new = [l for l in old if str(id) not in l]
    PIN('SUDO', '\n'.join(new))
    await ED(E, Q(M(AFTER_SUDO_NUKE.format(U(await EN(id))))))

"""Nuke ISUDO"""
@SPY(outgoing=True, pattern=NUKE_ISUDO_TRIG)
async def nuke_isudo(E):
    if not E.is_reply: return
    id = ID(await GR(E))
    if str(id) not in GIS(): await ED(E, Q(M(NOT_THERE))); return
    old = GIS()
    new = [l for l in old if str(id) not in l]
    PIN('ISUDO', '\n'.join(new))
    await ED(E, Q(M(AFTER_ISUDO_NUKE.format(U(await EN(id))))))

"""Add ISUDO"""
@SPY(outgoing=True, pattern=ADD_ISUDO_TRIG)
async def add_isudo(E):
    if not E.is_reply: return
    id = ID(await GR(E))
    if str(id) in GIS(): await ED(E, Q(M(ALREADY_THERE))); return
    PEN('ISUDO', '\n'+str(id))
    await ED(E, Q(M(AFTER_ISUDO.format(U(await EN(id))))))

"""Add Dmute"""
@SPY(outgoing=True, pattern=ADD_DMUTE_TRIG)
async def add_dmute(E):
    if not E.is_reply: return
    id = ID(await GR(E))
    PEN('DMUTE', '\n'+str(id))
    await ED(E, Q(M(AFTER_DMUTE.format(U(await EN(id))))))

"""Nuke Dmute"""
@SPY(outgoing=True, pattern=NUKE_DMUTE_TRIG)
async def nuke_dmute(E):
    if not E.is_reply: return
    id = ID(await GR(E))
    if str(id) not in GDM(): await ED(E, Q(M(NOT_THERE))); return
    old = GDM()
    new = [l for l in old if str(id) not in l]
    PIN('DMUTE', '\n'.join(new))
    await ED(E, Q(M(AFTER_DMUTE_NUKE.format(U(await EN(id))))))

"""Abort Shell Commands"""
@SPY(outgoing=True, pattern=ABORT_TRIG)
async def abort_shell(E):
    if not E.is_reply: return
    r = await GR(E)
    PENDING[str(r)[:20]].kill()
    await E.delete()

"""HTML Markdown Tester"""
@SPY(outgoing=True, pattern=HTML_TRIG)
async def html(E):
    if not E.is_reply: return
    r = await GR(E)
    t = T(r)
    try: await E.delete()
    except: pass
    try: await r.reply(t, parse_mode='HTML')
    except Exception:print(traceback.format_exc()); await ED(E,t)

"""Live Shell Command Listener"""
@SPY(outgoing=True, pattern=SU_TRIG)
async def shell(E):
    if not Shell_ON_T: return
    t = T(E)[1:]
    if "#LC=" in t: fn2 = int(t.split('#LC=',1)[1])
    else: fn2 = 0
    if fn2 == 0:
        outt = SU(t)
        await ED(E, outt)
        return
    else:
        if fn2 == 0:
            await ED(E, SU(t))
            return
        p = SSU(t)
        o = '\n'
        koll = p.kill
        def kell(*a,**kw):
            nonlocal koll, o
            o += "^C"
            koll(*a,**kw)
        p.kill = kell
        PENDING[str(E.message)[:20]] = p
        fn = 0
        async def a():
            nonlocal p, t, o, fn
            for l in p.stdout:
                if not l: continue
                o += l
                if fn % fn2 == 0: await ED(E,Q(M('$ ')+M(t)+M(o)))
                fn += 1
            await ED(E,Q(M('$ ')+M(t)+M(o)))
        th = Thread(target=(await a()))
        th.start()

"""SUDO Shell Command Listener"""
@SPY(pattern=SU_TRIG)
async def sub_shell(E):
    if not Shell_ON_T: return
    t = T(E)
    id = str(ID(E))
    if (id not in GS() and id not in GIS()): return
    cmd = t[1:]
    uname, fname = U(await EN(id),1)
    if id in GIS():
        #repl_msg = await E.get_reply_message()
        msg = await bot.send_message(E.chat_id, SU(t[1:]), parse_mode='HTML', reply_to=E.id) # await ED(E, SU(t[1:]))
    else:
        final = Q(M('SHELL REQUEST - By\n')+M(f'{fname}')+' ('+M(f'@{uname}')+M(')'))
        final += "\n"+Q(M('$ '+cmd))
        final += "\n"+Q(M('Waiting for confirmation'))
        #msg = await SM(E.chat_id, final)
        #repl_msg = await E.get_reply_message()
        msg = await bot.send_message(E.chat_id, final, parse_mode='HTML', reply_to=E.id)

"""SUDO Pending Requests"""
@SPY(outgoing=True, pattern=SUDO_YES_TRIG)
async def sudo_yes(E):
    if not E.is_reply: return
    r, rt = await GR(E,1)
    try: t = rt.split('\n')[2][3:][:-1]
    except IndexError: return
    await ED(r, SU(t))
    await E.delete()

"""Delete A Message"""
@SPY(outgoing=True, pattern=NUKE_TRIG)
async def nuke(E):
    try:
        await E.delete()
        await (await GR(E)).delete()
    except: pass

"""Upload Files"""
@SPY(outgoing=True, pattern=UPLOAD_TRIG)
async def upload(E):
    t = T(E)
    if not t.startswith(UPLOAD_TRIG): return
    t = t[len(UPLOAD_TRIG)+1:]
    f = t if t.startswith('/') else os.getcwd() + f'/{t}'
    async def CB(c,t):
        nonlocal E, f
        p = (c / t) * 100
        art = ""
        for i in range(20):
            art += "■" if i*5 < p else "□"
        c = str(c / 1024 / 1024)[:6]
        t = str(t / 1024 / 1024)[:6]
        p = str(p)[:6]
        pro = f"[{c}MB/{t}MB]"
        await ED(E, Q(M(f'{UPLOAD_TRIG} ')+M(f)+M(f'\n{pro} {p}%\n')+M(art)))
    try:
        if E.is_reply:
            repl = await E.get_reply_message()
            await bot.send_file(E.chat_id, f, progress_callback=CB, reply_to=repl.id)
        else:
            await bot.send_file(E.chat_id, f, progress_callback=CB, reply_to=E.id)
        await asyncio.sleep(1)
        #await E.edit("✅️")
        await asyncio.sleep(4)
        await E.delete()
    except Exception as e: await ED(E, Q(M(str(e))))

"""Upload Files"""
@SPY(outgoing=True, pattern=DOWNLOAD_TRIG)
async def download(E):
    t = T(E)
    if not t.startswith(DOWNLOAD_TRIG): return
    if not E.is_reply: return
    r = await GR(E)
    if not r.media: return
    t = t[len(DOWNLOAD_TRIG)+1:]
    f = t if t.startswith('/') else os.getcwd() + f'/{t}'
    async def CB(c,t):
        nonlocal E, f
        p = (c / t) * 100
        art = ""
        for i in range(20):
            art += "■" if i*5 < p else "□"
        c = str(c / 1024 / 1024)[:6]
        t = str(t / 1024 / 1024)[:6]
        p = str(p)[:6]
        pro = f"[{c}MB/{t}MB]"
        await ED(E, Q(M(f'{DOWNLOAD_TRIG} ')+M(f)+M(f'\n{pro} {p}%\n')+M(art)))
        #await event.delete()
    try:
        await r.download_media(f, progress_callback=CB)
        await asyncio.sleep(1)
        #await E.edit("✅️")
        await asyncio.sleep(4)
        await E.delete()
    except Exception as e: await ED(E, Q(M(str(e))))

#wth

continue_animation = False 
animated_message = None

@SPY(pattern=r'(?s)^!!animate (.+)')
async def animate(event):
    global continue_animation, animated_message
    if event.sender_id == MY_USER_ID:
        continue_animation = True
        #await event.delete()

        frames = event.pattern_match.group(1).split('.')
        if animated_message:
            await animated_message.delete()
        animated_message = await event.edit('Starting...')

        try:
            while continue_animation:
                for frame in frames:
                    if not continue_animation:
                        break
                    await animated_message.edit(frame.strip())
                    await asyncio.sleep(1)  # Adjust the delay to control animation speed
        except:
            continue_animation = False
            

@SPY(pattern=r'^!!stop')
async def stop(event):
    global continue_animation, animated_message
    if event.sender_id == MY_USER_ID:
        continue_animation = False
        if animated_message:
            await animated_message.delete()
            animated_message = None
        await event.delete()

"""
# Use the correct event type for deleted messages
@bot.on(events.MessageDeleted())
async def handle_deleted_message(event):
    global continue_animation
    if MY_USER_ID in event.deleted_ids:
        continue_animation = False
"""




@SPY(pattern=r'(?s)!!spam (\d+) (.+)')
async def spambkline(event):
    try:
        if event.sender_id == MY_USER_ID:
            count = int(event.pattern_match.group(1))
            message = event.pattern_match.group(2)

            spam_message = (message + '\n') * count
            spam_message = spam_message.rstrip()  # Remove the trailing newline
            if len(spam_message) >= 4096:spam_message[:4096]

            #await event.edit(spam_message)
            repl_msg = await event.get_reply_message()
            if repl_msg:
                await repl_msg.reply(spam_message)
            else:
                await event.reply(spam_message)
                await asyncio.sleep(1)
            await event.delete()
    except Exception as e:
        LOGS.error(f'Error in /spam command: {e}')

@SPY(pattern=r'(?s)!!spams (\d+) (.+)')
async def spammt(event):
    try:
        LOGS.info(f'Received /spams command from user_id: {event.sender_id}')
        print(f'Received /spams command from user_id: {event.sender_id}')
        if event.sender_id == MY_USER_ID:
            LOGS.info('User ID matched. Processing spams command...')
            countt = int(event.pattern_match.group(1))
            count = countt - int(1)
            message = event.pattern_match.group(2)

            #if count > int(1):
            repl_msg = await event.get_reply_message()
            if repl_msg:
                await repl_msg.reply(message)
            else:
                await event.reply(message)
            for _ in range(count):
                await event.reply(message)
                await asyncio.sleep(0.3)
            await asyncio.sleep(1)
            await event.delete()
        else:
            LOGS.info(f'User ID did not match. Expected {MY_USER_ID}, but got {event.sender_id}')
    except Exception as e:
        LOGS.error(f'Error in /spams command: {e}')


@SPY(pattern=r'(?s)!!spamss (\d+) (\d+) (.+)')
async def spammtdly(event):
    try:
        if event.sender_id == MY_USER_ID:
            count = int(event.pattern_match.group(1))
            delay = int(event.pattern_match.group(2))
            message = event.pattern_match.group(3)

            for _ in range(count):
                await asyncio.sleep(delay)
                await event.reply(message)
            await event.delete()
            LOGS.info(f'spamss done')
    except: pass



r'''
@SPY(pattern=r'/ok')
async def ok(event):
        if event.sender_id == MY_USER_ID:
            text_art = r"""
,  ___   _   _
 / __ \| |/ /
|  ||  | ' / 
|  |__|  | . \ 
 \___/|_|\_\
"""
            #messages = await bot.get_messages(event.chat_id, limit=1, from_user='me')
            #if messages:
                #await messages[0].edit(text_art)
            await event.edit(text_art)
# what should i do next
'''


@SPY(pattern=r'^!!myt$')
async def mytime(event):
    if event.sender_id == MY_USER_ID:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        #await asyncio.sleep(1)
        await event.edit(f'Current time: {current_time}')

@SPY(pattern=r'^!!myd$')
async def mydate(event):
    if event.sender_id == MY_USER_ID:
        current_date = datetime.datetime.now().strftime('%m-%d-%Y')
        #await asyncio.sleep(1)
        await event.edit(f'Current date: {current_date}')

@SPY(pattern=r'^!!mydt$')
async def mydaatetime(event):
    if event.sender_id == MY_USER_ID:
        current_date = datetime.datetime.now().strftime('%m-%d-%Y')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        #await asyncio.sleep(1)
        await event.edit(f'Current date: {current_date}\nCurrent time: {current_time}')



@SPY(pattern=r'(?s)!!later (\d+)([hms]) (.+)')
async def remindme(event):
    if event.sender_id == MY_USER_ID:
        delay = int(event.pattern_match.group(1))
        unit = event.pattern_match.group(2)
        message = event.pattern_match.group(3);
        await event.delete()
        if unit == 'h':
            delay *= 3600  # Convert hours to seconds
        elif unit == 'm':
            delay *= 60  # Convert minutes to seconds
        
        await asyncio.sleep(delay)  # Delay in seconds
        await event.respond(f'{message}')

# File to store tasks
TASKS_FILE = "./tgbot/saved/todotask"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return file.read().splitlines()
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Command: /todo
#@client.on(events.NewMessage(pattern='/todo'))
@SPY(pattern=r'!!todo')
async def todo(event):
    tasks = load_tasks()  # Load tasks from file
    command = event.raw_text.replace('!!todo', '').strip().split(maxsplit=1)
    if len(command) < 1:
        await event.reply("Welcome to the To-Do List UserBot! 🚀\n\n"
                            "Use \"!!todo add <task>\" to add a task.\n"
                            "Use \"!!todo list\" to see your tasks.\n"
                            "Use \"!!todo done <number>\" to mark a task as done.")
        await asyncio.sleep(3)
        await event.delete()
        #await event.reply("Invalid command.\nUse:\n/todo add <task>\n/todo view\n/todo done <number>`.")
        return

    action = command[0].lower()
    args = command[1] if len(command) > 1 else ""

    if action == 'add':
        if args:
            tasks.append(args)
            save_tasks(tasks)  # Save tasks to file
            await event.reply(f"Task added: {args}")
        else:
            await event.reply("Please provide a task after `/todo add`.")
        await asyncio.sleep(3)
        await event.delete()
    elif action == 'list':
        if not tasks:
            await event.reply("My to-do list is empty!")
        else:
            task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
            await event.reply(f"My To-Do List:\n{task_list}")
        await asyncio.sleep(3)
        await event.delete()
    elif action == 'done':
        try:
            task_num = int(args)
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                save_tasks(tasks)  # Save tasks to file
                await event.reply(f"Task marked as done: {removed_task}")
            else:
                await event.reply("Invalid task number.")
        except ValueError:
            await event.reply("Please enter a valid task number after `/todo done`.")
        await asyncio.sleep(3)
        await event.delete()
    else:
    #elif action == 'help':
        #await event.reply("Invalid command.\nUse:\n!!todo add <task>\n!!todo view\n!!todo done <number>`.")
        wrongmsg = await event.reply("Invalid command.\n\nUse: \"!!todo add <task>\" to add a task.\nUse: \"!!todo list\" to see your tasks.\nUse \"!!todo done <number>\" to mark a task as done.")
        await asyncio.sleep(3)
        await event.delete()
        await asyncio.sleep(5)
        await wrongmsg.delete()
    #else:
        #await event.reply("Use:\n/todo add <task>\n/todo view\/todo done <number>`.")

@SPY(outgoing=True, pattern=r'/dds ?(\d+)?')
async def purge(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        start_id = reply_msg.id
        ennd_id = event.id
        end_id = ennd_id - int(1)

        if event.pattern_match.group(1):
            n = int(event.pattern_match.group(1))
            for i in range(n):
                await event.edit(f"Purging in {n - i}s")
                await asyncio.sleep(1)

        # Edit the command message to "deleting..."
        await event.edit("Purging...")

        # Fetch all messages between the start and end IDs
        messages = await bot.get_messages(event.chat_id, min_id=start_id - 1, max_id=end_id + 1)

        for message in messages:
            try:
                await message.delete()
            except Exception as e:
                LOGS.error(f'Error deleting message: {e}')
            
        # Also delete the replied-to message
        try:
            await reply_msg.delete()
        except Exception as e:
            LOGS.error(f'Error deleting replied message: {e}')
            
        # Finally, delete the edited command message
        try:
            await event.edit("Purged")
            await asyncio.sleep(1)
            await event.delete()
        except Exception as e:
            LOGS.error(f'Error deleting command message: {e}')
        
    else:
        await event.edit("Please reply to a message to purge from.")
        #await event.respond("Please reply to a message to purge from.")
        await asyncio.sleep(1)
        await event.delete()



@SPY(pattern=MEME_TRIG)
async def meme(event):
    if event.sender_id == MY_USER_ID:
        try:
            args = event.text[len(MEME_TRIG):].split('-')
            if len(args) < 2:
                return

            top, bottom = args[0].strip(), args[1].strip()
            reply_msg = await event.get_reply_message()
            if not reply_msg or not reply_msg.media:
                return

            await event.edit('Running !!meme...')
            media = await reply_msg.download_media(bytes)
            image = Image.open(BIO(media))
            draw = ImageDraw.Draw(image)

            font = ImageFont.truetype(BIO(requests.get('https://fontsforyou.com/downloads/47031-impact').content), max(20, image.width // 10))

            def add_text(draw, text, y):
                lines = textwrap.fill(text, width=20)
                text_bbox = draw.textbbox((0, 0), lines, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                x = (image.width - text_width) / 2
                draw.text((x, y), lines, font=font, fill="white", stroke_fill="black", stroke_width=2)

            add_text(draw, top, 10)
            add_text(draw, bottom, image.height - font.size - 20)

            output = BIO()
            image.save(output, format="WEBP")
            output.name = "meme.webp"
            output.seek(0)

            await event.edit('Sending...️')
            await event.reply(file=output)
            #await event.respond(file=output)
            await event.edit('✅️')
            #await reply_msg.delete()                                  # Delete the replied image message
            #await reply_msg.reply(file=output)
            await asyncio.sleep(4)
            await event.delete()                                              # Delete the /meme command message

        except Exception:
            await event.delete()  # Delete the /meme command message

#r'''
#a coooooooooooooooooooolllllll cowsayyyyyyyy!
@SPY(pattern=r'(?s)!!cowsay (.+)')
async def cowsay(event):
    id = str(ID(event))
    #if id not in GS() and id not in GIS() and id != str(MY_USER_ID): return
    if id not in GIS() and id != str(MY_USER_ID): return
    C = "cowsay "+event.pattern_match.group(1)
    try: o = FIX(SSU(C).stdout.read())
    except Exception as e: o = f"{e}"
    if len(o)+len(C) >= 4000: o = f"{o[:4000-len(C)]}\n\n{'[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'}"
    if id == str(MY_USER_ID): await event.edit(Q(M('&#x00AD')+M(o)),parse_mode="HTML")
    else: await event.reply(Q(M("&#x00AD")+M(FIX(o))),parse_mode="HTML")
    r'''
        text = event.pattern_match.group(1).strip()
        cow_text = f"""
< {text} >
   \\   ^_ _^
     \\  (oo)\\_ _ _ _ _ 
         (__)\\              )\\
                 | |- - - -w |
                 | |         | |
"""
        await event.edit(cow_text)
    '''



r'''
@SPY(pattern=r'/ssay (.+)')
async def sussay(event):
    if event.sender_id == MY_USER_ID:
        sustext = event.pattern_match.group(1).strip()
        sussytext = f"""
< {sustext} >
   \\
     \\  .- - - - -.
     .- - - -.      \\
    (          )   + - -\\
     `- - - -´     |       |
       |            |       |
       |     _     + - -/
       \\_/    \\_/
"""
        await event.edit(sussytext)
'''
# what could i      do nexttttt ??????
r"""
@SPY(pattern=r'!!WTF')
async def wtf(e):
    if e.sender_id == MY_USER_ID:
        big = r'''
\                /
  \    /\    /
    \/    \/

  _ _ _ _ _
         |
         |
         |
         |

  _ _ _ _ _
  |
  |
  |- - - - 
  |
  |
'''
        await e.edit('WTF')
        await asyncio.sleep(1)
        await e.edit(big)



@SPY(pattern=r'!!lol')
async def brother(board):
    if board.sender_id == MY_USER_ID:
        sigmaboard = r'''
,_             _ _        _
|  |         /   _  \    |  |
|  |        |   |  |   |   |  |
|  |        |   |  |   |   |  |
|  |_ _ _ |   |_|   |   |  |_ _ _
|_ _ _ _| \ _ _ /    |_ _ _ _|
'''
#sigma sigmaboard sigmaboard sigmaboard
# SigmaBoard will do:
        await board.edit('LOL')
        await asyncio.sleep(1)
        await board.edit(sigmaboard)

@SPY(outgoing=True, pattern=r'!!wtf')
async def wtfbrother(board):
    sigmaboard = r'''
,                   _ _ _ _   _ _ _ _
\               /      |        |
  \    /\    /        |        |- - -
    \/    \/          |        |
'''
#sigma sigmaboard sigmaboard sigmaboard
# SigmaBoard will do:
    #await board.edit('LOL')
    #await asyncio.sleep(1)
    await board.edit(sigmaboard)
"""
@SPY(outgoing=True,pattern=r'!!pfp ?(\S+)? ?(\d+)?')
async def pfp(event):
    await event.edit('Getting pfp...')
    user_id = None
    limit = None
    msg = event.pattern_match.group(1)

    if msg:
        if msg[0] == "@":
            user_id = msg.strip()
        elif len(msg) < 5:
            limit = msg
        else:
            user_id = int(msg.strip())
    if event.is_reply and not user_id:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id

    if event.pattern_match.group(2):
        limit = int(event.pattern_match.group(2).strip())

    if user_id:
        try:
            user = await bot.get_entity(user_id)
            photos = await bot.get_profile_photos(user, limit=limit)
            if photos:
                await event.edit('Sending...️')
                await event.reply(file=photos)
                await event.edit('✅️')
                await asyncio.sleep(4)
                await event.delete()
            else:
                await event.edit("Can't get pfp:\nThis user has no pfp.")
                await asyncio.sleep(3)
                await event.delete()
        except Exception as e:
            await event.edit(f"Error: {e}")
            await asyncio.sleep(1)
            await event.delete()
    else:
        await event.edit("Please provide a username, user ID or reply to a user's message.")
        await asyncio.sleep(1)
        await event.delete()



"""
@SPY(pattern=r'!!pd (.+)')
async def pdhell(event):
    if event.sender_id == MY_USER_ID:
        cmd = event.pattern_match.group(1).strip()
        try:
            # Define the command to run within proot-distro
            proot_cmd = f'proot-distro login --user soth archlinux -- bash -c "{cmd}" 2>/dev/null'

            # Execute the command using Popen
            process = SSSU(proot_cmd, shell=True, stdout=PIPE, stderr=STDOUT, text=True)
            output, error = process.communicate()

            # Combine output and error into the response
            response = f'```\n$ {cmd}\n{output}{error if error else ""}\n```'

            await event.edit(response)
        except Exception as e:
            await event.edit(f'Error: {e}')
"""


@SPY(outgoing=True, pattern=r'!!flet (.+)')
async def ascii_ub(event):
    import pyfiglet
    # Get the text after the command
    text = event.pattern_match.group(1)
    if text:
        ascii_art = pyfiglet.figlet_format(text)
        #await event.edit(f"```\n{ascii_art}\n```", parse_mode='markdown')
        #figleet = '.\n' + Q(M(ascii_art))
        no_text = r"&#x00AD;"
        figleet = Q(M(no_text)+M(FIX(ascii_art)))
        await event.edit(figleet, parse_mode='html')
        #await event.delete()
    else:
        await event.edit("Please provide some text to convert to ASCII art!")
        await asyncio.sleep(1)
        await event.delete()
        
@SPY(outgoing=True, pattern=r'!!emj')
async def emoji_func(E):
    id = str(ID(E))
    if id == str(MY_USER_ID): L = await E.edit('Choosing random emoji...')
    elif id in GS() or id in GIS(): L = await E.reply('Choosing random emoji...')
    else: return
    emojis = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😭", "😉", "😗", "😙", "😚", "😘", "🥰", "😍", "🤩", "🥳", "🫠", "🙃", "🙂", "🥲", "🥹", "😊", "☺️", "😌", "🙂‍↕️", "🙂‍↔️", "😏", "🤤", "😋", "😛", "😝", "😜", "🤪", "🥴", "😔", "🥺", "😬", "😑", "😐", "😶", "😶‍🌫️", "🫥", "🤐", "🫡", "🤔", "🤫", "🫢", "🤭", "🥱", "🤗", "🫣", "😱", "🤨", "🧐", "😒", "🙄", "😮‍💨", "😤", "😠", "😡", "🤬", "😞", "😓", "😟", "😥", "😢", "☹️", "🙁", "🫤", "😕", "😰", "😨", "😧", "😦", "😮", "😯", "😲", "😳", "🤯", "😖", "😣", "😩", "😫", "😵", "😵‍💫", "🫨", "🥶", "🥵", "🤢", "🤮", "😴", "😪", "🤧", "🤒", "🤕", "😷", "🤥", "😇", "🤠", "🤑", "🤓", "😎", "🥸", "🤡", "😈", "👿", "👻", "💀", "☠️", "👹", "👺", "🎃", "💩", "🤖", "👽", "👾", "🌚", "🌝", "🌞", "🌛", "🌜", "🙈", "🙉", "🙊", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "💫", "⭐", "🌟", "✨", "💥", "💨", "💦", "💤", "🕳️", "🔥", "💯", "🎉", "❤️", "🧡", "💛", "💚", "🩵", "💙", "💜", "🤎", "🖤", "🩶", "🤍", "🩷", "💘", "💝", "💖", "💗", "💓", "💞", "💕", "💌", "💟", "♥️", "❣️", "❤️‍🩹", "💔", "❤️‍🔥", "💋", "🫂", "👥", "👤", "🗣️", "👣", "🧠", "🫀", "🫁", "🦠", "🦷", "🦴", "👀", "👁️", "👄", "🫦", "👅", "👃"]
    emoji = random.choice(emojis)
    await asyncio.sleep(1)
    await L.edit(f"Random emoji chosen: {emoji}")
    await asyncio.sleep(3)
    await L.edit(emoji)





@SPY(pattern=r'!!char (.+)')
async def char(event):
    if event.sender_id == MY_USER_ID:
        input_str = event.pattern_match.group(1).strip()
        base_path = os.path.expanduser('/data/data/com.termux/files/home/tgbot/sticker/abc/blue/')
        space_sticker = os.path.join(base_path, 'space.webp')
        await event.edit(f'character: {input_str}')
        
        for char in input_str:
            if char.isalpha():  # Check if the character is a letter
                sticker_path = os.path.join(base_path, f'{char.lower()}.tgs')
                if os.path.exists(sticker_path):
                    await event.reply(file=sticker_path)
                else:
                    await event.edit(f'Sticker for "{char}" not found.')
            elif char == ' ':  # Check if the character is a space
                if os.path.exists(space_sticker):
                    await event.reply(file=space_sticker)
                else:
                    await event.edit('Space sticker not found.')
        await event.edit(f'bomb! {input_str}')
        await asyncio.sleep(1)
        await event.delete()
        

"""Initialize ChatterBot"""
#chatbot = ChatBot('TelethonBot')
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the bot with the English corpus data
#trainer.train("chatterbot.corpus.english")

#@SPY(outgoing=True, pattern=r"^/ai")
#async def chat(E):
#    user_message = E.message.message[len("/ai "):]  # Extract the message text
#    response = chatbot.get_response(user_message)  # Get a response from ChatterBot
#    await E.edit(str(response))  # Send the response back as a reply




@SPY(pattern=r'!!ts (\w+) (.+)')
async def text(event):
    if event.sender_id == MY_USER_ID:
        font_name = event.pattern_match.group(1).strip()
        text_message = event.pattern_match.group(2).strip()
        await event.edit(f'Text Sticker {font_name}.ttf {text_message}')

        
        # Define font directory
        font_directory = os.path.expanduser('/data/data/com.termux/files/home/tgbot/sticker/font/')
        font_path = os.path.join(font_directory, f'{font_name}.ttf')
        
        # Check if the specified font exists
        if not os.path.exists(font_path):
            # List all available fonts if the specified font is not found
            available_fonts = [f for f in os.listdir(font_directory) if f.endswith('.ttf')]
            await event.edit(f"Font '{font_name}' not found. Available fonts:\n" + "\n".join(available_fonts))
            await asyncio.sleep(5)
            await event.delete()
            return
        
        # Define initial dimensions and font size
        initial_height = 512
        font_size = 300
        
        # Create a transparent image with initial width (adjusted later)
        image = Image.new('RGBA', (1000, initial_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path, font_size)
        
        # Dynamically adjust font size
        while True:
            bbox = draw.textbbox((0, 0), text_message, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            if text_width < 10000 - 20 and text_height < initial_height - 20:
                break
            font_size -= 2
            font = ImageFont.truetype(font_path, font_size)
        
        # Resize the image to fit the text width
        final_width = text_width + 20
        final_height = max(text_height + 20, initial_height)
        image = image.resize((final_width, final_height))
        draw = ImageDraw.Draw(image)
        
        # Calculate text position and draw it on the image
        text_x = (final_width - text_width) // 2
        text_y = (final_height - text_height) // 2
        draw.text((text_x, text_y), text_message, font=font, fill=(255, 255, 255, 255))
        
        # Save the image as WebP
        file_path = os.path.expanduser('/data/data/com.termux/files/home/tgbot/sticker/proc/text_sticker.webp')
        image.save(file_path, 'WEBP')
        
        # Send the sticker
        repl_msg = await event.get_reply_message()
        if repl_msg:
            await repl_msg.reply(file=file_path)
        else:
            await event.reply(file=file_path)
        
        # Delete the file after sending
        if os.path.exists(file_path):
            os.remove(file_path)
        await asyncio.sleep(1)
        await event.delete()




@SPY(pattern=r'(?s)!!th (.+)')
async def tweb(event):
    if event.sender_id == MY_USER_ID:
        text_message = event.pattern_match.group(1).strip()
        await event.edit(f'Text HTML: {text_message}\nFile Name: {text_message}.html')
        
        # HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{text_message}</title>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(45deg, #ff7e5f, #feb47b, #86a8e7, #91eae4, #f8b500, #ff3cac, #20E2D7, #FA709A);
                    background-size: 800% 800%;
                    animation: gradientAnimation 13.5s ease infinite;
                }}
                @keyframes fadeInScale {{
                    0% {{
                        opacity: 0;
                        transform: scale(0.5);
                    }}
                    70% {{
                        opacity: 1;
                        transform: scale(1.2);
                    }}
                    100% {{
                        transform: scale(1);
                    }}
                }}
                @keyframes gradientAnimation {{
                    0% {{
                        background-position: 0% 50%;
                    }}
                    50% {{
                        background-position: 100% 50%;
                    }}
                    100% {{
                        background-position: 0% 50%;
                    }}
                }}
                .fade-in-scale {{
                    font-size: calc(4em + 4vw);
                    max-width: 100%;
                    max-height: 100%;
                    overflow: hidden;
                    word-wrap: break-word;
                    animation: fadeInScale 1.8s ease-in-out;
                }}
            </style>
        </head>
        <body>
            <h1 class="fade-in-scale">{text_message}</h1>
        </body>
        </html>
        """
        
        # Save HTML to a file
        file_path = os.path.expanduser(f'/data/data/com.termux/files/home/tgbot/sticker/proc/{text_message}.html')
        with open(file_path, 'w') as file:
            file.write(html_template)
        
        # Send the HTML file
        repl_msg = await event.get_reply_message()
        if repl_msg:
            await repl_msg.reply(file=file_path)
        else:
            await event.reply(file=file_path)
        
        # Delete the file after sending
        if os.path.exists(file_path):
            os.remove(file_path)
        await asyncio.sleep(1)
        await event.delete()

@SPY(pattern=r'(?s)!!teh (.+)')
async def teveweb(event):
    if event.sender_id == MY_USER_ID:
        text_message = event.pattern_match.group(1).strip()
        await event.edit(f'Text Everything HTML: {text_message}\nFile Name: {text_message}.html')
        
        # HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{text_message}</title>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
            <style>
                :root {{
                    --primary-color: #6200ea;
                    --background-color: #e0e0e0;
                    --text-color: #333;
                    --card-background: #e0e0e0;
                    --box-shadow-light: #ffffff;
                    --box-shadow-dark: #bebebe;
                }}
                @media (prefers-color-scheme: dark) {{
                    :root {{
                        --primary-color: #bb86fc;
                        --background-color: #121212;
                        --text-color: #e0e0e0;
                        --card-background: #1e1e1e;
                        --box-shadow-light: #2c2c2c;
                        --box-shadow-dark: #000000;
                    }}
                }}
                body {{
                    font-family: 'Roboto', sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: var(--background-color);
                    color: var(--text-color);
                    line-height: 1.6;
                    overflow-y: scroll;
                    scroll-behavior: smooth;
                }}
                h1, h2, h3 {{
                    color: var(--text-color);
                }}
                h1 {{
                    font-size: 2.5em;
                    margin-bottom: 10px;
                }}
                h2 {{
                    font-size: 2em;
                    margin-top: 40px;
                    margin-bottom: 10px;
                    border-bottom: 2px solid var(--primary-color);
                    display: inline-block;
                    padding-bottom: 5px;
                }}
                h3 {{
                    font-size: 1.5em;
                    margin-top: 30px;
                    margin-bottom: 10px;
                }}
                .code {{
                    background-color: var(--card-background);
                    border-radius: 8px;
                    padding: 15px;
                    font-family: 'Courier New', Courier, monospace;
                    overflow-x: auto;
                    margin: 20px 0;
                    box-shadow: 4px 4px 8px var(--box-shadow-dark), -4px -4px 8px var(--box-shadow-light);
                }}
                pre {{
                    margin: 0;
                }}
                p {{
                    margin-bottom: 15px;
                }}
                a {{
                    color: var(--primary-color);
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .neumorphism-card {{
                    background: var(--card-background);
                    border-radius: 10px;
                    box-shadow: 20px 20px 60px var(--box-shadow-dark), -20px -20px 60px var(--box-shadow-light);
                    padding: 20px;
                    margin-bottom: 20px;
                    opacity: 0;
                    transform: scale(0.8);
                    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
                }}
                .neumorphism-card.visible {{
                    opacity: 1;
                    transform: scale(1);
                }}
                .neumorphism-card.hidden {{
                    opacity: 0;
                    transform: scale(0.8);
                }}
            </style>
        </head>
        <body>
            <div class="neumorphism-card">
                <h1>{text_message}</h1>
                <p>{text_message}</p>
            </div>
    
            <div class="neumorphism-card">
                <h2>Getting Started</h2>
                <p>{text_message}</p>
            </div>
    
            <div class="neumorphism-card">
                <h3>Prerequisites</h3>
                <p>{text_message}</p>
            </div>
    
            <div class="neumorphism-card">
                <h3>Installation</h3>
                <p>{text_message}</p>
                <div class="code">
                    <pre>
# {text_message}
{text_message}
{text_message}
{text_message}
                </div>
            </div>

            <div class="neumorphism-card">
                <h2>Usage</h2>
                <p>{text_message}</p>
                <div class="code">
                    <pre>
# {text_message}
{text_message}
                    </pre>
                </div>
            </div>
    
            <div class="neumorphism-card">
                <h2>Contributing</h2>
                <p>{text_message}</p>
            </div>
    
            <div class="neumorphism-card">
                <h2>License</h2>
                <p>{text_message}</p>
            </div>

            <script>
                const observer = new IntersectionObserver((entries) => {{
                    entries.forEach(entry => {{
                        if (entry.isIntersecting) {{
                            entry.target.classList.add('visible');
                            entry.target.classList.remove('hidden');
                        }} else {{
                            entry.target.classList.add('hidden');
                            entry.target.classList.remove('visible');
                        }}
                    }});
                }});

                document.querySelectorAll('.neumorphism-card').forEach(card => {{
                    observer.observe(card);
                }});
            </script>
        </body>
        </html>
        """
        
        # Save HTML to a file
        file_path = os.path.expanduser(f'/data/data/com.termux/files/home/tgbot/sticker/proc/{text_message}.html')
        with open(file_path, 'w') as file:
            file.write(html_template)
        
        # Send the HTML file
        repl_msg = await event.get_reply_message()
        if repl_msg:
            await repl_msg.reply(file=file_path)
        else:
            await event.reply(file=file_path)
        
        # Delete the file after sending
        if os.path.exists(file_path):
            os.remove(file_path)
        await asyncio.sleep(1)
        await event.delete()



@SPY(outgoing=True,pattern=r'(?s)!!tsbgh (.+)')
async def txtshakbgweb(event):
    if event.sender_id == MY_USER_ID:
        text_parts = event.pattern_match.group(1).split('|')
        welcome_text = text_parts[0].strip()
        bglinkk = [
            'https://images.pexels.com/photos/2327372/pexels-photo-2327372.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/1819650/pexels-photo-1819650.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/18499547/pexels-photo-18499547/free-photo-of-view-of-seceda-in-dolomites-italy.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/1670187/pexels-photo-1670187.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/15959850/pexels-photo-15959850/free-photo-of-view-of-the-chapmans-peak-cape-town-south-africa.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/9085049/pexels-photo-9085049.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
            ]
        random.seed()
        bgll = random.choice(bglinkk)
        bgl = bgll
        description_text = text_parts[1].strip() if len(text_parts) > 1 else ""
        await event.edit(f'Text On Shaking Blur Background HTML\nFile: {welcome_text}\nTitle: {welcome_text}\nDescription: {description_text}\nBackground: {bgl}')
        
        # HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{welcome_text}</title>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    padding: 2rem;
                    font-family: 'Arial', sans-serif;
                    background: url('{bgl}') no-repeat center center/cover;
                    animation: shake 0.5s;
                    animation-iteration-count: infinite;
                    }}

                    @keyframes shake {{
                    0% {{ transform: translate(1px, 1px) rotate(0deg); }}
                    10% {{ transform: translate(-1px, -2px) rotate(-1deg); }}
                    20% {{ transform: translate(-3px, 0px) rotate(1deg); }}
                    30% {{ transform: translate(3px, 2px) rotate(0deg); }}
                    40% {{ transform: translate(1px, -1px) rotate(1deg); }}
                    50% {{ transform: translate(-1px, 2px) rotate(-1deg); }}
                    60% {{ transform: translate(-3px, 1px) rotate(0deg); }}
                    70% {{ transform: translate(3px, 1px) rotate(-1deg); }}
                    80% {{ transform: translate(-1px, -1px) rotate(1deg); }}
                    90% {{ transform: translate(1px, 2px) rotate(0deg); }}
                    100% {{ transform: translate(1px, -2px) rotate(-1deg); }}
                    }}

                .glass {{
                    backdrop-filter: blur(10px);
                    background: rgba(255, 255, 255, 0.2);
                    border-radius: 10px;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                    padding: 2rem;
                    text-align: center;
                    animation: fadeIn 1s ease-in-out;
                    max-width: 95%;
                    width: auto;
                    min-width: 0;
                    word-wrap: break-word;
                    overflow-y: auto;
                    max-height: 80vh;
                }}

                @keyframes fadeIn {{
                    0% {{
                        opacity: 0;
                        transform: scale(0);
                    }}
                    55% {{
                        opacity: 1;
                        transform: scale(1.2);
                    }}
                    80% {{
                        opacity: 1;
                        transform: scale(0.9);
                    }}
                    100% {{
                        transform: scale(1);
                    }}
                }}

                @keyframes fadeIn5 {{
                    0% {{
                        opacity: 0;
                        transform: scale(0);
                        filter: blur(20px);
                    }}
                    40% {{
                        opacity: 0;
                    }}
                    55% {{
                        opacity: 1;
                        transform: scale(1.6);
                        filter: blur(25px);
                    }}
                    100% {{
                        opacity: 1;
                        transform: scale(1);
                        filter: blur(0px);
                    }}
                }}
                @keyframes fadeIn2 {{
                    0% {{
                        opacity: 0;
                        transform: scale(0);
                        filter: blur(20px);
                    }}
                    40% {{
                        opacity: 0;
                    }}
                    55% {{
                        opacity: 1;
                        transform: scale(1.5) translateY(100px);
                        filter: blur(15px);
                    }}
                    100% {{
                        opacity: 1;
                        transform: scale(1);
                        filter: blur(0px);
                    }}
                }}
                
                h1 {{
                    color: #ffffff;
                    animation: fadeIn5 1.2s ease-in-out;
                }}

                ul {{
                    list-style: none;
                    padding: 0;
                    animation: fadeIn2 1.4s ease-in-out;
                }}

                li {{
                    margin: 0.5rem 0;
                    font-size: 1.2rem;
                    color: #ffffff;
                }}
            </style>
        </head>
        <body>
            <div class="glass">
                <h1>{welcome_text}</h1>
                <ul>
                    <li>
                        <p>{description_text}</p>
                    </li>
                </ul>
            </div>
        </body>
        </html>
        """
        
        # Save HTML to a file
        file_path = os.path.expanduser(f'/data/data/com.termux/files/home/tgbot/sticker/proc/{welcome_text}.html')
        with open(file_path, 'w') as file:
            file.write(html_template)
        
        # Send the HTML file
        repl_msg = await event.get_reply_message()
        if repl_msg:
            await repl_msg.reply(file=file_path)
        else:
            await event.reply(file=file_path)
        
        # Delete the file after sending
        if os.path.exists(file_path):
            os.remove(file_path)
        await asyncio.sleep(1)
        await event.delete()

#@SPY(pattern=r'/tbgh (.+)')
#@SPY(pattern=r'/tbgh (.+)', flags=re.S)
@SPY(outgoing=True,pattern=r'(?s)!!tbghn (.+)')
async def txtbgwebnew(E):
    text_parts = E.pattern_match.group(1).split('|')
    welcome_text = FIX(text_parts[0].strip())
    bglinkk = [
        'https://images.pexels.com/photos/2327372/pexels-photo-2327372.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'https://images.pexels.com/photos/1819650/pexels-photo-1819650.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'https://images.pexels.com/photos/18499547/pexels-photo-18499547/free-photo-of-view-of-seceda-in-dolomites-italy.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'https://images.pexels.com/photos/1670187/pexels-photo-1670187.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'https://images.pexels.com/photos/15959850/pexels-photo-15959850/free-photo-of-view-of-the-chapmans-peak-cape-town-south-africa.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'https://images.pexels.com/photos/9085049/pexels-photo-9085049.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
    ]
    bgl = random.choice(bglinkk)
    description_text = FIX(text_parts[1].strip() if len(text_parts) > 1 else "")
    await E.edit(f"wt: {welcome_text}\ndt: {description_text}\nbg: {bgl}")
    html_template = f"""\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{welcome_text}</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  </head>
  <body>
    <div class="flex bg-fixed drop-shadow-xl/100 touch-pan-y justify-center dark:brightness-70 bg-cover place-items-center w-screen h-screen bg-[url({bgl})]">
      <div class="anime1 drop-shadow-xl/25 border-3 border-white/10 dark:border-black/5 relative bg-white/10 dark:bg-black/10 backdrop-blur-md justify-center overflow-hidden rounded-4xl h-[80vh] w-85">
        <div class="anime2">
          <h1 class="font-bold z-100 mt-6 mb-3 text-black dark:text-white text-center text-4xl">{welcome_text}</h1>
          <p class="anime3 text-wrap mx-5 mb-5 text-2xl mt-[0px] text-black dark:text-white">{description_text}</p>
        </div>
      </div>
    </div>
    <script type="module">
      import {{ animate, createDraggable, createSpring }} from 'https://cdn.jsdelivr.net/npm/animejs/+esm';
      let bottom = 0;
      const popUpHeight = document.querySelector('.anime1').offsetHeight;
      const textHeight = document.querySelector('.anime2 .anime3').getBoundingClientRect().height;
      if (textHeight + 100 > popUpHeight) {{ bottom = textHeight - popUpHeight + 110 }}
      createDraggable(".anime2", {{ container: [-bottom, 0, 0, 0], releaseContainerFriction: 0, releaseStiffness: 5, containerFriction: 0, releaseEase: createSpring({{ stiffness: 125 }}) }});
      if (textHeight < popUpHeight) {{ animate(".anime1", {{ height: textHeight + 110 , duration: 0 }})}}
      animate(".anime1", {{ scale: {{ from: 0 }}, ease: 'outElastic(1, .45)', duration: 2000 }});
    </script>
  </body>
</html>"""
    file_path = os.path.expanduser(f'/data/data/com.termux/files/home/tgbot/sticker/proc/{welcome_text}.html')
    with open(file_path, 'w') as file:
        file.write(html_template)
    repl_msg = await E.get_reply_message()
    if repl_msg:
        await repl_msg.reply(file=file_path)
    else:
        await E.reply(file=file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
    await E.delete()

@SPY(outgoing=True,pattern=r'(?s)!!tbgh (.+)')
async def txtbgweb(event):
    if event.sender_id == MY_USER_ID:
        text_parts = event.pattern_match.group(1).split('|')
        welcome_text = text_parts[0].strip()
        bglinkk = [
            'https://images.pexels.com/photos/2327372/pexels-photo-2327372.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/1819650/pexels-photo-1819650.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/18499547/pexels-photo-18499547/free-photo-of-view-of-seceda-in-dolomites-italy.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/1670187/pexels-photo-1670187.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/15959850/pexels-photo-15959850/free-photo-of-view-of-the-chapmans-peak-cape-town-south-africa.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
            'https://images.pexels.com/photos/9085049/pexels-photo-9085049.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
            ]
        random.seed()
        bgll = random.choice(bglinkk)
        bgl = bgll
        description_text = text_parts[1].strip() if len(text_parts) > 1 else ""
        await event.edit(f'Text On Blur Background HTML\nFile: {welcome_text}\nTitle: {welcome_text}\nDescription: {description_text}\nBackground: {bgl}')
        
        # HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{welcome_text}</title>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    padding: 2rem;
                    font-family: 'Arial', sans-serif;
                    background: url('{bgl}') no-repeat center center/cover;
                }}

                .glass {{
                    backdrop-filter: blur(10px);
                    background: rgba(255, 255, 255, 0.2);
                    border-radius: 10px;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                    padding: 2rem;
                    text-align: center;
                    animation: fadeIn 1s ease-in-out;
                    max-width: 95%;
                    width: auto;
                    min-width: 0;
                    word-wrap: break-word;
                    overflow-y: auto;
                    max-height: 80vh;
                }}

                @keyframes fadeIn {{
                    0% {{
                        opacity: 1;
                        transform: scale(0);
                        filter: blur(20px);
                    }}
                    55% {{
                        opacity: 1;
                        transform: scale(1.2);
                        filter: blur(0px);
                    }}
                    80% {{
                        opacity: 1;
                        transform: scale(0.9);
                    }}
                    100% {{
                        transform: scale(1);
                    }}
                }}

                @keyframes fadeIn5 {{
                    0% {{
                        opacity: 0;
                        transform: scale(0);
                        filter: blur(20px);
                    }}
                    40% {{
                        opacity: 0;
                    }}
                    55% {{
                        opacity: 1;
                        transform: scale(1.6);
                        filter: blur(25px);
                    }}
                    100% {{
                        opacity: 1;
                        transform: scale(1);
                        filter: blur(0px);
                    }}
                }}
                @keyframes fadeIn2 {{
                    0% {{
                        opacity: 0;
                        transform: scale(0);
                        filter: blur(20px);
                    }}
                    40% {{
                        opacity: 0;
                    }}
                    55% {{
                        opacity: 1;
                        transform: scale(1.5) translateY(100px);
                        filter: blur(15px);
                    }}
                    100% {{
                        opacity: 1;
                        transform: scale(1);
                        filter: blur(0px);
                    }}
                }}
                
                h1 {{
                    color: #ffffff;
                    animation: fadeIn5 1.2s ease-in-out;
                }}

                ul {{
                    list-style: none;
                    padding: 0;
                    animation: fadeIn2 1.4s ease-in-out;
                }}

                li {{
                    margin: 0.5rem 0;
                    font-size: 1.2rem;
                    color: #ffffff;
                }}
            </style>
        </head>
        <body>
            <div class="glass">
                <h1>{welcome_text}</h1>
                <ul>
                    <li>
                        <p>{description_text}</p>
                    </li>
                </ul>
            </div>
        </body>
        </html>
        """
        
        # Save HTML to a file
        file_path = os.path.expanduser(f'/data/data/com.termux/files/home/tgbot/sticker/proc/{welcome_text}.html')
        with open(file_path, 'w') as file:
            file.write(html_template)
        
        # Send the HTML file
        repl_msg = await event.get_reply_message()
        if repl_msg:
            await repl_msg.reply(file=file_path)
        else:
            await event.reply(file=file_path)
        
        # Delete the file after sending
        if os.path.exists(file_path):
            os.remove(file_path)
        await asyncio.sleep(1)
        await event.delete()


@SPY(outgoing=True, pattern='!!fload')
async def typewriter(typew):
	await typew.edit("`start loading...`")
	sleep(1)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "%   ▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   █████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ██████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▊")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ███████████████▉")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▎")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▍")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	number = number+ 1
	sleep(0.03)
	await typew.edit(str(number) + "%   ████████████████▌")
	sleep(1)
	await typew.edit("`Done!`")
	sleep(3)
	await typew.delete()


@SPY(outgoing=True, pattern=r'!!vidrz (\d+) (\d+) ?(r)?')
async def videoresizer(event):
    from moviepy import VideoFileClip
    match = event.pattern_match
    width = int(match.group(1))
    height = int(match.group(2))
    reply_flag = match.group(3)
    reply_msg = await event.get_reply_message()
    await event.edit(f'Video Resizer\nWidth: {width}\nHeight: {height}\n(Downloading...)')
       
    if event.is_reply:
        if reply_msg.media:
            try:
                video = await bot.download_media(reply_msg.media, '/data/data/com.termux/files/home/tgbot/sticker/proc/temp_video.mp4')
                await event.edit(f'Video Resizer\nWidth: {width}\nHeight: {height}\n(Resizing...)')
            
               # Load your video
                clip = VideoFileClip('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_video.mp4')
               
               # Resize the video
                clip = clip.resized((width, height))
               
               # Save the resized video
                clip.write_videofile('/data/data/com.termux/files/home/tgbot/sticker/proc/video_resized.mp4', codec='libx264', audio_codec='aac')
                await event.edit(f'Video Resizer\nWidth: {width}\nHeight: {height}\n(Sending...)')
               # Upload the resized video
                if reply_flag == 'r':
                    await bot.send_file(event.chat_id, '/data/data/com.termux/files/home/tgbot/sticker/proc/video_resized.mp4', reply_to=reply_msg.id, attributes=[
                        types.DocumentAttributeVideo(
                            duration=int(clip.duration),
                            w=clip.w,
                            h=clip.h,
                            round_message=False,
                            supports_streaming=True
                        )
                    ])
                elif not reply_flag:
                    await bot.send_file(event.chat_id, '/data/data/com.termux/files/home/tgbot/sticker/proc/video_resized.mp4', reply_to=event.id, attributes=[
                        types.DocumentAttributeVideo(
                            duration=int(clip.duration),
                            w=width,
                            h=height,
                            round_message=False,
                            supports_streaming=True
                        )
                    ])
                await event.edit("Video resized and uploaded successfully!")
            except Exception as e:
                print(e)
                try:
                    await event.edit(e)
                except Exception as e:
                    print(e)
               
               # Clean up the temporary files
            try:
                os.remove('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_video.mp4')
            except: pass
            try:
                os.remove('/data/data/com.termux/files/home/tgbot/sticker/proc/video_resized.mp4')
            except: pass
    await asyncio.sleep(1)
    await event.delete()

#@SPY(outgoing=True, pattern=r'/vidrz (\d+) (\d+) ?(r)?')
#async def videoresizer(event):
    #match = event.pattern_match
    #width = int(match.group(1))
    #height = int(match.group(2))
    #reply_flag = match.group(3)
    #reply_msg = await event.get_reply_message()
    #await event.edit(f'Video Resizer\nWidth: {width}\nHeight: {height}\n(Downloading...)')

    #if event.is_reply:
        #if reply_msg.media:
            #try:
                #video_path = '/data/data/com.termux/files/home/tgbot/sticker/proc/temp_video.mp4'
                #resized_video_path = '/data/data/com.termux/files/home/tgbot/sticker/proc/video_resized.mp4'
                #video = await bot.download_media(reply_msg.media, video_path)
                #await event.edit(f'Video Resizer\nWidth: {width}\nHeight: {height}\n(Resizing...)')

                # Resize the video using ffmpeg noooooooo
                #subprocess.run([
                    #'ffmpeg', '-i', video_path, '-vf', f'scale={width}:{height}',
                    #'-c:a', 'aac', resized_video_path
                #])
                 # Resize the video using ffmpeg yes
                #cmd = [
                #    'ffmpeg', '-i', video_path, '-vf', f'scale={width}:{height}',
                #    '-c:a', 'aac', resized_video_path
                #]
                #process = SSSU(cmd, stdout=PIPE, stderr=STDOUT)
                #output, error = process.communicate()

                #if process.returncode != 0:
                    #raise Exception(f'Error during resizing: {output.decode()}')

                #await event.edit(f'Video Resizer\nWidth: {width}\nHeight: {height}\n(Sending...)')

                #if reply_flag == 'r':
                    #await bot.send_file(event.chat_id, resized_video_path, reply_to=reply_msg.id, attributes=[
                        #types.DocumentAttributeVideo(
                        #    duration=0,  # Set to 0 as a placeholder
                        #    w=width,
                        #    h=height,
                        #    round_message=False,
                        #    supports_streaming=True
                        #)
                    #])
                #else:
                    #await bot.send_file(event.chat_id, resized_video_path, reply_to=event.id, attributes=[
                        #types.DocumentAttributeVideo(
                            #duration=0,  # Set to 0 as a placeholder
                            #w=width,
                            #h=height,
                            #round_message=False,
                            #supports_streaming=True
                        #)
                    #])
                #await event.edit("Video resized and uploaded successfully!")
            
            #except Exception as e:
                #await event.edit(f"An error occurred: {str(e)}")
            
            #finally:
                #if os.path.exists(video_path):
                    #os.remove(video_path)
                #if os.path.exists(resized_video_path):
                    #os.remove(resized_video_path)
    #await asyncio.sleep(1)
    #await event.delete()
            

@SPY(outgoing=True, pattern=r'!!imarz (\d+) (\d+) ?(r)?')
async def imageresizer(event):
    match = event.pattern_match
    width = int(match.group(1))
    height = int(match.group(2))
    reply_flag = match.group(3)
    reply_msg = await event.get_reply_message()
    await event.edit(f'Image Resizer\nWidth: {width}\nHeight: {height}\n(Downloading...)')
       
    if event.is_reply:
        if reply_msg.media:
            image_path = await bot.download_media(reply_msg.media, '/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image')
               
               # Load your image and convert to PNG if necessary
            await event.edit(f'Image Resizer\nWidth: {width}\nHeight: {height}\n(Converting...)')
            with Image.open(image_path) as img:
                if img.format in ['JPEG', 'JPG', 'WEBP']:
                    img = img.convert('RGB' if img.format in ['JPEG', 'JPG'] else 'RGBA')
                    image_path = '/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image.png'
                    img.save(image_path)
                    img = Image.open(image_path)
                   
                   # Resize the image
                    await event.edit(f'Image Resizer\nWidth: {width}\nHeight: {height}\n(Resizing...)')
                    img = img.resize((width, height))
                   
                   # Save the resized image in PNG format
                    resized_image_path = '/data/data/com.termux/files/home/tgbot/sticker/proc/image_resized.png'
                    img.save(resized_image_path)
            await event.edit(f'Image Resizer\nWidth: {width}\nHeight: {height}\n(Sending...)')
               # Upload the resized video
            if reply_flag == 'r':
                await bot.send_file(event.chat_id, resized_image_path, reply_to=reply_msg.id)
            elif not reply_flag:
                await bot.send_file(event.chat_id, resized_image_path, reply_to=event.id)
            await event.edit("Image resized and uploaded successfully!")
            #await asyncio.sleep(1)
            #await event.delete()
               # Clean up the temporary files
            os.remove(image_path)
            os.remove(resized_image_path)
            if os.path.exists('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image.png'):
                os.remove('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image.png')
            if os.path.exists('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image.webp'):
                os.remove('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image.webp')
            if os.path.exists('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image.jpg'):
                os.remove('/data/data/com.termux/files/home/tgbot/sticker/proc/temp_image.jpg')
            #directory = os.path.expanduser('/data/data/com.termux/files/home/tgbot/sticker/proc/')
            #delete_all_files_in_directory(directory)
            await asyncio.sleep(1)
    await event.delete()

@SPY(outgoing=True, pattern='!!bin (.+)')
async def text_to_binary_handler(event):
    text = event.pattern_match.group(1)
    binary = ' '.join(format(ord(char), '08b') for char in text)
    await event.edit(binary)

@SPY(outgoing=True, pattern='!!dbin ?(.+)?')
async def binary_to_text_handler(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
        binary = reply_message.raw_text
    else:
        binary = event.pattern_match.group(1)
    text = ''.join(chr(int(b, 2)) for b in binary.split(' '))
    await event.edit(text)

#@bot.on(events.NewMessage(pattern='/tts'))
@SPY(outgoing=True, pattern='!!tts')
async def tts(event):
    message = event.message
    args = event.text.split()[1:]
    delmsg = ""

    if message.is_reply:
        delmsg = await message.get_reply_message()
        delmsg = delmsg.text

    if args:
        delmsg = " ".join(args).lower()

    if delmsg:
        await event.edit(f'TTS: {delmsg}')
        current_time = datetime.datetime.strftime(datetime.datetime.now(), "%d.%m.%Y %H:%M:%S")
        filename = datetime.datetime.now().strftime("%d%m%y-%H%M%S%f") + ".mp3"
        lang = "ml"
        tts = gTTS(delmsg, lang)
        tts.save(filename)

        with open(filename, "rb") as speech:
            file_bytes = speech.read()

        if os.path.getsize(filename) == 0:
            lang = "en"
            tts = gTTS(delmsg, lang)
            tts.save(filename)
            with open(filename, "rb") as speech:
                file_bytes = speech.read()

        reply_msg = await event.get_reply_message()
        if reply_msg:
            await bot.send_file(event.chat_id, filename, voice_note=True, reply_to=reply_msg.id)
        else:
            await bot.send_file(event.chat_id, filename, voice_note=True, reply_to=event.id)
        os.remove(filename)
        await asyncio.sleep(1)
        await event.delete()
    else:
        await event.delete()

normiefont = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z",
]

weebyfont = [
    "卂", "乃", "匚", "刀", "乇", "下", "厶", "卄", "工", "丁", "长", "乚", "从", "𠘨", 
    "口", "尸", "㔿", "尺", "丂", "丅", "凵", "リ", "山", "乂", "丫", "乙",
]

@SPY(outgoing=True, pattern='!!wbf')
async def weebify(event):
    args = event.message.message.split()[1:]  # Split message to get arguments
    string = "  ".join(args).lower() if args else ""
    
    if event.is_reply and not string:
        reply_message = await event.get_reply_message()
        string = reply_message.text.lower().replace(" ", "  ")


    for normiecharacter in normiefont:
        if normiecharacter in string:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    reply_msg = await event.get_reply_message()
    if event.is_reply:
        await reply_msg.reply(string)
    else:
        await event.reply(string)
        await asyncio.sleep(1)
    
    
    await event.delete()

STICK = 'Stickers'
SPLIT_TRIG = r'!!split '
DEF['%%'] = lambda *a,**k: types.MessageEntityBlockquote(*a,**k,collapsed=True)

def N(t): return f'`{t}`'
def R(t): return f'%%{t}%%'
async def EEDD(E,t,e=False): await (E.edit(R(N(t))) if e else E.edit(Q(M(t)), parse_mode='HTML'))
async def ST(f): await bot.send_message(STICK, file=f, force_document=True)
async def PM(a):
    for t in a:
        await bot.send_message(STICK, t)
        await asyncio.sleep(2)

"""Split Image Into Pack"""
@SPY(outgoing=True, pattern=SPLIT_TRIG)
async def split(E):
    try:
        await EEDD(E, 'Creating...')
        t = T(E)
        a = t.split()[1:]
        name = ' '.join(a[2:])
        await PM(('/cancel', '/newpack', name))
        s = int(a[0])
        await EEDD(E, 'Downloading media...')
        i = Image.open(BIO(await (await GR(E)).download_media(bytes)))
        await EEDD(E, 'Resizing...')
        i = thumb(i, 512)
        await EEDD(E, 'Creating pack...')
        uid = ('split_' + str(UID())).replace('-', '_')
        info = Q(M(f'Name: {name}\nEmoji: {a[1]}\nSticker size: {s}*{s}\n'))

        w, h = i.size
        gs = 5
        sq_w = w // gs
        sq_h = h // gs

        n = 0
        at = []
        for row in range(gs):
            for col in range(gs):
                st = time()
                n += 1

                left = col * sq_w
                upper = row * sq_h
                right = left + sq_w if col < gs - 1 else w
                lower = upper + sq_h if row < gs - 1 else h
                cropped = i.crop((left, upper, right, lower))
                resized = cropped.resize((512, 512), Image.Resampling.LANCZOS)

                b = BIO()
                resized.save(b, format="WEBP")
                b.name = f'part_{n}.webp'
                b.seek(0)

                await ST(b)
                await PM((a[1]))

                at.append(time()-st)
                avg = len(at)/sum(at)
                eta = (25-n)*(avg**-1)

                art = f"{'■'*n}{'□'*(25-n)} [{n}/25]"
                omg = f"{str(avg)[:5]} IMG/s [{str(eta)[:5]}s]"
                pro = Q(M(f'Adding stickers...\n{art}\n{omg}'))

                await E.edit(info+pro, parse_mode='HTML')

        await PM(('/publish', '/skip', uid))
        l = f'https://t.me/addstickers/{uid}'
        res = Q(M(f'Time spent: {str(sum(at))[:7]}s\nStick pack: ')+f'<a href="{l}">{str(uid)[:8]}</a>')
        await E.edit(info+res, parse_mode='HTML')
    except Exception as e:
        await EEDD(E, f"Error: {str(e)}", True)

"""Generate A Square"""
def thumb(i, s):
    sf = max(s / i.width, s / i.height)
    expanded_size = (int(i.width * sf), int(i.height * sf))
    i = i.resize(expanded_size, Image.Resampling.LANCZOS)
    n = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    n.paste(i, ((s - i.width) // 2, (s - i.height) // 2))
    return n

@SPY(outgoing=True, pattern='(?s)!!cp ?(.+)?')
async def copyable(event):
    try:
        reply_msg = await event.get_reply_message()
        #print(formatted_output)'
        # Extract text after the command
        #final_text = event.message.message.split()[1:]
        final_text = event.pattern_match.group(1)
        if reply_msg and not final_text:
            final_text = reply_msg.text
        elif not reply_msg and not final_text:
            return
        #print("Final Text:", final_text)
        #final_text = ' '.join(text_parts)
        final_text = "".join("<code>"+char+"</code>" for char in final_text)
        #final_text = f"<code>{final_text}</code>"
        
        # Print the final text to check for any issues
        #print("Final Text:", final_text)
        
        reply_msg = await event.get_reply_message()
        if reply_msg:
            await bot.send_message(event.chat_id, final_text, parse_mode='HTML', reply_to=reply_msg.id)
        else:
            await bot.send_message(event.chat_id, final_text, parse_mode='HTML', reply_to=event.id)
    finally:
        await asyncio.sleep(1)
        await event.delete()

fun_strings = {
    "SLAP_TEMPLATES": [
        "{user1} slaps {user2} with {item}",
        "{user1} hits {user2} using {item}",
        "{user1} throws {item} at {user2}",
        "{user2} was killed by magic.",
        "{user2} starved without pats.",
        "{user2} was knocked into the void by {user1}.",
        "{user2} fainted.",
        "{user2} is out of usable Pokemon! {user2} whited out!.",
        "{user2} is out of usable Pokemon! {user2} blacked out!.",
        "{user2} got rekt.",
        "{user2}'s melon was split by {user1}.",
        "{user2} was sliced and diced by {user1}.",
        "{user2} played hot-potato with a grenade.",
        "{user2} was knifed by {user1}.",
        "{user2} ate a grenade.",
        "{user2} is what's for dinner!",
        "{user2} was terminated by {user1}.",
        "{user1} spammed {user2}'s email.",
        "{user1} RSA-encrypted {user2} and deleted the private key.",
        "{user1} put {user2} in the friendzone.",
        "{user1} slaps {user2} with a DMCA takedown request!",
        "{user2} got a house call from Doctor {user1}.",
        "{user1} beheaded {user2}.",
        "{user2} got stoned...by an angry mob.",
        "{user1} sued the pants off {user2}.",
        "{user2} was one-hit KO'd by {user1}.",
        "{user1} sent {user2} down the memory hole.",
        "{user2} was a mistake. - '{user1}' ",
        "{user2} was made redundant.",
        "{user1} {hits} {user2} with a bat!.",
        "{user1} {hits} {user2} with a Taijutsu Kick!.",
        "{user1} {hits} {user2} with X-Gloves!.",
        "{user1} {hits} {user2} with a Jet Punch!.",
        "{user1} {hits} {user2} with a Jet Pistol!.",
        "{user1} {hits} {user2} with a United States of Smash!.",
        "{user1} {hits} {user2} with a Detroit Smash!.",
        "{user1} {hits} {user2} with a Texas Smash!.",
        "{user1} {hits} {user2} with a California Smash!.",
        "{user1} {hits} {user2} with a New Hampshire Smash!.",
        "{user1} {hits} {user2} with a Missouri Smash!.",
        "{user1} {hits} {user2} with a Carolina Smash!.",
        "{user1} {hits} {user2} with a King Kong Gun!.",
        "{user1} {hits} {user2} with a baseball bat - metal one.!.",
        "*Serious punches {user2}*.",
        "*Normal punches {user2}*.",
        "*Consecutive Normal punches {user2}*.",
        "*Two Handed Consecutive Normal Punches {user2}*.",
        "*Ignores {user2} to let them die of embarassment*.",
        "*points at {user2}* What's with this sassy... lost child?.",
        "*Hits {user2} with a Fire Tornado*.",
        "{user1} pokes {user2} in the eye !",
        "{user1} pokes {user2} on the sides!",
        "{user1} pokes {user2}!",
        "{user1} pokes {user2} with a needle!",
        "{user1} pokes {user2} with a pen!",
        "{user1} pokes {user2} with a stun gun!",
        "{user2} is secretly a Furry!",
        "Hey Everybody! {user1} is asking me to be mean!",
        "( ･_･)ﾉ⌒●~* (･.･;) <-{user2}",
        "Take this {user2}\n(ﾉﾟДﾟ)ﾉ ))))●~* ",
        "Here {user2} hold this\n(｀・ω・)つ ●~＊",
        "( ・_・)ノΞ●~*  {user2}\nDieeeee!!.",
        "( ・∀・)ｒ鹵~<≪巛;ﾟДﾟ)ﾉ\n*Bug sprays {user2}*.",
        "( ﾟДﾟ)ﾉ占~<巛巛巛.\n-{user2} You pest!",
        "( う-´)づ︻╦̵̵̿╤── \\(˚☐˚”)/ {user2}.",
        "{user1} {hits} {user2} with a {item}.",
        "{user1} {hits} {user2} in the face with a {item}.",
        "{user1} {hits} {user2} around a bit with a {item}.",
        "{user1} {throws} a {item} at {user2}.",
        "{user1} grabs a {item} and {throws} it at {user2}'s face.",
        "{user1} launches a {item} in {user2}'s general direction.",
        "{user1} starts slapping {user2} silly with a {item}.",
        "{user1} pins {user2} down and repeatedly {hits} them with a {item}.",
        "{user1} grabs up a {item} and {hits} {user2} with it.",
        "{user1} ties {user2} to a chair and {throws} a {item} at them.",
        "{user1} gave a friendly push to help {user2} learn to swim in lava.",
        "{user1} bullied {user2}.",
        "Nyaan ate {user2}'s leg. *nomnomnom*",
        "{user1} {throws} a master ball at {user2}, resistance is futile.",
        "{user1} hits {user2} with an action beam...bbbbbb (ง・ω・)ง ====*",
        "{user1} ara ara's {user2}.",
        "{user1} ora ora's {user2}.",
        "{user1} muda muda's {user2}.",
        "{user2} was turned into a Jojo reference!",
        "{user1} hits {user2} with {item}.",
        "Round 2!..Ready? .. FIGHT!!",
        "WhoPixel will oof {user2} to infinity and beyond.",
        "{user2} ate a bat and discovered a new disease.",
        "{user1} folded {user2} into a paper plane",
        "{user1} served {user2} some bat soup.",
        "{user2} was sent to their home, the planet of the apes.",
        "{user1} kicked {user2} out of a moving train.",
        "{user2} just killed John Wick’s dog.",
        "{user1} performed an Avada Kedavra spell on {user2}.",
        "{user1} subjected {user2} to a fiery furnace.",
        "Sakura Haruno just got more useful than {user2}",
        "{user1} unplugged {user2}'s life support.",
        "{user1} subscribed {user2}' to 5 years of bad internet.",
        "You know what’s worse than Dad jokes? {user2}!",
        "{user1} took all of {user2}'s cookies.",
        "{user2} wa mou.......Shindeiru! - {user1}.",
        "{user2} lost their race piece!",
        "Shut up {user2}, you are just {user2}.",
        "{user1} hits {user2} with Aka si anse!",
        "@galaxya546euser scratches {user2}",
        "Majin buu ate {user2}",
        "Goblin slayer slays {user2}",
    ],
    "SLAP_SAITAMA_TEMPLATES": [
        "One Punch!",
        "TF stop slapping me 😠",
        "Stop slapping me pls 😥",
        ["BOOM!", "Silence sir!", "tmute"],
    ],
    "ITEMS": [
        "a large trout",
        "a wooden stick",
        "a frying pan",
        "cast iron skillet",
        "angry meow",
        "cricket bat",
        "wooden cane",
        "shovel",
        "toaster",
        "book",
        "laptop",
        "rubber chicken",
        "spiked bat",
        "heavy rock",
        "chunk of dirt",
        "ton of bricks",
        "rasengan",
        "spirit bomb",
        "100-Type Guanyin Bodhisattva",
        "rasenshuriken",
        "Murasame",
        "ban",
        "chunchunmaru",
        "Kubikiribōchō",
        "rasengan",
        "spherical flying kat",
    ],
    "HIT": [
        "hits",
        "whacks",
        "slaps",
        "smacks",
        "bashes",
        "pats",
        "hard",
        "softly",
    ],
    "THROW": [
        "fiercely",
        "gently",
        "throws",
        "flings",
        "chucks",
        "hurls",
    ],
}

@SPY(pattern='!!slap')
#@SPY(outgoing=True, pattern='!!slap')
async def slap(event):
    id = str(ID(event))
    if id not in GS() and id not in GIS() and event.sender_id != MY_USER_ID: return
    message = event.message
    curr_user = FIX(event.sender.first_name)
    args = event.message.text.split()[1:]  # Get the arguments

    if event.is_reply:
        reply_message = await event.get_reply_message()
    else:
        reply_message = None

    user_id = event.sender_id if not reply_message else reply_message.sender_id

    if user_id == MY_USER_ID:
        temp = random.choice(fun_strings["SLAP_SAITAMA_TEMPLATES"])
        """
        if isinstance(temp, list) and temp[2] == "tmute":
            if event.is_group:
                await event.reply(temp[1])
                return

            mutetime = int(time.time() + 60)
            await bot.edit_permissions(event.chat_id, event.sender_id, until_date=mutetime, send_messages=False)
            await event.reply(temp[0])
        else:
        """
        await event.reply(temp)
        return

    if user_id:
        slapped_user = await bot.get_entity(user_id)
        user1 = curr_user
        user2 = FIX(slapped_user.first_name)
    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings["SLAP_TEMPLATES"])
    item = random.choice(fun_strings["ITEMS"])
    hit = random.choice(fun_strings["HIT"])
    throw = random.choice(fun_strings["THROW"])

    reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)
    reply_msg = await event.get_reply_message()
    if reply_msg:
        await reply_msg.reply(reply, parse_mode='html')
    else:
        await event.reply(reply, parse_mode='html')

@SPY(pattern='!!n$')
async def sub_nuke(E):
    id = str(ID(E))
    if id not in GS() and id not in GIS(): return
    reply_msg = await E.get_reply_message()
    if not reply_msg: return
    try:
        #await (await GR(E)).delete()
        await reply_msg.delete()
        await E.delete()
    except: pass

@SPY(outgoing=True, pattern='!!sav ?(\\S+)? ?(.+)?')
async def save_handler(event):
    loll = event.pattern_match.group(1) if event.pattern_match.group(1) else None
    lolll = event.pattern_match.group(2) if event.pattern_match.group(2) else ""

    if event.is_reply:
        reply_message = await event.get_reply_message()
        try:
            if not loll:
                # Forward to default group link
                entity = await bot.get_entity(default_group_link)
            elif loll == 'gay':
                # Forward to channel link
                entity = await bot.get_entity(gay_channel_link)
            elif loll.startswith("kang"):
                entity = await bot.get_entity(default_group_link)
            elif loll.startswith("h") or loll.startswith("t"):
                # Assume loll contains a valid group or channel link
                entity = await bot.get_entity(loll)
            else:
                return

            entity_name = entity.title if hasattr(entity, 'title') else (entity.username if entity.username else 'Unknown Name')
            entity_username = f'@{entity.username}' if entity.username else 'No Username'
            entity_type = 'Channel' if entity.broadcast else 'Group'

            if loll == "kang":
                bombb1 = await bot.forward_messages(entity, reply_message)
            else:
                await bot.forward_messages(entity, reply_message)
            await event.edit(f"Message forwarded\nName: {M(entity_name)}\nUsername: {M(entity_username)}\nType: {M(entity_type)}" if loll != "kang" else Q(M("Kanging...")), parse_mode="HTML")
            await asyncio.sleep(1)
            if loll == "kang": await bombb1.reply(f"/kang {lolll}")
        except Exception as e:
            await event.edit(f"Failed to forward message: {e}")
            await asyncio.sleep(10)
        if loll and loll != "kang":
            await asyncio.sleep(10)
        elif loll == "kang":
            await asyncio.sleep(1)
            await event.edit(f"Sticker kanged{f' as {lolll}' if lolll else ''}")
            await asyncio.sleep(3)
        await event.delete()

# OpenAI client
apiopenrouter = OpenAI(api_key=openrouter_api, base_url="https://openrouter.ai/api/v1")
apiai = OpenAI(api_key=ai_ml_api_key, base_url="https://api.aimlapi.com/v1")
gemini_ai = geminiai.Client(api_key=gemini_ai_api_key)
the_ai_model = "Gemini"

@SPY(outgoing=True, pattern=r"^!!set ai ?(.+)?")
async def theaimodel(E):
    global the_ai_model
    themodel = E.pattern_match.group(1)
    if themodel == "1" or themodel == "Mistral" or themodel == "mistral":
        the_ai_model = "Mistral"
    elif themodel == "2" or themodel == "Deepseek" or themodel == "deepseek":
        the_ai_model = "Deepseek"
    elif themodel == "3" or themodel == "Gemma" or themodel == "gemma":
        the_ai_model = "Gemma"
    elif themodel == "4" or themodel == "Meta" or themodel == "meta":
        the_ai_model = "Meta"
    elif themodel == "5" or themodel == "Dolphin" or themodel == "dolphin":
        the_ai_model = "Dolphin"
    elif themodel == "6" or themodel == "Gemini" or themodel == "gemini":
        the_ai_model = "Gemini"
    elif themodel == "7" or themodel == "Bytedance" or themodel == "bytedance":
        the_ai_model = "Bytedance"
    elif themodel == "8" or themodel == "Qwen" or themodel == "qwen":
        the_ai_model = "Qwen"
    elif themodel == "off" or themodel == "Off" or themodel == "stop":
        the_ai_model = False
    else:
        await E.edit(
            f"""Model set to <code>{the_ai_model}</code>

Available models:
1: <code>Mistral</code>
2: <code>Deepseek</code>
3: <code>Gemma</code>
4: <code>Meta</code>
5: <code>Dolphin</code>
6: <code>Gemini</code>
7: <code>Bytedance</code>
8: <code>Qwen</code>""",
            parse_mode="HTML"
        )
        await asyncio.sleep(5)
    await E.delete()

@SPY(pattern=r'(?s)!!ai ?(.+)?')
async def aichat(event):
    global LAST_MSG_ID, LAST_CHAT_ID
    if not the_ai_model: return
    id = str(ID(event))
    if id not in GS() and id not in GIS() and id != str(MY_USER_ID): return
    print(event.message.id)
    if event.message.id <= LAST_MSG_ID and event.chat_id == LAST_CHAT_ID: return
    else: LAST_MSG_ID = event.message.id; LAST_CHAT_ID = event.chat_id
    user_prompt = event.pattern_match.group(1)
    reply_msg = await event.get_reply_message()
    if not reply_msg and not user_prompt:
        return
    #running_msg = await event.reply(r"`✨️AI:` `RUNNING...`")
    running_msg = await event.reply("✨️")
    completion = None
    response = None
    #has_img = False
    if id == str(MY_USER_ID) and event.is_reply:
        #if reply_msg.media:
        #if reply_msg.photo or (reply_msg.document and reply_msg.document.mime_type == "application/x-tgsticker"):
        #if reply_msg.photo or reply_msg.document.mime_type == "application/x-tgsticker":
            #print(reply_msg.document.mime_type)
            #print("yes it is image or sticker")
        if reply_msg.media and (the_ai_model == "Gemini" or the_ai_model == "Gemini" or the_ai_model == "Gemma" or the_ai_model == "Qwen" or the_ai_model == "Bytedance"):
            print("yes it is image or sticker(media)")
            if os.path.isdir("./ai_temp_image") is False:
                os.mkdir("./ai_temp_image")
            image_path = await bot.download_media(reply_msg.media, 'ai_temp_image/temp_img')
            with Image.open(image_path) as img:
                if img.format in ['JPEG', 'JPG', 'WEBP']:
                    img = img.convert('RGB' if img.format in ['JPEG', 'JPG'] else 'RGBA')
                    img.save("./ai_temp_image/ai_temp_image.png")
                    has_img = True
                else:
                    has_img = False
            #if os.path.isdir("./ai_temp_image") is True:
                #rmtree("./ai_temp_image")
        else:
            has_img = False
    else:
        has_img = False
                
        #if os.path.exists('temp_image'):
            #os.remove('temp_image')
    try:
        if the_ai_model == "Mistral":
            if reply_msg and reply_msg.text != None and user_prompt != None:
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiai.chat.completions.create(
                    model="mistralai/Mistral-7B-Instruct-v0.2",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.7,
                    max_tokens=256,
                )
            else:
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiai.chat.completions.create(
                    model="mistralai/Mistral-7B-Instruct-v0.2",
                    messages=[
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.7,
                    max_tokens=256,
                )

            response = completion.choices[0].message.content

            #print("User:", user_prompt)
            await event.reply(f"`✨️AI️:`{response}")
            return
        elif the_ai_model == "Deepseek":
            if reply_msg and reply_msg.text != None and user_prompt != None:
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="deepseek/deepseek-r1:free",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                )
            else:
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="deepseek/deepseek-r1:free",
                    messages=[
                        {"role": "user", "content": user_prompt},
                    ],
                )
        elif the_ai_model == "Gemma":
            if reply_msg and user_prompt != None and os.path.exists('./ai_temp_image/ai_temp_image.png') and has_img and reply_msg.media:
                with open("./ai_temp_image/ai_temp_image.png", "rb") as b64img:
                    completion = apiopenrouter.chat.completions.create(
                        model="google/gemma-3-27b-it:free",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": user_prompt
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/png;base64,{base64.b64encode(b64img.read()).decode('utf-8')}",
                                        },
                                    },
                                ]
                            },
                        ],
                    )
                    #if os.path.exists('temp_image'):
                        #os.remove('temp_image')
                    #if os.path.exists('ai_temp_image.png'):
                        #os.remove('ai_temp_image.png')
            elif reply_msg and reply_msg.text != None and user_prompt != None and completion == None:
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="google/gemma-3-27b-it:free",
                    messages=[
                        {
                            "role": "system",
                            "content": [
                                {
                                    "type": "text",
                                    "text": system_prompt
                                },
                            ]
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": user_prompt
                                },
                            ]
                        },
                    ],
                )
            else:
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="google/gemma-3-27b-it:free",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": user_prompt
                                },
                            ]
                        },
                    ],
                )
                print(completion)
        elif the_ai_model == "Meta":
            if reply_msg and reply_msg.text != None and user_prompt != None:
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="meta-llama/llama-3.3-70b-instruct:free",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                )
            else:
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="meta-llama/llama-3.3-70b-instruct:free",
                    messages=[
                        {"role": "user", "content": user_prompt},
                    ],
                )
        elif the_ai_model == "Dolphin":
            if reply_msg and reply_msg.text != None and user_prompt != None:
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                )
            else:
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
                    messages=[
                        {"role": "user", "content": user_prompt},
                    ],
                )
        elif the_ai_model == "Gemini":
            if reply_msg and user_prompt != None and os.path.exists('./ai_temp_image/ai_temp_image.png') and has_img and reply_msg.media:
                with Image.open("./ai_temp_image/ai_temp_image.png") as ai_open_img:
                    print("gemini did it")
                    completion = gemini_ai.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=[user_prompt, ai_open_img]
                    )
                #ai_open_img.close()
            elif reply_msg and reply_msg.text != None and user_prompt != None:
                print("sys reply")
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                """
                print(reply_msg.text[1:])
                print(reply_msg.text[2:])
                print(reply_msg.text[3:])
                print(reply_msg.text[7:])
                print(system_prompt)
                """
                completion = gemini_ai.models.generate_content(
                    model="gemini-2.0-flash",
                    config=geminiai.types.GenerateContentConfig(system_instruction=system_prompt),
                    contents=user_prompt,
                )
            else:
                #print("non")
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = gemini_ai.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=user_prompt,
                )
            response = completion.text
            await running_msg.edit(f"`✨️AI️:` {response}")
            return
        elif the_ai_model == "Bytedance":
            if reply_msg and user_prompt != None and os.path.exists('./ai_temp_image/ai_temp_image.png') and has_img and reply_msg.media:
                with open("./ai_temp_image/ai_temp_image.png", "rb") as b64img:
                    completion = apiopenrouter.chat.completions.create(
                        model="bytedance-research/ui-tars-72b:free",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": user_prompt
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/png;base64,{base64.b64encode(b64img.read()).decode('utf-8')}",
                                        },
                                    },
                                ]
                            },
                        ],
                    )
                    #if os.path.exists('temp_image'):
                        #os.remove('temp_image')
                    #if os.path.exists('ai_temp_image.png'):
                        #os.remove('ai_temp_image.png')
            elif reply_msg and reply_msg.text != None and user_prompt != None and completion == None:
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                """
                print(reply_msg.text[1:])
                print(reply_msg.text[2:])
                print(reply_msg.text[3:])
                print(reply_msg.text[9:])
                print(system_prompt)
                """
                completion = apiopenrouter.chat.completions.create(
                    model="bytedance-research/ui-tars-72b:free",
                    messages=[
                        {
                            "role": "system",
                            "content": [
                                {
                                    "type": "text",
                                    "text": system_prompt
                                },
                            ]
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": user_prompt
                                },
                            ]
                        },
                    ],
                )
            else:
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="bytedance-research/ui-tars-72b:free",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": user_prompt
                                },
                            ]
                        },
                    ],
                )
        
        elif the_ai_model == "Qwen":
            if reply_msg and user_prompt != None and os.path.exists('./ai_temp_image/ai_temp_image.png') and has_img and reply_msg.media:
                with open("./ai_temp_image/ai_temp_image.png", "rb") as b64img:
                    completion = apiopenrouter.chat.completions.create(
                        model="qwen/qwen2.5-vl-32b-instruct:free",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": user_prompt
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/png;base64,{base64.b64encode(b64img.read()).decode('utf-8')}",
                                        },
                                    },
                                ]
                            },
                        ],
                    )
                    #if os.path.exists('temp_image'):
                        #os.remove('temp_image')
                    #if os.path.exists('ai_temp_image.png'):
                        #os.remove('ai_temp_image.png')
            elif reply_msg and reply_msg.text != None and user_prompt != None and completion == None:
                system_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="qwen/qwen2.5-vl-32b-instruct:free",
                    messages=[
                        {
                            "role": "system",
                            "content": [
                                {
                                    "type": "text",
                                    "text": system_prompt
                                },
                            ]
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": user_prompt
                                },
                            ]
                        },
                    ],
                )
            else:
                if user_prompt == None:
                    user_prompt = reply_msg.text[9:] if reply_msg.text[3:].startswith("AI") else reply_msg.text
                completion = apiopenrouter.chat.completions.create(
                    model="qwen/qwen2.5-vl-32b-instruct:free",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": user_prompt
                                },
                            ]
                        },
                    ],
                )

        print(completion)
        response = completion.choices[0].message.content

        #print("User:", user_prompt)
        await running_msg.edit(f"`✨️AI️:` {response}")
        if os.path.isdir("./ai_temp_image") is True:
            try:
                print("ok deleting")
                rmtree("./ai_temp_image")
            except:
                print(traceback.format_exc())
    except Exception:
        if response:
            with open('output.txt', 'w') as file:
                file.write(response)
            await bot.send_file(event.chat_id, "output.txt", reply_to=event.id)
            if os.path.exists('output.txt'):
                os.remove('output.txt')
            await running_msg.delete()
            if os.path.isdir("./ai_temp_image") is True:
                rmtree("./ai_temp_image")
            return
        if os.path.isdir("./ai_temp_image") is True:
                rmtree("./ai_temp_image")
        await running_msg.edit(f"`⚠️AI:` {traceback.format_exc()}")



@SPY(outgoing=True, pattern="!!stop_bot$")
async def stop_my_bot(E):
    await event.edit("stopped_bot")
    delyaymsg = await bot.send_message(7129584730, "/stowuehhehbuthgehheart09165287gcvso9hv2u67e0h2vo9e8h2vhoe92hv2bj2oeieb2h2ieieb2vevge7")
    await asyncio.sleep(10)
    await delyaymsg.delete()

#@BOT.add_cmd(cmd="ping")
@SPY(outgoing=True, pattern="!!ping$")
async def ping(E):
    start = datetime.datetime.now()
    #resp = await E.reply("Checking Ping.....")
    await E.edit("Checking Ping.....")
    end = (datetime.datetime.now() - start).microseconds / 1000
    #await resp.delete()
    repl_msg = await E.get_reply_message()
    if repl_msg:
        await repl_msg.reply(f"Pong! {end} ms.")
    else:
        await E.reply(f"Pong! {end} ms.")
    #await asyncio.sleep(1)
    await E.delete()

@SPY(pattern="!!ping$")
async def ping_bot(E):
    id = str(ID(E))
    if (id not in GS() and id not in GIS()): return
    start = datetime.datetime.now()
    #resp = await E.reply("Checking Ping.....")
    check_ping = await E.reply("Checking Ping.....")
    end = (datetime.datetime.now() - start).microseconds / 1000
    #await resp.delete()
    repl_msg = await E.get_reply_message()
    if repl_msg:
        await repl_msg.reply(f"Pong! {end} ms.")
    else:
        await E.reply(f"Pong! {end} ms.")
    #await asyncio.sleep(1)
    await check_ping.delete()

@SPY(pattern='!!shell ?(.+)?')
async def toggle_shell(E):
    id = str(ID(E))
    if id not in GIS() and id != str(MY_USER_ID): return
    global Shell_ON_T
    C = E.pattern_match.group(1)
    if C:
        try: o = SSU(C).stdout.read()
        except Exception as e: o = f"{e}"
        if len(o)+len(C) >= 4000: o = f"{o[:4000-len(C)]}\n\n{'[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'}"
        finaltext = Q('<code>$ </code><code>'+FIX(C)+'</code>\n'+M(FIX(o)) if o else f'$ {M(FIX(C))}')

        if id == str(MY_USER_ID): await E.edit(finaltext,parse_mode="HTML")
        else: await E.reply(finaltext,parse_mode="HTML")
    elif E.sender_id == MY_USER_ID:
        if Shell_ON_T:
            Shell_ON_T = False
            await E.edit("<code>SHELL</code>\n\nON\nOFF", parse_mode='HTML')
            await asyncio.sleep(0.3)
            await E.edit("<code>SHELL</code>\n\nON\n<blockquote>OFF</blockquote>", parse_mode="HTML")
        else:
            Shell_ON_T = True
            await E.edit("<code>SHELL</code>\n\nON\nOFF", parse_mode="HTML")
            await asyncio.sleep(0.3)
            await E.edit("<code>SHELL</code>\n\n<blockquote>ON</blockquote>\nOFF", parse_mode='HTML')
        await asyncio.sleep(5)
        await E.delete()
    else:
        if Shell_ON_T:
            Shell_ON_T = False
            shell_t = await E.reply("ON\n<blockquote>OFF</blockquote>", parse_mode="HTML")
        else:
            Shell_ON_T = True
            shell_t = await E.reply("<blockquote>ON</blockquote>\nOFF", parse_mode='HTML')
        await asyncio.sleep(5)
        await shell_t.delete()
        await E.delete()

try:
    with open('afkmsg.txt', 'r') as file:
        afk_msg = file.read().strip()
except:
    with open('afkmsg.txt', 'w') as file:
        file.write("Bruh I'm AFK rn...")
        afk_msg = "Bruh I'm AFK rn..."
afk_me_now = False
afk_mode = 'off'
afk_msg_now = None

#@bot.on(events.NewMessage(outgoing=True, pattern=r'(?s)!!afk ?(.+)?'))
@SPY(outgoing=True, pattern=r"!!afk (.+) (.+)")
async def setafk(event):
    global afk_msg, afk_mode, afk_me_now, afk_msg_now
    msg = event.pattern_match.group(1)
    msg2 = event.pattern_match.group(2)
    if msg == "now":
        afk_msg_now = msg2
        afk_me_now = True
        await event.edit(f"AFK message: <blockquote>{msg2}</blockquote>", parse_mode="html")
    elif msg == "set":
        afk_msg = msg2
        with open('afkmsg.txt', 'w') as file:
            file.write(afk_msg)
        await event.edit(f"AFK message: <blockquote>{afk_msg}</blockquote>", parse_mode="html")
    elif msg == "mode":
        if msg2 == 'on':
            afk_mode = 'on'
            afk_me_now = True
            await event.edit("AFK mode:\n\nai\nauto\n<blockquote>on</blockquote>\noff", parse_mode='html')
        elif msg2 == 'off':
            afk_mode = 'off'
            afk_me_now = False
            await event.edit('AFK mode:\n\nai\nauto\non\n<blockquote>off</blockquote>', parse_mode='html')
        elif msg2 == 'auto':
            afk_mode = 'auto'
            afk_me_now = False
            await event.edit("AFK mode:\n\nai\n<blockquote>auto</blockquote>\non\noff", parse_mode='html')
        elif msg2 == "ai":
            afk_mode = "ai"
            afk_me_now = True
            await event.edit("AFK mode:\n\n<blockquote>ai</blockquote>\nauto\non\noff", parse_mode='html')
    await asyncio.sleep(5)
    await event.delete()

    
"""
@bot.on(events.UserUpdate)
async def hmmmmmm(event):
    global afk_me_now
    if afk_mode != 'auto': return
    if event.online:
        afk_me_now = False
    else:
        afk_me_now = True
"""
"""
@bot.on(events.NewMessage)
async def hhmmm(event):
    if afk_me_now:
        if event.sender_id == MY_USER_ID:
            return
        if event.is_private:
            await event.reply(afk_msg)
        elif event.is_group and event.message.mentioned:
            await event.reply(afk_msg)
"""

def create_neon_text_imagef(text, font_path, font_size, background_path, text_color):
    # Open the background image
    background = Image.open(background_path)
    image_size = background.size

    # Create a blank image with the same size as the background
    image = Image.new('RGBA', image_size, (0, 0, 0, 0))  # Use 'RGBA' for transparency
    draw = ImageDraw.Draw(image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Draw the text
    draw.text((image_size[0] // 2, image_size[1] // 2), text, font=font, fill=text_color, anchor="mm")

    # Add a glow effect
    glow_image = image.filter(ImageFilter.GaussianBlur(radius=10))

    # Enhance the glow effect by adding the text again with more intensity
    draw.text((image_size[0] // 2, image_size[1] // 2), text, font=font, fill=text_color, anchor="mm")

    # Composite the glow image with the background
    combined_image = Image.alpha_composite(background.convert('RGBA'), glow_image)

    # Paste the text on the combined image
    final_image = Image.alpha_composite(combined_image, image)

    return final_image

def interpolate_colorf(color1, color2, factor):
    return tuple(int(color1[i] * (1 - factor) + color2[i] * factor) for i in range(3))

def create_neon_giff(text, font_path, font_size, background_path, colors, output_file, frames_per_transition=10):
    from moviepy import ImageSequenceClip
    frames = []
    for i in range(len(colors)):
        color1 = colors[i]
        color2 = colors[(i + 1) % len(colors)]
        for j in range(frames_per_transition):
            factor = j / frames_per_transition
            color = interpolate_colorf(color1, color2, factor) + (255,)  # Add alpha channel
            image = create_neon_text_imagef(text, font_path, font_size, background_path, color)
            frames.append(image)

    # Save images as temporary files
    image_files = []
    for i, img in enumerate(frames):
        file_path = f'temp_image_{i}.png'
        img.save(file_path)
        image_files.append(file_path)

    # Create GIF
    clip = ImageSequenceClip(image_files, fps=10)
    clip.write_gif(output_file, fps=10)

    # Clean up temporary images
    for file_path in image_files:
        os.remove(file_path)

#font_path = "/data/data/com.termux/files/home/tgbot/sticker/font/t.ttf"  # Replace with the path to your font file
#font_size = 100
#background_path = "/sdcard/Download/neon_wall.jpg"  # Replace with the path to your neon wall image
#colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, green, blue
#output_file = "neon_text.gif"



@SPY(outgoing=True, pattern=r'/tgif (\w+) (.+)')
async def text(event):
    font_name = event.pattern_match.group(1).strip()
    user_text = event.pattern_match.group(2).strip()
    await event.edit(f'tgif {font_name}.ttf {user_text}')

    font_directory = os.path.expanduser('/data/data/com.termux/files/home/tgbot/sticker/font/')
    font_path = os.path.join(font_directory, f'{font_name}.ttf')
        
    if not os.path.exists(font_path):
        available_fonts = [f for f in os.listdir(font_directory) if f.endswith('.ttf')]
        await event.edit(f"Font '{font_name}' not found. Available fonts:\n" + "\n".join(available_fonts))
        await asyncio.sleep(5)
        await event.delete()
        return
        
    #create_neon_gif(user_text, font_path, font_size, background_path, colors, output_file)
    create_neon_giff(user_text, font_path, 100, "/data/data/com.termux/files/home/tgbot/img/neon_wall.jpg", [(255, 0, 0), (0, 255, 0), (0, 0, 255)], "/data/data/com.termux/files/home/tgbot/sticker/proc/ahhhhhhhhh.gif")
        
    # Send the sticker
    repl_msg = await event.get_reply_message()
    if repl_msg:
        await repl_msg.reply(file="/data/data/com.termux/files/home/tgbot/sticker/proc/ahhhhhhhhh.gif")
    else:
        await event.reply(file="/data/data/com.termux/files/home/tgbot/sticker/proc/ahhhhhhhhh.gif")
        
    # Delete the file after sending
    if os.path.exists("/data/data/com.termux/files/home/tgbot/sticker/proc/ahhhhhhhhh.gif"):
        os.remove("/data/data/com.termux/files/home/tgbot/sticker/proc/ahhhhhhhhh.gif")
    await asyncio.sleep(1)
    await event.delete()

delete_my_msg = False
delete_my_msg_delay = None

@SPY(outgoing=True, pattern=r'/tdd ?(\d+)?')
async def adelete(event):
    global delete_my_msg, delete_my_msg_delay
    if event.is_reply and event.pattern_match.group(1):
        reply_msg = await event.get_reply_message()
        n = int(event.pattern_match.group(1))
        for i in range(n):
            await event.edit(f"Deleting in {n - i}s")
            await asyncio.sleep(1)
        await event.delete()
        #await (await GR(event)).delete()
        await reply_msg.delete()
        return
    elif event.pattern_match.group(1) == None:
        delete_my_msg = False
        await event.edit("tdd off")
        await asyncio.sleep(1)
        await event.delete()
        return
    delete_my_msg_delay = int(event.pattern_match.group(1))
    delete_my_msg = True
    await event.edit(f"tdd on ({delete_my_msg_delay}s)")
    await asyncio.sleep(1)
    await event.delete()

#@BOT.on(events.NewMessage(pattern=r'!!(promote|demote)'))
DEMOTE_PRIVILEGES = ChatAdminRights(
    change_info=False, post_messages=False, edit_messages=False,
    delete_messages=False, ban_users=False, invite_users=False,
    pin_messages=False, add_admins=False, anonymous=False, manage_call=False
)

FULL_PRIVILEGES = ChatAdminRights(
    change_info=True, post_messages=True, edit_messages=True,
    delete_messages=True, ban_users=True, invite_users=True,
    pin_messages=True, add_admins=False, anonymous=False, manage_call=True
)
@SPY(outgoing=True, pattern=r'!!(promote|demote)')
async def promote_or_demote(event):
    """Promote or Demote users in a chat."""
    if not event.is_group:
        await event.reply("This command only works in group chats.")
        return

    sender = await event.get_sender()
    if not sender:
        await event.reply("Unable to fetch sender details.")
        return

    args = event.text[len("!!"):] #event.raw_text.split()
    action = "promote" if args.startswith("p") else "demote"
    #action = args#[0].lstrip(".").lower()
    if event.is_reply:
        target = await event.get_reply_message()
    else:
        target = event.text[len(f"!!{action} "):]

    if not target:
        await event.edit("Reply to a user or provide a username.")
        return

    if event.is_reply:
        user = await bot.get_entity(target.sender_id)
    else:
        if target.startswith("@"):
            target = target[1:]
        else:
            target = int(target)
        user = await bot.get_entity(target)
    rights = FULL_PRIVILEGES if action == "promote" else DEMOTE_PRIVILEGES

    try:
        await bot(EditAdminRequest(
            channel=event.chat_id,
            user_id=user.id,
            admin_rights=rights,
            rank="Admin" if action == "promote" else ""
        ))
        await event.edit(f"{'Promoted' if action == 'promote' else 'Demoted'}: <code>{user.first_name}</code>", parse_mode="HTML")
    except Exception as e:
        await event.edit(f"Error: {e}")

# Define ban/unban rights
BAN_RIGHTS = ChatBannedRights(
    until_date=None,  # Permanently banned
    view_messages=True
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,  # Unban or revoke restrictions
    view_messages=False
)

@SPY(outgoing=True, pattern=r'!!(ban|unban)')
async def ban_or_unban(event):
    """Ban or Unban users."""
    if not event.is_group:
        await event.reply("This command only works in group chats.")
        return

    args = event.text[2:]
    action = "unban" if args.startswith("un") else "ban"
    if event.is_reply:
        target = await event.get_reply_message()
    else:
        target = event.text[len(f"!!{action} "):]

    if not target:
        await event.edit("Reply to a user or provide a username.")
        return

    if event.is_reply:
        user = await bot.get_entity(target.sender_id)
    else:
        if target.startswith("@"):
            target = target[1:]
        else:
            target = int(target)
        user = await bot.get_entity(target)
        

    # Set rights based on the command
    rights = BAN_RIGHTS if action == "ban" else UNBAN_RIGHTS

    try:
        await bot(EditBannedRequest(
            channel=event.chat_id,
            participant=user.id,
            banned_rights=rights
        ))
        action_str = "Banned" if action == "ban" else "Unbanned"
        await event.edit(f"{action_str}: <code>{user.first_name}</code>",parse_mode="HTML")
    except Exception as e:
        await event.edit(f"Error: {e}")

# Define unmute rights
UNMUTE_RIGHTS = ChatBannedRights(
    until_date=0,  # Use 0 for indefinite unmute
    send_messages=False  # Allow sending messages again
)

@SPY(outgoing=True, pattern=r'!!unmute')
async def unmute_user(event):
    """Unmute users in a group chat."""
    if not event.is_group:
        await event.reply("This command only works in group chats.")
        return

    args = event.text[len("!!unmute "):]
    if event.is_reply:
        target = await event.get_reply_message()
        user = await bot.get_entity(target.sender_id)
    elif args:
        if args.startswith("@"):
            target = args[1:]
        else:
            target = int(args)
        user = await bot.get_entity(target)
    else:
        await event.edit("Reply to a user or provide a username.")
        return

    try:
        await bot(EditBannedRequest(
            channel=event.chat_id,
            participant=user.id,
            banned_rights=UNMUTE_RIGHTS
        ))
        await event.edit(f"Unmuted: <code>{user.first_name}</code>",parse_mode="HTML")
    except Exception as e:
        await event.edit(f"Error: {e}")

# Define mute rights
MUTE_RIGHTS = ChatBannedRights(
    until_date=None,  # None means it's indefinite
    send_messages=True,  # Restrict sending messages
    send_media=True,  # Restrict sending media
    send_stickers=True,  # Restrict sending stickers
    send_gifs=True,  # Restrict sending gifs
    send_games=True,  # Restrict sending games
    send_inline=True,  # Restrict inline queries
    embed_links=True  # Restrict sending embedded links
)

@SPY(outgoing=True, pattern=r'!!mute')
async def mute_user(event):
    """Mute users in a group chat."""
    if not event.is_group:
        await event.reply("This command only works in group chats.")
        return

    args = event.text[len("!!mute "):]
    if event.is_reply:
        target = await event.get_reply_message()
        user = await bot.get_entity(target.sender_id)
    elif args:
        if args.startswith("@"):
            target = args[1:]
        else:
            target = int(args)
        user = await bot.get_entity(target)
    else:
        await event.edit("Reply to a user or provide a username.")
        return

    try:
        await bot(EditBannedRequest(
            channel=event.chat_id,
            participant=user.id,
            banned_rights=MUTE_RIGHTS
        ))
        await event.edit(f"Muted: <code>{user.first_name}</code>", parse_mode="HTML")
    except Exception as e:
        await event.edit(f"Error: {e}")

def speed_convert(size):
    """
    Hi human, you can't read bytes? I'll translate 4 u
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'KB/s', 2: 'MB/s', 3: 'GB/s', 4: 'TB/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)/8} {units[zero]}"

@SPY(outgoing=True, pattern="^!!speed$")
async def speedtst(spd):
    """ For !!speed command, use SpeedTest to check server speeds. """
    import speedtest
    try:
        #if os.environ.get("isSuspended") == "True":
        #    return
        await spd.edit("`Running speed test . . .`")
        test = speedtest.Speedtest()

        test.get_best_server()
        test.download()
        test.upload()
        test.results.share()
        result = test.results.dict()

        await spd.edit("`"
                    "Started at "
                    f"{result['timestamp']} \n\n"
                    "Download "
                    f"{speed_convert(result['download'])} \n"
                    "Upload "
                    f"{speed_convert(result['upload'])} \n"
                    "Ping "
                    f"{result['ping']} \n"
                    "ISP "
                    f"{result['client']['isp']}"
                    "`")
    except Exception:
        await spd.edit(f"`Error: {traceback.format_exc()}`")

@SPY(pattern=r"(?s)^!!device ?(.+)?")
async def device_info(request):
    """get android device basic info from its codename"""
    id = str(ID(request))
    if id not in GS() and id not in GIS() and id != str(MY_USER_ID): return
    textx = await request.get_reply_message()
    codename = request.pattern_match.group(1)
    if codename:
        pass
    elif textx:
        codename = textx.text
    else:
        if id == str(MY_USER_ID):
            await request.edit("`Usage: !!device <codename> / <model>`")
        elif textx:
            await textx.reply("`Usage: !!device <codename> / <model>`")
        else:
            await request.reply("`Usage: !!device <codename> / <model>`")
        return
    data = json.loads(
        requests.get(
            "https://raw.githubusercontent.com/androidtrackers/"
            "certified-android-devices/master/by_device.json"
        ).text
    )
    results = data.get(codename)
    if results:
        reply = f"**Search results for {codename}**:\n\n"
        for item in results:
            reply += (
                f"**Brand**: `{item['brand']}`\n"
                f"**Name**: `{item['name']}`\n"
                f"**Model**: `{item['model']}`\n\n"
            )
    else:
        reply = f"`Couldn't find info about {codename}!`\n"
    if id == str(MY_USER_ID):
        await request.edit(reply)
    elif textx:
        await textx.reply(reply)
    else:
        await request.reply(reply)

@SPY(outgoing=True, pattern="(?s)^!!setgpic$")
async def set_group_photo(gpic):
    """ For .setgpic command, changes the picture of a group """
    if not gpic.is_group:
        await gpic.edit("`I don't think this is a group.`")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None

    if not admin and not creator:
        await gpic.edit(NO_ADMIN)
        return

    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split('/'):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await gpic.edit("`Invalid Extension`")

    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await
                                 gpic.client.upload_file(photo)))
            await gpic.edit("`Chat Picture Changed`")

        except Exception as e:
            await gpic.edit(e)

#log
msg_for_percentage = types.Message

async def callback(current, total):
    global msg_for_percentage
    percent = round(current/total * 100, 2)
    await msg_for_percentage.edit(f"Uploaded `{current}` out of `{total}` bytes: `{percent}%`")
    await asyncio.sleep(2)


TMP_DOWNLOAD_DIRECTORY = "./"

async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity,
                          types.MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(
                GetFullUserRequest(user_object.id))
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return replied_user


async def fetch_info(replied_user, event):
    """ Get details from the User object. """
    
    user = replied_user.users[0]  # Access the first user object in the `users` list

    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    user_bio = replied_user.full_user.about
    is_bot = user.bot
    restricted = user.restricted
    verified = user.verified

    """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    """
    first_name = first_name.replace(
        "\u2060", "") if first_name else ("This User has no First Name")
    last_name = last_name.replace(
        "\u2060", "") if last_name else ("This User has no Last Name")
    username = "@{}".format(username) if username else (
        "This User has no Username")
    user_bio = "This User has no About" if not user_bio else user_bio

    if user_id != (await event.client.get_me()).id:
        common_chat = replied_user.full_user.common_chats_count
    else:
        common_chat = "I've seen them in... Wow. Are they stalking me? "
        common_chat += "They're in all the same places I am... oh. It's me."

    caption = "<b>USER INFO:</b> \n"
    caption += f"First Name: {first_name} \n"
    caption += f"Last Name: {last_name} \n"
    caption += f"Username: {username} \n"
    caption += f"Is Bot: {is_bot} \n"
    caption += f"Is Restricted: {restricted} \n"
    caption += f"Is Verified by Telegram: {verified} \n"
    caption += f"ID: <code>{user_id}</code> \n \n"
    caption += f"Bio: \n<code>{user_bio}</code> \n \n"
    caption += f"Common Chats with this user: {common_chat} \n"
    caption += f"Permanent Link To Profile: "
    caption += f"<a href=\"tg://user?id={user_id}\">{first_name}</a>"

    return caption

@SPY(pattern="^!!whois(?: |$)(.*)")
async def who(event):
    """ For ' command, get info about a user. """
    id = str(ID(event))
    if id not in GS() and id not in GIS() and event.sender_id != MY_USER_ID: return

    #if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        #os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    
    #the_user = await event.get_reply_message()

    replied_user = await get_user(event)

    caption = await fetch_info(replied_user, event)

    #message_id_to_reply = event.message.reply_to_msg_id

    #if not message_id_to_reply:
        #message_id_to_reply = None

    if event.sender_id == MY_USER_ID:
        await event.edit(caption, parse_mode="html")
    else:
        await event.reply(caption, parse_mode="html")

@SPY(pattern="^!!fulldump$")
async def whodump(event):
    """ For !!whois command, get info about a user. """
    id = str(ID(event))
    if id not in GS() and id not in GIS() and event.sender_id != MY_USER_ID: return
    replied_user = await get_user(event)
    #print(replied_user)
    if len(f"{Q(M(replied_user))}") > 4000:
        with open('full_user_info.txt', 'w') as file:
            file.write(f"{replied_user}")
        if event.is_reply:
            await bot.send_file(event.chat_id, "full_user_info.txt", reply_to=event.reply_to_msg_id)
        else:
            await bot.send_file(event.chat_id, "full_user_info.txt", reply_to=event.id)
        await event.delete()
        if os.path.exists('output.txt'):
            os.remove('output.txt')
    elif event.sender_id == MY_USER_ID:
        await event.edit(f"{Q(M(replied_user))}",parse_mode="HTML")
    else:
        await event.reply(f"{Q(M(replied_user))}",parse_mode="HTML")

def progress(current, total):
    """ Calculate and return the download progress with given arguments. """
    print("Downloaded {} of {}\nCompleted {}".format(current, total,
                                                     (current / total) * 100))

@SPY(pattern=r"^!!getqr$", outgoing=True)
async def parseqr(qr_e):
    """ For .getqr command, get QR Code content from the replied photo. """
    start = datetime.datetime.now()
    downloaded_file_name = await qr_e.client.download_media(
        await qr_e.get_reply_message(), progress_callback=progress)
    url = "https://api.qrserver.com/v1/read-qr-code/?outputformat=json"
    file = open(downloaded_file_name, "rb")
    files = {"file": file}
    resp = requests.post(url, files=files).json()
    qr_contents = resp[0]["symbol"][0]["data"]
    file.close()
    os.remove(downloaded_file_name)
    end = datetime.datetime.now()
    duration = (end - start).seconds
    await qr_e.edit("Obtained QRCode contents in {} seconds.\n{}".format(
        duration, qr_contents))
    await asyncio.sleep(5)
    await qr_e.edit(f"{qr_contents}")


@SPY(pattern=r"^!!mkqr(?: |$)([\s\S]*)")
async def make_qr(qrcode):
    """ For .makeqr command, make a QR Code containing the given content. """
    id = str(ID(qrcode))
    if id not in GS() and id not in GIS() and qrcode.sender_id != MY_USER_ID: return
    start = datetime.datetime.now()
    input_str = qrcode.pattern_match.group(1)
    message = "SYNTAX: `.makeqr <long text to include>`"
    if qrcode.is_reply:
        reply_msg_id = await qrcode.get_reply_message()
    else:
        reply_msg_id = qrcode.id
    if input_str:
        message = input_str
    elif qrcode.reply_to_msg_id:
        previous_message = await qrcode.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await qrcode.client.download_media(
                previous_message, progress_callback=progress)
            m_list = None
            with open(downloaded_file_name, "rb") as file:
                m_list = file.readlines()
            message = ""
            for media in m_list:
                message += media.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message

    url = "https://api.qrserver.com/v1/create-qr-code/?data={}&\
size=200x200&charset-source=UTF-8&charset-target=UTF-8\
&ecc=L&color=0-0-0&bgcolor=255-255-255\
&margin=1&qzone=0&format=jpg"

    resp = requests.get(url.format(message), stream=True)
    required_file_name = "temp_qr.webp"
    with open(required_file_name, "w+b") as file:
        for chunk in resp.iter_content(chunk_size=128):
            file.write(chunk)
    await qrcode.client.send_file(
        qrcode.chat_id,
        required_file_name,
        reply_to=reply_msg_id,
        progress_callback=progress,
    )
    os.remove(required_file_name)
    duration = (datetime.datetime.now() - start).seconds
    if qrcode.sender_id == MY_USER_ID:
        await qrcode.edit("Created QRCode in {} seconds".format(duration))
        await asyncio.sleep(5)
        await qrcode.delete()
    else:
        await qrcode.reply("Created QRCode in {} seconds".format(duration))

"""
@SPY(outgoing=True, pattern=r"^!!pdf2img$")
async def pdf(e):
  message = await e.get_reply_message()
  if message.file.mime_type == "application/pdf":
    file = message.document
    await e.edit("**Downloading...**")
    file = await bot.download_file(file, "file.pdf")
    if os.path.isdir("./files") is False:
      os.mkdir("./files")
    else:
      rmtree("./files")
      os.mkdir("./files")
    await e.edit("**Processing...**")  
    images_from_path = convert_from_path('./file.pdf', output_folder='./files', fmt='png')
    await e.edit("**Sending...**")
    for filename in os.listdir("./files"):
      await e.client.send_file(e.chat_id, open('./files/' + filename, 'rb'), reply_to=message)
    rmtree("./files")
    os.remove("./file.pdf")
  else:
    await e.edit("`Not a pdf file. Aborting...`")
    return
"""
"""
@SPY(outgoing=True, pattern=r"^!!doc2pdf$")
async def doc(e):
  if CONVERT_TOKEN == False:
    await e.edit("**No converter API defined. Fill it in config.env file. Aborting...**")
    return
  convertapi.api_secret = CONVERT_TOKEN
  message = await e.get_reply_message()
  if message.file.mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or message.file.mime_type == "application/msword":
    file = message.document
    await e.edit("**Downloading...**")
    result = None
    if  message.file.mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document": #docx
      file = await bot.download_file(file, "file.docx")
      await e.edit("**Converting...**")
      result = convertapi.convert('pdf', { 'File': 'file.docx' })
      os.remove('file.docx')
    if message.file.mime_type == "application/msword": #docx
        file = await bot.download_file(file, "file.doc")
        await e.edit("**Converting...**")
        result = convertapi.convert('pdf', { 'File': 'file.doc' })
        os.remove('file.doc')
    result.file.save('file.pdf')
    await e.edit("**Sending...**")
    await e.client.send_file(e.chat_id, f'file.pdf',reply_to=message)
    
    os.remove('file.pdf')
  else:
    await e.edit("`Not a doc/docx file. Aborting...`")
    return
@SPY(outgoing=True, pattern=r"^!!doc2img$")
async def doc_png(e):
  message = await e.get_reply_message()
  if CONVERT_TOKEN == False:
    await e.edit("**No converter API defined. Fill it in config.env file. Aborting...**")
    return
  convertapi.api_secret = CONVERT_TOKEN
  if message.file.mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or message.file.mime_type == "application/msword":
    file = message.document
    await e.edit("**Downloading...**")
    result = None
    if  message.file.mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document": #docx
      file = await bot.download_file(file, "file.docx")
      await e.edit("**Converting...**")
      result = convertapi.convert('pdf', { 'File': 'file.docx' })
      os.remove('file.docx')
    if message.file.mime_type == "application/msword": #docx
        file = await bot.download_file(file, "file.doc")
        await e.edit("**Converting...**")
        result = convertapi.convert('pdf', { 'File': 'file.doc' })
        os.remove('file.doc')
    result.file.save('file.pdf')
    if os.path.isdir("./files") is False:
      os.mkdir("./files")
    else:
      rmtree("./files")
      os.mkdir("./files")
    await e.edit("**Processing...**")
    images_from_path = convert_from_path('./file.pdf', output_folder='./files', fmt='png')
    await e.edit("**Sending...**")
    for filename in os.listdir("./files"):
      await e.client.send_file(e.chat_id, open('./files/' + filename, 'rb'), reply_to=message)
    rmtree("./files")
    os.remove(f"file.pdf")
  else:
    await e.edit("`Not a doc file. Aborting...`")
    return
  
@SPY(outgoing=True, pattern=r"^!!xls2img$")
async def xls_png(e):
  message = await e.get_reply_message()
  if CONVERT_TOKEN == False:
    await e.edit("**No converter API defined. Fill it in config.env file. Aborting...**")
    return
  convertapi.api_secret = CONVERT_TOKEN
  if message.file.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or message.file.mime_type == "application/vnd.ms-excel":
    file = message.document
    await e.edit("**Downloading...**")
    result = None
    if  message.file.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": #xlsx
      file = await bot.download_file(file, "file.xlsx")
      await e.edit("**Converting...**")
      result = convertapi.convert('pdf', { 'File': 'file.xlsx' })
      os.remove('file.xlsx')
    if message.file.mime_type == "application/vnd.ms-excel": #xls
        file = await bot.download_file(file, "file.xls")
        await e.edit("**Converting...**")
        result = convertapi.convert('pdf', { 'File': 'file.xls' })
        os.remove('file.xls')
    result.file.save('file.pdf')
    if os.path.isdir("./files") is False:
      os.mkdir("./files")
    else:
      rmtree("./files")
      os.mkdir("./files")
    await e.edit("**Processing...**")
    images_from_path = convert_from_path('./file.pdf', output_folder='./files', fmt='png')
    await e.edit("**Sending...**")
    for filename in os.listdir("./files"):
      await e.client.send_file(e.chat_id, open('./files' + filename, 'rb'), reply_to=message)
    rmtree("./files")
    os.remove(f"file.pdf")
  else:
    await e.edit("`Not a xls/xlsx file. Aborting...`")
    return
@SPY(outgoing=True, pattern=r"^!!xls2pdf$")
async def xls_png(e):
  message = await e.get_reply_message()
  if CONVERT_TOKEN == False:
    await e.edit("**No converter API defined. Fill it in config.env file. Aborting...**")
    return
  convertapi.api_secret = CONVERT_TOKEN
  if message.file.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or message.file.mime_type == "application/vnd.ms-excel":
    file = message.document
    await e.edit("**Downloading...**")
    result = None
    if  message.file.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": #xlsx
      file = await bot.download_file(file, "file.xlsx")
      await e.edit("**Converting...**")
      result = convertapi.convert('pdf', { 'File': 'file.xlsx' })
      os.remove('file.xlsx')
    if message.file.mime_type == "application/vnd.ms-excel": #xls
        file = await bot.download_file(file, "file.xls")
        await e.edit("**Converting...**")
        result = convertapi.convert('pdf', { 'File': 'file.xls' })
        os.remove('file.xls')
    result.file.save('file.pdf')
    await e.edit("**Sending...**")
    await e.client.send_file(e.chat_id, f'file.pdf',reply_to=message)
  else:
    await e.edit("`Not a xls/xlsx file. Aborting...`")
    return

@SPY(outgoing=True, pattern=r"^!!ppt2img$")
async def ppt_png(e):
  message = await e.get_reply_message()
  if CONVERT_TOKEN == False:
    await e.edit("**No converter API defined. Fill it in config.env file. Aborting...**")
    return
  convertapi.api_secret = CONVERT_TOKEN
  if message.file.mime_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation" or message.file.mime_type == "application/vnd.ms-powerpoint":
    file = message.document
    await e.edit("**Downloading...**")
    result = None
    if  message.file.mime_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation": #pptx
      file = await bot.download_file(file, "file.pptx")
      await e.edit("**Converting...**")
      result = convertapi.convert('pdf', { 'File': 'file.pptx' })
      os.remove('file.pptx')
    if message.file.mime_type == "application/vnd.ms-powerpoint": #ppt
        file = await bot.download_file(file, "file.ppt")
        await e.edit("**Converting...**")
        result = convertapi.convert('pdf', { 'File': 'file.ppt' })
        os.remove('file.ppt')
    result.file.save('file.pdf')
    if os.path.isdir("./files") is False:
      os.mkdir("./files")
    await e.edit("**Processing...**")
    images_from_path = convert_from_path('./file.pdf', output_folder='./files', fmt='png')
    await e.edit("**Sending...**")
    for filename in os.listdir("/root/Telegram-UserBot/files/"):
      await e.client.send_file(e.chat_id, open('./files/' + filename, 'rb'), reply_to=message)
    rmtree("./files")
    os.remove(f"./file.pdf")
  else:
    await e.edit("`Not a ppt/pptx file. Aborting...`")
    return
@SPY(outgoing=True, pattern=r"^!!ppt2pdf$")
async def ppt_pdf(e):
  message = await e.get_reply_message()
  if CONVERT_TOKEN == False:
    await e.edit("**No converter API defined. Fill it in config.env file. Aborting...**")
    return
  convertapi.api_secret = CONVERT_TOKEN
  if message.file.mime_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation" or message.file.mime_type == "application/vnd.ms-powerpoint":
    file = message.document
    await e.edit("**Downloading...**")
    result = None
    if  message.file.mime_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation": #pptx
      file = await bot.download_file(file, "file.pptx")
      await e.edit("**Converting...**")
      result = convertapi.convert('pdf', { 'File': 'file.pptx' })
      os.remove('file.pptx')
    if message.file.mime_type == "application/vnd.ms-powerpoint": #ppt
        file = await bot.download_file(file, "file.ppt")
        await e.edit("**Converting...**")
        result = convertapi.convert('pdf', { 'File': 'file.ppt' })
        os.remove('file.ppt')
    result.file.save('file.pdf')
    await e.edit("**Sending...**")
    await e.client.send_file(e.chat_id, f'file.pdf',reply_to=message)
  else:
    await e.edit("`Not a ppt/pptx file. Aborting...`")
    return
"""


@SPY(outgoing=True, pattern=r"^!!voice$")
async def vc(v):
    global msg_for_percentage
    msg_for_percentage = v
    message = await v.get_reply_message()
    if message.audio or message.voice:
      file = message.audio or message.voice
      await v.edit("**Downloading...**")
      file = await bot.download_file(file, "voice.mp3")
      await v.edit("**Sending...**")
      await v.client.send_file(v.chat_id,
                             f'voice.mp3',
                             reply_to=message, voice_note=True, progress_callback = callback)
      os.remove(f'voice.mp3')
      await asyncio.sleep(3)
      await v.delete()
    else:
         await v.edit("**Bot doesn't support magic! Use audio or voice message!**")

@SPY(outgoing=True, pattern=r"^!!mp3$")
async def mp3(e):
  global msg_for_percentage
  from moviepy import VideoFileClip
  msg_for_percentage = e
  message = await e.get_reply_message()
  if message.audio or message.voice:
    file = message.audio or message.voice
    file = await bot.download_file(file, "voice.mp3")
    await e.edit("**Sending...**")
    await e.client.send_file(e.chat_id,
                            f'voice.mp3',
                            reply_to=message, progress_callback = callback)
    os.remove(f'voice.mp3')
    await asyncio.sleep(3)
    await e.delete()
    return
  if message.video:
    video = message.video
    await e.edit("**Downloading...**")
    video = await bot.download_file(video, "video.mp4")
    await e.edit("**Converting video...**")
    clip = VideoFileClip('video.mp4')
    clip.audio.write_audiofile('video.mp3')
    os.remove(f'video.mp4')
    await e.edit("**Sending mp3...**")
    await e.client.send_file(e.chat_id,
                             'video.mp3',
                             reply_to=message, progress_callback = callback)
    os.remove('video.mp3')
    await asyncio.sleep(3)
    await e.delete()
    return
  else:
         await e.edit("**Bot doesn't support magic! Use video or voice message.**")
         return

@SPY(outgoing=True, pattern=r"^!!mp4$")
async def mp4(v):
  global msg_for_percentage
  msg_for_percentage = v
  message = await v.get_reply_message()
  if message.video_note:
    file = message.video_note
    await v.edit("**Downloading...**")
    file = await bot.download_file(file, "video.mp4")
    await v.edit("**Sending...**")
    await v.client.send_file(v.chat_id,
                            f'video.mp4',
                            reply_to=message, progress_callback = callback)
    os.remove(f'video.mp4')
    return
  else:
         await v.edit("**Bot doesn't support magic! Use video_note.**")
         return

@SPY(outgoing=True, pattern=r"^!!wiki (.*)")
async def wiki(wiki_q):
    """ For .google command, fetch content from Wikipedia. """
    import wikipedia
    id = str(ID(wiki_q))
    if id not in GS() and id not in GIS() and id != str(MY_USER_ID): return
    replied = await wiki_q.get_reply_message()
    match = wiki_q.pattern_match.group(1)
    try:
        wikipedia.summary(match)
    except wikipedia.exceptions.DisambiguationError as error:
        if id == str(MY_USER_ID): 
            await wiki_q.edit(f"Disambiguated page found.\n\n{error}")
        else:
            if replied:
                await replied.reply(f"Disambiguated page found.\n\n{error}")
            else:
                await wiki_q.reply(f"Disambiguated page found.\n\n{error}")
        return
    except wikipedia.exceptions.PageError as pageerror:
        if id == str(MY_USER_ID): 
            await wiki_q.edit(f"Page not found.\n\n{pageerror}")
        else:
            if replied:
                await replied.reply(f"Page not found.\n\n{pageerror}")
            else:
                await wiki_q.reply(f"Page not found.\n\n{pageerror}")
        return
    result = wikipedia.summary(match)
    if len(result) >= 4000:
        file = open("output.txt", "w+")
        file.write(result)
        file.close()
        await wiki_q.client.send_file(
            wiki_q.chat_id,
            "output.txt",
            reply_to=wiki_q.id,
            caption="`Output too large, send as file.`",
        )
        if id == str(MY_USER_ID): 
            await wiki_q.delete()
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        return
    if id == str(MY_USER_ID): 
        await wiki_q.edit("<b>Search:</b>\n<blockquote><code>" + match + "</code></blockquote>\n\n<b>Result:</b>\n<blockquote>" + result + "</blockquote>", parse_mode="html")
    elif replied:
        await replied.reply("<b>Search:</b>\n<blockquote><code>" + match + "</code></blockquote>\n\n<b>Result:</b>\n<blockquote>" + result + "</blockquote>", parse_mode="html")
    else:
        await wiki_q.reply("<b>Search:</b>\n<blockquote><code>" + match + "</code></blockquote>\n\n<b>Result:</b>\n<blockquote>" + result + "</blockquote>", parse_mode="html")

def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = len(line) // 55
                for z in range(1, k + 2):
                    lines.append(line[((z - 1) * 55) : (z * 55)])
    return lines[:25]


@SPY(pattern="(?s)^!!write ?(.*)?")
async def writer(e):
    id = str(ID(e))
    #print(id)
    if id not in GS() and id not in GIS() and id != str(MY_USER_ID): return
    if e.pattern_match.group(1):
        text = e.text.split(maxsplit=1)[1]
    elif e.is_reply:
        reply = await e.get_reply_message()
        text = reply.text
        if not text:
            return
    else:
        return# await e.edit("error")
    if id == str(MY_USER_ID):
        await e.edit("running")
    img = Image.open("tgbot/img/note.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("tgbot/sticker/font/ass.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    bbox = font.getbbox("hg")
    line_height = bbox[3] - bbox[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "ult.jpg"
    img.save(file)
    if e.is_reply:
        rmsg = await e.get_reply_message()
        await rmsg.reply(file=file)
    else:
        await e.reply(file=file)
    os.remove(file)
    await e.delete()

@SPY(outgoing=True, pattern="^!!me joke$")
async def joker(E):
    try:
        await E.edit("&#x00AD;", parse_mode="HTML")
        #response = requests.get("https://v2.jokeapi.dev/joke/Any")
        joke_data = requests.get("https://v2.jokeapi.dev/joke/Any").json()
    
        # Check if it's a two-part joke or single
        if joke_data["type"] == "twopart":
            await E.edit(f'{joke_data["setup"]}\n{joke_data["delivery"]}')
        else:
            await E.edit(joke_data["joke"])
    except:
        await E.delete()


# Define dual character. Make sure that mapping is bijective.
FLIP_RANGES = [
    (string.ascii_lowercase, "ɐqɔpǝɟƃɥᴉɾʞꞁɯuodbɹsʇnʌʍxʎz"),
    # alternatives: l:ʅ
    (string.ascii_uppercase, "ⱯᗺƆᗡƎᖵ⅁HIᒋ⋊ꞀWNOԀꝹᴚS⊥∩ɅMX⅄Z"),
    # alternatives: L:ᒣ⅂, J:ſ, F:߃Ⅎ, A:∀ᗄ, U:Ⴖ, W:Ϻ, C:ϽↃ, Q:Ό, M:Ɯꟽ
    (string.digits, "0ІᘔƐᔭ59Ɫ86"),
    (string.punctuation, "¡„#$%⅋,)(*+'-˙/:؛>=<¿@]\\[ᵥ‾`}|{~"),
]

UNICODE_COMBINING_DIACRITICS = {'̈': '̤', '̊': '̥', '́': '̗', '̀': '̖',
                                '̇': '̣', '̃': '̰', '̄': '̱', '̂': '̬', '̆': '̯', '̌': '̭',
                                '̑': '̮', '̍': '̩'}

TRANSLITERATIONS = {'ß': 'ss'}

# character lookup
_CHARLOOKUP = {}
for chars, flipped in FLIP_RANGES:
    _CHARLOOKUP.update(zip(chars, flipped))

# get reverse direction
for char in _CHARLOOKUP.copy():
    # make 1:1 back transformation possible
    assert (_CHARLOOKUP[char] not in _CHARLOOKUP
            or _CHARLOOKUP[_CHARLOOKUP[char]] == char), \
        ("%s has ambiguous mapping" % _CHARLOOKUP[char])
    _CHARLOOKUP[_CHARLOOKUP[char]] = char

# lookup for diacritical marks, reverse first
_DIACRITICSLOOKUP = dict([(UNICODE_COMBINING_DIACRITICS[char], char)
                          for char in UNICODE_COMBINING_DIACRITICS])
_DIACRITICSLOOKUP.update(UNICODE_COMBINING_DIACRITICS)


def transform(text, transliterations=None):
    transliterations = transliterations or TRANSLITERATIONS

    for character in transliterations:
        text = text.replace(character, transliterations[character])

    input_chars = list(text)
    input_chars.reverse()

    output = []
    for character in input_chars:
        if character in _CHARLOOKUP:
            output.append(_CHARLOOKUP[character])
        else:
            char_normalized = unicodedata.normalize("NFD", character)

            for c in char_normalized[:]:
                if c in _CHARLOOKUP:
                    char_normalized = char_normalized.replace(c, _CHARLOOKUP[c])
                elif c in _DIACRITICSLOOKUP:
                    char_normalized = char_normalized.replace(c, _DIACRITICSLOOKUP[c])

            output.append(unicodedata.normalize("NFC", char_normalized))

    return ''.join(output)


@SPY(outgoing=True, pattern=r"^!!flip(\s+[\S\s]+|$)")
async def flip_message(e):
    reply_message = await e.get_reply_message()
    text = reply_message.text if reply_message and not e.pattern_match.group(1) else e.pattern_match.group(1)
    flipped = transform(text)
    await e.edit(flipped)


@SPY(outgoing=True, pattern='(?s)!!type ?(.+)?')
async def typeerr(event):
    try:
        reply_msg = await event.get_reply_message()
        final_text = event.pattern_match.group(1)
        if reply_msg and not final_text:
            final_text = reply_msg.text
        elif not reply_msg and not final_text:
            return
        i = ""
        await event.edit("|")
        await asyncio.sleep(0.2)
        for j in final_text:
            await asyncio.sleep(0.05)
            await event.edit(i+j+"|")
            i += j
            await asyncio.sleep(0.3)
        await event.edit(i)
            #await event.edit(i)
    except Exception:
        print(traceback.format_exc())

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

COLORS = [
    "#F07975",
    "#F49F69",
    "#F9C84A",
    "#8CC56E",
    "#6CC7DC",
    "#80C1FA",
    "#BCB3F9",
    "#E181AC",
]


async def process(msg, user, client, reply, replied=None):
    # Importing fonts and gettings the size of text
    font = ImageFont.truetype("tgbot/sticker/font/Roboto-Medium.ttf", 43, encoding="utf-16")
    font2 = ImageFont.truetype("tgbot/sticker/font/Roboto-Regular.ttf", 33, encoding="utf-16")
    mono = ImageFont.truetype("tgbot/sticker/font/DroidSansMono.ttf", 30, encoding="utf-16")
    italic = ImageFont.truetype("tgbot/sticker/font/Roboto-Italic.ttf", 33, encoding="utf-16")
    fallback = ImageFont.truetype("tgbot/sticker/font/Quivira.otf", 43, encoding="utf-16")

    # Splitting text
    maxlength = 0
    width = 0
    text = []
    for line in msg.split("\n"):
        length = len(line)
        if length > 43:
            text += textwrap.wrap(line, 43)
            maxlength = 43
            if width < fallback.getbbox(line[:43])[2]:
                if "MessageEntityCode" in str(reply.entities):
                    width = mono.getbbox(line[:43])[2] + 30
                else:
                    width = fallback.getbbox(line[:43])[2]
            next
        else:
            text.append(line + "\n")
            if width < fallback.getbbox(line)[2]:
                if "MessageEntityCode" in str(reply.entities):
                    width = mono.getbbox(line)[2] + 30
                else:
                    width = fallback.getbbox(line)[2]
            if maxlength < length:
                maxlength = length
            
            #print(mono.getbbox(line))
            #print(line)

    title = ""
    try:
        details = await client(
            GetParticipantRequest(reply.chat_id, user.id)
        )
        if isinstance(details.participant, types.ChannelParticipantCreator):
            title = details.participant.rank if details.participant.rank else "Creator"
        elif isinstance(details.participant, types.ChannelParticipantAdmin):
            title = details.participant.rank if details.participant.rank else "Admin"
    except UserNotParticipantError:
        pass
    except TypeError:
        pass
    titlewidth = font2.getbbox(title)[2]

    # Get user name
    tot = (
        f"{user.first_name} {user.last_name}" if (user.first_name and user.last_name) else
        user.first_name or
        getattr(user, 'title', '') or
        getattr(user, 'username', '') or
        "Bot"
    )

    namewidth = fallback.getbbox(tot)[2] + 10

    if namewidth > width:
        width = namewidth
    width += titlewidth + 30 if titlewidth > width - namewidth else -(titlewidth - 30)
    height = len(text) * 40

    # Profile Photo BG
    pfpbg = Image.new("RGBA", (125, 600), (0, 0, 0, 0))

    # Draw Template
    top, middle, bottom = await drawer(width, height)
    # Profile Photo Check and Fetch
    yes = False
    color = random.choice(COLORS)
    async for photo in client.iter_profile_photos(user, limit=1):
        yes = True
    if yes:
        pfp = await client.download_profile_photo(user)
        paste = Image.open(pfp)
        os.remove(pfp)
        paste.thumbnail((105, 105))

        # Mask
        mask_im = Image.new("L", paste.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.ellipse((0, 0, 105, 105), fill=255)

        # Apply Mask
        pfpbg.paste(paste, (0, 0), mask_im)
    else:
        paste, color = await no_photo(user, tot)
        pfpbg.paste(paste, (0, 0))

    # Creating a big canvas to gather all the elements
    canvassize = (
        middle.width + pfpbg.width,
        top.height + middle.height + bottom.height,
    )
    canvas = Image.new("RGBA", canvassize)
    draw = ImageDraw.Draw(canvas)

    y = 80
    if replied:
        # Creating a big canvas to gather all the elements
        reptot = (
            f"{replied.sender.first_name} {replied.sender.last_name}".strip()
            if getattr(replied.sender, 'last_name', None)
            else replied.sender.first_name or
            getattr(replied.sender, 'title', '') or
            getattr(replied.sender, 'username', '') or
            "Bot"
        )
        replywidth = font2.getbbox(reptot)[2]
        if reply.sticker:
            sticker = await reply.download_media()
            stimg = Image.open(sticker)
            canvas = canvas.resize((stimg.width + pfpbg.width, stimg.height + 160))
            top = Image.new("RGBA", (200 + stimg.width, 300), (29, 29, 29, 255))
            draw = ImageDraw.Draw(top)
            try:
                testreplymsg = replied.message.replace("\n", " ")
            except:
                testreplymsg = ""
            await replied_user(draw, reptot, testreplymsg, 20, 0)
            top = top.crop((135, 70, top.width, 300))
            canvas.paste(pfpbg, (0, 0))
            canvas.paste(top, (pfpbg.width + 10, 0))
            canvas.paste(stimg, (pfpbg.width + 10, 140))
            os.remove(sticker)
            return True, canvas
        canvas = canvas.resize((canvas.width + 60, canvas.height + 120))
        top, middle, bottom = await drawer(middle.width + 60, height + 105)
        canvas.paste(pfpbg, (0, 0))
        canvas.paste(top, (pfpbg.width, 0))
        canvas.paste(middle, (pfpbg.width, top.height))
        canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
        draw = ImageDraw.Draw(canvas)
        if replied.sticker:
            replied.text = "Sticker"
        elif replied.photo:
            replied.text = "Photo"
        elif replied.audio:
            replied.text = "Audio"
        elif replied.voice:
            replied.text = "Voice Message"
        elif replied.document:
            replied.text = "Document"
        
        try:
            testreplymsg = replied.message.replace("\n", " ")
        except:
            testreplymsg = ""
        await replied_user(
            draw,
            reptot,
            testreplymsg,
            maxlength + len(title),
            len(title),
        )
        y = 200
    elif reply.sticker:
        sticker = await reply.download_media()
        stimg = Image.open(sticker)
        canvas = canvas.resize((stimg.width + pfpbg.width + 30, stimg.height + 10))
        canvas.paste(pfpbg, (0, 0))
        canvas.paste(stimg, (pfpbg.width + 10, 10))
        os.remove(sticker)
        return True, canvas
    elif reply.document and not reply.audio and not reply.audio:
        docname = ".".join(reply.document.attributes[-1].file_name.split(".")[:-1])
        doctype = reply.document.attributes[-1].file_name.split(".")[-1].upper()
        if reply.document.size < 1024:
            docsize = str(reply.document.size) + " Bytes"
        elif reply.document.size < 1048576:
            docsize = str(round(reply.document.size / 1024, 2)) + " KB "
        elif reply.document.size < 1073741824:
            docsize = str(round(reply.document.size / 1024 ** 2, 2)) + " MB "
        else:
            docsize = str(round(reply.document.size / 1024 ** 3, 2)) + " GB "
        docbglen = (
            font.getbbox(docsize)[2]
            if font.getbbox(docsize)[2] > font.getbbox(docname)[2]
            else font.getbbox(docname)[2]
        )
        canvas = canvas.resize((pfpbg.width + width + docbglen, 160 + height))
        top, middle, bottom = await drawer(width + docbglen, height + 30)
        canvas.paste(pfpbg, (0, 0))
        canvas.paste(top, (pfpbg.width, 0))
        canvas.paste(middle, (pfpbg.width, top.height))
        canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
        canvas = await doctype(docname, docsize, doctype, canvas)
        y = 80 if text else 0
    else:
        canvas.paste(pfpbg, (0, 0))
        canvas.paste(top, (pfpbg.width, 0))
        canvas.paste(middle, (pfpbg.width, top.height))
        canvas.paste(bottom, (pfpbg.width, top.height + middle.height))
        y = 85

    # Writing User's Name
    space = pfpbg.width + 30
    namefallback = ImageFont.truetype("tgbot/sticker/font/Quivira.otf", 43, encoding="utf-16")
    for letter in tot:
        """
        if letter in emoji.EMOJI_DATA:
            newemoji, mask = await emoji_fetch(letter)
            canvas.paste(newemoji, (space, 24), mask)
            space += 40
        else:
            if not await fontTest(letter):
                draw.text((space, 20), letter, font=namefallback, fill=color)
                space += namefallback.getbbox(letter)[2]
            else:
                draw.text((space, 20), letter, font=font, fill=color)
                space += font.getbbox(letter)[2]
        """
        if not await fontTest(letter):
            draw.text((space, 20), letter, font=namefallback, fill=color)
            space += namefallback.getbbox(letter)[2]
        else:
            draw.text((space, 20), letter, font=font, fill=color)
            space += font.getbbox(letter)[2]

    # Writing all separating emojis and regular texts
    x = pfpbg.width + 30
    bold, mono, italic, link = await get_entity(reply)
    mdlength = 0
    index = 0
    emojicount = 0
    textfallback = ImageFont.truetype("tgbot/sticker/font/Quivira.otf", 33, encoding="utf-16")
    textcolor = "white"
    for line in text:
        for letter in line:
            index = (
                msg.find(letter) if emojicount == 0 else msg.find(letter) + emojicount
            )
            for offset, length in bold.items():
                if index in range(offset, length):
                    font2 = ImageFont.truetype(
                        "tgbot/sticker/font/Roboto-Medium.ttf", 33, encoding="utf-16"
                    )
                    textcolor = "white"
            for offset, length in italic.items():
                if index in range(offset, length):
                    font2 = ImageFont.truetype(
                        "tgbot/sticker/font/Roboto-Italic.ttf", 33, encoding="utf-16"
                    )
                    textcolor = "white"
            for offset, length in mono.items():
                if index in range(offset, length):
                    font2 = ImageFont.truetype(
                        "tgbot/sticker/font/DroidSansMono.ttf", 30, encoding="utf-16"
                    )
                    textcolor = "white"
            for offset, length in link.items():
                if index in range(offset, length):
                    font2 = ImageFont.truetype(
                        "tgbot/sticker/font/Roboto-Regular.ttf", 30, encoding="utf-16"
                    )
                    textcolor = "#898989"
            """
            if letter in emoji.EMOJI_DATA:
                newemoji, mask = await emoji_fetch(letter)
                canvas.paste(newemoji, (x, y - 2), mask)
                x += 45
                emojicount += 1
            else:
                if not await fontTest(letter):
                    draw.text((x, y), letter, font=textfallback, fill=textcolor)
                    x += textfallback.getbbox(letter)[2]
                else:
                    draw.text((x, y), letter, font=font2, fill=textcolor)
                    x += font2.getbbox(letter)[2]
            """
            if not await fontTest(letter):
                draw.text((x, y), letter, font=textfallback, fill=textcolor)
                x += textfallback.getbbox(letter)[2]
            else:
                draw.text((x, y), letter, font=font2, fill=textcolor)
                x += font2.getbbox(letter)[2]
            #"""
            msg = msg.replace(letter, "¶", 1)
        y += 40
        x = pfpbg.width + 30
    return True, canvas


async def drawer(width, height):
    # Top part
    top = Image.new("RGBA", (width, 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(top)
    draw.line((10, 0, top.width - 20, 0), fill=(29, 29, 29, 255), width=50)
    draw.pieslice((0, 0, 30, 50), 180, 270, fill=(29, 29, 29, 255))
    draw.pieslice((top.width - 75, 0, top.width, 50), 270, 360, fill=(29, 29, 29, 255))

    # Middle part
    middle = Image.new("RGBA", (top.width, height + 75), (29, 29, 29, 255))

    # Bottom part
    bottom = ImageOps.flip(top)

    return top, middle, bottom


async def fontTest(letter):
    test = TTFont("tgbot/sticker/font/Roboto-Medium.ttf")
    for table in test["cmap"].tables:
        if ord(letter) in table.cmap.keys():
            return True


async def get_entity(msg):
    bold = {0: 0}
    italic = {0: 0}
    mono = {0: 0}
    link = {0: 0}
    if not msg.entities:
        return bold, mono, italic, link
    for entity in msg.entities:
        if isinstance(entity, types.MessageEntityBold):
            bold[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityItalic):
            italic[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityCode):
            mono[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityUrl):
            link[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityTextUrl):
            link[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityMention):
            link[entity.offset] = entity.offset + entity.length
    return bold, mono, italic, link


async def doctype(name, size, type, canvas):
    font = ImageFont.truetype("tgbot/sticker/font/Roboto-Medium.ttf", 38)
    doc = Image.new("RGBA", (130, 130), (29, 29, 29, 255))
    draw = ImageDraw.Draw(doc)
    draw.ellipse((0, 0, 130, 130), fill="#434343")
    draw.line((66, 28, 66, 53), width=14, fill="white")
    draw.polygon([(67, 77), (90, 53), (42, 53)], fill="white")
    draw.line((40, 87, 90, 87), width=8, fill="white")
    canvas.paste(doc, (160, 23))
    draw2 = ImageDraw.Draw(canvas)
    draw2.text((320, 40), name, font=font, fill="white")
    draw2.text((320, 97), size + type, font=font, fill="#AAAAAA")
    return canvas


async def no_photo(reply, tot):
    pfp = Image.new("RGBA", (105, 105), (0, 0, 0, 0))
    pen = ImageDraw.Draw(pfp)
    color = random.choice(COLORS)
    pen.ellipse((0, 0, 105, 105), fill=color)
    letter = "" if not tot else tot[0]
    font = ImageFont.truetype("tgbot/sticker/font/Roboto-Regular.ttf", 60)
    pen.text((32, 17), letter, font=font, fill="white")
    return pfp, color


async def emoji_fetch(emoji):
    try:
        emojis = json.loads(
            urllib.request.urlopen(
                "https://github.com/erenmetesar/modules-repo/raw/master/emojis.txt"
            )
            .read()
            .decode()
        )
        print(type(emojis))
    except Exception:
        print(traceback.format_exc())
        emojis = 0 # traceback.format_exc()
    
    print(emojis)
    print(emoji)
    if emoji in emojis:
        img = emojis[emoji]
        return await transparent(
            urllib.request.urlretrieve(img, "tgbot/sticker/font/emoji.png")[0]
        )
    else:
        img = emojis["⛔"]
        return await transparent(
            urllib.request.urlretrieve(img, "tgbot/sticker/font/emoji.png")[0]
        )


async def transparent(emoji):
    emoji = Image.open(emoji).convert("RGBA")
    emoji.thumbnail((40, 40))

    # Mask
    mask = Image.new("L", (40, 40), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 40, 40), fill=255)
    return emoji, mask


async def replied_user(draw, tot, text, maxlength, title):
    namefont = ImageFont.truetype("tgbot/sticker/font/Roboto-Medium.ttf", 38)
    namefallback = ImageFont.truetype("tgbot/sticker/font/Quivira.otf", 38)
    textfont = ImageFont.truetype("tgbot/sticker/font/Roboto-Regular.ttf", 32)
    textfallback = ImageFont.truetype("tgbot/sticker/font/Roboto-Medium.ttf", 38)
    maxlength = maxlength + 7 if maxlength < 10 else maxlength
    text = text[: maxlength - 2] + ".." if len(text) > maxlength else text
    draw.line((165, 90, 165, 170), width=5, fill="white")
    space = 0
    for letter in tot:
        if not await fontTest(letter):
            draw.text((180 + space, 86), letter, font=namefallback, fill="#888888")
            space += namefallback.getbbox(letter)[2]
        else:
            draw.text((180 + space, 86), letter, font=namefont, fill="#888888")
            space += namefont.getbbox(letter)[2]
    space = 0
    for letter in text:
        if not await fontTest(letter):
            draw.text((180 + space, 132), letter, font=textfallback, fill="#888888")
            space += textfallback.getbbox(letter)[2]
        else:
            draw.text((180 + space, 132), letter, font=textfont, fill="white")
            space += textfont.getbbox(letter)[2]


#@bot.on(events.NewMessage(pattern="^(?s)!!q ?(.+)?"))
@SPY(outgoing=True, pattern="(?s)^!!q ?(.*)?")
async def quotly(event):
    id = str(ID(event))
    if id not in GS() and id not in GIS() and id != str(MY_USER_ID): return
    try:
        if event.fwd_from:
            return
        reply = await event.get_reply_message()
        if reply is None:
            #await event.reply("What to quote?")
            return
        msg = reply.message
        if event.pattern_match.group(1):
            msg = event.pattern_match.group(1)
        repliedreply = await reply.get_reply_message()
        user = (
            await event.client.get_entity(reply.forward.sender)
            if reply.fwd_from
            else reply.sender
        )
        res, canvas = await process(msg, user, event.client, reply, repliedreply)
        if not res:
            return
        canvas.save("sticker.webp")
        await event.client.send_file(
            event.chat_id, "sticker.webp", reply_to=event.reply_to_msg_id
        )
        os.remove("sticker.webp")
    except Exception:
        terr = await event.reply(traceback.format_exc())
        await asyncio.sleep(10)
        await terr.delete()
    finally:
        await asyncio.sleep(1)
        await event.delete()


# old
'''
def random_gradient(width, height):
    """Generate a random gradient as the background."""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    # Generate two random colors for the gradient
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    for y in range(height):
        for x in range(width):
            r = int(color1[0] + (color2[0] - color1[0]) * y / height)
            g = int(color1[1] + (color2[1] - color1[1]) * y / height)
            b = int(color1[2] + (color2[2] - color1[2]) * y / height)
            draw.point((x, y), (r, g, b))
    
    return img

def draw_window_with_dots_and_wrapped_text(width, height, font_path, text):
    """Draw a window with rounded corners, three dots, and wrapped text below the dots."""
    margin = 20

    # Add wrapped mono-font text inside the window, below the dots
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)

    # Wrap text to fit the window width
    text_margin = margin + 45  # Adjust margin to position below dots
    max_text_width = width + 210  #* (font_size // 2) #* margin - 15  # Subtract margins
    current_height = text_margin

    # Dynamically adjust height by output text
    for i in text.split("\n"):
        wrapped_t = textwrap.fill(i, width=(max_text_width // font_size))

        # Start drawing wrapped text
        for line in wrapped_t.split("\n"):
            height += font_size + 5

    # Create the gradient background
    background = random_gradient(width, height)
    draw = ImageDraw.Draw(background)

    # Define the rounded black window area
    border_radius = 25
    window_rect = [
        (margin, margin),
        (width - margin, height - margin)
    ]
    draw.rounded_rectangle(window_rect, fill=(0, 0, 0), radius=border_radius)

    # Add the three dots in the top-left corner
    dot_radius = 7
    dot_spacing = 23
    dot_positions = [
        (margin + 24, margin + 21),
        (margin + 24 + dot_spacing, margin + 21),
        (margin + 24 + 2 * dot_spacing, margin + 21)
    ]
    dot_colors = [(255, 59, 48), (255, 204, 0), (76, 217, 100)]  # Red, yellow, green (Mac OS-style)

    for pos, color in zip(dot_positions, dot_colors):
        draw.ellipse([
            (pos[0] - dot_radius, pos[1] - dot_radius),
            (pos[0] + dot_radius, pos[1] + dot_radius)
        ], fill=color)
            
            
    for j in text.split("\n"):
        wrapped_text = textwrap.fill(j, width=(max_text_width // font_size))

        # Start drawing wrapped text
        for line in wrapped_text.split("\n"):
            draw.text((margin + 20, current_height), line, font=font, fill=(255, 255, 255))
            current_height += font_size + 5  # Move to the next line with spacing

    return background
'''

#g_image_path = "/storage/emulated/0/Download/aiiiii/1/IMG_20250831_123647_Cute Wallpaper 1.png"
def g_image_path():
    if os.path.exists("./tgbot/img/background"):
        files = os.listdir("./tgbot/img/background")
        if files == []: return None
        return f"./tgbot/img/background/{random.choice(files)}"
    return None
    """
    if os.path.exists("./tgbot/img/background.jpg"):
        return "./tgbot/img/background.jpg"
    elif os.path.exists("./tgbot/img/background.png"):
        return "./tgbot/img/background.png"
    elif os.path.exists("./tgbot/img/background.jpeg"):
        return "./tgbot/img/background.jpeg"
    else:
        return None 
    """

def random_gradient(width, height):
    """Generate a random gradient as the background."""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for y in range(height):
        for x in range(width):
            r = int(color1[0] + (color2[0] - color1[0]) * y / height)
            g = int(color1[1] + (color2[1] - color1[1]) * y / height)
            b = int(color1[2] + (color2[2] - color1[2]) * y / height)
            draw.point((x, y), (r, g, b))
    return img


def get_img(width, height, image):
    """Resize and crop a image for the background."""
    with Image.open(image) as im:
        im_w, im_h = im.size
        scale = max(width / im_w, height / im_h)
        s_x, s_y = int(im_w * scale), int(im_h * scale)
        if im_w != width and im_h != height:
            im = im.resize((s_x, s_y), Image.LANCZOS)
        if s_x != width or s_y != height:
            left   = (s_x - width) / 2
            top    = (s_y - height) / 2
            right  = left + width
            bottom = top + height
            im = im.crop((left, top, right, bottom))
    return im


'''
def draw_window(width, font_path, text, image_path=None):
    """Draw a window with rounded corners, three dots, and wrapped text below the dots."""
    print(image_path)
    margin = 20
    height = 120
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)
    current_height = margin + 45
    if width == 0:
        text_col = 0
        for i in text.split("\n"):
            height += font_size + 5
            if len(i) > text_col:
                text_col = len(i)
        width = text_col * 12 + 20 * 4 + 10 if text_col * 12 + 20 * 4 + 10 >= 154 else 154
    else:
        if width < 154:
            width = 154
        for i in text.split("\n"):
            wrapped_t = textwrap.fill(i, width=(width - 40*2)//12)
            for line in wrapped_t.split("\n"):
                height += font_size + 5
    height -= 25
    if image_path:
        background = get_img(width, height, image_path)
    else:
        background = random_gradient(width, height)
    blurred_bg = ImageEnhance.Brightness(background.filter(ImageFilter.GaussianBlur(radius=20))).enhance(0.75)
    border_radius = 25
    window_rect = [
        (margin, margin),
        (width - margin, height - margin)
    ]
    mask = Image.new('L', background.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle(window_rect, fill=255, radius=border_radius)
    background = Image.composite(blurred_bg, background, mask)
    draw = ImageDraw.Draw(background)
    dot_radius = 7
    dot_spacing = 23
    dot_positions = [
        (margin + 24, margin + 21),
        (margin + 24 + dot_spacing, margin + 21),
        (margin + 24 + 2 * dot_spacing, margin + 21)
    ]
    dot_colors = [(255, 59, 48), (255, 204, 0), (76, 217, 100)]  # Red, yellow, green (Mac OS-style)
    for pos, color in zip(dot_positions, dot_colors):
        draw.ellipse([
            (pos[0] - dot_radius, pos[1] - dot_radius),
            (pos[0] + dot_radius, pos[1] + dot_radius)
        ], fill=color)
    if width == 0:
        for i in text.split("\n"):
            draw.text((margin + 20, current_height), i, font=font, fill=(255, 255, 255))
            current_height += font_size + 5
    else:
        for j in text.split("\n"):
            wrapped_text = textwrap.fill(j, width=(width - 40*2)//12)

            # Start drawing wrapped text
            for line in wrapped_text.split("\n"):
                draw.text((margin + 20, current_height), line, font=font, fill=(255, 255, 255))
                current_height += font_size + 5  # Move to the next line with spacing

    return background
#'''


def draw_window(font_path, text, image_path=None):
    """Draw a window with rounded corners, three dots, and wrapped text below the dots."""
    margin = 36
    patting = 28
    border_radius = 30
    dot_size = 32/2
    group_spacing = 16/2
    blur = 32
    newline_spacing = 8

    # Add wrapped mono-font text inside the window, below the dots
    font_size = 32
    font = ImageFont.truetype(font_path, font_size)

    # Wrap text to fit the window width
    current_height = margin + patting + group_spacing + dot_size  # Adjust margin to position below dots

    height = margin*2 + patting*3 + dot_size
    width = 0
    for i in text.split("\n"):
        height += font_size + newline_spacing
        i = font.getbbox(i)[2]
        if i > width:
            width = i
    width = width + (margin + patting)*2 if width + (margin + patting)*2 >= 128 else 128
    height = height - newline_spacing*2 - font_size if text.endswith("\n") else height - newline_spacing

    # Create the gradient background
    if image_path:
        background = get_img(width, height, image_path)
    else:
        background = random_gradient(width, height)
    
    draw = background# ImageDraw.Draw(background)
    
    blurred_bg = ImageEnhance.Brightness(background.filter(ImageFilter.GaussianBlur(radius=blur))).enhance(0.75)

    # Define the rounded black window area
    window_rect = [
        (margin, margin),
        (width - margin, height - margin)
    ]
    # Create a mask for rounded rectangle
    mask = Image.new('L', background.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle(window_rect, fill=255, radius=border_radius)

    # Composite the blurred region onto the original background
    background = Image.composite(blurred_bg, background, mask)
    draw = ImageDraw.Draw(background)

    # Add the three dots in the top-left corner
    dot_positions = [
        (margin + patting, margin + patting),
        (margin + patting + dot_size + group_spacing, margin + patting),
        (margin + patting + 2 * (group_spacing + dot_size), margin + patting)
    ]
    dot_colors = [(255, 59, 48), (255, 204, 0), (76, 217, 100)]  # Red, yellow, green (Mac OS-style)

    for pos, color in zip(dot_positions, dot_colors):
        draw.ellipse([
            (pos[0], pos[1]),
            (pos[0] + dot_size, pos[1] + dot_size)
        ], fill=color)

    # Add the text
    for i in text.split("\n"):
        draw.text((margin + patting, current_height), i, font=font, fill=(255, 255, 255))
        current_height += font_size + newline_spacing

    return background




@SPY(pattern="(?s)^!!sh (.*)")
async def winsh(E):
    id = str(ID(E))
    if id in GS(): await E.reply("This feature doesn't work at the moment."); return
    elif id not in GIS() and id != str(MY_USER_ID): return
    C = E.pattern_match.group(1)
    if id == str(MY_USER_ID): await E.edit(f"{Q(M(f'!!sh {FIX(C)}'))}", parse_mode="HTML")
    try: o = SSU(C).stdout.read()
    except Exception as e: o = f"{e}"
    if len(o)+len(C) >= 4000: o = f"{o[:4000-len(C)]}\n\n{'[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'}"
    finaltext = '$ '+C+'\n'+o if o else f'$ {C}'
    try:
        window_image = draw_window("./tgbot/sticker/font/mono.ttf", finaltext, g_image_path())
        window_image.save("wrapped_text_window_with_gradient.png")
        if E.is_reply: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.reply_to_msg_id)
        else: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.id)
        if id==str(MY_USER_ID): await E.delete()
    except Exception:
        if id==str(MY_USER_ID): await E.edit(traceback.format_exc())
        else: await E.reply(traceback.format_exc())
    try: os.remove("wrapped_text_window_with_gradient.png")
    except: pass


def spoiler(l, t):
    ree = ""
    k = 0
    j = 2

    for i in t:
        if j > l:
            ree += "||" + i + "||"
            j = 2
        else:
            ree += i
            k += 2
            j += 1
        #ree += " "
    return ree


@SPY(outgoing=True,pattern=r"(?s)^!!sp (\d+) (.+)")
async def spoil(E):
    if E.is_reply:
        R = await E.get_reply_message()
        await R.reply(spoiler(int(E.pattern_match.group(1)),E.pattern_match.group(2)))
    else:
        await E.reply(spoiler(int(E.pattern_match.group(1)),E.pattern_match.group(2)))
    await E.delete()



@SPY(pattern=r"(?s)^!!icowsay (.+)")
async def imgcow(E):
    id = str(ID(E))
    if id not in GIS() and id != str(MY_USER_ID): return
    C = "cowsay "+E.pattern_match.group(1)
    try: o = SSU(C).stdout.read()
    except Exception as e: o = f"{e}"
    if len(o)+len(C) >= 4000: o = f"{o[:4000-len(C)]}\n\n{'[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'}"
    try:
        window_image = draw_window("./tgbot/sticker/font/mono.ttf", o, g_image_path())
        window_image.save("wrapped_text_window_with_gradient.png")
        if E.is_reply: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.reply_to_msg_id)
        else: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.id)
        if id==str(MY_USER_ID): await E.delete()
    except Exception:
        if id==str(MY_USER_ID): await E.edit(traceback.format_exc())
        else: await E.reply(traceback.format_exc())
    try: os.remove("wrapped_text_window_with_gradient.png")
    except: pass
    """
    if id == str(MY_USER_ID): await E.edit(Q(M('&#x00AD')+M(o)),parse_mode="HTML")
    else: await E.reply(Q(M("&#x00AD")+M(o)),parse_mode="HTML")
    """


@SPY(pattern=r"(?s)^!!iflet (.+)")
async def imgfiglet(E):
    id = str(ID(E))
    if id not in GIS() and id != str(MY_USER_ID): return
    C = "figlet "+E.pattern_match.group(1)
    try: o = SSU(C).stdout.read()
    except Exception as e: o = f"{e}"
    if len(o)+len(C) >= 4000: o = f"{o[:4000-len(C)]}\n\n{'[CUT OUTPUT TO '+str(4000 - len(C))+'/'+str(len(o)+len(C))+' CHARS; NO MORE SPACE]'}"
    try:
        window_image = draw_window("./tgbot/sticker/font/mono.ttf", o, g_image_path())
        window_image.save("wrapped_text_window_with_gradient.png")
        if E.is_reply: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.reply_to_msg_id)
        else: await E.client.send_file(E.chat_id, "wrapped_text_window_with_gradient.png", reply_to=E.id)
        if id==str(MY_USER_ID): await E.delete()
    except Exception:
        if id==str(MY_USER_ID): await E.edit(traceback.format_exc())
        else: await E.reply(traceback.format_exc())
    try: os.remove("wrapped_text_window_with_gradient.png")
    except: pass


@SPY(outgoing=True, pattern="!!gamebot")
async def gamebot(E):
    try:
        entity = entity = await bot.get_entity("https://t.me/galaxyA54developer")
        #entity = 2418746716
        await bot.send_message(entity, "/grow@DickGrowerBot", reply_to=180297)
        await E.edit("✅️")
        await asyncio.sleep(5)
        await E.edit("✅️ Successful!")
    except Exception:
        e = traceback.format_exc()
        print(e)
        await E.edit(e)


@SPY(outgoing=True, pattern="!!rand (\\d+) (.+)")
async def random_q(E):
    count = int(E.pattern_match.group(1))
    query = E.pattern_match.group(2)
    text = ""
    for i in range(count if count != 0 else len(query)):
        text += random.choice(query)
    await E.edit(text)


LANGUAGES = {
    "python": ("Python", "py"), "py": ("Python", "py"),
    "java": ("Java", "java"),
    "c++": ("C++", "cpp"), "cpp": ("C++", "cpp"),
    "javascript": ("JavaScript", "js"), "js": ("JavaScript", "js"),
    "c#": ("C#", "cs"), "cs": ("C#", "cs"),
    "html": ("HTML", "html"),
    "kotlin": ("Kotlin", "kt"), "kt": ("Kotlin", "kt"),
    "assembly": ("Assembly", "asm"), "asm": ("Assembly", "asm"),
    "go": ("Go", "go"), "golang": ("Go", "go"),
    "rust": ("Rust", "rs"), "rs": ("Rust", "rs"),
    "swift": ("Swift", "swift"),
    "ruby": ("Ruby", "rb"), "rb": ("Ruby", "rb"),
    "php": ("PHP", "php"),
    "c": ("C", "c"),
    "brainfuck": ("Brainfuck", "bf"), "bf": ("Brainfuck", "bf"),
    "lolcode": ("LOLCODE", "lol"), "lol": ("LOLCODE", "lol"),
    "shell": ("Shell", "sh"), "sh": ("Shell", "sh"),
    "bash": ("Bash", "sh"), "zsh": ("Zsh", "sh"), "fish": ("Fish", "sh"),
    "zig": ("Zig", "zig"),
    "gleam": ("Gleam", "gleam"),
    "lua": ("Lua", "lua"),
}


def mulcode(s,cs,t,ce,e,br):
    st = False
    tcode = f"{s}"
    for j in t.split("\n"):
        if st:
            tcode += "\n"
        else:
            st = True
        for i in j:
            tcode += f"{cs}{i}{ce}\n"
        tcode += f"{br}"
    return tcode


def text_to_brainfuck(text):
    brainfuck_code = []
    memory = [0]
    pointer = 0
    
    for char in text:
        target_value = ord(char)
        current_value = memory[pointer]
        diff = target_value - current_value
        simple_way = ('+' * diff if diff > 0 else '-' * abs(diff))
        loop_way = ""

        if abs(diff) > 10:
            factor = int(target_value**0.5)
            if factor > 1:
                remaining = target_value - (factor * factor)
                loop_code = f">{'+'*factor}[<{''.join(['+']*factor)}>-]<"
                if remaining > 0:
                    loop_code += '+' * remaining
                else:
                    loop_code += '-' * abs(remaining)
                if len(loop_code) < len(simple_way):
                    loop_way = loop_code

        if loop_way and not current_value:
             brainfuck_code.append(loop_way)
        else:
            brainfuck_code.append(simple_way)

        brainfuck_code.append('.')
        memory[pointer] = target_value
    brainfuck_code.append('[-]')
    return "".join(brainfuck_code)


def generate_code(language, text, file):
    """Generates a 'Hello, World!'-style program for the given language and text."""

    if language == "Brainfuck":
        return text_to_brainfuck(text+"\n")
    if language in ["Shell", "Fish", "Bash", "Zsh"]:
        escaped_text = text.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'").replace("`", "\\`").replace("$", "\\$").replace("&", "\\&").replace("|", "\\|").replace("~","\\~").replace("#", "\\#").replace("<", "\\<").replace(">", "\\>").replace("(","\\(").replace(")", "\\)").replace("\n","\\n")
        return f"#!/bin/{'sh' if language == 'Shell' else language.lower()}\necho {escaped_text}"

    escaped_text = text.replace('\\', '\\\\').replace('"', '\\"').replace("\n","\\n")
    code_templates = {
        "Python": f'print("{escaped_text}")',
        "Java": f'public class {file} {{\n    public static void main(String[] args) {{\n        System.out.println("{escaped_text}");\n    }}\n}}',
        "C++": f'#include <iostream>\n\nint main() {{\n    std::cout << "{escaped_text}" << std::endl;\n    return 0;\n}}',
        "JavaScript": f'console.log("{escaped_text}");',
        "C#": f'using System;\n\nclass Program {{\n    static void Main(string[] args) {{\n        Console.WriteLine("{escaped_text}");\n    }}\n}}',
        "HTML": f'<!DOCTYPE html>\n<html>\n<head><title>{file}</title></head>\n<body>\n    <p>{FIX(text)}</p>\n</body>\n</html>',
        "Kotlin": f'fun main() {{\n    println("{escaped_text}")\n}}',
        "Assembly": (
            'section .data\n'
            f'    msg db "{escaped_text}", 0\n\n'
            'section .text\n'
            '    global _start\n\n'
            '_start:\n'
            '    mov rax, 1\n'
            '    mov rdi, 1\n'
            '    mov rsi, msg\n'
            '    mov rdx, 14\n'
            '    syscall\n\n'
            '    mov rax, 60\n'
            '    xor rdi, rdi\n'
            '    syscall'
        ),
        "Go": f'package main\n\nimport "fmt"\n\nfunc main() {{\n    fmt.Println("{escaped_text}")\n}}',
        "Rust": f'fn main() {{\n    println!("{escaped_text}");\n}}',
        "Swift": f'print("{escaped_text}")',
        "Ruby": f'puts "{escaped_text}"',
        "PHP": f'<?php\n\necho "{escaped_text}";\n?>',
        "C": f'#include <stdio.h>\n\nint main() {{\n    printf("{escaped_text}\\n");\n    return 0;\n}}',
        "LOLCODE": (
            'HAI 1.2\n'
            f'VISIBLE "{text}"\n'
            'KTHXBYE'
        ),
        "Zig": f'const std = @import("std");\n\npub fn main() !void {{\n    std.debug.print("{escaped_text}\n", .{{}});\n}}',
        "Gleam": f'import gleam/io\n\npub fn main() {{\n  io.println("{escaped_text}")\n}}',
    }
    return code_templates.get(language, f"// Language '{language}' not supported.")


@SPY(outgoing=True,pattern="(?s)^!!codeit (\\S+) (\\S+) ?(\\S+)? ?(.+)?")
async def codeit(E):
    """
        !!codeit <mode> <lang> <name file or text> <text>
        
        t: text message quote
        f: file
        n: name file
        c: text as code
        
    """
    #await E.edit("running...")
    mode = E.pattern_match.group(1).lower().strip()
    lang = E.pattern_match.group(2).lower().strip()
    code_name = E.pattern_match.group(3)
    coden = E.pattern_match.group(4)
    try:
        if code_name:
            if "n" in mode:
                code = coden
            else:
                code = f"{code_name}{f' {coden}' if coden else ''}"
        if (not code_name or ("n" in mode and not coden)) and E.is_reply and E.reply_to_msg_id:
            reply = await E.get_reply_message()
            code = reply.text
        elif not code_name and not E.is_reply: return
        if "b" in mode:
            if lang in ["py", "python"]:
                code = mulcode("","print(\"",code.replace("\\", "\\\\").replace("\"","\\\""),"\",end=\"\")","","print()")
            elif lang in ["js", "javascript"]:
                code = mulcode("","process.stdout.write(\"",code.replace("\\", "\\\\").replace("\"","\\\""),"\")","","console.log()")
            else:
                await E.edit("This language doesn't support yet.")
                await asyncio.sleep(4)
                await E.delete()
                return
            await E.edit(f"<blockquote><code>{code}</code></blockquote>",parse_mode="HTML")
            return
        if lang not in LANGUAGES:
            await E.edit(f"Unsupported language: <code>{lang}</code>.",parse_mode="HTML")
            await asyncio.sleep(4)
            await E.delete()
            return
        lang_name, file_ext = LANGUAGES[lang]
        if "n" in mode:
            file_name = code_name
        else:
            file_name = lang_name
        output_path = f"tgbot/sticker/proc/{file_name}.{file_ext}"
        code_output = generate_code(lang_name, code, file_name)
        cuted = ""
        if "t" in mode and "f" in mode:
            fix_code_text = f"<blockquote><code>{FIX(code_output)}"
            if len(fix_code_text + "</code></blockquote>") > 1024:
                cuted = f"<blockquote><code>CUT OUTPUT TO {1024 - len(code_output)}/{len(code_output)} CHARS</code></blockquote>"
                fix_code_text = fix_code_text[:1024 - len(cuted) - "</code></blockquote>"]
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(code_output)
            if E.reply_to_msg_id:
                await bot.send_file(E.chat_id, output_path, caption=f"{fix_code_text}</code></blockquote>{cuted}", parse_mode="HTML", reply_to=E.reply_to_msg_id)
            else:
                await bot.send_file(E.chat_id, output_path, caption=f"{fix_code_text}</code></blockquote>{cuted}", parse_mode="HTML", reply_to=E.id)
            await asyncio.sleep(3)
            await E.delete()
        elif "t" in mode:
            fix_code_text = f"<blockquote><code>{FIX(code_output)}"
            if len(fix_code_text + "</code></blockquote>") > 4096:
                cuted = f"<blockquote><code>CUT OUTPUT TO {4096 - len(code_output)}/{len(code_output)} CHARS</code></blockquote>"
                fix_code_text = fix_code_text[:4096 - len(cuted) - "</code></blockquote>"]
            await E.edit(f"{fix_code_text}</code></blockquote>{cuted}",parse_mode="HTML")
        elif "c" in mode:
            fix_code_text = f"```\n{code_output}"
            if len(fix_code_text + "\n```") > 4096:
                cuted = f"<blockquote><code>CUT OUTPUT TO {4096 - len(code_output)}/{len(code_output)} CHARS</code></blockquote>"
                fix_code_text = fix_code_text[:4096 - len(cuted) - "\n```"]
            await E.edit(f"{fix_code_text}\n```{cuted}")
        elif "f" in mode:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(code_output)
            if E.reply_to_msg_id:
                await bot.send_file(E.chat_id, output_path, reply_to=E.reply_to_msg_id)
            else:
                await bot.send_file(E.chat_id, output_path, reply_to=E.id)
            await asyncio.sleep(3)
            await E.delete()
        else:
            await E.edit("Mode doesn't support")
            await asyncio.sleep(3)
            await E.delete()
    except Exception:
        await E.edit(f"{traceback.format_exc()}")
    finally:
        if os.path.exists(output_path):
            os.remove(output_path)


#			#


async def runcodelang(lang, ext, code, media):
    #if not os.path.exists("runthefile"):
        #os.mkdir("runthefile")
    fname = f"main.{ext}"
    if not (media and lang != "Java"):
        with open(f"runthefile/{fname}", "w") as f:
            f.write(f"{code}")
    if lang in ["Shell", "Fish", "Bash", "Zsh"]:
        c = f'chmod +x {fname} && ./{fname}'
    else:
        code_templates = {
            "Python": f'python3 {fname}',
            "Java": 'cp -f main.java /sdcard/Download/ && javac main.java && java main',
            "C++": f'g++ {fname} -o main && ./main',
            "JavaScript": f'node {fname}',
            "C#": f'dotnet run {fname}',
            "Go": f'go run {fname}',
            "Rust": f'rustc {fname} && ./main',
            "Swift": f'swiftc {fname} && ./main',
            "Ruby": f'ruby {fname}',
            "PHP": f'php {fname}',
            "C": f'gcc {fname} -o main && ./main',
            "Zig": f'zig build-exe {fname} && ./main',
            "Brainfuck": f'brainfuck {fname}',
            "Lua": f'lua {fname}',
        }
        c = code_templates.get(lang, f"{lang}")
    o = SSU(f'cd runthefile && {c} ; cd && rm -rf runthefile').stdout.read()
    #await asyncio.sleep(1)
    #SSU("rm -rf runthefile")
    return o



def checkcode(c, lang):
    code = ""
    def addcode(co, sip, f, l):
        nonlocal code
        code += f"{f}"
        for i in co.split("\n"):
            code += f"{sip}{i}\n"
        code += f'{l}'
    if lang == "C":
        if "#include" not in c:
            addcode(c, "    ", "#include <stdio.h>\n\nint main() {\n", "     return 0;\n}")
    elif lang == "C++":
        if '#inclode' not in c:
            addcode(c, "    ", "#include <iostream>\n\nint main() {\n", "    return 0;\n}")
    elif lang == "Java":
        if "public class main" not in c:
            addcode(c, "        ", "public class main {\n    public static void main(String[] args) {\n", "    }\n}")
    elif lang == "Rust":
        if "fn main" not in c:
            addcode(c, "    ", "fn main() {\n", "}")
    elif lang == "PHP":
        if "?php" not in c:
            addcode(c, "", "<?php\n\n", "?>")
    elif lang == "Go":
        if "package main" not in c:
            addcode(c, "    ", 'package main\n\nimport "fmt"\n\nfunc main() {\n', "}")
    if code == "":
        return c
    return code


def checkjava(c):
    code = ""
    done = False
    for j in c.split("\n"):
        if j.startswith("public class ") and not done:
            code += "public class main {\n"
            done = True
            #print("yay")
        else:
            code += f"{j}\n"
            #print(f"{j}")
    return code


@SPY(outgoing=True, pattern="(?s)^!!run (\\S+) ?(.+)?")
async def runcode(E):
    try:
        lang = E.pattern_match.group(1)
        code = E.pattern_match.group(2)
        reply_msg = await E.get_reply_message()
        try: await E.edit(f"{Q(M(f'!!run {lang} {FIX(code)}'))}\nRunning...", parse_mode="HTML")
        except: pass
        is_media = False
        if not code:
            if reply_msg:
                if reply_msg.media:
                    is_media = True
                    code = " "
                elif E.message.reply_to.quote_text:
                    code = E.message.reply_to.quote_text
                elif reply_msg.text:
                    code = reply_msg.text
        if not code:
            await E.edit("Where is the code?")
            await asyncio.sleep(4)
            await E.delete()
            return
        if lang not in LANGUAGES:
            await E.edit(f"Unsupported language: <code>{lang}</code>.",parse_mode="HTML")
            await asyncio.sleep(4)
            await E.delete()
            return
        lang_name, file_ext = LANGUAGES[lang]
        if lang_name in ["Java", "C", "C++", "Rust", "Go", "PHP"]:
            code = checkcode(code, lang_name)
        if not os.path.exists("runthefile"):
            os.mkdir("runthefile")
        if is_media:
            file_path = await bot.download_media(reply_msg.media, f'runthefile/main.{file_ext}')
            print(file_path)
        if lang_name == "Java":
            if is_media:
                with open (file_path, "r") as f:
                    code = f.read()
            code = checkjava(code)
        output = await runcodelang(lang_name, file_ext, code, is_media)
        await E.edit(f"{Q(M(FIX(output)))}", parse_mode="HTML")
    except Exception:
        e = traceback.format_exc()
        print(e)
        await E.edit(e)
        await asyncio.sleep(2)
        await E.delete()


#from pprint import pprint


"""
@SPY(outgoing=True, pattern="^!!test")
async def testt(E):
    #ev = pprint(E.__dict__)
    #ev = dir(E)
    #replyheader = getattr(E.message, "replyto", None)

    ""if replyheader and getattr(replyheader, "quote_text", None):
        quote = replyheader.quotetext
        await E.reply(f"Quote detected:\n> {quote}")""
    await E.reply(f"{E.message.reply_to.quote_text}")
"""


@SPY(pattern=f"^/start{MY_USER_NAME}$")
async def start(E):
    #if lE.text[7:].lower() == f"/start@{MY_USER_NAME[1:].lower()}": await E.reply("Bomb! I'm already here")
    await E.reply("Bomb! I'm already here")


"""
@SPY(outgoing=True, pattern="!!image ?(.*)?")
async def f2i(e):
    txt = e.pattern_match.group(1).strip()
    html = None
    if txt:
        html = e.text.split(maxsplit=1)[1]
    elif e.reply_to:
        r = await e.get_reply_message()
        if r.media:
            html = await bot.download_media(r.media)
        elif r.text:
            html = r.text
    if not html:
        return await e.edit("`Either reply to any file or give any text`")
    html = html.replace("\n", "<br>")
    shot = WebShot(quality=85)
    css = "body {background: white;} p {color: red;}"
    pic = await shot.create_pic_async(html=html, css=css)
    await e.reply(file=pic, force_document=True)
    os.remove(pic)
    await e.delete()
    if os.path.exists(html):
        os.remove(html)
"""


try:
    with open('./tgbot/saved/last_response_date', 'r') as file:
        last_response_date = file.read().strip()
        #print(last_response_date)
except:
    with open('./tgbot/saved/last_response_date', 'w') as file:
        file.write(str(datetime.datetime.now(datetime.timezone.utc).date()))
        last_response_date = None

last_sp_time = 10
"""Event Listener"""
@bot.on(events.NewMessage)
async def ear(E):
    global afk_msg_now, last_response_date, last_sp_time
    #last_response_date_temp = last_response_date

    if last_sp_time < 2:
        current_date = datetime.datetime.now(datetime.timezone.utc).date()
        try:
            if last_response_date != str(current_date):
                last_response_date = str(current_date)
                # Respond and update the last response date
                entityy = await bot.get_entity("https://t.me/+JMnt71kRXcU3ODQ1")
                entity = await bot.get_entity("https://t.me/galaxyA54developer")
                #entity = 2418746716
                await bot.send_message(entity, "/grow@DickGrowerBot", reply_to=180297)
                #last_response_date = str(current_date)
                await asyncio.sleep(5)
                entity_aha = await bot.get_entity("https://t.me/+6TjrFR0rMno1Njg0")
                await bot.send_message(entity_aha, "/shipping@SHIPPERINGbot")
                await bot.send_message(entity_aha, "/grow@DickGrowerBot")
                print(f"{current_date}")
        except FloodWaitError as e: pass
        except Exception:
            #last_response_date = last_response_date_temp
            errr = traceback.format_exc()
            print(errr)
            #entityy = await bot.get_entity("https://t.me/+JMnt71kRXcU3ODQ1")
            await bot.send_message(entityy, f"Failed to grow, use !!gamebot to retry\nError: {errr}", reply_to=180297)
        finally:
            with open('./tgbot/saved/last_response_date', 'w') as file:
                file.write(str(current_date))
        last_sp_time = 500
    else:
        last_sp_time -= 1


    """Dmute"""
    if str(ID(E)) in GDM():
        try: await E.delete()
        except: pass
        """other"""
    elif delete_my_msg and E.sender_id == MY_USER_ID:
        if E.text.startswith("!!tdd "):
            await E.edit(E.text[len("!!tdd "):])
        else:
            await asyncio.sleep(delete_my_msg_delay)
            try:
                await E.delete()
            except: pass
    
    elif afk_msg_now != None:
        if E.sender_id == MY_USER_ID:
            afk_msg_now = None
        elif E.is_group and E.message.mentioned:
            await E.reply(afk_msg_now)
        elif E.is_private:
            await E.reply(afk_msg_now)
    elif afk_me_now and E.sender_id != MY_USER_ID:
        if afk_mode == "auto" or afk_mode == "on":
            if E.is_private:
                await E.reply(afk_msg)
            elif E.is_group and E.message.mentioned:
                await E.reply(afk_msg)
        elif afk_mode == "ai":
            if E.is_group and E.message.mentioned:
                try:
                    import ollama
                    text = ollama.generate(model='smollm2:135m', prompt=E.text)
                    text2 = text.response
                    await E.reply(text2)
                    """
                    resp: ollama.ChatResponse = ollama.chat(model='smollm2:135m', messages=[
                        {
                            'role': 'user',
                            'content': E.text,
                        },
                    ])
                    response = resp['message']['content']
                    await E.reply(response)
                    """
                except Exception as e:
                    await E.reply(f"Error: {e}")

"""Keep Bot Alive"""
print ("BOT ON!")
bot.run_until_disconnected()
print ("BOT OFF!")
