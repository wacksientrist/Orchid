from Lib1 import Instance
from ctypes import *
CDLL("Lib1.so")
from multiprocessing import Process

def D1(alp, password, C1):
    for i2 in range(len(alp)):
            
            test=""+alp[i2]
            C1.Process(test,password,"IF=")
            if C1.Read():
                print("password found! "+test)
                quit()
def D2(alp, password, C2):
    for i in range(len(alp)):
        test1 = alp[i]
        for i2 in range(len(alp)):
            
            test=test1+alp[i2]

            C2.Process(test,password,"IF=")
            if C2.Read():
                print("password found! "+test)
                quit()
def D3(alp, password, C3):
    for i3 in range(len(alp)):
        test2=alp[i3]
        for i in range(len(alp)):
            test1 = alp[i]
            for i2 in range(len(alp)):
                
                test=test2+test1+alp[i2]

                C3.Process(test,password,"IF=")
                if C3.Read():
                    print("password found! "+test)
                    quit()
def D4(alp, password, C4):
    for i4 in range(len(alp)):
        test3=alp[i4]
        for i3 in range(len(alp)):
            test2=alp[i3]
            for i in range(len(alp)):
                test1 = alp[i]
                for i2 in range(len(alp)):
                    
                    test=test3+test2+test1+alp[i2]

                    C4.Process(test,password,"IF=")
                    if C4.Read():
                        print("password found! "+test)
                        quit()
def D5(alp, password, C5):
    for i5 in range(len(alp)):
        test4=alp[i5]
        for i4 in range(len(alp)):
            test3=alp[i4]
            for i3 in range(len(alp)):
                test2=alp[i3]
                for i in range(len(alp)):
                    test1 = alp[i]
                    for i2 in range(len(alp)):
                        
                        test=test4+test3+test2+test1+alp[i2]

                        C5.Process(test,password,"IF=")
                        if C5.Read():
                            print("password found! "+test)
                            quit()
def D6(alp, password, C6):
    for i6 in range(len(alp)):
        test5=alp[i6]
        for i5 in range(len(alp)):
            test4=alp[i5]
            for i4 in range(len(alp)):
                test3=alp[i4]
                for i3 in range(len(alp)):
                    test2=alp[i3]
                    for i in range(len(alp)):
                        test1 = alp[i]
                        for i2 in range(len(alp)):
                            
                            test=test5+test4+test3+test2+test1+alp[i2]

                            C6.Process(test,password,"IF=")
                            if C6.Read():
                                print("password found! "+test)
                                quit()

if __name__ == "__main__":

    C1 = Instance("1")
    C2 = Instance("2")
    C3 = Instance("3")
    C4 = Instance("4")
    C5 = Instance("5")
    C6 = Instance("6")

    alp = "qwertyuiop1234567890asdfghjklzxcvbnm,./;'[]-=\\`~@#$\%^&*()_+QWEERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?!"
    password = input("Enter a password less than 6 digits: \t")

    if len(password) > 6:
        print("Your password is greater than 6 digits!")

    Proc1 = Process(target=D1, args=(alp, password, C1))
    Proc2 = Process(target=D2, args=(alp, password, C2))
    Proc3 = Process(target=D3, args=(alp, password, C3))
    Proc4 = Process(target=D4, args=(alp, password, C4))
    Proc5 = Process(target=D5, args=(alp, password, C5))
    Proc6 = Process(target=D6, args=(alp, password, C6))

    Proc1.start()
    Proc2.start()
    #Proc3.start()
    #Proc4.start()
    #Proc5.start()
    #Proc6.start()