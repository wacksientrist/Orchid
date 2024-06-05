import time

class Instance:
    def __init__(self, UUID):
        self.UUID = UUID
    
    def Process(self, A, B, Type):
        # Signal readiness for a new command
        with open(f"Comp{self.UUID}/Instrc_r_ready.txt", "w") as ready_file:
            ready_file.write("ready")
        
        # Write the command A, B, Type to Instrc_r.txt
        with open(f"Comp{self.UUID}/Instrc_r.txt", "w") as command_file:
            command_file.write(f"{A} {B} {Type}")
        
        # Wait for command processing to complete
        while True:
            with open(f"Comp{self.UUID}/Instrc_r_complete.txt", "r") as complete_file:
                if complete_file.read().strip() == "complete":
                    break
            time.sleep(0.001)
    
    def Read(self):
        time.sleep(0.001)  # Adjust sleep time as needed
        
        # Read the result from Instrc_s.txt
        with open(f"Comp{self.UUID}/Instrc_s.txt", "r") as result_file:
            result = result_file.read().strip()
        
        # Clear readiness for the next command
        with open(f"Comp{self.UUID}/Instrc_r_ready.txt", "w") as ready_file:
            ready_file.write("")
        
        # Return the processed result
        if result == "F":
            return False
        elif result == "T":
            return True
        else:
            return result
