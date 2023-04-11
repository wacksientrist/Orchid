import os
import sys

def InitPath():
    sys.path.insert(0, sys.path[0].removesuffix("Public\\"))