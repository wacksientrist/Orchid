import time

class Node():
        def __init__(self, UUID):
              self.UUID = UUID # Localize UUID variable
              self.result = None
        def Process(self, A, B, Type):
                Input_File = open("Comp"+str(self.UUID)+"/Instrc_r.txt", "w") # open the input file
                Output_File = open("Comp"+str(self.UUID)+"/Instrc_s.txt", "w") # open the output file for writing
                Output_File.write("P") # Write Placeholder to overwrite previous output
                Output_File.close()
                Output_File = open("Comp"+str(self.UUID)+"/Instrc_s.txt", "r") # open output file
                Input_File.write(str(A)+r" "+str(B)+r" "+str(Type)) # Send the Command to Be Processed
                Input_File.close()
                open("Comp"+str(self.UUID)+"/Instrc_n.txt", "w").write("n") # Inform the Node that there is a new command
                while Output_File.read() == "P": # Wait until the Output File changes from The Placeholder to the new Output
                        time.sleep(0.01)
                open("Comp"+str(self.UUID)+"/Instrc_n.txt", "w").write("") # Upon Receipt of Output Inform the Node there is no new command
        def Read(self):
                while(True):
                        Output_File = open("Comp"+str(self.UUID)+"/Instrc_s.txt", "r")
                        #time.sleep(0.01)
                        A_str = Output_File.read()
                        if A_str == "P": # Check Processing Status
                                Output_File.close()
                                continue
                        if A_str == "": # Check Processing Status
                                Output_File.close()
                                continue
                        if open("Comp"+str(self.UUID)+"/Instrc_n.txt", "r").read() == "n": # Check If file is ready for read
                                Output_File.close()
                                continue
                        if A_str == "F": # Check if its a boolean and return proper output
                                Output_File.close()
                                return False
                        elif A_str == "T": # Check if its a boolean and return proper output
                                Output_File.close()
                                return True
                        else: # Output is a number, to keep float and int, support return string
                                Output_File.close()
                                return A_str
                        