
import os

f = open(os.path.join(os.path.dirname(__file__), '../input/8/part1.txt'), 'r')

registers = {}

def evaluate(condition):
    value = registers.get(condition['register'], 0)

    if condition['type'] == '==':
        return value == condition['value']
    elif condition['type'] == '!=':
        return value != condition['value']
    elif condition['type'] == '<':
        return value < condition['value']
    elif condition['type'] == '>':
        return value > condition['value']
    elif condition['type'] == '<=':
        return value <= condition['value']
    elif condition['type'] == '>=':
        return value >= condition['value']
    
def execute(expression):
    value = registers.get(expression['register'], 0)

    if expression['operation'] == 'inc':
        registers[expression['register']] = value + expression['value']
    elif expression['operation'] == 'dec':
        registers[expression['register']] = value - expression['value']
    
    return registers[expression['register']]

def main():

    maxValue = 0

    line = f.readline().rstrip()
    while line:
        parts = line.split(" ")

        expression = {
            'register': parts[0],
            'operation': parts[1],
            'value': int(parts[2]),
        }

        condition = {
            'register': parts[4],
            'type': parts[5],
            'value': int(parts[6]),
        }

        result = 0
        if (evaluate(condition)):
            result = execute(expression)

        if (result > maxValue):
            maxValue = result

        line = f.readline().rstrip()

    print(maxValue) 


if __name__ == '__main__':
       main()
