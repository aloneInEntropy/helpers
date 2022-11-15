from auxi import *
from numpy import dot

def main():
    start()
    
def start():
    print("matrix a")
    _, _, mata, sa = buildMatrix() # matrix a
    print("matrix b")
    _, _, matb, sb = buildMatrix() # matrix b
    a = combineMat(mata, sa)
    b = combineMat(matb, sb)
    
    print(dot(a, b))
    
if __name__ == '__main__':
    main()
