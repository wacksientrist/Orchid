import re

pattern1 = r'^(.*)=$'
pattern2 = r'^(.*):$'

if_statement = open("Code/Input_Code/test.py", "r").read().splitlines()


#if_statement = "if A != B: A+1 else: pass"
out = open("Code/Input_Code/out.py", "w")
out.write("")
out = open("Code/Input_Code/out.py", "a")
for i2 in range(len(if_statement)):
    if1=if_statement[i2].split(None)

    if if_statement[i2].find("if") == -1:
        out.write(if_statement[i2]+"\n")
    if if_statement[i2].find(":") != -1:
        out.write("\t")
    for i in range(len(if1)):
        if if1[i] == "if":
            A = if1[i+1]
            B = if1[i+2]
            C = if1[i+3]
            match = re.match(pattern1, B)
            if match:
                B = match.group(1)

            match = re.match(pattern2, C)
            if match:
                C = match.group(1)
            

            out.write(f"C1.Process({A}, {C}, 'if{B}')\n")
            i2=i2+1
            out.write(f"if C1.Read():\n")