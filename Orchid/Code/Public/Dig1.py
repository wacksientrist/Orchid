from Paths import InitPath
InitPath()
from Lib1 import Instance

C1 = Instance("1")
C2 = Instance("2")

C1.Process(2,3,"A")
C2.Process(2,3,"M")

print(C1.Read())
print(C2.Read())

A = 5
B = 6

while True:
	C1.Process(A,B,"IF=")
	if C1.Read(): 
		A+1
	else: 
		break
print("Found "+str(A))

C1.Process(2,3,"A")
C2.Process(2,3,"M")