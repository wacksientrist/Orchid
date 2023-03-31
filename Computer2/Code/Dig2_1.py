import sys
sys.path.insert(0, 'C:/Users/Administrator/Desktop/Code/Orchestrator/')
from Lib1 import Process

alp = "qwertyuiop1234567890asdfghjklzxcvbnm,./;'[]-=\\`~!@#$\%^&*()_+QWEERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"

password = open("Computer1/Code/pass.txt", "r").read()
check = open("C:/Users/Administrator/Desktop/Code/Orchestrator/Instrc_s.txt", "r").read()

if check == 'T':
    exit("Password Already Found")

for i in range(25,50):
    test1 = alp[i]
    for i2 in range(0,len(alp)):
        test = test1+alp[i2]
        Process(test, password)