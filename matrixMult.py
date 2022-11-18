"""Matrix multiplier."""

from auxi import *
from numpy import dot

def main():
    start()
    
def start():
    print("Please enter the first matrix.")
    a = buildMatrix()[-1] # matrix a
    print("Please enter the second matrix.")
    b = buildMatrix()[-1] # matrix b
    
    print(dot(a, b))
    
if __name__ == '__main__':
    main()
