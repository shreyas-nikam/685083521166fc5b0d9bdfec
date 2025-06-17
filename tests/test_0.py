"""
import pytest
import pandas as pd
from definitions_0473639f925d4974b9bb029358b4133b import load_data


def test_load_data_returns_dataframe():
    """
    Test that load_data function returns a Pandas DataFrame.
    """
    df = load_data()
    assert isinstance(df, pd.DataFrame), "load_data should return a Pandas DataFrame"


def test_load_data_not_empty():
    """
    Test that the DataFrame returned by load_data is not empty.
    """
    df = load_data()
    assert not df.empty, "DataFrame should not be empty"


def test_load_data_column_names():
    """
    Test that the DataFrame returned by load_data has expected column names.
    """
    expected_columns = ['asset_class', 'signal_type', 'return', 'volatility', 'sharpe_ratio',
                        'own_asset_predictability', 'cross_asset_predictability',
                        'signal_correlation', 'signal_mean_imbalance',
                        'signal_variance_imbalance', 'unexplained_effect']
    df = load_data()
    actual_columns = df.columns.tolist()
    assert all(col in actual_columns for col in expected_columns), "DataFrame should have required columns"
    assert all(col in expected_columns for col in actual_columns), "DataFrame should have only required columns"

def test_load_data_column_types():
    """
    Test that the DataFrame returned by load_data has correct column types.
    """
    df = load_data()
    assert df['return'].dtype == 'float64', "Return column should be float64"
    assert df['volatility'].dtype == 'float64', "Volatility column should be float64"
    assert df['sharpe_ratio'].dtype == 'float64', "Sharpe Ratio column should be float64"
    assert df['own_asset_predictability'].dtype == 'float64', "Own Asset Predictability column should be float64"
    assert df['cross_asset_predictability'].dtype == 'float64', "Cross Asset Predictability column should be float64"
    assert df['signal_correlation'].dtype == 'float64', "Signal Correlation column should be float64"
    assert df['signal_mean_imbalance'].dtype == 'float64', "Signal Mean Imbalance column should be float64"
    assert df['signal_variance_imbalance'].dtype == 'float64', "Signal Variance Imbalance column should be float64"
    assert df['unexplained_effect'].dtype == 'float64', "Unexplained Effect column should be float64"
    assert df['asset_class'].dtype == 'object', "Asset Class column should be object (string)"
    assert df['signal_type'].dtype == 'object', "Signal Type column should be object (string)"

def test_load_data_valid_asset_classes():
    """
    Test that the asset_class column contains only valid asset classes.
    """
    df = load_data()
    valid_asset_classes = ['equities', 'bonds', 'currencies', 'commodities']
    assert all(asset_class in valid_asset_classes for asset_class in df['asset_class'].unique()), "Asset Class column should contain valid asset classes"

def test_load_data_valid_signal_types():
    """
    Test that the signal_type column contains only valid signal types.
    """
    df = load_data()
    valid_signal_types = ['value', 'momentum', 'carry']
    assert all(signal_type in valid_signal_types for signal_type in df['signal_type'].unique()), "Signal Type column should contain valid signal types"

def test_load_data_no_null_values():
    """
    Test that the DataFrame does not contain any null values.
    """
    df = load_data()
    assert df.isnull().sum().sum() == 0, "DataFrame should not contain null values"

def test_load_data_reasonable_ranges():
    """
    Test that the numerical columns have reasonable ranges (basic sanity check).
    """
    df = load_data()
    assert df['return'].between(-1, 1).all(), "Return values should be within a reasonable range (-1 to 1)"
    assert df['volatility'].between(0, 1).all(), "Volatility values should be within a reasonable range (0 to 1)"
    assert df['sharpe_ratio'].between(-10, 10).all(), "Sharpe Ratio values should be within a reasonable range (-10 to 10)"
    assert df['signal_correlation'].between(-1, 1).all(), "Signal Correlation should be between -1 and 1"

"""