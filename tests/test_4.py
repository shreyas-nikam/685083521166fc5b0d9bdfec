import pytest
import pandas as pd
import plotly.graph_objects as go
from definition_3a06065f4d89461080d8772a81ba4d78 import generate_bar_chart


def test_generate_bar_chart_empty_dataframe():
    """Test with an empty DataFrame."""
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        generate_bar_chart(empty_df)
    assert "Input DataFrame is empty." in str(excinfo.value)


def test_generate_bar_chart_missing_columns():
    """Test with a DataFrame missing required columns."""
    missing_cols_df = pd.DataFrame({'Driver': ['A', 'B'], 'Contribution': [0.1, 0.2]})
    with pytest.raises(KeyError) as excinfo:
        generate_bar_chart(missing_cols_df)
    assert "Missing required column: Pair" in str(excinfo.value)


def test_generate_bar_chart_non_numeric_contribution():
    """Test with a DataFrame having non-numeric 'Contribution' values."""
    non_numeric_df = pd.DataFrame({'Pair': ['X', 'Y'], 'Driver': ['A', 'B'], 'Contribution': ['0.1', '0.2']})
    with pytest.raises(TypeError) as excinfo:
        generate_bar_chart(non_numeric_df)
    assert "Contribution column must be numeric." in str(excinfo.value)

def test_generate_bar_chart_valid_data():
    """Test with a valid DataFrame."""
    valid_df = pd.DataFrame({
        'Pair': ['Pair1', 'Pair1', 'Pair2', 'Pair2'],
        'Driver': ['DriverA', 'DriverB', 'DriverC', 'DriverD'],
        'Contribution': [0.1, 0.2, 0.3, 0.4]
    })
    fig = generate_bar_chart(valid_df)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0
    assert fig.layout.barmode == 'group'
    assert fig.layout.title.text == 'Contribution of Each Driver to Pair Portfolio Return'
    assert fig.layout.xaxis.title.text == 'Driver'
    assert fig.layout.yaxis.title.text == 'Contribution'


def test_generate_bar_chart_single_pair():
    """Test with a DataFrame containing data for only one pair."""
    single_pair_df = pd.DataFrame({
        'Pair': ['Pair1', 'Pair1'],
        'Driver': ['DriverA', 'DriverB'],
        'Contribution': [0.1, 0.2]
    })
    fig = generate_bar_chart(single_pair_df)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0
    assert fig.layout.barmode == 'group'
    assert fig.layout.title.text == 'Contribution of Each Driver to Pair Portfolio Return'
    assert fig.layout.xaxis.title.text == 'Driver'
    assert fig.layout.yaxis.title.text == 'Contribution'


def test_generate_bar_chart_negative_contributions():
     """Test with negative contribution values"""
     negative_contribution_df = pd.DataFrame({
        'Pair': ['Pair1', 'Pair1', 'Pair2', 'Pair2'],
        'Driver': ['DriverA', 'DriverB', 'DriverC', 'DriverD'],
        'Contribution': [-0.1, 0.2, -0.3, 0.4]
    })
     fig = generate_bar_chart(negative_contribution_df)
     assert isinstance(fig, go.Figure)

def test_generate_bar_chart_zero_contributions():
     """Test with zero contribution values"""
     zero_contribution_df = pd.DataFrame({
        'Pair': ['Pair1', 'Pair1', 'Pair2', 'Pair2'],
        'Driver': ['DriverA', 'DriverB', 'DriverC', 'DriverD'],
        'Contribution': [0, 0, 0, 0]
    })
     fig = generate_bar_chart(zero_contribution_df)
     assert isinstance(fig, go.Figure)

def test_generate_bar_chart_large_numbers():
    """Test with large numbers in contributions."""
    large_numbers_df = pd.DataFrame({
        'Pair': ['Pair1', 'Pair1', 'Pair2', 'Pair2'],
        'Driver': ['DriverA', 'DriverB', 'DriverC', 'DriverD'],
        'Contribution': [1000000, 2000000, 3000000, 4000000]
    })
    fig = generate_bar_chart(large_numbers_df)
    assert isinstance(fig, go.Figure)

def test_generate_bar_chart_duplicate_driver_pair():
    """Test with duplicate Driver/Pair combinations."""
    duplicate_df = pd.DataFrame({
        'Pair': ['Pair1', 'Pair1', 'Pair1', 'Pair2'],
        'Driver': ['DriverA', 'DriverA', 'DriverB', 'DriverC'],
        'Contribution': [0.1, 0.2, 0.3, 0.4]
    })

    fig = generate_bar_chart(duplicate_df)
    assert isinstance(fig, go.Figure)