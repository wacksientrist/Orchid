from time import sleep

while True:
    if open("Comp2/Instrc_n.txt", 'r').read() == "n":
        
        sleep(0.1)

        fil1 = open("Comp2/Instrc_r.txt", "r").read()
        fil2 = open("Comp2/Instrc_s.txt", "w")

        fil1 = fil1.split('!!!!!!!')
        print(fil1)

        A = fil1[0]
        B = fil1[1]
        Type = fil1[2]


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
        fil2.write(str(Out))
        fil2.close()
