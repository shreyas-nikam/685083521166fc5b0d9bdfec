
import pytest
import pandas as pd
import numpy as np
from definition_4237e35669434923a5a418e98a03b3de import compare_to_benchmark

@pytest.fixture
def sample_data():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({
        'pair_portfolio_return': [0.1, 0.12, 0.15, 0.13, 0.16],
        'benchmark_return': [0.08, 0.1, 0.12, 0.11, 0.14]
    })
    return data

def test_compare_to_benchmark_linear_weights(sample_data):
    # Test with linear weights benchmark strategy
    result = compare_to_benchmark(sample_data, 'linear_weights', {})
    assert isinstance(result, pd.DataFrame)
    assert 'pair_portfolio_return' in result.columns
    assert 'benchmark_return' in result.columns

def test_compare_to_benchmark_quantile_sorting(sample_data):
    # Test with quantile sorting benchmark strategy
    result = compare_to_benchmark(sample_data, 'quantile_sorting', {'quantile': 0.75})
    assert isinstance(result, pd.DataFrame)
    assert 'pair_portfolio_return' in result.columns
    assert 'benchmark_return' in result.columns

def test_compare_to_benchmark_no_data():
    # Test with empty data
    data = pd.DataFrame()
    result = compare_to_benchmark(data, 'linear_weights', {})
    assert isinstance(result, pd.DataFrame)

def test_compare_to_benchmark_invalid_strategy(sample_data):
    # Test with an invalid benchmark strategy
    with pytest.raises(ValueError):  # Or whatever exception your code raises
        compare_to_benchmark(sample_data, 'invalid_strategy', {})

def test_compare_to_benchmark_none_data():
    # Test when the input data is None
    with pytest.raises(TypeError):  # Expecting a TypeError if data is None
        compare_to_benchmark(None, 'linear_weights', {})

def test_compare_to_benchmark_benchmark_params_not_dict(sample_data):
     # Test when benchmark_parameters is not a dictionary
    with pytest.raises(TypeError):
        compare_to_benchmark(sample_data, "quantile_sorting", "not_a_dict")

def test_compare_to_benchmark_nan_values(sample_data):
    # Test with NaN values in dataframe
    sample_data.loc[0, 'pair_portfolio_return'] = np.nan
    result = compare_to_benchmark(sample_data, 'linear_weights', {})
    assert isinstance(result, pd.DataFrame)
    assert 'pair_portfolio_return' in result.columns
    assert 'benchmark_return' in result.columns

def test_compare_to_benchmark_inf_values(sample_data):
    #Test with inf values in dataframe
    sample_data.loc[0, 'pair_portfolio_return'] = np.inf
    result = compare_to_benchmark(sample_data, 'linear_weights', {})
    assert isinstance(result, pd.DataFrame)
    assert 'pair_portfolio_return' in result.columns
    assert 'benchmark_return' in result.columns
