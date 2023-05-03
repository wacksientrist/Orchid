from Paths import InitPath
InitPath()
from Lib1 import Instance

C1 = Instance("1")
C2 = Instance("2")

alp = "qwertyuiop1234567890asdfghjklzxcvbnm,./;'[]-=\\`~!@#$\%^&*()_+QWEERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"

password = input("Enter a password less than 6 digits: \t")

if len(password) > 6:
    print("Your password is greater than 6 digits!")

for i2 in range(len(alp)):
        file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
        test=""+alp[i2]
        C1.Process(test,password,"IF=")
        if C1.Read:
            print("password found! "+test)
            quit()

for i in range(len(alp)):
    test1 = alp[i]
    for i2 in range(len(alp)):
        file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
        test=test1+alp[i2]

        C2.Process(test,password,"IF=")
        if C2.Read:
            print("password found! "+test)
            quit()

for i3 in range(len(alp)):
    test2=alp[i3]
    for i in range(len(alp)):
        test1 = alp[i]
        for i2 in range(len(alp)):
            file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
            test=test2+test1+alp[i2]

            C1.Process(test,password,"IF=")
            if C1.Read:
                print("password found! "+test)
                quit()

for i4 in range(len(alp)):
    test3=alp[i4]
    for i3 in range(len(alp)):
        test2=alp[i3]
        for i in range(len(alp)):
            test1 = alp[i]
            for i2 in range(len(alp)):
                file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
                test=test3+test2+test1+alp[i2]

                C1.Process(test,password,"IF=")
                if C1.Read:
                    print("password found! "+test)
                    quit()
                    
    
    