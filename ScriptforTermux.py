import os

def menu():

    print(""" 
#############################################
    ______           _        __  ____  __    
   / ____/__  ____  (_)  __  /  |/  / |/ /    
  / /_  / _ \/ __ \/ / |/_/ / /|_/ /|   /     
 / __/ /  __/ / / / />  <  / /  / //   |      
/_/    \___/_/ /_/_/_/|_| /_/  /_//_/|_|                                                                     
==========================================
 TERMUX
 pack by Fenix_Sec_MX 
 Script by Rodrigo Franco :D
------------------------------------------
1. Instala Nmap 
2. Instala Hydra 
3. Instala SQLMap
4. Instala Metasploit
5. Instala ngrok
6. Instala Kali Nethunter
7. Instala angryFuzzer
8. Instala Red_Hawk
9. Instala Weeman
10. Instala IPGeoLocation
11. Instala Cupp
12. Instagram Bruteforcer (instahack)
13. Twitter Bruteforcer   (TwitterSniper)
14. Instala Ubuntu
15. Instala Fedora
16. Instala viSQL
17. Instala Hash-Buster
18. Instala D-TECT
19. Instala routersploit
------------------------------------------
99. Exit
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("This will install: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit and viSQL with one click.")
        print("----------------")
        hm = input("[?] Deseas continuar? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Please put down you android and go to the toilet...")
            print("Because this will take a long time.")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] satisfactoriamente instalado :)")
            print("[+] feliz Hacking <3")
            print("========================================")
        else:
            rmenu = input("[?] Regresar al Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap satisfactoriamente instalado :)")
        print("[+] Type 'nmap' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al  Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra installed successfully :)")
        print("[+] Type 'hydra' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al  Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        print("====================================")
        rmenu = input("[?] 	Regresar al menu (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit installed successfully :)")
        print("[+] escriba 'msfconsole' para empezar.")
        print("====================================")
        rmenu = input("[?] Regresar al  Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok installed successfully :)")
        print("[+] Go to ngrok folder and type './ngrok http 80' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al  Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter installed successfully :)")
        print("[+] Go to Nethunter-In-Termux folder and type './kalinethunter' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al  Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer installed successfully :)")
        print("[+] Go to angryFuzzer folder and type 'python2 angryFuzzer.py' to start.")
        print("====================================")
        rmenu = input("[?] 	Regresar al  Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Go to RED_HAWK folder and type 'php rhawk.php' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman installed successfully :)")
        print("[+] Go to weeman folder and type 'python2 weeman.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation satisfactoriamente instalado :)")
        print("[+] Go to IPGeoLocation folder and type 'python ipgeolocation.py' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp satisfactoriamente instalado :)")
        print("[+] Go to cupp folder and type 'python cupp3.py' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        print("[+] Go to instahack folder and type 'python hackinsta.py' to start.")
        print("====================================")
        rmenu = input("[?] satisfactoriamente instalado? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper satisfactoriamente instalado :)")
        print("[+] Go to TwitterSniper folder and type 'python TwitterSniper.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntusatisfactoriamente instalado :)")
        print("[+] Go to termux-ubuntu folder and type './start.sh' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora satisfactoriamente instalado :)")
        print("[+] Type 'sh termux-fedora.sh f26_arm64' or 'sh termux-fedora.sh f26_arm' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL satisfactoriamente instalado :)")
        print("[+] Go to viSQL folder and type 'python2 viSQL.py --help' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster satisfactoriamente instalado :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Regresar al  Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit satisfactoriamente instalado :)")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            rmenu = input("[?] 	Regresar al  Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "99":
        print("~HappyHacking~.")
        break