import fullCalc as fc
import calcGUI as gfc
import gauss_seidel as gs
import matrixMult as mm
import bpm as pm
from auxi import *


intro_txt = """
To start, please select a calculator mode [1-4]:
    1. General Calculator
    2. Gauss-Seidel Matrix Iterator
    3. Matrix Multiplier
    4. Basic Power Method Iterator
Or enter 'q' to quit.
"""


def main():
    print("Welcome to my General-Purpose Calculator!")

    while True:
        print(intro_txt)
        clc_mode = input()
        try:
            clc_mode = int(clc_mode)
        except:
            if clc_mode in QUITS:
                print("Exiting...")
                break
            print("Invalid option")
            continue
        match clc_mode:
            case 1:
                op1 = True
                while op1:
                    tans = input("Start in GUI mode? [y/n] ")
                    match tans.lower():
                        case "y"| "yes":
                            gfc.start()
                            op1 = False
                        case "n"| "no":
                            fc.start()
                            op1 = False
                        case _:
                            print("Invalid answer, please try again")
            case 2:
                try:
                    gs.start()
                except SystemExit:
                    continue
            case 3:
                mm.start()
            case 4:
                pm.start()
            case _:
                print("Invalid choice, please try again")


if __name__ == '__main__':
    main()
