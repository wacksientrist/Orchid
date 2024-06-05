from time import sleep

while True:
    # Check if there's a new command to process
    if open("Instrc_n.txt", 'r').read() == "n":
        
        # Read the command
        with open("Instrc_r.txt", "r") as f:
            command = f.read().strip()
        
        # Inform other nodes that it's still processing
        with open("Instrc_s.txt", "w") as f:
            f.write("P")
        
        # Parse the command
        A, B, Type = command.split()
        
        # Execute the command
        if Type == "A":
            Out = float(A) + float(B)
        elif Type == "S":
            Out = float(A) - float(B)
        elif Type == "M":
            Out = float(A) * float(B)
        elif Type == "D":
            Out = float(A) / float(B)
        elif Type == "IF=":
            Out = "T" if A == B else "F"
        elif Type == "IF!":
            Out = "T" if A != B else "F"
        elif Type == "IF>":
            Out = "T" if float(A) > float(B) else "F"
        elif Type == "IF<":
            Out = "T" if float(A) < float(B) else "F"
        else:
            Out = "Unknown Type"
        
        # Return the output
        with open("Instrc_s.txt", "w") as f:
            f.write(str(Out))
