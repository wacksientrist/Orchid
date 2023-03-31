import os

def Process(A, B):
        A_fil = open("Computer1/Interperet/Instrc_r.txt", "w")
        A_fil.write(A+"!!!!!!!"+B)
        A_fil.close()
        os.system("C:/Users/Administrator/AppData/Local/Programs/Python/Python311/python.exe C:/Users/Administrator/Desktop/Code/Orchestrator/Computer1/Interperet/Test.py")

        A_fil = open("Instrc_s.txt", "r")
        if A_fil.read() == "T":
            exit()
        A_fil.close()