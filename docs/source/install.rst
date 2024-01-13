.. _install:

Installation
=========================

This documentation shows how to install the Quadratic Equation Solver. The software is available under MIT-License.

Installation with whl-file:
-------------------------------------------

Download of whl-file:

.. raw:: html

    <style>
    .bold-code-block {
        font-family: monospace;
        background-color: #f0f0f0; /* typical code block background */
        display: block;
        padding: 10px;
        font-weight: bold;
    }
    </style>

.. rst-class:: bold-code-block

.. code-block:: text

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

.. code-block:: bash

    wget https://wetterwien22.at/projekte/QUEQSolver/QUEQSolver-1.0.0-py3-none-any.whl


The source archive (.tar.gz) can be downloaded with

.. raw:: html

    <style>
    .bold-code-block {
        font-family: monospace;
        background-color: #f0f0f0; /* typical code block background */
        display: block;
        padding: 10px;
        font-weight: bold;
    }
    </style>

.. rst-class:: bold-code-block

.. code-block:: text

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

.. code-block:: bash

    wget https://wetterwien22.at/projekte/QUEQSolver/QUEQSolver-1.0.0.tar.gz

To install run:

.. raw:: html

    <style>
    .bold-code-block {
        font-family: monospace;
        background-color: #f0f0f0; /* typical code block background */
        display: block;
        padding: 10px;
        font-weight: bold;
    }
    </style>

.. rst-class:: bold-code-block

.. code-block:: text

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


.. code-block:: bash

    pip install QUEQSolver-1.0.0-py3-none-any.whl

To uninstall use:

.. code-block:: bash

    pip uninstall QUEQSolver

Example for usage of the installed version:
First open the Python console:

.. code-block:: bash

    python

Then in the python console use the following commands to import and
run the Quadratic Equation Solver:

.. code-block:: python

    from QUEQSolver.qesolver import run_quadraticEQSolver
    run_quadraticEQSolver(1,2,3)

`Impressum <https://wetterwien22.at/impressum.html>`_
