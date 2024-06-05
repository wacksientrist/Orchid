from time import sleep

while True:
<<<<<<< HEAD
       # check if theres a new command to process

       if open("Instrc_n.txt", 'r').read() == "n":
            
            sleep(0.1)
            # read the commands

            fil1 = open("Instrc_r.txt", "r").read()
            fil2 = open("Instrc_s.txt", "w")
            # informs the other nodes that its still processing

            fil2.write("P")
            fil2.close()
            fil2 = open("Instrc_s.txt", "w")
            print(fil1)
            fil1 = fil1.split(" ")
            print(fil1)
            A = fil1[0]
            B = fil1[1]
            Type = fil1[2]

            # execute the new command
            if Type == "A":
                Out = float(A)+float(B)
            if Type == "S":
                Out = float(A)-float(B)
            if Type == "M":
                Out = float(A)*float(B)
            if Type == "D":
                Out = float(A)/float(B)
            if Type == "IF=":
                print(A)
                print(B)
                if A == B:
                    Out = "T"
                else:
                    Out = "F"
            if Type == "IF!":
                if A == B:
                    Out = "F"
                else:
                    Out = "T"   
            if Type == "IF>":
                if A > B:
                    Out = "T"
                else:
                    Out = "F"
            if Type == "IF<":
                if A < B:
                    Out = "T"
                else:
                    Out = "F"

            # return the output
            fil2.write(str(Out))
            fil2.close()
=======
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
>>>>>>> ecff9f7 (- Optimized Instance.py)
