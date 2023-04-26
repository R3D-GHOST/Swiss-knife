#librerias
import os , time
import subprocess
#
#
#banner
banner = """
(By R3D-GH0ST)
  ________  __   __  ___   __      ________  ________      __   ___  _____  ___    __     _______   _______  
 /"       )|"  |/  \|  "| |" \    /"       )/"       )    |/"| /  ")(\"   \|"  \  |" \   /"     "| /"     "| 
(:   \___/ |'  /    \:  | ||  |  (:   \___/(:   \___/     (: |/   / |.\\   \    | ||  | (: ______)(: ______) 
 \___  \   |: /'        | |:  |   \___  \   \___  \       |    __/  |: \.   \\  | |:  |  \/    |   \/    |   
  __/  \\   \//  /\'    | |.  |    __/  \\   __/  \\      (// _  \  |.  \    \. | |.  |  // ___)   // ___)_  
 /" \   :)  /   /  \\   | /\  |\  /" \   :) /" \   :)     |: | \  \ |    \    \ | /\  |\(:  (     (:      "| 
(_______/  |___/    \___|(__\_|_)(_______/ (_______/      (__|  \__) \___|\____\)(__\_|_)\__/      \_______) 
                                                                                                             



"""
#def
#
#Whatweb
def Whatweb():
    os.system('clear')
    print(banner)
    url = input(">>> ")
    time.sleep(2)
    os.system('clear')
    print("Start Whatweb")
    os.system("clear")
    os.system('whatweb --no-error -v ' + str(url) )

#Nmap port scan
def nmap():
    os.system("clear")
    print(banner)
    print("[1] Scan all ports with Nmap")
    print("")
    print("[2] Aggressive utility scanning")
    print("")
    print("[3] Stealth full network scan with OS detection")
    print("")
    print("[4] Nmap scan vuln")
    print("")
    
    menu_nmap = input(">>> ")
    
    if menu_nmap == "1":
        os.system('clear')
        print(banner)
        time.sleep(2)
        ip = input(">>> ")
        os.system('clear')
        os.system("sudo nmap -p-" +str(ip))
    
    elif menu_nmap == "2":
        os.system('clear')
        time.sleep(2)
        print(banner)
        ip = input(">>> ")
        os.system('clear')
        os.system("sudo nmap -sV --version-intensity 5" +str(ip))
        
    elif menu_nmap == "3":
        os.system('clear')
        time.sleep(2)
        print(banner)
        ip = input(">>> ")
        os.system('clear')
        os.system("sudo nmap -sS -O " +ip+ "/24")
    
    elif menu_nmap == "4":
        os.system("clear")
        time.sleep(2)
        print(banner)
        ip = input(">>> ")
        os.system('clear')
        os.system('sudo nmap --script "vuln" -Pn --open -A ' + str(ip))
        
#Sqlmap test
def sqlmap():
    os.system("clear")
    time.sleep(2)
    print(banner)
    url = input(">>> ")
    os.system('clear')
    os.system('sqlmap -u ' +url+ '--dbs --forms --crawl=2')
        
#SsLScan
def ssl():
    os.system("clear")
    time.sleep(2)
    print(banner)
    url = input(">>> ")
    os.system('clear')
    os.system("sslscan -v " +str(url))

#dns scan
def dns():
    os.system("clear")
    time.sleep(2)
    print(banner)
    url = input(">>> ")
    os.system('clear')
    os.system("dnsmap " +str(url))
    
#dmitry
def dmitry():
    os.system("clear")
    time.sleep(2)
    print(banner)
    ip = input(">>> ")
    os.system('clear')
    os.system("dmitry -i " +str(ip))


#Menu de web hacking
def web():
    os.system("clear")
    print(banner)
    print("[1] Whatweb Fast Scan")
    print("")
    print("[2] Scan Nmap")
    print("")
    print("[3] Sqlmap Test")
    print()
    print("[4] SSl Scan")
    print()
    print("[5] DNS Scan")
    print()
    print("[6] Dmitry ")
    print()
    menu = input(">>> ")
    if menu == "1":
        Whatweb()
    elif menu == "2":
        nmap()
    elif menu == "3":
        sqlmap()
    elif menu == "4":
        ssl()
    elif menu == "5":
        dns()
    elif menu == "6":
        dmitry()
#menu osint phone sms
def osint():
    os.system('clear')
    time.sleep(2)
    print(banner)
    nickname = input(">>> ")
    print("Start Osint")
    os.system('clear')
    os.system('sudo maigret -a ' +str(nickname))
    
def phone():
    os.system('clear')
    time.sleep(2)
    print(banner)
    call = input(">>> ")
    os.system("clear")
    os.system("./phoneinfoga scan -n " +str(call))
    
def sms():
    os.system('clear')
    print(banner)
    print("[1] Instagram")
    print("")
    print("[2] Telegram")
    print("")
    print("[3] Facebook")
    print("")
    sms = input(">>> ")
    
    if sms == "1":
        instagram = subprocess.getoutput("firefox https://www.instagram.com/accounts/password/reset/")
    
    elif sms == "3":
        Facebook = subprocess.getoutput("firefox https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2F&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&_rdr")
        
    elif sms == "2":
        Telegram = subprocess.getoutput("firefox https://web.telegram.org/z/")

def menu_sc():
    os.system('clear')
    print(banner)
    print("[1] OSINT")
    print("")
    print("[2] Phoneinfoga")
    print("")
    print("[3] SMS")
    print("")
    social = input(">>> ")
    
    if social == "1":
        osint()
    
    elif social == "2":
        phone()
        
    elif social == "3":
        sms()
        
#Wifi
def wifi():
    os.system('clear')
    print(banner)
    time.sleep(2)
    os.system('sudo bash config/WIFI-DEATH/start.sh')
#
#menu
os.system('clear')
print(banner)
time.sleep(2)
print("[1] Social engineering")
print("")
print("[2] Web Hacking")
print("")
print("[3] Wifi Hacking")
print("")

menu = input(">>> ")

if menu == "1":
    menu_sc()
    
elif menu == "2":
    web()

elif menu == "3":
    wifi()
