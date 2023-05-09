import time

class Instance():
        def __init__(self, UUID):
              self.UUID = UUID
        def Process(self, A, B, Type):
                A_fil = open("Comp"+str(self.UUID)+"/Instrc_r1.txt", "w")
                B_fil = open("Comp"+str(self.UUID)+"/Instrc_r2.txt", "w")
                Type_fil = open("Comp"+str(self.UUID)+"/Instrc_r3.txt", "w")
                if Type == "IF=":
                        A_fil.write(str(A))
                        B_fil.write(str(B))
                elif Type == "IF!":
                        A_fil.write(str(A))
                        B_fil.write(str(B))
                else:
                        A_fil.write(str(float(A)))
                        B_fil.write(str(float(B)))
                A_fil.close()
                B_fil.close()
                Type_fil.write(str(Type))
                Type_fil.close()
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