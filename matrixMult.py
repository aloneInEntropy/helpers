"""Matrix multiplier."""

from auxi import *
from numpy import dot

def main():
    start()
    
def start():
    print("Please enter the first matrix.")
    _, _, mata, sa = buildMatrix() # matrix a
    print("Please enter the second matrix.")
    _, _, matb, sb = buildMatrix() # matrix b
    a = combineMatrices(mata, sa)
    b = combineMatrices(matb, sb)
    
    print(dot(a, b))
    
if __name__ == '__main__':
    main()
