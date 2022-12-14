"""Auxiliary code. Contains custom functions and exceptions."""

import time
# import sys

QUITS = ("q", "quit", "exit")
GAP = "  "


class Error(Exception):
    """Basic class."""
    pass


class CancelOperation(Error):
    """To exit out of a module without exiting the overall program."""
    pass


class InvalidInputException(Error):
    """When the user enters an invalid input according to whatever the used function dictates."""
    pass


def check_exit(qs: str):
    """Check if a given string is an exit string\n          
    
    - -
    Parameters:
        - `(str) qs`: quit string
    """

    if qs.lower() in QUITS:
        raise CancelOperation


def buildPartialMatrix(bind_r=-1, bind_c=-1) -> tuple[int, int, list[list[int]], list[int]]:
    """Takes in user input and builds and returns a matrix and its solutions.\n          
    
    - -
    Parameters:
        - `bind_r = -1`: the amount of rows the matrix must have. if -1, no binds are placed. (optional)
        - `bind_c = -1`: the amount of columns the matrix must have. if -1, no binds are placed. (optional)
    - -
    Returns:
        - `(tuple[int, int, list[list[int]], list[int]])`:  
            - `int`: the number of rows 
            - `int`: the number of colums
            - `list[list[int]]`: the expression matrix [A]
            - `list[int]`: the solution matrix [b]
    - -
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
                raise InvalidInputException
            check_exit(eq)
            for j in range(len(eq)):
                if not (valid_char(eq[j])):
                    raise InvalidInputException
            mat[i] = list(map(float, eq.split(" ")))[:-1]
            sltns.append(list(map(float, eq.split(" ")))[-1])
    except ValueError as e:
        print(e, "\nInvalid matrix, please try again...")
        time.sleep(1)
        return

    return rs, cs, mat, sltns


def buildMatrix(bind_r=-1, bind_c=-1):
    """Takes in user input and builds and returns a matrix combined with its solutions.\n          
    
    - -
    Parameters:
        - `bind_r = -1`: the amount of rows the matrix must have. if -1, no binds are placed. (optional)
        - `bind_c = -1`: the amount of columns the matrix must have. if -1, no binds are placed. (optional)
    - -
    Returns:
        - `(tuple[int, int, list[list[int]]])`:  
            - `int`: the number of rows 
            - `int`: the number of colums
            - `list[list[int]]`: the equation matrix [A]
    - -
    Returns a tuple containing the number of rows in the matrix, number of columns, and the matrix itself [A].
    Optionally binds the dimensions of the entered matrix using the controls `bind_r` to bind row length and 
    `bind_c` to bind column length. If the given row is longer than the bound value, an InvalidInputException is raised.  
    """

    m = buildPartialMatrix(bind_c=bind_c, bind_r=bind_r)
    return m[0], m[1], combineMatrices(m[2], m[3])


def combineMatrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """Combine two matrices by adding each row in `b` to the row in `a`.\n          
    
    - -
    Parameters:
        - `(list[list[int]]) a`: matrix a
        - `(list[list[int]]) b`: matrix b
    - -
    Returns:
        - `(list[list[int]])`: the appended matrix a:b
    - -
    Combine two matrices by adding each row in `b` to the row in `a`. Both `a` and `b` MUST have the same number of rows. 
    This is not checked for, so be wary.
    """
    c = a
    for i in range(len(a)):
        c[i].append(b[i])
    return c


def prettifyMatrix(mat: list[list]) -> str:
    """Prettify and align a matrix\n          
    
    - -
    Parameters:
        - `(list[list]) mat`: matrix to be prettified
    - -
    Returns:
        - `(str)`: prettified matrix as a newline-separated string
    """

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


def transitionMatrices(a: list[list[int]], b: list[list[int]], v="", label_a="", label_b="") -> str:
    """Create a transition between matrix `a` and `b` during a normalisation.\n          
    
    - -
    Parameters:
        - `(list[list[int]]) a`: the matrix `a`
        - `(list[list[int]]) b`: the matrix `b`
        - `(str) v = ""`: the result value label (optional)
        - `(str) label_a = ""`: label for matrix `a` (optional)
        - `(str) label_b = ""`: label for matrix `b` (optional)
    - -
    Returns:
        - `(str)`: the series of transitions during the normalisation
    - -
    `label_a` adds a label to the vector multiplied by `a`, and `label_b` adds a label to the resulting vector. `v` 
    is the resulting value from the normalisation, but must be passed through like the labels.  
    """
    
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


def distanceToValueInMatrix(mat: list[list[int]], target: int) -> list[list[int]]:
    """Given a matrix, return a normalised matrix of the same dimensions with distances to the nearest specified value\n          
    
    - -
    Parameters:
        - `(list[list[int]]) mat`: the input matrix
        - `(int) target`: the values to judge proximity to
    - -
    Returns:
        - `(list[list[int]])`: a matrix with the same dimensions as `mat`, where every cell is either 0, or the distance to the 
        nearest 0 (where `target` is in `mat`)
    """
    
    paths = [[[] for _ in range(len(mat[0]))] for _ in range(len(mat))]

    nm = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    r, c = 0, 0

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == target:
                nm[r][c] = 0
            else:
                nm[r][c] = updateClosestDistance(nm, r, c)

    for r in range(len(mat)-1, -1, -1):
        for c in range(len(mat[r])-1, -1, -1):
            if mat[r][c] == target:
                nm[r][c] = 0
            else:
                nm[r][c] = updateClosestDistance(nm, r, c)

    return nm


def updateClosestDistance(mat: list[list[int]], r: int, c: int) -> int:
    """Get the smallest value surrounding the point `(r, c)`\n          
    
    - -
    Parameters:
        - `(list[list[int]]) mat`: the matrix containing the specified point
        - `(int) r`: the row the point is in
        - `(int) c`: the column the point is in
    - -
    Returns:
        - `(int)`: the updated distance between the given point and all adjacent points
    - -
    Given a matrix and point (r, c), return the smallest value surrounding the point + 1, and -1 if all values are -1
    """

    adj = []

    # below
    if r >= 0:
        if len(mat) > 1 and r < len(mat) - 1:
            if mat[r+1][c] != -1:
                adj.append(mat[r+1][c])

    # right
    if c >= 0:
        if len(mat[r]) > 1 and c < len(mat[r]) - 1:
            if mat[r][c+1] != -1:
                adj.append(mat[r][c+1])

    # left
    if c <= len(mat[0]) - 1:
        if len(mat[r]) > 1 and c >= 1:
            if mat[r][c-1] != -1:
                adj.append(mat[r][c-1])

    # above
    if r <= len(mat) - 1:
        if len(mat) > 1 and r >= 1:
            if mat[r-1][c] != -1:
                adj.append(mat[r-1][c])

    # above-right
    if r <= len(mat) - 1 and c >= 0:
        if len(mat) > 1 and r >= 1 and c < len(mat[r]) - 1:
            if mat[r-1][c+1] != -1:
                adj.append(mat[r-1][c+1])

    # above-left
    if r <= len(mat) - 1 and c <= len(mat[0]) - 1:
        if len(mat) > 1 and r >= 1 and c >= 1:
            if mat[r-1][c-1] != -1:
                adj.append(mat[r-1][c-1])

    # below-right
    if r >= 0 and c >= 0:
        if len(mat) > 1 and r < len(mat) - 1 and c < len(mat[r]) - 1:
            if mat[r+1][c+1] != -1:
                adj.append(mat[r+1][c+1])

    # below-left
    if r >= 0 and c <= len(mat[0]) - 1:
        if len(mat) > 1 and r < len(mat) - 1 and c >= 1:
            if mat[r+1][c-1] != -1:
                adj.append(mat[r+1][c-1])

    if len(adj) == 0:
        return -1
    return min(adj) + 1


def printMatrix(mat: list[list[int]]):
    """Print a matrix line by line (unprettified)\n          
    
    - -
    Parameters:
        - `(list[list[int]]) mat`: matrix to be prettified
    """

    for i in mat:
        print(i)
