from auxi import *
from numpy import amax, dot

def main():
    start()
    pass
    
def start():
    print("Welcome to my Basic Power Method calculator! You will need to enter two matrices here, " +
    "with both matrices having the same number of rows and \nthe second matrix having only 1 column.\n" +
    "If either of these are not true, the program will reset.\n")
    iterate()
    
def iterate():
    _, _, x1, x1s = buildMatrix(bind_c=1, bind_r=3) # temporary bindings
    _, _, mat, mats = buildMatrix(bind_r=3) # temporary bindings
    mat = combineMat(mat, mats) # matrix A
    x1 = combineMat(x1, x1s) # matrix x1
    dev = 0 # dominant eigenvalue
    
    prevX = x1
    for _ in range(8):
        # newX = [[prevX[0][0]*mat[0][0]+prevX[1][0]*mat[0][1]+prevX[2][0]*mat[0][2]],
        #         [prevX[0][0]*mat[1][0]+prevX[1][0]*mat[1][1]+prevX[2][0]*mat[1][2]],
        #         [prevX[0][0]*mat[2][0]+prevX[1][0]*mat[2][1]+prevX[2][0]*mat[2][2]]]
        newX = dot(mat, prevX)
        dev = amax(newX)
        print(dev)
        for i in range(len(newX)):
            newX[i][0] /= dev
        print(newX)
        prevX = newX


if __name__ == '__main__':
    main()

# copy below test values and paste to autofill inputs (remove '#')
# 1
# 3
# 1
# -0.8
# 0.9
# 3
# 3
# -7 13 -16
# 13 -10 13
# -16 13 -7
