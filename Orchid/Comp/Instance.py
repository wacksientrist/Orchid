from time import sleep

while True:
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