# Iris' Helpers

A place where I (plan to) store files that help with annoying, exhaustive or otherwise tedious mathematical or programming tasks that would require a lot of writing or typing out. A general-purpose calculator. My IGPC. .py. hell yeah

Files added currently:
  - Gauss-Seidel iterative solver (gaussSeidel.py)
    - Takes in a matrix by input and prints out the steps for each iteration to the console, where they can be copied easily.
  - Calculator (fullCalc.py)
    - Takes in an expression by keyboard and solves it. Works with brackets, loge(x) and e^x expressions
    - Also has an accompanying GUI, in calcGUI.py
  - Basic Power Method (bpm.py)
    - Takes in 2 matrices by input and calculates the largest eigenvalue, and prints out the values at each iteration.
  - Inverse Power Method (ipm.py)
    - Takes in 2 matrices by input and calculates the smallest eigenvalue, and prints out the values at each iteration.
  - Matrix Multiplier (matrixMult.py)
    - Takes in 2 matrices and multiplies them, printing out the result
  - Main Hub (IGPC.py)
    - The hub for the other calculators, currently CLI only
    - Allows the user to access calcGUI.py
   

Planned:
  - LU decomposition via Crout's method
  - Best fit with least squares
    - A graphing utility (using numpy) for a future GUI
  - GUIs for other screens
