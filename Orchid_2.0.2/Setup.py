import os

inp = input("Computer Count: ")
content = open("Orchid/int.sh", "r").read()
content_snp = content
file = open("Orchid/int.sh", "w")

file.write("#! /bin/sh \n")

for i in range(1, int(inp)):
    content = content_snp.replace("_", str(i))+"\n"
    file.write(content)
    os.system(f"mkdir Build/Comp{i}; cp -R Orchid/Comp/ Build/Comp{i}")
file.close()
os.system("cp Orchid/int.sh Build/")
file = open("Orchid/int.sh", "w")
file.write(content_snp)
file.close()