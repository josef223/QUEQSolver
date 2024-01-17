# plotQE: plot the quadratic equation and results
# last modified: 4.11.2023

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from pydantic import BaseModel, ConfigDict
from typing import Union, List
###################################### Pydantic
class QuadraticParameters(BaseModel):
    x: Union[float, List[float]]
    a: float
    b: float
    c: float
###############################################

def quadratic(x, a, b, c):
    '''
    Function calculates the value of the quadratic equation for a given x value

    Args:
       x (Union[float, List[float]]): given value or list, for which the quadratic equation is evaluated
       a, b, c (float): Coefficients of the quadratic equation

    Returns:
       float: The solution of the quadratic equation for the given value x
    '''

    params = QuadraticParameters(x=x, a=a, b=b, c=c)

    if isinstance(params.x, list):
        return [params.a * xi**2 + params.b * xi + params.c for xi in params.x]
    else:
        return params.a * params.x**2 + params.b * params.x + params.c
###################################### Pydantic
class ComplexParameters(BaseModel):
    z: Union[float,complex, List[complex]]
    a: Union[float,complex]
    b: Union[float,complex]
    c: Union[float,complex]
    model_config = ConfigDict(arbitrary_types_allowed=True, extra='ignore')

def complex_quadratic(z,a,b,c):
    '''
    Function calculates the quadratic equation for a given complex number

    Args:
       z (Union[float,complex]): complex number as input for which the quadratic equation is solved
       a, b, c (complex): Coefficients of the quadratic equation

    Returns:
       complex: value of the quadratic equation at the given complex number z
    '''
    #return a * z**2 + b * z + c

    if isinstance(z, np.ndarray):
        # Directly handle the NumPy array case
        return a * z**2 + b * z + c
    else:
        # Use Pydantic validation for non-array inputs
        params = ComplexParameters(z=z, a=a, b=b, c=c)
        return params.a * params.z**2 + params.b * params.z + params.c
####################################### Pydantic
class QuadraticCoefficients(BaseModel):
    a: Union[int,float,complex]
    b: Union[int,float,complex]
    c: Union[int,float,complex]
    model_config = ConfigDict(arbitrary_types_allowed=True, extra='ignore')

def plotComplexPlane(a,b,c):
    '''
    Function plots the phase and roots of a quadratic eqation with complex coefficients

    Description:
        Generates a heatmap of the phase of the quadratic equation while using a complex grid. It also plots the complex roots of the equation.

    Args:
       a, b, c (Union[int, float, complex]): Coefficients of the quadratic equation
    '''
    coeffs = QuadraticCoefficients(a=a, b=b, c=c)
    a, b, c = coeffs.a, coeffs.b, coeffs.c

    # Generate a grid of complex numbers
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    # Calculate the discriminant
    a=complex(a); b=complex(b); c=complex(c)
    D = b**2 - 4*a*c
    # Calculate the two roots using the quadratic formula
    root1 = (-b - np.lib.scimath.sqrt(D)) / (2*a)
    root2 = (-b + np.lib.scimath.sqrt(D)) / (2*a)

    # Complex roots: real and imaginary parts
    # Calculate the phase of the output
    phase = np.angle(complex_quadratic(Z,a,b,c))

    # Heatmap plot of the phase
    plt.figure(figsize=(12, 6))
    plt.subplot(1,2,1)
    phase_map = plt.imshow(phase, extent=(x.min(), x.max(), y.min(), y.max()), origin='lower', cmap='hsv') #hsv
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.title('Heatmap: Phase of the Quadratic Equation')
    plt.colorbar(phase_map)

    plt.subplot(1,2,2)
    plt.scatter(root1.real, root1.imag, color='red', zorder=5, label='Complex Root 1')
    plt.scatter(root2.real, root2.imag, color='blue', zorder=5, label='Complex Root 2')
    plt.axhline(0, color='black', linewidth=0.5)  # Add y=0 axis
    plt.axvline(0, color='black', linewidth=0.5)  # Add x=0 axis
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.grid(True)
    plt.legend()
    plt.title('Complex Roots of the Quadratic Equation\n'+f'{a}*x^2 + {b}*x + {c} = 0')
    plt.savefig('quadratic_roots.png')
    plt.show()


################################### Pydantic
class RealQuadraticParameters(BaseModel):
    a: Union[int,float]
    b: Union[int,float]
    c: Union[int,float]
    x1: Union[int,float]
    x2: Union[int,float]

def plotReal(a,b,c,x1,x2):
    '''
    Plots the real roots of a quadratic equation

    Description:
       Plots the quadratic curve and marks the real roots on the plot

    Args:
       a, b, c (Union[int, float]): Coefficients of the quadratic equation
       x1, x2 (Union[int, float]): Real roots of the quadratic equation
    '''
    params = RealQuadraticParameters(a=a, b=b, c=c, x1=x1, x2=x2)
    a, b, c, x1, x2 = params.a, params.b, params.c, params.x1, params.x2

    x = np.linspace(-10, 10, 400)
    y = quadratic(x, a, b, c)

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, label=f'{a}*x^2 + {b}*x + {c} = 0')
    plt.title('Quadratic Equation Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)  # Add y=0 axis
    plt.axvline(0, color='black', linewidth=0.5)  # Add x=0 axis
    plt.grid(True)
    plt.legend()
    plt.scatter([x1, x2], [0, 0], color='red', zorder=5, label='roots')
    plt.savefig('quadratic_roots.png')
    plt.show()

class QuadraticEquationParameters(BaseModel):
    a: Union[float, complex]
    b: Union[float, complex]
    c: Union[float, complex]
    x1: sp.Expr  # Assuming x1 and x2 are SymPy expressions
    x2: sp.Expr
    model_config = ConfigDict(arbitrary_types_allowed=True, extra='ignore')

def QEplot(a,b,c,x1,x2):
    '''
    Function decides on the roots if a real or a complex quadratic equation is plotted

    Description:
       Determines if the roots are real or complex and call then the appropriate plot function (plotReal or plotComplex)

    Args:
       a, b, c (Union[float, complex]): Coefficients of the quadratic equation
       x1, x2 (SymPy Expr): Roots of the quadratic equation 
    '''
    params = QuadraticEquationParameters(a=a, b=b, c=c, x1=x1, x2=x2)
    if params.x1.is_real and params.x2.is_real:
        print('real')
        plotReal(params.a, params.b, params.c, params.x1, params.x2)  # if both numbers are real
    else:
        print('complex')
        plotComplexPlane(params.a, params.b, params.c)
