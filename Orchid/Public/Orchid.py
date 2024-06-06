import io

class Instance:
    def __init__(self, UUID):
        self.UUID = UUID
        self.ready_file = io.BytesIO()
        self.command_file = io.BytesIO()
        self.complete_file = io.BytesIO()
        self.result_file = io.BytesIO()
    
    def Process(self, A, B, Type):
        # Signal readiness for a new command
        self.ready_file.seek(0)
        self.ready_file.write(b"ready")
        
        # Write the command A, B, Type to Instrc_r.txt
        self.command_file.seek(0)
        self.command_file.write(str(str(A)+" "+str(B)+" "+Type).encode())
        
        # Simulate command processing completion
        self.complete_file.seek(0)
        self.complete_file.write(b"complete")
    
    def Read(self):
        # Simulate reading the result from Instrc_s.txt
        self.result_file.seek(0)
        result = self.result_file.read().strip().decode()
        
        # Clear readiness for the next command
        self.ready_file.seek(0)
        self.ready_file.write(b"")
        
        # Return the processed result
        if result == "F":
            return False
        elif result == "T":
            return True
        else:
            try:
                if '.' in result:
                    return float(result)
                else:
                    return int(result)
            except ValueError:
                return result
