import os,time
os.system('clear')
os.system('xdg-open https://facebook.com/groups/MUB4SH4R/')
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
    print(' \n\033[1;37m Your Device Support This Tools');time.sleep(2)
    os.system('chmod 777 dump && ./dump')
else:
    print(' \033[1;31m Sorry device not support this tools');exit()
