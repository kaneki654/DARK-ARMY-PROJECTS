import os
import random
import sys
import time
import pyfiglet
from functionality.drkrmydnction import clear

class colors:
    RAWR = '\033[91m'
    TAE = '\033[92m'

print(colors.RAWR + "WAIT MO LANG YA, BILANG KA SAMPO..")
time.sleep(10)
clear()

ascii_banner = pyfiglet.figlet_format("DARK-ARMY-DDOS-TOOLS")
print(ascii_banner)

print(colors.TAE + '[1]DDOSit')
print(colors.RAWR + '[2]C2')

user_input = int(input('PILI KA ISA YA: '))

if user_input == 1:
    from GRAA import *
    import subprocess

    cmd = 'python GRAA.py'
    p=subprocess.Popen(cmd,shell=True)
    NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
    print(BOBO_ERROR_HAHAHAH_KAWAWA)
    print(NAG_OUT_TANGINANG_YAN)

if user_input == 2:
    from POWPOW import *
    import subprocess

    cmd = 'python POWPOW.py'
    p=subprocess.Popen(cmd,shell=True)
    NAG_OUT_TANGINANG_YAN,BOBO_ERROR_HAHAHAH_KAWAWA =p.communicate()
    print(BOBO_ERROR_HAHAHAH_KAWAWA)
    print(NAG_OUT_TANGINANG_YAN)