from decimal import Decimal

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def precedence(operator):
    if (operator == "("):
        return 0
    elif (operator == "+" or operator == "-"):
        return 1
    else:
        return 2

def to_infix(string):
    if (string.count("(") != string.count(")")):
        return "ERROR"

    newstr = ""
    for index, char in enumerate(string):
        if (char == "x"):
            newstr += "*"
        elif (char == "(" and index < len(string) - 1 and string[index + 1] == ")"):
            return "ERROR"
        elif (char.isnumeric() and index < len(string) - 1 and string[index + 1] == "("):
            newstr += (char + "*")
        elif (char == ")" and index < len(string) - 1 and (string[index + 1].isnumeric() or string[index + 1] == "(" or string[index+1] == ".")):
            newstr += (char + "*")
        elif (char == "-" and (string[index + 1].isnumeric() or string[index + 1] == "(" or string[index+1] == ".")):
            newstr += "n"
        elif (char != " "):
            newstr += char

    string = ""
    stack = []
    for char in newstr:

        if (char == "("):
            stack.append("")
        elif (char == ")"):
            result = stack.pop()
            if (is_number(result) == False):
                result = "(" + result + ")"
            if (len(stack) > 0):
                stack[-1] += result
            else:
                string += result
        elif (len(stack) > 0):
            stack[-1] = stack[-1] + char
        else:
            string += char


    return string

def to_postfix(string):
    if string == "ERROR":
        return ["ERROR"]

    q = []
    stack = []
    num = ""

    for char in string:
        if (char.isdecimal() or char == "." or char == "n"):
            num += char
        else:
            if (num != ""):
                if (num[0] == "n"):
                    num = "-" + num[1:]
                q.append(num)
            num = ""
            if (char == "("):
                stack.append(char)
            elif (char == ")"):
                while (len(stack) > 0 and stack[-1] != "("):
                    q.append(stack.pop())
                if (len(stack) > 0):
                    stack.pop()
            else:
                while (len(stack) > 0 and precedence(stack[-1]) >= precedence(char)):
                    q.append(stack.pop())
                stack.append(char)

    if (num != ""):
        if (num[0] == "n"):
            num = "-" + num[1:]
        q.append(num)
    while (len(stack) > 0):
        q.append(stack.pop())

    return q

def to_result(arr):
    if (arr[0] == "ERROR"):
        return arr[0]

    stack = []
    for element in arr:
        if (element == "."):
            return "ERROR"
        if (is_number(element)):
            stack.append(element)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if (element == "+"):
                stack.append(Decimal(num2) + Decimal(num1))
            elif (element == "-"):
                stack.append(Decimal(num2) - Decimal(num1))
            elif (element == "*"):
                stack.append(Decimal(num2) * Decimal(num1))
            elif (element == "/"):
                if (Decimal(num1) == Decimal('0')):
                    return "UNDEFINED"
                stack.append(Decimal(num2) / Decimal(num1))
            
    return float(Decimal(stack[0]))