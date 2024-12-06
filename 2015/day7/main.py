wires = {}

def evaluateStatement(statement: str):

    expression, variable = statement.split(" -> ")

    expression = " ".join([f"wires['{i}']" if i.isalpha() and i not in ["LSHIFT","AND","NOT","RSHIFT","OR"] else i for i in expression.split(" ")])
    fixedExpression = expression.replace("LSHIFT","<<").replace("AND","&").replace("NOT ", "0xFFFF^").replace("RSHIFT",">>").replace("OR","|")
    print(fixedExpression)
    wires[variable] = eval(fixedExpression)

with open("2015/day7/text.txt") as file:
    lines = file.read().split("\n")
    for line in lines:
        evaluateStatement(line)
    