# Calculate quadratic eqation, step by step and print all steps
# last modified: 4.11.2023

import numpy as np
import sympy as sp

def is_numeric(value):
    '''
    Function to check if the value is numeric (int, float or complex)

    Args:
        value (any type): input variable that is checked, any type

    Returns:
        bool: True if value is numeric (int, float or complex)
    '''
    return isinstance(value, (int, float, complex))

def is_numeric_or_complex(value):
    '''
    Function checks if a value can be converted to a complex number

    Args:
        value (any type): input variable that is checked, any type

    Returns:
        bool: True if the value can be converted to complex datatype
    '''
    
    try:
        complex(value)
    except ValueError:
        # The conversion failed, so it's not a numeric input
        return False
    else:
        # The conversion succeeded, so it's a numeric input
        return True
    
def quadraticEQSolver(a,b,c):
    '''
    Function solved a quadratic equation and prints all steps

    Args:
        a, b, c (numeric or string): input coefficients of the quadratic equation

    Returns:
        tuple: A tuple containing a boolean if the equation is plotable, the roots x1 and x2 as well as the coefficients a, b, c
    '''
    # Assign values as strings
    #a=5; b=8; c=3
    #a=1; b=3; c=8
    #a=1; b='p'; c='q'
    print('QUADRATIC EQUATION SOLVER:')
    #c=1+2j ####################
    print(f'solving: {a}*x^2+{b}*x+{c}=0\n')

    # Calculate p and q using sympy for symbolic computation
    a_sym, b_sym, c_sym = sp.symbols('a b c')
    p = b_sym / a_sym
    q = c_sym / a_sym

    # Create symbolic expressions for p and q
    p_expr = p.subs({a_sym: a, b_sym: b})
    q_expr = q.subs({a_sym: a, c_sym: c})

    plotable=False
    if (is_numeric_or_complex(a) and is_numeric_or_complex(b) and is_numeric_or_complex(c)):
        a=complex(a); b=complex(b); c=complex(c)
        if a.imag==0 and b.imag==0 and c.imag==0:
            a=float(a.real); b=float(b.real); c=float(c.real)
        p=b/a; q=c/a
        p_expr=p
        q_expr=q
        plotable=True

    print(f'p = b/a = {p_expr}')
    print(f'q = c/a = {q_expr}\n')

    # Printing the expressions
    tab=40
    YELLOW = '\033[93m'; RESET = '\033[0m'
    print(f'x^2+{p_expr}*x+{q_expr}=0'.ljust(tab), f'{YELLOW}/-{q_expr} | on both sides{RESET}')
    print(f'x^2+{p_expr}*x={-q_expr}'.ljust(tab), f'{YELLOW}/+(p/2)^2 | completing the square\n{RESET}')

    print(f'x^2 + 2*{p_expr}/2*x + ({p_expr}/2)^2 = ({p_expr}/2)^2 - {q_expr}'.ljust(tab),f'{YELLOW}| bionomial formula{RESET}')
    print(f'(x+{p_expr}/2)^2 = ({p_expr}/2)^2 - {q_expr}'.ljust(tab), f'{YELLOW}| sqrt() on both sides{RESET}')
    print(f'|x+{p_expr}/2| = sqrt( ({p_expr}/2)^2 - {q_expr} )'.ljust(tab), f'{YELLOW}| next solve absolute value{RESET}')
    print(f'x+{p_expr}/2 = \u00B1sqrt( ({p_expr}/2)^2 - {q_expr} )'.ljust(tab), f'{YELLOW}/ -{p_expr}/2 | subtract p/2 from both sides{RESET}')
    print(f'x = {-p_expr}/2 \u00B1 sqrt( ({p_expr}/2)^2 - {q_expr} )\n')

    # Evaluate the quadratic equation for x1 and x2
    x_sym = sp.symbols('x')
    equation = sp.Eq(x_sym**2 + p_expr*x_sym + q_expr, 0)
    solutions = sp.solve(equation, x_sym)
    x2, x1 = solutions

    print(f'x1 = {x1.evalf()} \nx2 = {x2.evalf()}')
    return plotable,x1,x2,a,b,c

