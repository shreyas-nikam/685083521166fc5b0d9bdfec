import pytest
from definition_40601a87688f499da1ab9afe2c25af8d import calculate_sharpe_ratio

@pytest.mark.parametrize("returns, risk_free_rate, std_dev, expected", [
    (0.10, 0.02, 0.05, 1.6),
    (0.15, 0.05, 0.10, 1.0),
    (0.08, 0.03, 0.04, 1.25),
    (0.05, 0.05, 0.10, 0.0),
    (0.02, 0.05, 0.05, -0.6),
    (0.10, 0.0, 0.05, 2.0),
    (0.0, 0.0, 0.1, 0.0),
    (-0.10, 0.05, 0.10, -1.5),
    (0.10, 0.05, 0.01, 5.0),
    (0.10, 0.05, 0.001, 50.0),

    # Edge cases
    (0.0, 0.0, 0.0, ZeroDivisionError),
    (0.1, 0.0, 0.0, ZeroDivisionError),
    (0.0, 0.1, 0.0, ZeroDivisionError),
    (0.1, 0.1, 0.0, ZeroDivisionError),

    # Type Errors
    ("a", 0.02, 0.05, TypeError),
    (0.10, "b", 0.05, TypeError),
    (0.10, 0.02, "c", TypeError),
    (None, 0.02, 0.05, TypeError),
    (0.10, None, 0.05, TypeError),
    (0.10, 0.02, None, TypeError),
])
def test_calculate_sharpe_ratio(returns, risk_free_rate, std_dev, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_sharpe_ratio(returns, risk_free_rate, std_dev)
    else:
        try:
            result = calculate_sharpe_ratio(returns, risk_free_rate, std_dev)
            assert isinstance(result, float)
            assert round(result, 5) == round(expected, 5)
        except Exception as e:
            raise e
