import pytest
import pandas as pd
from definition_6823ae508aa3491086fd295dfc2fd2c1 import compare_to_benchmark

def test_compare_to_benchmark_empty_dataframe():
    data = pd.DataFrame()
    benchmark_strategy = "static_weights"
    benchmark_parameters = {"weights": [0.5, 0.5]}
    with pytest.raises(ValueError):
        compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

def test_compare_to_benchmark_invalid_benchmark_strategy():
    data = pd.DataFrame({'pair_returns': [0.01, 0.02, -0.01], 'benchmark_returns': [0.005, 0.01, -0.005]})
    benchmark_strategy = "invalid_strategy"
    benchmark_parameters = {}
    with pytest.raises(ValueError):
        compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

def test_compare_to_benchmark_static_weights_insufficient_parameters():
        data = pd.DataFrame({'pair_returns': [0.01, 0.02, -0.01], 'asset1': [100, 101, 99], 'asset2':[50,51,49]})

        benchmark_strategy = "static_weights"
        benchmark_parameters = {}
        with pytest.raises(KeyError):  # Changed from ValueError to KeyError as weights are missing
            compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

def test_compare_to_benchmark_static_weights_invalid_parameters_type():
    data = pd.DataFrame({'pair_returns': [0.01, 0.02, -0.01], 'asset1': [100, 101, 99], 'asset2':[50,51,49]})

    benchmark_strategy = "static_weights"
    benchmark_parameters = {"weights": "invalid"}
    with pytest.raises(TypeError):
            compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

def test_compare_to_benchmark_static_weights_valid_input():
    data = pd.DataFrame({'pair_returns': [0.01, 0.02, -0.01], 'asset1': [100, 101, 99], 'asset2':[50,51,49]})
    benchmark_strategy = "static_weights"
    benchmark_parameters = {"weights": [0.5, 0.5]}

    result = compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert 'pair_portfolio' in result.columns
    assert 'benchmark' in result.columns

def test_compare_to_benchmark_rebalancing_window_valid_input():
    data = pd.DataFrame({'pair_returns': [0.01, 0.02, -0.01], 'asset1': [100, 101, 99], 'asset2':[50,51,49]})
    benchmark_strategy = "rebalancing_window"
    benchmark_parameters = {"window": 2}

    result = compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert 'pair_portfolio' in result.columns
    assert 'benchmark' in result.columns

def test_compare_to_benchmark_rebalancing_window_missing_parameter():
    data = pd.DataFrame({'pair_returns': [0.01, 0.02, -0.01], 'asset1': [100, 101, 99], 'asset2':[50,51,49]})
    benchmark_strategy = "rebalancing_window"
    benchmark_parameters = {}

    with pytest.raises(KeyError):
        compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

def test_compare_to_benchmark_rebalancing_window_invalid_parameter_type():
    data = pd.DataFrame({'pair_returns': [0.01, 0.02, -0.01], 'asset1': [100, 101, 99], 'asset2':[50,51,49]})
    benchmark_strategy = "rebalancing_window"
    benchmark_parameters = {"window": "invalid"}

    with pytest.raises(TypeError):
        compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

def test_compare_to_benchmark_data_missing_columns_static_weights():
    data = pd.DataFrame({'returns': [0.01, 0.02, -0.01]})
    benchmark_strategy = "static_weights"
    benchmark_parameters = {"weights": [0.5, 0.5]}
    with pytest.raises(KeyError):
        compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

def test_compare_to_benchmark_data_insufficient_rows():
    data = pd.DataFrame({'pair_returns': [0.01], 'asset1': [100], 'asset2':[50]})
    benchmark_strategy = "static_weights"
    benchmark_parameters = {"weights": [0.5, 0.5]}
    result = compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)

    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert 'pair_portfolio' in result.columns
    assert 'benchmark' in result.columns

def test_compare_to_benchmark_all_zeros_returns():
    data = pd.DataFrame({'pair_returns': [0.0, 0.0, 0.0], 'asset1': [100, 100, 100], 'asset2':[50,50,50]})
    benchmark_strategy = "static_weights"
    benchmark_parameters = {"weights": [0.5, 0.5]}

    result = compare_to_benchmark(data, benchmark_strategy, benchmark_parameters)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert 'pair_portfolio' in result.columns
    assert 'benchmark' in result.columns