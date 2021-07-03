import re

def arrange(list, solve = False):
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in list:
        if(re.search("[^\s0-9.+-]", problem)):
            if(re.search("[/]", problem) or re.search("[*]")):
                print("Operator must be + or -")
            print("Enter digits only")

        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
            print("Numbers cannot be more than 4 digits")
        
        sum = ""
        if(operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        else:
            sum = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = ""
        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"
        
        if(problem != list[-1]):
            first += top + "    "
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom 
            lines += line
            sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    print(string)
        
arrange(["300 + 90", "300 - 90", "60 + 9", "72 - 3"], True)