def additions(line: str) -> str:
    line = line.split(' ')
    return int(line[0]) + int(line[1])


def subtraction(line: str) -> str:
    line = line.split(' ')
    return int(line[0]) - int(line[1])


def multiplication(line: str) -> str:
    line = line.split(' ')
    return int(line[0]) * int(line[1])


def division(line: str) -> str:
    line = line.split(' ')
    return int(line[0]) / int(line[1])


with open('pairs.txt', 'r') as f, open('answer.txt', 'w') as g:
    for line in f:
        a = input('Pick one operation with pairs ' + line.strip() + "\n")
        if a == '+':
            g.write("+ " + str(additions(line)) + "\n")
        elif a == '-':
            g.write("- " + str(subtraction(line)) + "\n")
        elif a == '*':
            g.write("* " + str(multiplication(line)) + "\n")
        elif a == '/':
            g.write("/ " + str(division(line)) + "\n")
