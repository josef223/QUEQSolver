''' QUEQSolver

Quadratic Equation Solver that prints all steps and plots the results

Args:
 a (array): variable
Returns:
'''
# QUEQ Solver: Quadratic Equation Solver that prints all steps and plots the results
# last modified: 4.11.2023

# Input:
# Values can be provided from command line by entering a, b, c as arguments
# If argument -f is entered, the values are read from values.txt
# If it is started without an argument, the user input is started
# Also alphanumeric values can be entered as a value, not only float
# The final values are shown as an output

import sys
from calcStep import quadraticEQSolver
from plotQE import QEplot

def read_file(filename):
    values=[]
    with open(filename, 'r') as file:
        next(file); #skip one line as header
        for line in file:
            number=line.split('#')[0].strip()
            values.append(number)
    return values

def inputValues():
    '''
    input
    
    Read the input from file, command-line or keyboard input
    
    Args:
    
    Returns:

    '''

    try:
        if len(sys.argv) == 4:
            a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
        else:
            if len(sys.argv) == 2 and sys.argv[1]=='-f':
                print('reading values from file: values.txt')
                a, b, c = read_file('values.txt')
            else:
                print('use -f command to read values from file')
                print('less than 3 arguments provided in command line: starting input\n')
                print('user input:')
                a = input("a = ")
                b = input("b = ")
                c = input("c = ")
        a = a.replace('i', 'j').replace('I', 'j').replace('J', 'j')
        b = b.replace('i', 'j').replace('I', 'j').replace('J', 'j')
        c = c.replace('i', 'j').replace('I', 'j').replace('J', 'j')
        print(f"values: a = {a}, b = {b}, c = {c}")
        return a,b,c
    # Print error messages:
    except FileNotFoundError as e:
        print("Error: The file values.txt was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

[a,b,c]=inputValues()
plotable,x1,x2,a,b,c=quadraticEQSolver(a,b,c)
if plotable:
    QEplot(a,b,c,x1,x2)

# input = main file
# print step
# plot
