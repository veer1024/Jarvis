import requests
import re
from prettytable import PrettyTable
import pyfiglet
import argparse
#colors
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    B = "\033[0;34;40m" # Blue
    orange='\033[43m' 
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    pink='\033[95m'
banner = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢠⣴⣧⣶⣧⣴⣦⣾⣿⣶⣿⣿⣶⣿⣿⣾⣇⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                              
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣾⣿⣿⠟⣿⣿⡿⣿⡿⢻⠿⠋⠽⠟⠻⠟⣿⢿⣿⣿⣿⣿⣿⣿⣷⣿⣧⣴⣦⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⠿⠟⠛⠋⠉⠁⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠙⠋⠻⠟⠻⡿⢿⣿⣿⣿⣿⣿⣷⣶⣦⠀⠀
⠀⠀⠀⠀⠀⠀⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿⠀⠀                         ____.                  .__        
⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢿⠿⠃⠀                        |    |____ __________  _|__| ______
⠀⠀⠀⠀⠀⡀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                        |    \__  \\_  __ \  \/ /  |/  ___/
⠀⠀⠳⡀⠀⠱⡀⠀⢱⡀⠀⠀⢇⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 /\__|    |/ __ \|  | \/\   /|  |\___ \ 
⣄⠀⠀⠙⢄⠀⠱⡄⠀⢣⠀⠀⠘⡄⠘⡄⠀⠒⠒⠒⢒⠛⠛⢓⠒⠒⠒⠒⠠⠭⢁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 \________(____  /__|    \_/ |__/____  >
⠈⠢⡀⠀⠐⣷⢄⡈⢦⣠⡳⣔⢄⠘⣤⣹⣄⡄⢠⡠⣘⣄⣧⣼⣦⣦⣀⡇⢰⠀⡄⠈⡝⠒⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                             \/                    \/ 
⠀⠀⠈⠓⢤⡛⠷⣿⣶⣿⣿⣾⣿⣷⣿⣿⣿⣿⡿⠿⠿⠿⣿⠿⣿⠿⠿⢿⣿⣦⣷⣾⣧⣤⣆⣀⠀⠉⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀                                             by - Viraj Vaishnav ( @hackpeas )
⠀⢀⠀⠢⢄⡙⠷⢮⣝⣿⣿⣿⡿⠟⠋⠉⠁⠀⠀⠀⠀⢠⣃⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣽⣳⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                                                   
⠀⠀⠉⠒⠢⠬⠽⣶⣿⣿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣀⣭⣭⣤⣀⣠⣾⣿⣿⣿⣿⡷⠝⠿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀                                                                                                                                                                                  
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⡻⠝⠂⣸⠋⠉⢻⣿⣿⡟⠣⣄⠀⠩⣿⠈⠙⠻⣿⣿⣶⡀⠀⠀⠀⠀                                                                                                                                                                                   
⠀⠀⠀⠀⠀⠈⠀⣩⣿⡿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣎⡡⠞⠁⢠⣾⡿⢿⣷⡑⢄⠢⡉⣰⠇⠀⠀⠀⠀⠙⠿⣿⣦⠀⠀⠀                                                                                                                                                                                      
⠀⠀⠀⠀⠀⠀⠐⠀⢈⠞⡽⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣌⡐⢡⠃⡇⡀⣿⢳⡈⣲⠞⠃⠀⠀⠀⠀⢀⡤⠞⠁⠙⢷⠀⠀                                                                                                                                                                                      
⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⣨⠋⡸⢻⠷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠶⠧⠿⠒⠋⠁⠀⠀⢀⣀⡤⠖⠉⡠⠆⠀⠀⠈⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠃⠈⠀⠀⠀⢁⠟⢛⡷⣶⣤⣤⣤⣄⣀⣀⣀⣀⣀⡀⢠⡤⠤⠴⡖⠒⠙⠏⠈⢀⡠⠊⠀⠀⠀⠀⠀⠈⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠃⡰⠁⡝⠀⣾⢠⣇⠀⣇⠀⠼⠀⠀⠃⠀⠀⠀⠀⠠⠤⠚⠹⠂⠀⠀⠀⠀⠀⠀⠀⠀

"""
banner2 = """
                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⠀⡀⠀⠂⡀⢀⢰⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀
                                  ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣐⣬⣄⣷⡀⢸⡃⡘⡸⡄⢸⠀⠀⡇⠀⢠⠀⠀⠀
                                  ⠀⠀⠀⠀⠀⣠⡴⠚⢉⢍⢂⣼⣴⣿⣿⣿⣷⣷⣷⣣⣏⣆⣼⠀⠀⠄⠀⠀⠀
                                  ⠀⠀⠀⢠⡞⠋⠀⡑⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣼⣆⣌⡠⢁⡤
                                  ⠀⠀⣰⠋⠀⣀⣺⣾⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁
                                  ⠀⡼⠁⢀⣿⣿⣿⡿⣿⡛⣿⣿⣿⡷⢸⣿⠀⠀⠀⠀⣹⣿⣿⣿⣟⠣⠀⠀⠀
                                  ⡰⠁⢀⣼⣿⠟⢿⡇⠹⣿⣿⣿⠟⠀⢠⡿⠀⠀⣠⣾⡿⣿⡥⠊⠁⠀⠀⠀⠀
                                  ⠁⢠⣾⠟⠁⠀⠈⠳⢿⣦⣠⣤⣦⣼⠟⠁⣠⣾⣿⣿⣟⠍⠒⠀⠠⠀⠀⠀⠀
                                  ⢠⡟⠁⢀⣀⣀⣀⣀⡀⠈⣉⣉⣡⣤⣶⣿⡿⡿⡿⡻⠥⠑⡀⠀⠀⠀⠀⠀⠀
                                  ⠏⡠⠚⠉⠋⢍⠋⢫⠋⠛⢹⢻⡟⠻⣟⢏⠌⢊⡌⠌⠄⠀⠀⠀⠀⠀⠀⠀⠀
                                  ⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠘⠂⠘⠂⠿⠈⠀⠀⠀⠘⠀⠀
                                  

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     _____    | || |      __      | || |  _______     | || | ____   ____  | || |     _____    | || |    _______   | |
| |    |_   _|   | || |     /  \     | || | |_   __ \    | || ||_  _| |_  _| | || |    |_   _|   | || |   /  ___  |  | |
| |      | |     | || |    / /\ \    | || |   | |__) |   | || |  \ \   / /   | || |      | |     | || |  |  (__ \_|  | |
| |   _  | |     | || |   / ____ \   | || |   |  __ /    | || |   \ \ / /    | || |      | |     | || |   '.___`-.   | |
| |  | |_' |     | || | _/ /    \ \_ | || |  _| |  \ \_  | || |    \ ' /     | || |     _| |_    | || |  |`\____) |  | |
| |  `.___.'     | || ||____|  |____|| || | |____| |___| | || |     \_/      | || |    |_____|   | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                             Reconn tool
"""
eye = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢠⣴⣧⣶⣧⣴⣦⣾⣿⣶⣿⣿⣶⣿⣿⣾⣇⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣾⣿⣿⠟⣿⣿⡿⣿⡿⢻⠿⠋⠽⠟⠻⠟⣿⢿⣿⣿⣿⣿⣿⣿⣷⣿⣧⣴⣦⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⠿⠟⠛⠋⠉⠁⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠙⠋⠻⠟⠻⡿⢿⣿⣿⣿⣿⣿⣷⣶⣦⠀⠀
⠀⠀⠀⠀⠀⠀⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿⠀⠀                    
⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢿⠿⠃⠀                                                                                                                                                                     
⠀⠀⠀⠀⠀⡀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                                                                                      
⠀⠀⠳⡀⠀⠱⡀⠀⢱⡀⠀⠀⢇⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                          
⣄⠀⠀⠙⢄⠀⠱⡄⠀⢣⠀⠀⠘⡄⠘⡄⠀⠒⠒⠒⢒⠛⠛⢓⠒⠒⠒⠒⠠⠭⢁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                                                                                
⠈⠢⡀⠀⠐⣷⢄⡈⢦⣠⡳⣔⢄⠘⣤⣹⣄⡄⢠⡠⣘⣄⣧⣼⣦⣦⣀⡇⢰⠀⡄⠈⡝⠒⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                                  
⠀⠀⠈⠓⢤⡛⠷⣿⣶⣿⣿⣾⣿⣷⣿⣿⣿⣿⡿⠿⠿⠿⣿⠿⣿⠿⠿⢿⣿⣦⣷⣾⣧⣤⣆⣀⠀⠉⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                                                        
⠀⢀⠀⠢⢄⡙⠷⢮⣝⣿⣿⣿⡿⠟⠋⠉⠁⠀⠀⠀⠀⢠⣃⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣽⣳⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                                                   
⠀⠀⠉⠒⠢⠬⠽⣶⣿⣿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣀⣭⣭⣤⣀⣠⣾⣿⣿⣿⣿⡷⠝⠿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀                                                                                                                                                                                  
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⡻⠝⠂⣸⠋⠉⢻⣿⣿⡟⠣⣄⠀⠩⣿⠈⠙⠻⣿⣿⣶⡀⠀⠀⠀⠀                                                                                                                                                                                   
⠀⠀⠀⠀⠀⠈⠀⣩⣿⡿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣎⡡⠞⠁⢠⣾⡿⢿⣷⡑⢄⠢⡉⣰⠇⠀⠀⠀⠀⠙⠿⣿⣦⠀⠀⠀                                                                                                                                                                                      
⠀⠀⠀⠀⠀⠀⠐⠀⢈⠞⡽⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣌⡐⢡⠃⡇⡀⣿⢳⡈⣲⠞⠃⠀⠀⠀⠀⢀⡤⠞⠁⠙⢷⠀⠀                                                                                                                                                                                      
⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⣨⠋⡸⢻⠷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠶⠧⠿⠒⠋⠁⠀⠀⢀⣀⡤⠖⠉⡠⠆⠀⠀⠈⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠃⠈⠀⠀⠀⢁⠟⢛⡷⣶⣤⣤⣤⣄⣀⣀⣀⣀⣀⡀⢠⡤⠤⠴⡖⠒⠙⠏⠈⢀⡠⠊⠀⠀⠀⠀⠀⠈⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠃⡰⠁⡝⠀⣾⢠⣇⠀⣇⠀⠼⠀⠀⠃⠀⠀⠀⠀⠠⠤⠚⠹⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
Jarvis = """

     ____.                  .__        
    |    |____ __________  _|__| ______
    |    \__  \\_  __ \  \/ /  |/  ___/
/\__|    |/ __ \|  | \/\   /|  |\___ \ 
\________(____  /__|    \_/ |__/____  >
              \/                    \/ 
               by - Viraj Vaishnav ( @hackpeas )
"""

#ascii_banner_anonymous = pyfiglet.figlet_format(banner)
print(f"{bcolors.FAIL}"+banner2+f"{bcolors.RESET}")
#print(ascii_banner)
print(f"{bcolors.pink}Presented by : hackpeas{bcolors.RESET}")
ascii_banner = pyfiglet.figlet_format("Installation will begin shortly ... ")
print(ascii_banner)
#print(f"{bcolors.pink}Head of Network and Security and Department{bcolors.RESET}")
#print(f"{bcolors.pink}Bug-Bounty Hunter{bcolors.RESET}")
#print(f"{bcolors.pink}CTF Player on HTB,tryhafckme,picoctf etc{bcolors.RESET}")
#print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
