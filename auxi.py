"""Auxiliary code. Contains custom functions and exceptions."""

import time
# import sys

QUITS = ("q", "quit", "exit")


class Error(Exception):
    """Basic class."""
    pass


class CancelOperation(Error):
    """To exit out of a module without exiting the overall program."""
    pass


class InvalidInputException(Error):
    """When the user enters an invalid input according to whatever the used function dictates."""
    pass


def check_exit(qs:str):
    """Check if a given string is an exit string"""
    
    if qs.lower() in QUITS:
        raise CancelOperation


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


def combineMatrices(a: list[list[int]], b: list[list[int]]):
    """Combine two matrices by adding each row in `b` to the row in `a`. Both `a` and `b` MUST have the same number of rows."""
    c = a
    for i in range(len(a)):
        c[i].append(b[i])
    return c


def buildMatrix(bind_r=-1, bind_c=-1):
    """Build a full matrix using user input, with the expressions and solutions combined"""

    m = buildPartialMatrix(bind_c=bind_c, bind_r=bind_r)
    return m[0], m[1], combineMatrices(m[2], m[3])


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
