"""Gauss-Seidel matrix iterator. An iterative method of solving a system of linear equations."""

import sys
import time


def main():
    start()


def start():
    print(
        "Welcome to Iris' Gauss-Seidel matrix iterator!\n" +
        "Please don't make any mistakes; there's very little error checking going on here.\n" +
        "Also, please ensure that your matrix is diagonally dominant (https://en.wikipedia.org/wiki/Diagonally_dominant_matrix) before continuing.\n" +
        "Please include the solution too.\n"
    )
    gs_input()  # gauss-seidel user interface


valid_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-", " "]
mat = []
QUITS = ("q", "quit", "exit")


def valid_char(char):
    return char in valid_chars


def check_exit(qs: str):
    """Check if a given string is an exit string"""

    if qs.lower() in QUITS:
        raise Exception


def check_dd(mat):
    """Check if the given matrix is diagonally dominant"""
    for r in range(len(mat)):
        s = 0
        for c in range(len(mat[r])):
            s += abs(mat[r][c])
        s -= abs(mat[r][r])
        if abs(mat[r][r]) < s:
            return False
    return True


def gs_input():
    while True:
        print("Enter \"q\" at any point to quit.")

        try:
            try:
                _, cs, mat, sltns = buildPartialMatrix()
            except Exception:
                print("Invalid input, please try again.")
                continue

            if not check_dd(mat):
                print(
                    "\nWARNING: Your matrix is not diagonally dominant and may not converge.\n")
            else:
                print("\nYour matrix is diagonally dominant and will converge.\n")

            iters = input("How many iterations? ")
            check_exit(iters)
            iters = int(iters)

            # dp = input("How many decimal places? ")
            # if dp == exit_string:
            #     break
            # dp = int(dp)

            ig = input("Initial Guesses(x1 x2 ... xn)? (\"n\" for 0s) ")
            check_exit(ig)
            if ig == "n" or ig == "N":
                ig = []
                for _ in range(int(cs)):
                    ig.append(0)
            else:
                for i in range(len(ig)):
                    if not (valid_char(ig[i])):
                        print("Invalid character in guesses, restarting...")
                        time.sleep(1)
                        sys.exit()
                ig = list(map(float, ig.split(" ")))
        except ValueError as e:
            print(e, "\nInvalid character, restarting...")
            time.sleep(1)
            sys.exit()
        except IndexError as e:
            print(e, "\nInvalid matrix dimensions, restarting...")
            time.sleep(1)
            continue

        gauss_seidel(mat, ig, sltns, iters)


def gauss_seidel(a, x, b, iters):
    """Take in a matrix `a`, initial guesses `x`, and the solutions `b` to the matrix `a`, and print out a formatted layout of its calculation with `iters` iterations."""

    a2 = ""
    # calculation, taken from https://www.geeksforgeeks.org/gauss-seidel-method/
    for it in range(iters):
        for r in range(len(a)):
            a2 = ""
            # for each row in the matrix
            p = b[r]
            for c in range(len(a[r])):
                if (r != c):
                    p -= a[r][c] * x[c]
                    a2 += "{:.3f}".format(a[r][c]) + \
                        "*" + "{:.3f}".format(x[c]) + " + "
            x[r] = p / a[r][r]  # answer

            # output string
            if r == 0:
                print("k = " + str(it+1) + ":", sep='',
                      end='')  # iteration number
            print("\tx" + str(r+1) +
                  " = (" +
                  "{:.3f}".format(b[r]) +
                  " - (" +
                  a2[:-3] +  # remove last " + "
                  ")) / " +
                  "{:.3f}".format(a[r][r]) +
                  " = " +
                  "{:.3f}".format(x[r]))
        print()  # newline


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
        time.sleep(1)
        return

    return rs, cs, mat, sltns


if __name__ == '__main__':
    main()
