.. _examples:

Examples
=========================

Example how to use the Quadratic Equation Solver

Basic Usage
-----------

Read the values directly from a file

.. code-block:: bash

    python qesolver.py -f values.txt

The following command is also possible. The program will try to read
from a file name in the same directory called values.txt as the hardcoded name is used, if no filename is specified

.. code-block:: bash

    python qesolver.py -f 

It is also possible to pass the coefficients directly from command-line.

.. code-block:: bash

    python qesolver.py 1 2 -3

If the script is executed without any arguments, it will promt the user during runtime for the coefficients

.. code-block:: bash

    python qesolver.py

Example of values.txt
---------------------

The file 'values.txt' must be of the following form. The first line is a header, which is skipped. Then each line represents one value and a comment can be added after the # symbol.
Please note: If a symbol is entered instead of a value, the program will evaluate symbolically.

.. code-block:: text

    # Input File:
    w   # value for a
    r   # value for b
    t   # value for c

This file uses numerical values for real case. In this case, a plot is possible.

.. code-block:: text

    # Input File:
    2   # value for a
    3   # value for b
    -5  # value for c

This file uses numerical values for complex case. There also a plot is possible.

.. code-block:: text

    # Input File:
    2   # value for a
    3   # value for b
    5   # value for c


Examples and Plots 
------------------
1. Symbolic Calculation
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python qesolver.py -f values.txt

Output:

.. code-block:: text

   reading values from file: values.txt
   values: a = w, b = r, c = t
   QUADRATIC EQUATION SOLVER:
   solving: w*x^2+r*x+t=0
   
   p = b/a = r/w
   q = c/a = t/w
   
   x^2+r/w*x+t/w=0                          /-t/w | on both sides
   x^2+r/w*x=-t/w                           /+(p/2)^2 | completing the square
   
   x^2 + 2*r/w/2*x + (r/w/2)^2 = (r/w/2)^2 - t/w | bionomial formula
   (x+r/w/2)^2 = (r/w/2)^2 - t/w            | sqrt() on both sides
   |x+r/w/2| = sqrt( (r/w/2)^2 - t/w )      | next solve absolute value
   x+r/w/2 = ±sqrt( (r/w/2)^2 - t/w )       / -r/w/2 | subtract p/2 from both sides
   x = -r/w/2 ± sqrt( (r/w/2)^2 - t/w )
   
   x1 = -0.5*(r + 2.0*(0.25*r**2 - t*w)**0.5)/w
   x2 = 0.5*(-r + 2.0*(0.25*r**2 - t*w)**0.5)/w

2. Quadratic Equation: Real Case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python qesolver.py -f values2.txt

Output:

.. code-block:: text

   reading values from file: values2.txt
   values: a = 2, b = 3, c = -5
   QUADRATIC EQUATION SOLVER:
   solving: 2*x^2+3*x+-5=0
   
   p = b/a = 1.5
   q = c/a = -2.5
   
   x^2+1.5*x+-2.5=0                         /--2.5 | on both sides
   x^2+1.5*x=2.5                            /+(p/2)^2 | completing the square
   
   x^2 + 2*1.5/2*x + (1.5/2)^2 = (1.5/2)^2 - -2.5 | bionomial formula
   (x+1.5/2)^2 = (1.5/2)^2 - -2.5           | sqrt() on both sides
   |x+1.5/2| = sqrt( (1.5/2)^2 - -2.5 )     | next solve absolute value
   x+1.5/2 = ±sqrt( (1.5/2)^2 - -2.5 )      / -1.5/2 | subtract p/2 from both sides
   x = -1.5/2 ± sqrt( (1.5/2)^2 - -2.5 )
   
   x1 = 1.00000000000000
   x2 = -2.50000000000000
   real

Plot:

.. image:: /_static/real.png
   :alt: real case - quadratic equation
   :width: 800px
   :align: center


3. Quadratic Equation: Complex Case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python qesolver.py -f values3.txt

Output:

.. code-block:: text

   reading values from file: values3.txt
   values: a = 2, b = 3, c = 5
   QUADRATIC EQUATION SOLVER:
   solving: 2*x^2+3*x+5=0
   
   p = b/a = 1.5
   q = c/a = 2.5
   
   x^2+1.5*x+2.5=0                          /-2.5 | on both sides
   x^2+1.5*x=-2.5                           /+(p/2)^2 | completing the square
   
   x^2 + 2*1.5/2*x + (1.5/2)^2 = (1.5/2)^2 - 2.5 | bionomial formula
   (x+1.5/2)^2 = (1.5/2)^2 - 2.5            | sqrt() on both sides
   |x+1.5/2| = sqrt( (1.5/2)^2 - 2.5 )      | next solve absolute value
   x+1.5/2 = ±sqrt( (1.5/2)^2 - 2.5 )       / -1.5/2 | subtract p/2 from both sides
   x = -1.5/2 ± sqrt( (1.5/2)^2 - 2.5 )
   
   x1 = -0.75 + 1.39194109070751*I
   x2 = -0.75 - 1.39194109070751*I
   complex

Plot:

.. image:: /_static/complex.png
   :alt: complex case - quadratic equation
   :width: 800px
   :align: center
