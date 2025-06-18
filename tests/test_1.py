import pytest
import pandas as pd
from definition_c583382de86a464f92de10349df9dd46 import filter_data

# Mock DataFrame for testing
@pytest.fixture
def sample_data():
    data = {'asset_class': ['Equity', 'Equity', 'Fixed Income', 'Fixed Income', 'Equity'],
            'signal_type': ['Momentum', 'Value', 'Carry', 'Momentum', 'Growth'],
            'pair_performance': [0.1, 0.2, 0.3, 0.4, 0.5]}
    return pd.DataFrame(data)

def test_filter_data_valid_input(sample_data):
    filtered_data = filter_data(sample_data, 'Equity', 'Momentum', 0.5)
    assert isinstance(filtered_data, pd.DataFrame)

def test_filter_data_empty_dataframe():
    empty_df = pd.DataFrame()
    filtered_data = filter_data(empty_df, 'Equity', 'Momentum', 0.5)
    assert isinstance(filtered_data, pd.DataFrame)
    assert filtered_data.empty

def test_filter_data_no_matching_asset_class(sample_data):
    filtered_data = filter_data(sample_data, 'Commodity', 'Momentum', 0.5)
    assert isinstance(filtered_data, pd.DataFrame)
    assert filtered_data.empty

def test_filter_data_no_matching_signal_type(sample_data):
    filtered_data = filter_data(sample_data, 'Equity', 'Volatility', 0.5)
    assert isinstance(filtered_data, pd.DataFrame)
    assert filtered_data.empty

def test_filter_data_selectivity_level_0(sample_data):
    filtered_data = filter_data(sample_data, 'Equity', 'Momentum', 0.0)
    assert isinstance(filtered_data, pd.DataFrame)
    assert filtered_data.empty

def test_filter_data_selectivity_level_1(sample_data):
    filtered_data = filter_data(sample_data, 'Equity', 'Momentum', 1.0)
    assert isinstance(filtered_data, pd.DataFrame)

def test_filter_data_selectivity_level_greater_than_1(sample_data):
     with pytest.raises(ValueError):
        filter_data(sample_data, 'Equity', 'Momentum', 1.5)

def test_filter_data_selectivity_level_less_than_0(sample_data):
    with pytest.raises(ValueError):
        filter_data(sample_data, 'Equity', 'Momentum', -0.5)

def test_filter_data_invalid_asset_class_type(sample_data):
    with pytest.raises(TypeError):
        filter_data(sample_data, 123, 'Momentum', 0.5)

def test_filter_data_invalid_signal_type(sample_data):
    with pytest.raises(TypeError):
        filter_data(sample_data, 'Equity', 456, 0.5)

def test_filter_data_invalid_selectivity_level_type(sample_data):
     with pytest.raises(TypeError):
        filter_data(sample_data, 'Equity', 'Momentum', "abc")

def test_filter_data_nan_values_in_dataframe():
    data = {'asset_class': ['Equity', 'Equity', 'Fixed Income', 'Fixed Income', 'Equity'],
            'signal_type': ['Momentum', 'Value', 'Carry', 'Momentum', 'Growth'],
            'pair_performance': [0.1, float('nan'), 0.3, 0.4, 0.5]}
    df = pd.DataFrame(data)
    filtered_data = filter_data(df, 'Equity', 'Momentum', 0.5)
    assert isinstance(filtered_data, pd.DataFrame)

def test_filter_data_case_insensitive_asset_class(sample_data):
    filtered_data = filter_data(sample_data, 'equity', 'Momentum', 0.5)
    assert isinstance(filtered_data, pd.DataFrame)

def test_filter_data_case_insensitive_signal_type(sample_data):
    filtered_data = filter_data(sample_data, 'Equity', 'momentum', 0.5)
    assert isinstance(filtered_data, pd.DataFrame)

def test_filter_data_no_pair_performance_column(sample_data):
    data = {'asset_class': ['Equity', 'Equity', 'Fixed Income', 'Fixed Income', 'Equity'],
            'signal_type': ['Momentum', 'Value', 'Carry', 'Momentum', 'Growth']}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        filter_data(df, 'Equity', 'Momentum', 0.5)
