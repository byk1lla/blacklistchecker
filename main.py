from checker import *


scr = scan()

def mai():
    mainmenu=renk.BLUE+f"""
                    
        ___________________________________________   

                     ~ Welcome {usr}! ~         
                PYTHON BLACKLIST CHECKER    

        ___________________________________________
                                                
            [ #1 ] Scan 
            [ #2 ] Settings
            [ #3 ] Programmers
            [ #4 ] Exit"""


    print(mainmenu+renk.ENDC)
    while True:
        try:
            sc = int(input(renk.YELLOW+"\nChoose:"))
        except ValueError as e:
            error(f"{e}\nPlease Enter A Number")
        except KeyboardInterrupt:
            error("User Aborted!(CTRL+C)")
        if sc == 1:
            scr.getinput()
        if sc == 2:
            scr.usrsettings()
        if sc == 3:
            aboutus()
        if sc == 4:
            exit(renk.FAIL+'Closing...'+renk.ENDC)
    
def aboutus():
    ab = """
                 [ Github ]                  [ Discord ]    
Ismail--->https://github.com/iisma1ll      Jesse Pinkman#0001
Sedat--->https://github.com/Vaispeny        RuinedKing#6586

    Press Enter to Return to the Mainmenu.
    """
    print(ab)
    try:
        input()
    except KeyboardInterrupt:
        error("User Aborted!(CTRL+C)")
    system("cls||clear")
    mai()
    
if __name__ == "__main__":
    mai()