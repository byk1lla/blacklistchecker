
from req import * 
from time import sleep as w8
import configparser
import os
from halo import Halo






class Config:
    def __init__(self):
        try:
            self.config_file = 'user.config'
            self.system_file = "sys.config"
            self.dsya = os.path.abspath(self.config_file)
            if not os.path.exists(self.config_file):
                self.conf()
            elif os.path.exists(self.config_file) == True:
                self.getconfig()
        except KeyboardInterrupt:
            error("User Aborted!(CTRL+C)")
    def conf(self):
        try:
            config = configparser.ConfigParser()        
            config['UserSettings'] = {
                'username': os.getlogin(),
                'defipfilename': 'IP.txt',
                'defblacklstfilename': 'blacklist.txt',
                'defaultfileextenion' : '.txt'
            }
            
            with open(self.config_file, 'w') as f:
                config.write(f)
        
            print(err.eror+"Config File Not Available.")
            with Halo(text='Making Your Settings Please Wait.', spinner='dots') as spinner:
                spinner.start()
                w8(5)
                spinner.succeed(f'User Settings Configured! Save To--->{self.dsya}')
                print("Restarting...")
                w8(5)
                system("cls||clear")
                system("main.py||python main.py")
        except KeyboardInterrupt:
            error("User Aborted!(CTRL+C)")
        

        
    def getconfig(self):
        global usr,ipdf,bldf,ext
        try:
            print(err.succ+"Config File Has Found!")
            config = configparser.ConfigParser()
            config.read(self.config_file)
            
            
            if not config.sections() or 'UserSettings' not in config:
                error_msg = f"Config dosyası hatalı veya eksik: {self.config_file}"
                error(error_msg)
            else:
                self.username = config['UserSettings'].get('username')
                self.dfipflnm= config['UserSettings'].get('defipfilename')
                self.dfblnm = config['UserSettings'].get('defblacklstfilename')
                self.flextn = config['UserSettings'].get('defaultfileextenion')
                with Halo(text='Retrieving User Information from Config File Please Wait...', spinner='dots') as spinner:
                    spinner.start()
                    w8(5)
                    spinner.succeed('The operation was successful!')
                    spinner.stop()
                    print("You Are Redirected To The Main Menu...")
                    w8(6)
                    system("cls||clear")
        except KeyboardInterrupt:        
            error("User Aborted!(CTRL+C)")

            
        

