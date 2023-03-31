fil1 = open("C:/Users/Administrator/Desktop/Code/Orchestrator/Computer1/Interperet/Instrc_r.txt", "r").read()
fil2 = open("C:/Users/Administrator/Desktop/Code/Orchestrator/Instrc_s.txt", "w")

fil1 = fil1.split('!!!!!!!')

A = fil1[0]
B = fil1[1]

if A == B:
    fil2.write("T")
    exit()
if A != B:
    fil2.write("F")
    exit()

fil2.close()