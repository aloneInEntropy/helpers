import time
import os
import sys

QUITS = ("q", "quit", "Q", "QUIT", "exit")

class Error(Exception):
    pass


class CancelOperation(Error):
    pass

class InvalidInputException(Error):
    """When the user enters an invalid input"""
    pass


def buildMatrix(qt=QUITS):
    """
        Takes in user input and builds and returns a matrix.\n
        Returns a list containing the number of rows in the matrix, number of columns, the matrix itself [A], and the solutions [b]
        """

    def check_exit(qs):
        if qs in qt:
            raise CancelOperation

    def valid_char(c):
        return c in valid_chars

    valid_chars = ["1", "2", "3", "4", "5",
                   "6", "7", "8", "9", "0", ".", "-", " "]
    rs = input("How many rows? ")
    check_exit(rs)
    cs = input("How many columns? ")
    check_exit(cs)

    try:
        mat = [[0 for _ in range(int(cs))] for _ in range(int(rs))]
        sltns = []

        for i in range(int(rs)):
            eq = input(
                "Please enter line {} of your matrix, separated by spaces: ".format(i+1))
            if len(eq.split(' ')) != int(cs):
                raise InvalidInputException
            check_exit(eq)
            for j in range(len(eq)):
                if not (valid_char(eq[j])):
                    print("Invalid character in matrix, please try again...")
                    raise InvalidInputException
            mat[i] = list(map(float, eq.split(" ")))[:-1]
            sltns.append(list(map(float, eq.split(" ")))[-1])
    except ValueError as e:
        print(e, "\nInvalid character, please try again...")
        time.sleep(1)
        sys.exit()
    
    

    return (rs, cs, mat, sltns)
