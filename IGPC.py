import fullCalc as fc
import gauss_seidel as gs
import matrixMult as mm

intro_txt = """
To start, please select a calculator mode [1-3]:
    1. General Calculator
    2. Gauss-Seidel Matrix Iterator
    3. Matrix Multiplier
Or enter 'q' to quit.
"""


def main():
    print("Welcome to my General-Purpose Calculator!")

    quit = ("q", "quit", "Q", "QUIT", "exit")

    while True:
        print(intro_txt)
        clc_mode = input()
        try:
            clc_mode = int(clc_mode)
        except:
            if clc_mode in quit:
                print("Exiting...")
                break
            print("Invalid option")
            continue
        match clc_mode:
            case 1:
                fc.start()
            case 2:
                try:
                    gs.start()
                except SystemExit:
                    continue
            case 3:
                print("(In development!)")
            case _:
                print("Invalid choice, please try again")


if __name__ == '__main__':
    main()
