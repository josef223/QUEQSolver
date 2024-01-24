import sys
sys.path.append('../')
print (sys.path)

import tempfile
import os 
import pytest
import cmath
import QUEQSolver.qesolver as qe
import QUEQSolver.plotQE as qeplot
from QUEQSolver.qesolver import *

# Test function for quadraticEQSolver
def test_run_quadraticEQSolver():
    test_cases = [
        (1, 2, -3),  # Roots are 1 and -3
        (1, -3, 2),  # Roots are 1 and 2
        (1, 2, 1),   # One root, -1 (double root)
        (1, 0, -1),  # Roots are -1 and 1
        # test cases, for complex roots
        (1, 0, 1),   # Roots are complex: 0 + i and 0 - i
        (1, 2, 5),   # Roots are complex
        (complex(0,-1),complex(0.5,0.6),complex(0.3,0.1)),
    ]
    expected_results = [
        (1, -3),      # Roots are 1 and -3
        (1, 2),       # Roots are 1 and 2
        (-1, -1),     # One root, -1 (double root)
        (1, -1),      # Roots are -1 and 1
        (complex(0, 1), complex(0, -1)),  # Roots are complex: 0 + i and 0 - i
        (complex(-1, 2), complex(-1, -2)),# Roots are complex: -1 + 2i and -1 - 2i
	(complex(0.845533617126418,-0.662440210715484),complex(-0.245533617126418,0.162440210715484))
    ]
    
    for (a, b, c), (expected_x1, expected_x2) in zip(test_cases, expected_results):
        print(a, b, c)
        plotable, x1, x2, _, _, _ = qe.quadraticEQSolver(a, b, c)

        # Assertions to check if x1 and x2 are correct
        # Convert SymPy expressions to Python complex numbers
        if not isinstance(x1, (float, complex)):
            x1 = complex(x1)
            if not isinstance(x2, (float, complex)):
                x2 = complex(x2)

        # Comparisons
        if isinstance(expected_x1, complex) or isinstance(expected_x2, complex):
            assert cmath.isclose(x1.real, expected_x1.real, abs_tol=1e-6) and cmath.isclose(x1.imag, expected_x1.imag, abs_tol=1e-6)
            assert cmath.isclose(x2.real, expected_x2.real, abs_tol=1e-6) and cmath.isclose(x2.imag, expected_x2.imag, abs_tol=1e-6)
        else:
            assert pytest.approx(x1) == expected_x1 or pytest.approx(x1) == expected_x2
            assert pytest.approx(x2) == expected_x1 or pytest.approx(x2) == expected_x2

def test_read_file():
    # Create temporary file
    with open("test_values.txt", "w") as f:
        f.write("Header\n")
        f.write("1 # Text\n")
        f.write("2 # Text2\n")

    # Call the function
    result = read_file("test_values.txt")
    assert result == ['1', '2']

    # Clean up test file
    os.remove("test_values.txt")

from unittest.mock import patch
@patch('builtins.input', side_effect=['1', '2', '3'])
def test_inputValues_user_input(mock_input):
    with patch('sys.argv', ['script_name']):
        a, b, c = inputValues()
        assert a == '1' and b == '2' and c == '3'
@patch('sys.argv', ['script_name', '-f', 'test_values.txt'])
def test_inputValues_file_input():
 # Create a temporary test file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Header\n")
        temp_file.write("1 # Text\n")
        temp_file.write("2 # Text2\n")
        temp_file.write("3\n")
        temp_filename = temp_file.name

    # Mock sys.argv to simulate command-line arguments
    with patch('sys.argv', ['script_name', '-f', temp_filename]):
        a, b, c = inputValues()
        assert a == '1' and b == '2' and c == '3'
    # temporary file is automatically deleted

# Test with command line arguments
@patch('sys.argv', ['script_name', '1', '2', '3'])
def test_inputValues_cmd_args():
    a, b, c = qe.inputValues()
    assert a == '1' and b == '2' and c == '3'

from unittest.mock import patch, mock_open
@patch('sys.argv', ['script_name', '-f', 'nonexistent_file.txt'])
def test_inputValues_file_with_insufficient_data():
    # Mock the file open operation to return an empty content
    with patch('builtins.open', mock_open(read_data="")) as mock_file:
        with patch('builtins.print') as mock_print:
            qe.inputValues()
            # Use startswith to check if the print message starts with the expected string
            error_message_starts_with = "An unexpected error occurred: "
            assert any(error_message_starts_with in call_arg[0][0] for call_arg in mock_print.call_args_list)


# Test: GenericExceptionHandling
from unittest.mock import patch, MagicMock

@patch('QUEQSolver.qesolver.read_file', side_effect=Exception('Test error'))
@patch('sys.argv', ['script_name', '-f', 'values.txt'])
@patch('builtins.print')
def test_inputValues_generic_exception(mock_print, mock_read_file):
    qe.inputValues()
    mock_print.assert_called_with("An unexpected error occurred: Test error")

# run_quadraticEQSolver valid
@patch('QUEQSolver.qesolver.QEplot')
def test_run_quadraticEQSolver_valid(mock_plot):
    mock_plot.return_value = None 
    qe.run_quadraticEQSolver(1, -3, 2)
    mock_plot.assert_called_once()
    mock_plot.assert_called_with(1, -3, 2, 2, 1)

# run_quadraticEQSolver with complex inputs
from sympy import I, simplify, Abs
@patch('QUEQSolver.qesolver.QEplot')
def test_run_quadraticEQSolver_complex(mock_plot):
    mock_plot.return_value = None
    qe.run_quadraticEQSolver(complex(1, 1), complex(1, -1), complex(1, 0))
    mock_plot.assert_called_once()
    args, _ = mock_plot.call_args
    expected_args = (complex(1, 1), complex(1, -1), complex(1, 0),
                     0.275125261350169 + 1.40867701051199*I,
                     -0.275125261350169 - 0.408677010511985*I)
    tolerance = 1e-12
    for actual_arg, expected_arg in zip(args, expected_args):
        if isinstance(actual_arg, complex):
            assert actual_arg == expected_arg
        else:
            assert Abs(simplify(actual_arg - expected_arg)) < tolerance

# test with empty file:
def test_read_file_empty():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_filename = temp_file.name
    with pytest.raises(ValueError, match="The file does not have the expected format"):
        result = qe.read_file(temp_filename)
    os.remove(temp_filename)

# File not found test for file values.txt
@patch('sys.argv', ['script_name', '-f','t.txt'])
@patch('builtins.print')
def test_inputValues_invalid_file_arg(mock_print):
    qe.inputValues()
    # Expected message
    mock_print.assert_called_with('Error: The file values.txt was not found.')

# Testing reading from file
from unittest.mock import patch, MagicMock
# Test inputValues with '-f' flag and default 'values.txt' file
@patch('sys.argv', ['script_name', '-f'])
@patch('builtins.print')
@patch('QUEQSolver.qesolver.read_file', return_value=('1', '2', '3'))
def test_inputValues_default_file(mock_read_file, mock_print):
    a, b, c = qe.inputValues()
    # Check that read_file was called with 'values.txt'
    mock_read_file.assert_called_with('values.txt')
    # Verify the correct print statement was executed
    mock_print.assert_any_call('reading values from file: values.txt')
    # Check returned values
    assert a == '1' and b == '2' and c == '3'

# Testing main()
from unittest.mock import patch
@patch('QUEQSolver.qesolver.inputValues', return_value=('1', '2', '3'))
@patch('QUEQSolver.qesolver.quadraticEQSolver', return_value=(True, 'x1', 'x2', 'a', 'b', 'c'))
@patch('QUEQSolver.qesolver.QEplot')
def test_main(mock_qeplot, mock_quadratic_eq_solver, mock_input_values):
    qe.main()
    # Assert that these functions were called
    mock_input_values.assert_called_once()
    mock_quadratic_eq_solver.assert_called_once_with('1', '2', '3')
    mock_qeplot.assert_called_once_with('a', 'b', 'c', 'x1', 'x2')
