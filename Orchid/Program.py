import sys
import os
import time
sys.path.insert(0, os.getcwd() + '/Public')
from Orchid import Instance

# Ensure the Java server has enough time to start
time.sleep(2)

C2 = Instance('2', 'localhost')
for i in range(100000):
    A = C2.Process(i, 3, '*')
    B = C2.Process(A, 5, '+')
