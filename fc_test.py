from fullCalc import *

def tformat(eq, dp=3):
    """Format equation output for testing"""
    
    return '{:.{prec}f}'.format(float(eq), prec=dp)

# Testing isNum method
def test_isNum():
    assert isNum('%') == False
    assert isNum('/') == False
    assert isNum('*') == False
    assert isNum('+') == False

    assert isNum('1') == True
    assert isNum('8') == True
    assert isNum('0') == True
    assert isNum('3.56') == True


# Testing prec method
def test_prec():
    assert prec("+") == 1
    assert prec("-") == 1
    assert prec("*") == 2
    assert prec("/") == 2
    assert prec("^") == 3
    assert prec("%") == -1
    assert prec("exp") == -1
    assert prec("log") == -1

#Testing check_op method
def test_check_op():
    assert check_op(1) == ["+", "-"]
    assert check_op(2) == ["*", "/"]
    assert check_op(3) == ["^"]

# Testing calc method
def test_calc():
    ts_1 = "1+2"
    ts_2 = "0*0"
    ts_3 = "100-100-1001"
    ts_4 = "3*3-1"
    ts_5 = "0+4*0*180+1"
    ts_6 = "8*2-4*4"
    ts_7 = "-1-2*-3+-1000*0+3"
    ts_8 = "3*3*3*3*3*3*-3*-3*-3"
    ts_9 = "1/2/3"
    ts_10 = "5^7^3"
    assert calc(ts_1) == '3'
    assert calc(ts_2) == '0'
    assert calc(ts_3) == '-1001'
    assert calc(ts_4) == '8'
    assert calc(ts_5) == '1'
    assert calc(ts_6) == '0'
    assert calc(ts_7) == '8'
    assert calc(ts_8) == '-19683'
    assert tformat(calc(ts_9)) == '0.167'
    assert calc(ts_10) == '476837158203125'
    
    assert calc('10/2') == '5.0'
    assert calc('4*2-3+5') == '10'
    assert calc('2+3-1') == '4'
    assert calc('3^2') == '9'
    assert calc('3+4^2') == '19'
    assert calc('9/3-8^2+5') == '-56.0'
    assert tformat(calc('3.456+3')) == '6.456'

    assert calc('4+3*4-1') == "15"
    assert calc('21/3') == "7.0"
    assert calc('2^3') == "8"
    assert calc('9++8') == "17"
    assert calc('3--1') == "4"

    assert calc('2^19237') == "Invalid: Result too large"
    assert calc('3/0') == "Invalid: Division by zero"
    assert calc('20*2/0') == "Invalid: Division by zero"

def test_solve():
    assert solve("(1+2+3)") == '6'
    assert solve("(1+2+3)+(2-3)") == '5'
    assert solve("((4+2+3)+(2-4)^4)") == '25'
    
    assert tformat(solve('log(5)')) == "1.609"
    assert tformat(solve('exp(4)')) == "54.598"
    assert solve('(3*4)+3') == "15"
    assert tformat(solve('(log(3)+4)-2')) == "3.099"
    assert tformat(solve('3+5*exp(4.2)/(5+7)')) == "30.786"
    assert tformat(solve('(12.344754 + 5) * exp(4)')) == "946.991"
    assert tformat(solve('(634.4982938 - 45.19283473) + log(8)')) == "591.385"
    assert tformat(solve("log(3*(exp(6)))")) == '7.099'
    assert tformat(solve("log(3*(exp(6/100)))")) == '1.159'
    assert tformat(solve("1/exp(3*(exp(6/100)))", 6), 6) == '0.041357'
    assert tformat(solve("1/exp(3*(exp(6/100)))")) == '0.041'
    assert tformat(solve("exp(4+5)", 5), dp=5) == '8103.08393'
    assert tformat(solve("8/7^2+5*(8-3)")) == '25.163'
    assert tformat(solve("log(5-(log(10-(log(15+1)))))")) == '1.106'
    assert tformat(solve("exp(5-(exp(10-(exp(15+1)))))")) == '148.413'
    assert tformat(solve("4log(293)")) == '22.721'
    assert tformat(solve("10exp(10)")) == '220264.658'
    
    assert solve("10exp10") == "Invalid: Unary operator exp must enclose its parameter in brackets (e.g. exp(4))"
    assert solve("10log10") == "Invalid: Unary operator log must enclose its parameter in brackets (e.g. log(4))"
    assert solve("(3*(1--exp(4))-10))") == 'Invalid: Parenthesis closed before opening'

# Testing sub_calc
def test_sub_calc():
    assert sub_calc(4, 6, "*") == 24
    assert sub_calc(102, 3, "/") == 34
    assert sub_calc(4, 0, "/") == None
    assert sub_calc(4, 6, "-") == -2
    assert sub_calc(4, 6, "+") == 10
    assert sub_calc(4, 6, "^") == 4096
    assert sub_calc(4.25, 8, "+") == 12.25
    assert sub_calc(6.0, 54.367, "*") == 326.202
    assert sub_calc(4, 9, "%") == None


# Testing validate method
def test_validate():
    assert(validate('3+4-1.')) == "Invalid: Illegal position for decimal point (.)"
    assert(validate('.')) == "Invalid: Illegal position for decimal point (.)"
    assert(validate('4..5')) == "Invalid: Illegal position for decimal point (.)"
    assert(validate('+3+4^2')) == "Invalid: Can only have number or \"-\" (negative) at beginning of expression"
    assert(validate('5*3+')) == "Invalid: Cannot end expression with an operator"
    assert(validate('4&5-2')) == "Invalid: Contains invalid character: \"&\""
    assert(validate('3*4+++2')) == "Invalid: Can't have more than three operators in a row"
    assert(validate('5+9-2+*)')) == "Invalid: Parenthesis closed before opening"
    assert(validate('8+9**2')) == "Invalid: Consecutive operator not '+' or '-'"
    assert(validate('3+--3')) == "Invalid: Can't have more than three operators in a row"
    assert(validate('5-+-98')) == "Invalid: Can't have more than three operators in a row"
    assert(validate('.2+7')) == "Invalid: Illegal position for decimal point (.)"
    assert(validate('45+4.')) == "Invalid: Illegal position for decimal point (.)"
    assert(validate('3+5.&')) == "Invalid: Illegal position for decimal point (.)"
    assert(validate('7---3')) == "Invalid: Can't have more than three operators in a row"
    assert(validate('8+++4')) == "Invalid: Can't have more than three operators in a row"
    assert(validate('(3+5)5')) == "Invalid: Number after parenthesis has no preceeding operator"
    assert(validate('(+4-1)+4')) == "Invalid: Parenthesis cannot start with an operator"
    assert(validate('((6/2)-3*)')) == "Invalid: Parenthesis cannot end with an operator"
    assert(validate('()')) == "Invalid: Empty parentheses"
    assert(validate('log4')) == "Invalid: Unary operator log must enclose its parameter in brackets (e.g. log(4))"
    assert(validate('exp3.5')) == "Invalid: Unary operator exp must enclose its parameter in brackets (e.g. exp(4))"
    assert(validate('exp()')) == "Invalid: Empty parentheses"
    assert(validate('log()')) == "Invalid: Empty parentheses"
    assert(validate("log(r)")) == "Invalid: Contains invalid character: \"r\""
    assert(validate('(12.344754 + 5) * exp(5)')) == "Invalid: Contains invalid character: \" \""
    assert(validate('(634.4982938 - 45.19283473) + log(9)')) == "Invalid: Contains invalid character: \" \""

   
    assert(validate('4+3*4-1')) == "!4+3*4-1"
    assert(validate('21/3')) == "!21/3"
    assert(validate('2^3')) == "!2^3"
    assert(validate('9++8')) == "!9++8"
    assert(validate('3--1')) == "!3--1"
    assert(validate('log(5)')) == "!log(5)"
    assert(validate('exp(4)')) == "!exp(4)"
    assert(validate('(3*4)+3')) == "!(3*4)+3"
    assert(validate('(log(3)+4)-2')) == "!(log(3)+4)-2"
    assert(validate('3+5*exp(4.2)/(5+7)')) == "!3+5*exp(4.2)/(5+7)"

def test_normalise():
    assert normalise('exp(69)') == euler + '^(69)'
    assert normalise('exp(10+294)') == euler + '^(10+294)'
    assert normalise('exp()') == euler + '^()'
    assert normalise('exp') == "exp"
    assert tformat(normalise('log(4)')) == "1.386"
    assert tformat(normalise('log(exp(5))')) == "5.000"
    assert normalise('log()') == "Invalid: log must be positive real number"
    assert normalise('log(0)') == "Invalid: log must be positive real number"
    assert normalise('log(-1)') == "Invalid: log must be positive real number"
    assert normalise('log(-18329043245.4245)') == "Invalid: log must be positive real number"
    assert normalise('log') == "log"
    
    assert normalise('1++3') == "1+3"
    assert normalise('1+++++3') == "1+++3"
    assert normalise('1-3*3') == "1+-3*3"
    assert normalise('1--3') == "1--3"
    assert normalise('1-3^3') == "1-3^3"
    
    assert normalise('1') == "1"
