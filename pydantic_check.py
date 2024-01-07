from pydantic import ValidationError
import pytest

def is_numeric(value):
    return isinstance(value, (int, float, complex))

def test_is_numeric():
    # Test with valid numeric values
    valid_values = [123, 45.67, 3+4j]
    for val in valid_values:
        try:
            model_instance = AnyValueModel(value=val)
            assert is_numeric(model_instance.value)
        except ValidationError:
            pytest.fail(f"Validation failed for valid numeric value: {val}")

    # Test with invalid values
    invalid_values = ["string", None, [1, 2, 3], {"a": 1}]
    for val in invalid_values:
        model_instance = AnyValueModel(value=val)
        assert not is_numeric(model_instance.value)

