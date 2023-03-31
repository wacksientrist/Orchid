import sys
sys.path.insert(0, 'C:/Users/Administrator/Desktop/Code/Orchestrator/')
from Lib1 import Process

alp = "qwertyuiop1234567890asdfghjklzxcvbnm,./;'[]-=\\`~!@#$\%^&*()_+QWEERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"


password = input("Enter a password less than 6 digits: \t")
a = open("Computer1/Code/pass.txt", "w")
a.write(password)
a.close()
test = ""

if len(password) > 6:
    print("Your password is greater than 6 digits!")
    exit()

for i in range(0,int(len(alp)/2)):
    test = alp[i]
    Process(test, password)