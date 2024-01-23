#QUEQSolver: Quadratic Equation Solver that prints all steps and plots the results
'''
- Values can be provided from command line by entering a, b, c as arguments
-  If argument -f is entered, the values are read from values.txt
- If it is started without an argument, the user input is started
- Also alphanumeric values can be entered as a value, not only float
- The final values are shown as an output

last modified: 4.11.2023
'''
import sys
###from QUEQSolver.calcStep import quadraticEQSolver
###from QUEQSolver.plotQE import QEplot

# Pydantic:
from pydantic import FilePath
from pydantic import BaseModel, field_validator, ConfigDict
from typing import Union

def read_file(filename: FilePath):
    '''
    Function reads values from the specified file

    Description:
        The first line is skipped because it contains the header. Then it  parses each line, splitting it by '#' and stripping off all additional whitespaces such that the numerical value can be extracted.

    Args:
        filename (FilePath): name of the file to read

    Returns:
        list: A list of values read from the file
    '''
    values=[]
    try:
        with open(filename, 'r') as file:
            next(file); #skip one line as header
            for line in file:
                number=line.split('#')[0].strip()
                values.append(number)
            return values
    except StopIteration:
        raise ValueError("The file does not have the expected format")
def inputValues():
    '''
    Read the input from file, command-line or keyboard input

    Description: 3 different input Methods:
         - If the 3 arguments are passed via command line, they are used
         - If the '-f' flag is passed with a filename, it reads the coefficient from the specified file
         - If there are no valid command-line inputs, it prompts the user to enter the coefficients manually.
         - It replaces 'i', 'I', or 'J' with 'j' to support different complex number notations
         - It is able to handle errors like 'file not found' or 'unexpected errors'

    Args:
        None

    Returns:
        tuple: containing three values (a,b,c) representing the coefficients of a quadratic equation
    '''
    try:
        if len(sys.argv) == 4:
            a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
        else:
            if len(sys.argv) == 2 and sys.argv[1]=='-f':
                print('reading values from file: values.txt')
                a, b, c = read_file('values.txt')
            elif len(sys.argv) == 3 and sys.argv[1]=='-f':
                filename = sys.argv[2]
                print(f'reading values from file: {filename}')
                a, b, c = read_file(filename)
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

####### Pydantic for run_quadraticEQSolver ########
class Coefficients(BaseModel):
    a: Union[str, float, int, complex]
    b: Union[str, float, int, complex]
    c: Union[str, float, int, complex]
    model_config = ConfigDict(arbitrary_types_allowed=True, extra='ignore')

def run_quadraticEQSolver(a,b,c):
    '''
    Function runs the quadratic equation solver directly

    Args:
        a, b, c (int, float, str, complex): input coefficients of the quadratic equation
    '''
    from QUEQSolver.calcStep import quadraticEQSolver
    from QUEQSolver.plotQE import QEplot
    coeffs = Coefficients(a=a, b=b, c=c)
    plotable,x1,x2,a,b,c=quadraticEQSolver(coeffs.a,coeffs.b,coeffs.c)
    if plotable:
        QEplot(a,b,c,x1,x2)

def main():
    [a,b,c]=inputValues()
    from os.path import dirname, abspath
    parent_dir=dirname(dirname(abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0,parent_dir)

    from QUEQSolver.calcStep import quadraticEQSolver
    from QUEQSolver.plotQE import QEplot

    plotable,x1,x2,a,b,c=quadraticEQSolver(a,b,c)
    if plotable:
        QEplot(a,b,c,x1,x2)

if __name__ == "__main__":
    main()

