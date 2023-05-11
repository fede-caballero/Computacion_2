#!/usr/bin/env python3
import getopt
import sys

def calculate(operation, num1, num2):
    if operation == "mas":
        return num1 + num2
    elif operation == "por":
        return num1 * num2
    elif operation == "menos":
        return num1 - num2
    elif operation == "sobre":
        if num2 > 0:
            return num1 / num2
        else:
            raise ValueError("Invalid operation")

def main(argv):
    operation = ''
    num1 = 0
    num2 = 0

    try:
        opts, args = getopt.getopt(argv, "o:n:m:")
    except getopt.GetoptError:
        print('calculator.py -o <operation> -n <num1> -m <num2>')
        sys.exit(2) #Codigo de salida de error en el procesamiento de los argumentos de linea de comando

    for opt, arg in opts:
        if opt == '-o':
            operation = arg
        elif opt == '-n':
            num1 = int(arg)
        elif opt == '-m':
            num2 = int(arg)
    
    try:
        result = calculate(operation, num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(e)
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])

