import sys
sys.path.append('../')

import pytest
import cmath
from QUEQSolver.plotQE import *

def test_quadratic():
    assert quadratic(2, 1, -3, 2) == pytest.approx(0)

def test_complex_quadratic():
    assert complex_quadratic(1+2j, 1, -3, 2) == pytest.approx(-4 - 2j)

from unittest.mock import MagicMock, patch
@patch('matplotlib.pyplot.figure')
@patch('matplotlib.pyplot.subplot')
@patch('matplotlib.pyplot.imshow')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.colorbar')
@patch('matplotlib.pyplot.scatter')
@patch('matplotlib.pyplot.axhline')
@patch('matplotlib.pyplot.axvline')
@patch('matplotlib.pyplot.grid')
@patch('matplotlib.pyplot.legend')
@patch('matplotlib.pyplot.savefig')
@patch('matplotlib.pyplot.show')
def test_plotComplexPlane(mock_show, mock_savefig, mock_legend, mock_grid, mock_axvline, mock_axhline, mock_scatter, mock_colorbar, mock_title, mock_ylabel, mock_xlabel, mock_imshow, mock_subplot, mock_figure):
    plotComplexPlane(1, -3, 2)

    mock_figure.assert_called()
    mock_subplot.assert_called()
    mock_imshow.assert_called()
    mock_xlabel.assert_called_with('Real Part')


@patch('matplotlib.pyplot.figure')
@patch('matplotlib.pyplot.plot')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.axhline')
@patch('matplotlib.pyplot.axvline')
@patch('matplotlib.pyplot.grid')
@patch('matplotlib.pyplot.legend')
@patch('matplotlib.pyplot.scatter')
@patch('matplotlib.pyplot.savefig')
@patch('matplotlib.pyplot.show')
def test_plotReal(mock_show, mock_savefig, mock_scatter, mock_legend, mock_grid, mock_axvline, mock_axhline, mock_ylabel, mock_xlabel, mock_title, mock_plot, mock_figure):
    plotReal(1, -3, 2, 1, -2)

    mock_figure.assert_called()
    mock_plot.assert_called()
    mock_title.assert_called()


@patch('QUEQSolver.plotQE.plotReal')
@patch('QUEQSolver.plotQE.plotComplexPlane')
def test_QEplot(mock_plotComplexPlane, mock_plotReal):
    from sympy import sympify
    QEplot(1, -3, 2, sympify(1),sympify(-2))  # Real roots
    mock_plotReal.assert_called_with(1, -3, 2, 1, -2)

    QEplot(1, -3, 2, sympify(1+2j), sympify(1-2j))  # Complex roots
    mock_plotComplexPlane.assert_called_with(1, -3, 2)
