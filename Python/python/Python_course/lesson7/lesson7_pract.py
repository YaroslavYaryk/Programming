import sys
import os.path

print(sys.argv)

path1 = os.path.dirname(os.path.abspath(__file__))
path2 = os.path.dirname(path1)
path3 = os.path.join(path2, "fascination")
sys.path.append(path3)
import pretty_table