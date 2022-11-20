"""Matrix multiplier."""


from numpy import dot

QUITS = ("q", "quit", "exit")


def main():
    start()


def start():
    print("Please enter the first matrix.")
    a = buildMatrix()[-1]  # matrix a
    print("Please enter the second matrix.")
    b = buildMatrix()[-1]  # matrix b

    print(dot(a, b))


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


def check_exit(qs: str):
    """Check if a given string is an exit string"""

    if qs.lower() in QUITS:
        raise Exception


if __name__ == '__main__':
    main()
