import sys
sys.path.insert(0, 'C:/Users/Administrator/Desktop/Code/Orchestrator/')
from Lib1 import Process

alp = "qwertyuiop1234567890asdfghjklzxcvbnm,./;'[]-=\\`~!@#$\%^&*()_+QWEERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"

password = open("Computer1/Code/pass.txt", "r").read()
check = open("C:/Users/Administrator/Desktop/Code/Orchestrator/Instrc_s.txt", "r").read()

if check == 'T':
    exit("Password Already Found")
test = ""

if len(password) > 6:
    print("Your password is greater than 6 digits!")
    exit()

for i in range(int(len(alp)/2),len(alp)):
    test = alp[i]
    Process(test, password)