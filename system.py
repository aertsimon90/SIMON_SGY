import socket, threading, webbrowser, time, random, os, getpass, sys
if os.name == "nt":
	user = getpass.getuser()
	if os.getcwd() != f"C:\\Users\\{user}\\Desktop\\SIMON_SGY":
		try:
			os.chdir(f"C:\\Users\\{user}\\Desktop\\SIMON_SGY")
		except:
			print(f"\033[91m\033[1mHATA: Gereken dosya yolu C:\\Users\\{user}\\Desktop\\SIMON_SGY olmak zorundadır aksi takdirde müzikler çalışmaz. Bu repoyu indirdikten sonra SIMON_SGY ismiyle masaüstünde klasör olarak tutmanız önemlidir 5 saniye sonra devam edilecektir.\033[0m")
			time.sleep(5)
print("\033[92mMODULLER KURULUYOR...\033[0m")
time.sleep(3)
os.system("py -m pip install requests")
os.system("pip install requests")
import requests
class Finder:
	def __init__(self, n, botn):
		self.list = []
		self.lock = threading.Lock()
		ts = []
		for _ in range(n):
			t = threading.Thread(target=self.bot, args=(botn,))
			t.start()
			ts.append(t)
			time.sleep(0)
		for t in ts:
			t.join()
	def test(self, ip, port):
		s = socket.socket()
		s.settimeout(0.4)
		try:
			s.connect((ip, port))
			with self.lock:
				self.list.append([ip, port])
		except Exception as e:
			print(str(e), ip, port)
		s.close()
	def test_random(self):
		ip = str(random.randint(1, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
		port = random.choice([80, 443, random.randint(1, 65535)])
		print(f"Testing: {ip}:{port}")
		self.test(ip, port)
	def bot(self, botn):
		ts = []
		for _ in range(botn):
			t = threading.Thread(target=self.test_random, args=())
			t.start()
			ts.append(t)
			time.sleep(0)
		for t in ts:
			a = ((ts.index(t)+1)/len(ts))*100
			print(f"Test Joining... {a}%")
			t.join()
			time.sleep(0)
		print("Bot Finished.")
	def start(self, perwait, page, termux):
		for ip, port in self.list:
			if port == 80:
				url = "http://"+ip
			elif port == 443:
				url = "https://"+ip
			else:
				url = "http://"+ip+":"+str(port)
			if termux:
				os.system("termux-open-url "+url)
			else:
				webbrowser.open(url, new=page)
			time.sleep(perwait)
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
if os.name != "nt":
	termux = input("\033[92mBekle! Termux mu kullanıyorsun? ona göre konfigürasyon gerek. (E/h/Y/n): \033[0m").lower()
	if "e" in termux:
		termux = True
	elif "y" in termux:
		termux = True
	else:
		termux = False
else:
	termux = False
if termux:
	print("\033[92mTERMUX IÇIN MUSIC API KURULUYOR...\033[0m")
	os.system("pkg install termux-api")
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
print("\033[90mSimonun Yalnızlık Gezintisine hoş geldiniz!...")
print("""  ██████▓██   ██▓  ▄████                
▒██    ▒ ▒██  ██▒ ██▒ ▀█▒               
░ ▓██▄    ▒██ ██░▒██░▄▄▄░               
  ▒   ██▒ ░ ▐██▓░░▓█  ██▓               
▒██████▒▒ ░ ██▒▓░░▒▓███▀▒ ██▓  ██▓  ██▓ 
▒ ▒▓▒ ▒ ░  ██▒▒▒  ░▒   ▒  ▒▓▒  ▒▓▒  ▒▓▒ 
░ ░▒  ░ ░▓██ ░▒░   ░   ░  ░▒   ░▒   ░▒  
░  ░  ░  ▒ ▒ ░░  ░ ░   ░  ░    ░    ░   
      ░  ░ ░           ░   ░    ░    ░  
         ░ ░               ░    ░    ░  """)
print("by aertsimon90...")
print()
print("Bu gezintide rasgele sunucularda gezeceksiniz...")
print()
muzik = input("Gezinti yapılırken şarkı açalımmı? (E/h/Y/n): ").lower()
if "e" in muzik:
	muzik = True
elif "y" in muzik:
	muzik = True
else:
	muzik = False
bot = int(input("Bot sayısı girin (örnek 5): "))
tekrar = int(input("Her bot için deneme tekrarı sayısını girin (örnek 30): "))
bekleme = float(input("Her sunucu için bekleme süresi saniye cinsinden (örnek 5): "))
sayfa = int(input("Açılacak sayfa numarası (örnek 0): "))
input("[ ENTER TUŞUNA BASIN VE BAŞLASIN ]")
if muzik:
	print("Müzik yükleniyor...")
	music = random.choice(["music1.mp3", "music2.mp3"])
	if termux:
		threading.Thread(target=os.system, args=("termux-media-player play "+music, )).start()
	else:
		threading.Thread(target=os.system, args=("start "+music, )).start()
	print("Müzik bekletiliyor...")
	time.sleep(5)
while True:
	Finder(bot, tekrar).start(bekleme, page=sayfa, termux=termux)
