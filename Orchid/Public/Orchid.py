import time

class Instance():
        def __init__(self, UUID):
              self.UUID = UUID
        def Process(self, A, B, Type):
                open("Comp"+str(self.UUID)+"/Instrc_n.txt", "w").write("n")
                A_fil = open("Comp"+str(self.UUID)+"/Instrc_r.txt", "w")
                C = open("Comp"+str(self.UUID)+"/Instrc_s.txt", "w")
                C.write("P")
                C.close()
                B_fil = open("Comp"+str(self.UUID)+"/Instrc_s.txt", "r")
                A_fil.write(str(A)+r" "+str(B)+r" "+str(Type))
                A_fil.close()
                while B_fil.read() == "P":
                        time.sleep(0.01)
                open("Comp"+str(self.UUID)+"/Instrc_n.txt", "w").write("")
        def Read(self):
                time.sleep(0.1)
                A_fil = open("Comp"+str(self.UUID)+"/Instrc_s.txt", "r")
                while(True):
                        A_str = A_fil.read()
                        if A_str == "":
                                pass
                        else:
                                if A_str == "F":
                                        A_fil.close()
                                        
                                        return False
                                if A_str == "T":
                                        A_fil.close()
                                        
                                        return True
                                A_fil.close()
                                
                                return A_str