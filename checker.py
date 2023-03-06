from config import Config
from req import *
from time import sleep as w8
from os import getlogin as pcusr
from halo import Halo

cf = Config()
try:
    try:
        usr = cf.username
        ext = cf.flextn
        ipp = cf.dfipflnm
        blc = cf.dfblnm
        useros = pcusr
        ds = cf.dsya
    except AttributeError:
        pass
        
        

    class scan:
        def __init__(self):
            self.ipadd = ""
            self.blacklst = ""
            self.res = ""
            self.bilgi = f"""{err.info} Enter File Names Without Extension.
        For example if it is IP.txt Or C:\\Users\\{useros}\\Desktop\\IP.txt
        Just Your File Name or C:\\Users\\{useros}\\Desktop\\Your_File_Name
        You Can Write That Way."""
            
        def getinput(self):
            
            try:
                    
                    print(self.bilgi)
                    self.ipadd = input(err.info+f"Enter the Name of the File with the IP Addresses Without Extension:{renk.YELLOW}"+renk.ENDC)
                    self.blacklst = input(err.info+f"Enter the name of the file containing the blacklist without the extension:{renk.YELLOW}"+renk.ENDC)
                    self.res = input(err.info+f"Enter the Name of the File You Want to Print Results Without Extension:(Default : results.txt):{renk.YELLOW}"+renk.ENDC)
                    self.run()
            except KeyboardInterrupt as ki:
                    error("User Aborted!(CTRL+C)")
            except NameError and ValueError and OSError and WindowsError and ConnectionRefusedError and ConnectionError and ConnectionAbortedError as ne:
                    error(ne)
            
                    
        def run(self):
            defares = "result.txt"
            try:
                    if self.ipadd != "" and  self.blacklst != "":
                        blst = self.blacklst
                        ipad = self.ipadd
                        blst += ext
                        ipad+=ext
                    elif self.ipadd != ""  and self.blacklst == "":
                        error("Blacklist File Not Added.")
                        
                    elif self.ipadd == ""  and self.blacklst != "":
                        error("IP File Not Added.")
                
                    class fs:
                            
                            blstf = blst
                            ipf = ipad
                            if self.res == "":
                                resf = defares
                            else:
                                self.res+=ext
                                resf = self.res

            except KeyboardInterrupt as ki:
                    error("User Aborted!(CTRL+C)")

            if path.isfile(fs.resf) == True:
                    print(err.succ+f"File Found!-->{fs.resf}\n"+renk.ENDC+err.info+"Reading Data..."+renk.ENDC)
                    w8(3)
                    with open(fs.resf, 'r') as f:
                        varolan_ip_adresleri = set(line.strip() for line in f)
            else:
                    print(err.eror+f"File Not Found!--->{fs.resf}.\n"+renk.ENDC+err.info+"Creating a New File...")
                    varolan_ip_adresleri = set()
                    w8(5)
                    system("cls||clear")
                    if path.exists(fs.resf) == True:
                        print(err.succ+f"Created New File--->{fs.resf}.!\n"+renk.ENDC+err.info+"Writing Data..."+renk.ENDC)
                        w8(3)
                    
            try:
                    with open(fs.ipf, 'r') as f1, open(fs.blstf, 'r') as f2, open(fs.resf, 'a+') as f3:
                        ip_list = [line.strip() for line in f1]
                        blacklist = set(line.strip() for line in f2)
                        eslesen_ip_adresleri = set(ip for ip in ip_list if ip in blacklist)
                        snco = 0
                        sncy = 0
                        for ip in eslesen_ip_adresleri:
                            try:
                                if not re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
                                    print(err.eror+f"This Is Not An IP Address--->{ip}"+renk.ENDC)
                                    w8(1)
                                    continue
                            
                                if ip in varolan_ip_adresleri:
                                    snco += 1
                                    print(err.warn+f"This IP is already Banned!-->{ip}"+renk.ENDC)
                                    w8(1)
                                else:
                                    sncy += 1
                                    print(err.succ+f"IP Banned!-->{ip}"+renk.ENDC)
                                    f3.write(ip + '\n')
                                    w8(1)
                                    varolan_ip_adresleri.add(ip)
                            except KeyboardInterrupt:
                                sonuc = sncy + snco
                                result= f"""
                ================================
                    Scan Aborted By User!
                ================================
                Writing Data --> {str(sncy)}
                Reading Data --> {str(snco)}
                Total Appended Data --> {str(sonuc)}

                            """
                                print(".","Scan Aborted By User!\nLoading and Saving Results...")
                                w8(3)
                                print(result)
                                with open('userlog.log',"a+",encoding="utf8",errors="ignore") as f:
                                    f.write(result)
                                    w8(4)
                                    exit(err.info+'Save Has Done!\n'+renk.FAIL+'Exiting...'+renk.ENDC)
                        
                        sonuc = sncy + snco
                        result= f"""
        ================================
                Results
        ================================
        Writing Data --> {str(sncy)}
        Reading Data--> {str(snco)}
        Total Appended Data --> {str(sonuc)}

                            """
                        with Halo(text='Loading And Saving Results...', spinner='dots') as spinner:
                            print("Please Wait.")
                            spinner.start()
                            w8(10)
                            spinner.succeed('Results Saved!')
                            spinner.stop()
                        w8(1)    
                        print(renk.BOLD+renk.PURPLE+result)
                        with open('userlog.log',"a+",encoding="utf8",errors="ignore") as f:
                            f.write(result)
                        w8(5)
            except FileNotFoundError as ferror:
                    error(ferror)

        def usrsettings(self):
            system("cls||clear")
            self.setmenu = renk.YELLOW+"""
        🔧 SETTINGS 🔧
    [ 🛠️ 1 ] Change User Settings    
    [ 👤 2 ] View User Settings
    [ 💨 3 ] Return To Main Menu
            """
            self.usrsetmenu = renk.YELLOW+f"""
                👤User Settings👤
                Username : {usr}
        Default File Extention--->{ext}
        Default IP File Name--->{ipp}
        Default Blacklist File Name--->{blc}   
        Path Of The Config File--->{cf.dsya}
            """
            print(self.setmenu)
            try:
                self.ch = int(input(err.info+"Choose: "+renk.ENDC)) 
            except ValueError as ve:
                error(f"{ve}\nPlease Enter A Number")
            if self.ch == 1:
                self.succ()
            elif self.ch == 2:
                print(self.usrsetmenu+"\nPress Enter to Return to the SettingsMenu.")
                input()
                self.usrsettings()
            elif self.ch == 3:
                from main import mai
                system("cls||clear")
                mai()
                
        def succ(self):
                self.newus = input("Set a New Username: ")
                self.newip = input("Set a New IP File:")
                self.newbl = input("Set a New Blacklist: ")
                
            
                q = f"""
    New Username-->{self.newus}
    Default IP File Name--->{self.newip}
    Default Blacklist File Name--->{self.newbl}"""
                while True:
                    quest = input(q+"Changes Will Be Saved Are You Sure? Y/N:")
                    if quest == "y" or quest == "y".upper:
                        asqw(self.newus,self.newip,self.newbl)
                    elif quest == "n".upper or quest == "n":
                        print("Okay. You Return To Settings Menu.")
                        w8(3)
                        self.usrsettings()
                        break
                    else:
                        continue





    def asqw(username,defipadd,deflblnm):
            import configparser
            
            confi = configparser.ConfigParser()
            from config import Config
            cnf = Config()
            confi['UserSettings'] = {
                'username': username,
                'defipfilename': defipadd,
                'defblacklstfilename': deflblnm,
                'defaultfileextenion' : ".txt"
            }

            
            with open(cnf.config_file, 'w') as f:
                confi.write(f)

            
            with Halo(text='Your Settings Still Updating Please Wait', spinner='dots') as spinner:
                spinner.start()
                w8(7)
                spinner.succeed(f'{err.succ} Settings updated Successfully!')
                print("Restarting...")
                w8(5)
                system("cls||clear")
                system("main.py||python main.py")
                spinner.stop()
except KeyboardInterrupt:
    error("User Aborted!(CTRL+C)")











