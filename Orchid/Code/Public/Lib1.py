import os
import time

class Instance():
        def __init__(self, UUID):
              self.UUID = UUID
        def Process(self, A, B, Type):
                open("Comp"+str(self.UUID)+"/Instrc_n.txt", "w").write("n")
                A_fil = open("Comp"+str(self.UUID)+"/Instrc_r.txt", "w")
                A_fil.write(str(A)+"!!!!!!!"+str(B)+"!!!!!!!"+Type)
                A_fil.close()
                time.sleep(0.69)
                open("Comp"+str(self.UUID)+"/Instrc_n.txt", "w").write("")
        def Read(self):
                time.sleep(0.1)
                A_fil = open("Comp"+str(self.UUID)+"/Instrc_s.txt", "r")
                while(True):
                        A_str = A_fil.read()
                        if A_str == "":
                                pass
                        else:
                                if A_str == "T":
                                        A_fil.close()
                                        
                                        return True
                                if A_str == "F":
                                        A_fil.close()
                                        
                                        return False
                                A_fil.close()
                                
                                return A_str