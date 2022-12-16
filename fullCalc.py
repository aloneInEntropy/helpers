from math import e, log
from time import sleep

def main():
    # test cases moved to other file, not yet included
    start()


def start():
    """Start and run the calculator"""
    
    quit = ("q", "quit", "Q", "QUIT", "exit")
    while True:
        # try:
        ui = input("Please enter your equation. Enter 'q' to quit." +
                   "\nUse exp(x) for any equations involving e = 2.718..." +
                   "\nUse log for any equations involving loge(x), where e = 2.718...\n\n")
        if ui in quit:
            print("Exiting...")
            sleep(1)
            break
        print(solve(ui))

valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
valid_ops = ["+", "-", "*", "/", "^"]
valid_chars = ["(", ")", "."]
order = [["+", "-"], ["*", "/"], ["^"]]
euler = str(e)  # euler = e = 2.718281828...
disp_power_disc = False # display power discrepancy (0^0 returns 1, but should return an error)
power_disc_msg = "NOTE: this is considered undefined on standard calculators."
# # maximum allowed amount of iterations before returning an error (e.g., "3(*4)")
# MAX_ITER = 100
# c_iter = 1


def isNum(a):
    return a >= '0' and a <= '9'


def check_op(num):
    """Get the precedence order of a specific operator"""
    return order[num-1]


def prec(op):
    """Get the precedence order of a specific operator"""
    match op:
        case "+" | "-":
            return 1
        case "*" | "/":
            return 2
        case "^":
            return 3
        case _:
            return -1  # shouldn't be reached if i'm actually good at programming


def sub_calc(a, b, op):
    global disp_power_disc
    match op:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a/b if b != 0 else None
        case "^":
            if a == 0 and b == 0:
                disp_power_disc = True  # display power discrepancy
                print(power_disc_msg)
            return a**b
        case _:
            return None  # shouldn't be reached due to validate()


def validate(eq: str) -> str:
    """Validate the expression `eq`\n          
    
    - -
    Parameters:
        - `(str) eq`: the expression to be validated
    - -
    Returns:
        - `(str)`: the response; whether or not the expression is valid
    - -
    Checks and returns a value based on whether or not the given expression is valid or not. 
    If is it valid, it returns the equation with '!' prefixed to it to indicate it passed.
    Otherwise, it returns an error message.
    """

    if eq == "":
        return "Invalid: Expressions cannot be empty"

    # check first character of expression
    if eq[0] in valid_ops and eq[0] != "-":
        return "Invalid: Can only have number or \"-\" (negative) at beginning of expression"

    if eq.count('(') > eq.count(')'):
        return "Invalid: Unclosed expression"
    if eq.count('(') < eq.count(')'):
        return "Invalid: Parenthesis closed before opening"

    if eq[-1] in valid_ops and not eq[-1] == ")":
        return "Invalid: Cannot end expression with an operator"

    # check for too many adjacent instances of operators
    i = 0
    while i < len(eq):
        # check every character invidually now
        # "+-*-+" is invalid, but also "+++" or "---"
        if eq[i] in valid_ops and eq[i+1] in valid_ops:
            if not eq[i+1] in ('+', '-'):
                return "Invalid: Consecutive operator not '+' or '-'"
            if eq[i+2] in valid_ops:
                return "Invalid: Can't have more than three operators in a row"
        if eq[i] == ".":
            if (i == 0 or i == len(eq) - 1) or (isNum(eq[i-1]) and not isNum(eq[i+1])):
                return "Invalid: Illegal position for decimal point (.)"
        if i < len(eq) - 1 and eq[i] == ")" and isNum(eq[i+1]):
            return "Invalid: Number after parenthesis has no preceeding operator"
        if i < len(eq) - 1 and eq[i] == "(" and eq[i+1] in valid_ops and eq[i+1] != '-':
            return "Invalid: Parenthesis cannot start with an operator"
        if i > 0 and eq[i] == ")" and eq[i-1] in valid_ops:
            return "Invalid: Parenthesis cannot end with an operator"
        if i < len(eq) - 1 and eq[i] == "(" and eq[i+1] == ")":
            return "Invalid: Empty parentheses"
        if i < len(eq) - 3:
            if eq[i:i+3] in ("exp", "log"):
                t_op = eq[i:i+3]
                if not eq[i+3] == "(":
                    return "Invalid: Unary operator " + t_op + " must enclose its parameter in brackets (e.g. " + t_op + "(4))"
                i += 3  # continue past "exp(" or "log("
                if eq[i+1] == ")":
                    return "Invalid: Empty parentheses"
        if eq[i] not in valid_nums and eq[i] not in valid_ops and eq[i] not in valid_chars:
            return "Invalid: Contains invalid character: \"" + eq[i] + "\""

        i += 1

    return "!" + eq


def solve(eq: str, dp=3) -> str:
    """Solves the equation `eq`. `dp` refers to how many decimal points are to be shown, defaulting to 3.\n          
    
    - -
    Parameters:
        - `(str) eq`: expression to be solved
        - `(int) dp = 3`: decimal places to use (optional)
    - -
    Returns:
        - `(str)`: the result of the given expression
    - -
    This function deals with parentheses by picking the innermost pair and performing `calc()` on its contents,
    returning the answer to the same string. This is repeated until no parentheses are left. `calc()` is performed once 
    more at the end to account for a lack of parentheses in the total equation.
    
    e.g.: 8/7^2+5*(8-3)
    `solve()` starts by finding the first closed bracket [")"] and moving backwards until it finds its opening pair. From there, it takes the substring within 
    the bracket and calculates it using `calc()`.
    
    `calc()` takes the substring equation (`eq`) and `normalise()`s it, making it easier to use with the rest of `calc()`. In this case, it takes the '8-3' and
    checks for a character ahead of the '-'. It finds nothing, so it replaces the '-' with '+-' to force the algorithm into accepting that '3' is negative. 
    This makes no difference here, but for an equation such as '8-3*4', '3' would be taken to be negative, which would be wrong.
    
    Next, the function splits up the equation into lists of numbers and operators. 
    It sees the '-' and recognises that the value ahead of it, namely '3', is negative, and so adds the index of '3' to a list of values to update as negative 
    later (neg_pos). As `normalise()` replaced the '-' with '+-', there is still a '+' remaining in the string, which is added to the list of operators. Then, 
    all operators are removed from the equation string itself, including brackets, so that it can be split up into numbers. Before it is split up however, the 
    character '-' is added to the each index in neg_pos to mark the following number as negative. Finally, the string is split up by the commas added when 
    removing operators into a list of numbers. The operators were removed by replacing them with commas, but the parentheses were removed outright, with no 
    replacements.
    
    Finally, the actual calculation is performed. Going by BIMDAS/BODMAS/PEMDAS (whichever you prefer), the equation is iterated over by finding the highest 
    precedence operator and performing a binary calculation using that operator on the two values either side of it. It then removes the two values from nums 
    (the list of numbers) and the operator from ops (the list of operators) and places the new result in nums at the position of the first value used in the 
    calculation. That is, for example,
        - nums = [3, 4, 5]
        - ops = [+, *]
        - a = 4, b = 5, op = '*'
        - res = 20
        - nums = [3, 20]
        - ops = [+]
    
    and repeat. This is performed until there is only one value left in nums, which is then returned. The emptiness of ops is assumed due to `validate()` 
    having been performed already before calling `calc()`.
    In the case of our example, the returned result is 5, which is placed back into eq, which now looks like this:
    
        8/7^2+5*5
    
    Note that the parentheses are removed. Now, as there are no more parentheses left, the entire equation is entered into `calc()` a final time, just to 
    ensure that no calculation is left undone. The same steps as above are performed, with the calculation finding all operators with precedence 3 ('^') and 
    performing their calculations first, then precedence 2, then precedence 1.  Any operators of equal precedence are used as found (left to right). The 
    details of this are laid out as follows:
        - nums = [8, 7, 2, 5, 5]
        - ops = [/, ^, +, *]
        - prec = 3, so op = ^
        - a = 7, b = 2, op = '^'
        - res = 49
        - -
        - nums = [8, 49, 5, 5]
        - ops = [/, +, *]
        - prec = 2, so op ~= ['*', '/']
        - a = 8, b = 49, op = '/'
        - res = 0.163...
        - -
        - nums = [0.163, 5, 5]
        - ops = [+, *]
        - prec = 2, so op ~= ['*', '/']
        - a = 5, b = 5, op = '*'
        - res = 25
        - -
        - nums = [0.163, 25]
        - ops = [+]
        - prec = 1, so op ~= ['+', '-']
        - a = 0.163, b = 25, op = '+'
        - res = 25.163...
        - -
        - nums = [25.163]
        - ops = []
        - -
        => result is 25.163...
    When exp and log are used, the procedure is slightly different but still generally the same. 
        - When exp is found, the string "exp" is simply replaced with the value of `e`, Euler's constant, and '^', the power operator.
        - When log is found, the calculation is performed immediately, before the main calculation of the equation string, due to log having no binary 
        operator equivalent. The result is then placed back into the string, replacing log, and the function resumes as normal.
        
    One final caveat is the event in which the equation contains a substring similar to 'a-b^c'. It was stated above that 'b' should be made to be negative in 
    the case of '8-3*4', but given that '^' is the highest precedence operator, the numbers it uses must be prioritised over negation. As a result, any 
    substring 'a-b^c' does not pre-negate the value 'b' to avoid misinterpreting the equation.   
    """

    eq = eq.replace(" ", "")  # remove whitespace
    eq = validate(eq)
    if eq[0] != "!":
        return eq

    eq = eq[1:]
    i = 0
    p = i
    while i < len(eq) and "(" in eq and ")" in eq:
        while i < len(eq) and eq[i] != ")":
            i += 1
        p = i
        while i >= 0 and eq[p] != "(":
            p -= 1

        # to parse x(y)
        if p > 0 and isNum(eq[p-1]):
            eq = eq[:p] + "*" + eq[p:]
            p += 1
            i += 1

        small_eq = eq[p+1:i]

        ans = calc(small_eq)
        ahead = eq[i+1:]
        i = p + len(ans)
        eq = eq[:p] + ans + ahead

    # Recurse through the equation if there are still parenthesis in it
    if "(" in eq and ")" in eq:
        eq = solve(eq, dp=dp)

    # format output based on whether or not it is a decimal number
    final = calc(eq)
    if "." in final:
        return "{:.{prec}f}".format(float(final), prec=dp)
    else:
        return final


def normalise(eq: str) -> str:
    """Normalises the expression `eq`\n          
    
    - -
    Parameters:
        - `(str) eq`: the expression to be normalised
    - -
    Returns:
        - `(str)`: the result of the normalisation, which may or may not have passed
    - -
    Takes in a valid equation and normalises it, allowing it to work with `calc()`
    """

    for i in range(len(eq)):
        if i < len(eq) - 3:
            if eq[i:i+3] in ("exp", "log"):
                if i > 0 and isNum(eq[i-1]):
                    eq = eq[:i] + "*" + eq[i:]
                    i += 1
            if "exp" in eq[i:i+3]:
                # exp must use a minimum of 6 characters (e.g. len("exp(a)") == 6)
                eq = eq[:i] + euler + "^" + eq[i+3:]
                i += len(euler)
            if "log" in eq[i:i+3]:
                # log must use a minimum of 6 characters (e.g. len("log(a)") == 6)
                # replace the calculation of the current log(x) and put it back in this string
                p = i
                while p < len(eq) and eq[p] not in valid_ops:
                    p += 1
                try:
                    # horrible, but necessary
                    eq = eq[:i] + str(log(float(calc(eq[i+3:p])))) + eq[p:]
                except:
                    return "Invalid: log must be positive real number"
                
    if eq.find("--") == 0:
        eq = eq[1:]

    teq = eq[0]
    i = 0
    while i < len(eq):
        c = eq[i]
        p = ""
        if i != 0:
            if c == "-" and eq[i+1].isalnum() and eq[i-1].isalnum():
                # given an equation x - y * z, the program will assume y to be positive when multplying.
                # this loop takes any negative value and, as long as it isn't at the beginning, changes it from
                # - to +-
                # to make the program recognise that the value should be assumed to be negative rather than positive.
                # e.g., a - b = a + (-b) = a+-b
                # additionally, the order of precedence must be accounted for, so the value will NOT be negated if
                # the operator in front of it is the exponent
                # e.g., a-b^c = a - (b^c).
                q = i+1
                while q < len(eq) and (eq[q].isalnum() or eq[q] == "."):
                    q += 1
                if q != len(eq) and eq[q] != "^":
                    p = "+-"
                else:
                    p += c
            elif eq[i] == "+" and eq[i+1] == "+":
                # a ++ b == a + b, but a +++ b = invalid
                # it technically still counts when entered into an actual calculator,
                # but it is prohibited here based on the rules in `validate()`
                # w = i
                # while eq[w+1] == c:
                #     w += 1
                # i = w
                p = c
                i += 1
            else:
                # else just add it like a regular character
                p = c
        teq += p
        i += 1

    return teq


def calc(equation: str) -> str:
    """Separates the expression into two arrays, calculates the expression and returns the result.\n          
    
    - -
    Parameters:
        - `(str) equation`: the expression to be calculated
    - -
    Returns:
        - `(str)`: the result of the calculation, which may or may not have passed
    - -
    The algorithm forms two arrays, one with the values to be calculated with, and one with
    the operators. It then collapses the `nums` array by applying each operator in `ops` according to the 
    order of precedence laid out by the array `oper`. It then returns the last and only value in the array, as all
    other values have since been removed.  
    """

    nums = []  # numbers in equation
    ops = []  # operators in equation
    neg_pos = []  # positions to negate characters

    # normalise eq to allow it to work with the rest of this function
    eq = normalise(equation)
    if eq[0] == 'I':
        return eq

    # eq is now the equation to be worked from to avoid side effects
    for i in range(len(eq)):
        c = eq[i]
        if c in valid_ops:
            # if the current char is an operator (not a number)
            if i == 0:
                if c == "-":
                    neg_pos.append(0)
            elif eq[i-1] in valid_ops:
                # if the current and prev chars are negative operators, then this one must be negated
                neg_pos.append(i)
            elif c in valid_chars:
                continue
            else:
                # otherwise this is an operator
                ops.append(c)

    # remove all operators
    nums = eq.replace("+", ",").replace("-", ",").replace("*", ",")
    nums = nums.replace("^", ",").replace("/", ",")
    nums = nums.replace("(", "").replace(")", "")

    # for each value to be negated, replace the character at that position with '-'
    for i in range(len(nums)):
        if i in neg_pos:
            nums = nums[:i] + "-" + nums[i+1:]

    # split string by comma delimiter, leaving negative values in
    nums = nums.split(",")
    p_o = len(order)  # precedence orderer

    # actual calculation
    # calculate all adjacent values left to right, write result in left position, and remove right value
    
    try:
        while len(nums) > 1:
            while p_o > 0:
                # if the set of operators in the equation has at least one of the operators at the current precedence
                # in other words, while the equation can stay at the current precedence...
                while not set(ops).isdisjoint(check_op(p_o)):
                    i = 0
                    while i < len(ops):
                        if ops[i] in check_op(p_o):
                            a = float(nums[i]) if "." in nums[i] else int(nums[i])
                            b = float(nums[i+1]) if "." in nums[i+1] else int(nums[i+1])
                            nums[i+1] = None
                            c = sub_calc(a, b, ops[i])
                            if c == None:
                                return "Invalid: Division by zero"
                            nums[i] = str(c)
                            # break
                            [nums.remove(p) for p in nums if p == None]
                            del ops[i]
                            i -= 1  # operator was removed from string, so index is decreased
                        i += 1  # if operator wasn't removed, continue
                p_o -= 1  # decrease precedence orderer
    except ValueError:
        return "Invalid: Result too large"

    return nums[0]


if __name__ == '__main__':
    main()
