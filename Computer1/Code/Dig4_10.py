import sys
sys.path.insert(0, 'C:/Users/Administrator/Desktop/Code/Orchestrator/')
from Lib1 import Process

alp = "qwertyuiop1234567890asdfghjklzxcvbnm,./;'[]-=\\`~!@#$\%^&*()_+QWEERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"

password = open("Computer1/Code/pass.txt", "r").read()
check = open("C:/Users/Administrator/Desktop/Code/Orchestrator/Instrc_s.txt", "r").read()

if check == 'T':
    exit("Password Already Found")

if len(password) > 6:
    print("Your password is greater than 6 digits!")

for i4 in range(66,70):
    test3 = alp[i4]
    for i3 in range(0,len(alp)):
        test2 = alp[i3]
        for i in range(0,len(alp)):
            test1 = alp[i]
            for i2 in range(0,len(alp)):
                file = open(
                    "Code/pass.txt", "a")
                test = test3+test2+test1+alp[i2]

                if test == password:
                    print("password found! "+test)
                    Process(test, password)
