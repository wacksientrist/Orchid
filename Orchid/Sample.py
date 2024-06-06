import sys
import os
sys.path.insert(0, os.getcwd()+'/Public')
from Orchid import Instance
C1 = Instance('1')
for i in range(10000000):
	C1.Process(i, 3, '*')
	A = C1.Read()
	C1.Process(A, 5, '+')
	B = C1.Read()