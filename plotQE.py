# plotQE: plot the quadratic equation and results
# last modified: 4.11.2023

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def quadratic(x, a, b, c):
    a=float(a); b=float(b); c=float(c)
    return a * x**2 + b * x + c

def complex_quadratic(z,a,b,c):
    return a * z**2 + b * z + c

def plotComplexPlane(a,b,c):
    # Generate a grid of complex numbers
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    # Calculate the discriminant
    a=complex(a); b=complex(b); c=complex(c)
    D = b**2 - 4*a*c
    # Calculate the two roots using the quadratic formula
    # Use `numpy.lib.scimath.sqrt` to correctly handle the square root of negative numbers
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
    if (x1.is_real and x2.is_real):  
        print('real')
        a=float(a.real); b=float(b.real); c=float(c.real)
        plotReal(a,b,c,x1,x2)  # if both numbers are real      
    else:
        print('complex')
        #print(type(x1))
        plotComplexPlane(a,b,c)
