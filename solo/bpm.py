"""Basic Power Method. Calculating the largest eigenvalue and its eigenvector in a matrix."""

from numpy import dot

QUITS = ("q", "quit", "exit")
GAP = "  "


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
        mat = buildMatrix(bind_r=3)[-1]  # matrix A
        x1 = buildMatrix(bind_c=1, bind_r=3)[-1]  # matrix x1
        dev = 0  # dominant eigenvalue
        iters = input("How many iterations? ")
        check_exit(iters)

        # print(prettifyMatrix(mat), "\n\n")
        # print(prettifyMatrix(x1), "\n\n")

        prevX = x1
        for it in range(int(iters)):
            newX = dot(mat, prevX)  # multiply matrices
            # find largest magnitude
            dev = max(newX.min(), newX.max(), key=abs)
            tX = newX.copy()

            # print(prettifyMatrix(newX), '\n')
            print('i =', it+1)
            # print(dev)
            for i in range(len(newX)):
                newX[i][0] = float(format(newX[i][0] / dev, '.4f'))
            # print(prettifyMatrix(newX), '\n')
            # print(newX, '\n')
            # print(transitionMatrices(tX, newX, '{:.4f}'.format(dev), "/ " + str(dev) + " ", "= x" + str(it+1)))
            print(transitionMatrices(mat, newX, '{:.4f}'.format(
                dev), "* x" + str(it+1) + " ", "= x" + str(it+2)))
            prevX = newX
    except:
        return


def check_exit(qs: str):
    """Check if a given string is an exit string"""

    if qs.lower() in QUITS:
        raise Exception


def transitionMatrices(a: list[list[int]], b: list[list[int]], v="", label_a="", label_b="") -> str:
    """Create a transition between matrix `a` and `b` during a normalisation.
    `label_a` adds a label to the vector multiplied by `a`, and `label_b` adds a label to the resulting vector. `v` 
    is the resulting value from the normalisation, but must be passed through like the labels."""

    nv = len(v)
    ma = prettifyMatrix(a).split('\n')
    mb = prettifyMatrix(b).split('\n')
    s = ""
    for i in range(len(ma)):
        if i == len(ma)//2:
            s += ma[i] + label_a + "=> " + v + GAP + mb[i] + label_b + "\n"
        else:
            s += ma[i] + GAP*2 + " "*len(label_a) + " "*nv + " " + mb[i] + "\n"
    return s


def prettifyMatrix(mat: list[list]) -> str:
    """Prettify and align a matrix"""

    s = ''
    ml = 0

    for r in mat:
        for c in r:
            if len(str(c)) > ml:
                ml = len(str(c))  # max length to center matrix values by

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if c == 0:
                s += "| "  # left border
            s += str(mat[r][c]).center(ml)  # actual values
            if c == len(mat[r]) - 1:
                s += " |"  # right border
            s += '  '
        s += '\n'

    return s[:-1]


def buildPartialMatrix(bind_r=-1, bind_c=-1):
    """
    Takes in user input and builds and returns a matrix and its solutions.\n
    Returns a tuple containing the number of rows in the matrix, number of columns, the matrix itself [A], and the solutions [b].
    Optionally binds the dimensions of the entered matrix using the controls `bind_r` to bind row length and 
    `bind_c` to bind column length. If the given row is longer than the bound value, an InvalidInputException is raised.
    """

    def valid_char(c):
        return c in valid_chars

    valid_chars = ["1", "2", "3", "4", "5",
                   "6", "7", "8", "9", "0", ".", "-", " "]

    try:
        cs = input("How many columns? ")
        check_exit(cs)
        if bind_c != -1:
            cs = bind_c
        rs = input("How many rows? ")
        check_exit(rs)
        if bind_r != -1:
            rs = bind_r

        cs = int(cs)
        rs = int(rs)

        mat = [[0 for _ in range(cs)] for _ in range(rs)]
        sltns = []

        for i in range(rs):
            eq = input(
                "Please enter line {} of your matrix, separated by spaces: ".format(i+1))
            if len(eq.split(' ')) != cs:
                raise Exception
            check_exit(eq)
            for j in range(len(eq)):
                if not (valid_char(eq[j])):
                    raise Exception
            mat[i] = list(map(float, eq.split(" ")))[:-1]
            sltns.append(list(map(float, eq.split(" ")))[-1])
    except ValueError as e:
        print(e, "\nInvalid matrix, please try again...")
        return

    return rs, cs, mat, sltns


def buildMatrix(bind_r=-1, bind_c=-1):
    """Build a full matrix using user input, with the expressions and solutions combined"""

    m = buildPartialMatrix(bind_c=bind_c, bind_r=bind_r)
    return m[0], m[1], combineMatrices(m[2], m[3])


def combineMatrices(a: list[list[int]], b: list[list[int]]):
    """Combine two matrices by adding each row in `b` to the row in `a`. Both `a` and `b` MUST have the same number of rows."""
    c = a
    for i in range(len(a)):
        c[i].append(b[i])
    return c


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
