```python
"""
import pytest
import pandas as pd
import numpy as np
from definitions_94d67dfa6f1e4a8fb689d6b4713c8e96 import calculate_sharpe_ratio


def test_calculate_sharpe_ratio_typical():
    returns = pd.Series([0.1, 0.2, -0.1, 0.05, 0.15])
    risk_free_rate = 0.02
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_zero_std():
    returns = pd.Series([0.1, 0.1, 0.1, 0.1])
    risk_free_rate = 0.02
    assert np.isinf(calculate_sharpe_ratio(returns, risk_free_rate))

def test_calculate_sharpe_ratio_negative_std():
    returns = pd.Series([-0.1, -0.1, -0.1, -0.1])
    risk_free_rate = 0.02
    assert np.isinf(calculate_sharpe_ratio(returns, risk_free_rate) * -1)

def test_calculate_sharpe_ratio_zero_returns():
    returns = pd.Series([0, 0, 0, 0, 0])
    risk_free_rate = 0.02
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isnan(calculate_sharpe_ratio(returns, risk_free_rate))

def test_calculate_sharpe_ratio_negative_returns():
    returns = pd.Series([-0.1, -0.2, -0.3, -0.4, -0.5])
    risk_free_rate = 0.02
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_large_returns():
    returns = pd.Series([1.0, 2.0, -1.0, 0.5, 1.5])
    risk_free_rate = 0.02
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_small_returns():
    returns = pd.Series([0.001, 0.002, -0.001, 0.0005, 0.0015])
    risk_free_rate = 0.0002
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_mixed_positive_negative():
    returns = pd.Series([0.1, -0.2, 0.3, -0.4, 0.5])
    risk_free_rate = 0.02
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_zero_risk_free_rate():
    returns = pd.Series([0.1, 0.2, -0.1, 0.05, 0.15])
    risk_free_rate = 0.0
    expected_sharpe_ratio = returns.mean() / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_negative_risk_free_rate():
    returns = pd.Series([0.1, 0.2, -0.1, 0.05, 0.15])
    risk_free_rate = -0.02
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_empty_returns():
    returns = pd.Series([])
    risk_free_rate = 0.02
    with pytest.raises(ValueError):
        calculate_sharpe_ratio(returns, risk_free_rate)

def test_calculate_sharpe_ratio_invalid_returns_type():
    returns = [0.1, 0.2, -0.1, 0.05, 0.15]
    risk_free_rate = 0.02
    with pytest.raises(AttributeError):
        calculate_sharpe_ratio(returns, risk_free_rate)

def test_calculate_sharpe_ratio_invalid_risk_free_rate_type():
    returns = pd.Series([0.1, 0.2, -0.1, 0.05, 0.15])
    risk_free_rate = "0.02"
    with pytest.raises(TypeError):
        calculate_sharpe_ratio(returns, risk_free_rate)

def test_calculate_sharpe_ratio_returns_with_nan():
    returns = pd.Series([0.1, 0.2, np.nan, 0.05, 0.15])
    risk_free_rate = 0.02
    returns = returns.dropna()
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)

def test_calculate_sharpe_ratio_returns_with_inf():
    returns = pd.Series([0.1, 0.2, np.inf, 0.05, 0.15])
    risk_free_rate = 0.02
    returns = returns[~np.isinf(returns)]
    expected_sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
    assert np.isclose(calculate_sharpe_ratio(returns, risk_free_rate), expected_sharpe_ratio)
```