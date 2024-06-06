import sys
import os
sys.path.insert(0, os.getcwd()+'/Public')
from Orchid import Instance
C2 = Instance('2', 'localhost')
for i in range(100):
        A =     C2.Process(i, 3, 'M')

        B =     C2.Process(A, 5, 'A')
