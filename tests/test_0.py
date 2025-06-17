
import pytest
import pandas as pd
from definition_4718a78c0712441291f35be0dd1830ac import load_data

def test_load_data_returns_dataframe():
    """
    Test that load_data() returns a Pandas DataFrame.
    """
    df = load_data()
    assert isinstance(df, pd.DataFrame)

def test_load_data_dataframe_not_empty():
    """
    Test that the returned DataFrame is not empty.
    """
    df = load_data()
    assert not df.empty

def test_load_data_expected_columns():
    """
    Test that the DataFrame contains the expected columns.
    """
    expected_columns = [
        "asset_class",
        "signal_type",
        "return",
        "volatility",
        "sharpe_ratio",
        "own_asset_predictability",
        "cross_asset_predictability",
        "signal_correlation",
        "signal_mean_imbalance",
        "signal_variance_imbalance",
        "unexplained_effect",
    ]
    df = load_data()
    assert all(col in df.columns for col in expected_columns)

def test_load_data_column_types():
    """
    Test that the columns have the expected data types.
    This test checks that the columns such as 'return','volatility','sharpe_ratio',
    'own_asset_predictability', 'cross_asset_predictability', 'signal_correlation',
    'signal_mean_imbalance', 'signal_variance_imbalance', and 'unexplained_effect'
    have a numeric data type.
    """
    df = load_data()
    numeric_columns = [
        "return",
        "volatility",
        "sharpe_ratio",
        "own_asset_predictability",
        "cross_asset_predictability",
        "signal_correlation",
        "signal_mean_imbalance",
        "signal_variance_imbalance",
        "unexplained_effect",
    ]
    for col in numeric_columns:
        assert pd.api.types.is_numeric_dtype(df[col]), f"Column '{col}' should be numeric"

def test_load_data_asset_class_values():
    """
    Test that the 'asset_class' column contains valid values.
    """
    df = load_data()
    valid_asset_classes = ["equities", "bonds", "currencies", "commodities"]
    assert all(asset_class in valid_asset_classes for asset_class in df["asset_class"].unique())

def test_load_data_signal_type_values():
    """
    Test that the 'signal_type' column contains valid values.
    """
    df = load_data()
    valid_signal_types = ["value", "momentum", "carry"]
    assert all(signal_type in valid_signal_types for signal_type in df["signal_type"].unique())

def test_load_data_no_null_values_in_critical_columns():
    """
    Test that critical columns do not contain null values.
    """
    df = load_data()
    critical_columns = [
        "asset_class",
        "signal_type",
        "return",
        "volatility",
        "sharpe_ratio"
    ]
    for col in critical_columns:
        assert df[col].isnull().sum() == 0, f"Column '{col}' contains null values"
