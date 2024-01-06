# plotQE: plot the quadratic equation and results
# last modified: 4.11.2023
'''
plotQE: 

plot the quadratic equation and results

Args:
a (datatype)
b (datatype)
c (datatype)
x1 (datatype)
x2 (datatype)

Returns:


'''

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def quadratic(x, a, b, c):
    '''
    Function calculates the value of the quadratic equation for a given x value

    Args:
    x (float): given value, for which the quadratic equation is evaluated
    a, b, c (float): Coefficients of the quadratic equation
    
    Returns:
    float: The solution of the quadratic equation for the given value x
    '''
    a=float(a); b=float(b); c=float(c)
    return a * x**2 + b * x + c

def complex_quadratic(z,a,b,c):
    '''
    Function calculates the quadratic equation for a given complex number

    Args:
    z (complex): complex number as input for which the quadratic equation is solved
    a, b, c (complex): Coefficients of the quadratic equation

    Returns:
    complex: value of the quadratic equation at the given complex number z
    '''
    return a * z**2 + b * z + c

def plotComplexPlane(a,b,c):
    '''
    Function plots the phase and roots of a quadratic eqation with complex coefficients

    Args:
    a, b, c (complex): Coefficients of the quadratic equation

    Description:
    Generates a heatmap of the phase of the quadratic equation while using a complex grid. It also plots the complex roots of the equation.
    '''
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
    plt.title('Complex Roots of the Quadratic Equation')
    plt.show()

def plotReal(a,b,c,x1,x2):
    '''
    Plots the real roots of a quadratic equation

    Args:
    a, b, c (float): Coefficients of the quadratic equation
    x1, x2 (float): Real roots of the quadratic equation

    Description:
    Plots the quadratic curve and marks the real roots on the plot
    '''
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
    plt.show()
    
def QEplot(a,b,c,x1,x2):
    '''
    Function decides on the roots if a real or a complex quadratic equation is plotted

    Args:
    a, b, c (float or complex): Coefficients of the quadratic equation
    x1, x2 (float or complex): Roots of the quadratic equation

    Description:
    Determines if the roots are real or complex and call then the appropriate plot function (plotReal or plotComplex)
    '''
    if (x1.is_real and x2.is_real):  
        print('real')
        a=float(a.real); b=float(b.real); c=float(c.real)
        plotReal(a,b,c,x1,x2)  # if both numbers are real      
    else:
        print('complex')
        #print(type(x1))
        plotComplexPlane(a,b,c)
        
