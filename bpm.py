"""Basic Power Method. Calculating the largest eigenvalue and its eigenvector in a matrix."""

from auxi import *
from numpy import dot

def main():
    start()
    pass
    
def start():
    print("Welcome to my Basic Power Method calculator! You will need to enter two matrices here, " +
    "with both matrices having the same number of rows and \nthe second matrix having only 1 column.\n" +
    "If either of these are not true, the program will reset.\n")
    
    iterate_bpm()
    

def iterate_bpm():
    """Iterate over the given matrices and calculate the eigenvalues and eigenvectors for them."""
    
    try:
        # bindings here are temporary
        print("Creating matrix A...")
        mat = buildMatrix(bind_r=3)[-1] # matrix A
        print("Creating matrix x1...")
        x1= buildMatrix(bind_c=1, bind_r=3)[-1] # matrix x1
        ev = 0 # dominant eigenvalue
        iters = input("How many iterations? ")
        check_exit(iters)

        prevX = x1
        it = 0
        while it < int(iters):
            if it > 0: 
                print(transitionMatrices(tX, newX, '{:.20f}'.format(ev), "/ " + str(ev) + " ", "= x" + str(it+1)))
            newX = dot(mat, prevX) # multiply matrices
            ev = max(newX.min(), newX.max(), key=abs) # find largest magnitude
            tX = newX.copy()
            
            print('i =', it+1)
            for i in range(len(newX)):
                newX[i][0] = float(format(newX[i][0] / ev))
                
            print(transitionMatrices(mat, tX, v='', label_a="* x" + str(it+1) + " "))
            prevX = newX
            
            it += 1
        print(transitionMatrices(tX, newX, '{:.20f}'.format(ev), "/ " + str(ev) + " ", "= x" + str(it+1)))
        print("Maximum eigenvalue:", ev)
    except InvalidInputException:
        print("Invalid input")
    except CancelOperation:
        return

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
# _________________
# 3
# 3
# 0.1 0 0
# 0.15 -1.5 -1.75
# -0.05 0.5 0.75
# 1
# 3
# 1
# 1
# 1
# 10
