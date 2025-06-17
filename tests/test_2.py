
import pytest
from definition_d0749ccaf2734d40a375f1b02b426c8c import calculate_sharpe_ratio

@pytest.mark.parametrize("returns, risk_free_rate, std_dev, expected", [
    (0.10, 0.02, 0.15, (0.10 - 0.02) / 0.15),
    (0.05, 0.0, 0.10, (0.05 - 0.0) / 0.10),
    (0.15, 0.05, 0.05, (0.15 - 0.05) / 0.05),
    (0.08, 0.03, 0.20, (0.08 - 0.03) / 0.20),
    (0.0, 0.0, 0.1, 0.0),
    (-0.05, 0.02, 0.1, (-0.05 - 0.02) / 0.1),
    (0.1, 0.1, 0.1, 0.0),
    (0.1, 0.0, 0.0, float('inf')),
    (0.0, 0.0, 0.0, float('inf')),
    (-0.1, 0.0, 0.0, float('-inf')),
])
def test_calculate_sharpe_ratio(returns, risk_free_rate, std_dev, expected):
    if std_dev == 0:
        if returns - risk_free_rate > 0:
            assert calculate_sharpe_ratio(returns, risk_free_rate, std_dev) == float('inf')
        elif returns - risk_free_rate < 0:
            assert calculate_sharpe_ratio(returns, risk_free_rate, std_dev) == float('-inf')
        else:
            assert calculate_sharpe_ratio(returns, risk_free_rate, std_dev) == float('inf')
    else:
        assert calculate_sharpe_ratio(returns, risk_free_rate, std_dev) == (returns - risk_free_rate) / std_dev

@pytest.mark.parametrize("returns, risk_free_rate, std_dev, expected_exception", [
    ("abc", 0.02, 0.15, TypeError),
    (0.10, "abc", 0.15, TypeError),
    (0.10, 0.02, "abc", TypeError),
    (None, 0.02, 0.15, TypeError),
    (0.10, None, 0.15, TypeError),
    (0.10, 0.02, None, TypeError),
])
def test_calculate_sharpe_ratio_type_errors(returns, risk_free_rate, std_dev, expected_exception):
    with pytest.raises(expected_exception):
        calculate_sharpe_ratio(returns, risk_free_rate, std_dev)
