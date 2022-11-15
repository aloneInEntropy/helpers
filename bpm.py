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
    _, _, mat, mats = buildMatrix(bind_r=3) # temporary bindings
    _, _, x1, x1s = buildMatrix(bind_c=1, bind_r=3) # temporary bindings
    mat = combineMat(mat, mats) # matrix A
    x1 = combineMat(x1, x1s) # matrix x1
    dev = 0 # dominant eigenvalue
    iters = input("How many iterations? ")
    check_exit(iters)
    
    
    prevX = x1
    for _ in range(int(iters)+1):
        # newX = [[prevX[0][0]*mat[0][0]+prevX[1][0]*mat[0][1]+prevX[2][0]*mat[0][2]],
        #         [prevX[0][0]*mat[1][0]+prevX[1][0]*mat[1][1]+prevX[2][0]*mat[1][2]],
        #         [prevX[0][0]*mat[2][0]+prevX[1][0]*mat[2][1]+prevX[2][0]*mat[2][2]]]
        newX = dot(mat, prevX)
        dev = max(newX.min(), newX.max(), key=abs)
        # dev = newX[2][0] # this works too?? maybe???
        print(dev)
        for i in range(len(newX)):
            newX[i][0] /= dev
        print(newX)
        prevX = newX


if __name__ == '__main__':
    main()

# copy below test values and paste to autofill inputs (remove '#')
# 3
# 3
# -7 13 -16
# 13 -10 13
# -16 13 -7
# 1
# 3
# 1
# -0.8
# 0.9
# 7
# _________________
# 3
# 3
# 4 2 -2
# -2 8 1
# 2 4 -4
# 1
# 3
# 1
# 1
# 1
# 8
