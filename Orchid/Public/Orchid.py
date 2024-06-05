import time

class Instance:
    def __init__(self, UUID):
        self.UUID = UUID
    
    def Process(self, A, B, Type):
        with open(f"Comp{self.UUID}/Instrc_n.txt", "w") as n_file:
            n_file.write("n")
        
        with open(f"Comp{self.UUID}/Instrc_r.txt", "w") as A_file:
            A_file.write(f"{A} {B} {Type}")
        
        while True:
            with open(f"Comp{self.UUID}/Instrc_s.txt", "r") as B_file:
                if B_file.read() != "P":
                    break
            time.sleep(0.01)
        
        with open(f"Comp{self.UUID}/Instrc_n.txt", "w") as n_file:
            n_file.write("")
    
    def Read(self):
        time.sleep(0.1)
        with open(f"Comp{self.UUID}/Instrc_s.txt", "r") as A_file:
            A_str = A_file.read().strip()
            if A_str == "F":
                return False
            elif A_str == "T":
                return True
            else:
                return A_str
