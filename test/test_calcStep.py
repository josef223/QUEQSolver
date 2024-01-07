import sys
sys.path.append('../')

import pytest
import cmath
from calcStep import *

def test_is_numeric():
    assert is_numeric(5) == True
    assert is_numeric(3.14) == True
    assert is_numeric(2 + 3j) == True
    assert is_numeric("string") == False
    assert is_numeric(None) == False

def test_is_numeric_or_complex():
    assert is_numeric_or_complex(5) == True
    assert is_numeric_or_complex(3.14) == True
    assert is_numeric_or_complex(2 + 3j) == True
    assert is_numeric_or_complex("3+2j") == True
    assert is_numeric_or_complex("string") == False
    assert is_numeric_or_complex(None) == False

def test_quadraticEQSolver():
    # test cases: coefficients and expected results
    test_cases = [
        ((1, -3, 2), (True, 1, 2)),
        ((1, 2, 1), (True, -1, -1)),
        ((1, 0, -1), (True, 1, -1)),
    ]

    for coeffs, expected in test_cases:
        a, b, c = coeffs
        expected_plotable, expected_x1, expected_x2 = expected

        plotable, x1, x2, returned_a, returned_b, returned_c = quadraticEQSolver(a, b, c)

        assert plotable == expected_plotable
        assert x1.evalf() == pytest.approx(expected_x1) or x1.evalf() == pytest.approx(expected_x2)
        assert x2.evalf() == pytest.approx(expected_x2) or x2.evalf() == pytest.approx(expected_x1)
        assert (returned_a, returned_b, returned_c) == coeffs
