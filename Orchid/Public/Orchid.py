import io
import time

class Instance:
    def __init__(self, UUID):
        self.UUID = UUID
        self.ready_file = io.StringIO()
        self.command_file = io.StringIO()
        self.complete_file = io.StringIO()
        self.result_file = io.StringIO()
    
    def Process(self, A, B, Type):
        # Signal readiness for a new command
        self.ready_file.seek(0)
        self.ready_file.write("ready")
        self.ready_file.truncate()
        
        # Write the command A, B, Type to Instrc_r.txt
        self.command_file.seek(0)
        self.command_file.write(f"{A} {B} {Type}")
        self.command_file.truncate()
        
        # Simulate command processing completion
        self.complete_file.seek(0)
        self.complete_file.write("complete")
        self.complete_file.truncate()
    
    def Read(self):
        # Simulate reading the result from Instrc_s.txt
        self.result_file.seek(0)
        result = self.result_file.read().strip()
        
        # Clear readiness for the next command
        self.ready_file.seek(0)
        self.ready_file.write("")
        self.ready_file.truncate()
        
        # Return the processed result
        if result == "F":
            return False
        elif result == "T":
            return True
        else:
            if result == '':
                return result
            elif result.find('.') != -1:
                return float(result)
            else:
                return int(result)

# Example usage:
instance = Instance("123")
instance.Process("DataA", "DataB", "DataType")
time.sleep(1)  # Simulating some processing time
print(instance.Read())
