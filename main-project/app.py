import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'libs/calculator-lib'))

from calc import add

print("Addition:", add(5, 3))