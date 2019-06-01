import requests
import json

token = 'YOUR TOKEN HERE'

def change_status(token):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36', 'Authorization': token}

    requests.patch('https://discordapp.com/api/v6/users/@me/settings', json=json.loads(json.dumps({'status': 'online'})), headers=headers)
    requests.patch('https://discordapp.com/api/v6/users/@me/settings', json=json.loads(json.dumps({'status': 'idle'})), headers=headers)
    requests.patch('https://discordapp.com/api/v6/users/@me/settings', json=json.loads(json.dumps({'status': 'dnd'})), headers=headers)
    requests.patch('https://discordapp.com/api/v6/users/@me/settings', json=json.loads(json.dumps({'status': 'invisible'})), headers=headers)

def main():
    while True:
        change_status(token)

if __name__ == "__main__":
    main()