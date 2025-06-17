
import pytest
import pandas as pd
import plotly.graph_objects as go
from definition_de5717947d5044b482040c2d12225094 import generate_bar_chart

@pytest.fixture
def sample_data():
    """Creates a sample Pandas DataFrame for testing."""
    data = {
        'Key Driver': ['Own-asset predictability', 'Cross-asset predictability', 'Signal Correlation', 'Signal mean imbalance', 'Signal variance imbalance', 'Unexplained Effect'],
        'Contribution': [0.2, 0.3, 0.1, -0.05, 0.15, 0.2]
    }
    return pd.DataFrame(data)

def test_generate_bar_chart_valid_data(sample_data):
    """Tests the function with valid DataFrame input."""
    fig = generate_bar_chart(sample_data)
    assert isinstance(fig, go.Figure)
    assert fig.data[0]['type'] == 'bar'
    assert len(fig.data[0]['x']) == len(sample_data)
    assert len(fig.data[0]['y']) == len(sample_data)
    assert fig.layout.title.text == 'Contribution of Key Drivers to Pair Portfolio Return'
    assert fig.layout.xaxis.title.text == 'Key Driver'
    assert fig.layout.yaxis.title.text == 'Contribution to Return'

def test_generate_bar_chart_empty_dataframe():
    """Tests the function with an empty DataFrame."""
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        generate_bar_chart(empty_df)

def test_generate_bar_chart_missing_columns():
    """Tests the function with a DataFrame missing required columns."""
    data = {'Irrelevant Column': [1, 2, 3]}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        generate_bar_chart(df)

def test_generate_bar_chart_non_numeric_contributions():
    """Tests the function with a DataFrame containing non-numeric values in the contribution column."""
    data = {
        'Key Driver': ['Own-asset predictability'],
        'Contribution': ['invalid']
    }
    df = pd.DataFrame(data)
    with pytest.raises(TypeError):
        generate_bar_chart(df)

def test_generate_bar_chart_all_zero_contributions(sample_data):
    """Tests the function with a DataFrame where all contribution values are zero."""
    sample_data['Contribution'] = 0
    fig = generate_bar_chart(sample_data)
    assert isinstance(fig, go.Figure)

def test_generate_bar_chart_negative_contributions(sample_data):
    """Tests the function with a DataFrame containing negative contributions."""
    fig = generate_bar_chart(sample_data)
    assert isinstance(fig, go.Figure)

def test_generate_bar_chart_inf_contributions():
    """Tests the function with a DataFrame containing infinite contribution values."""
    data = {
        'Key Driver': ['Own-asset predictability'],
        'Contribution': [float('inf')]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        generate_bar_chart(df)

def test_generate_bar_chart_nan_contributions():
    """Tests the function with a DataFrame containing NaN contribution values."""
    data = {
        'Key Driver': ['Own-asset predictability'],
        'Contribution': [float('nan')]
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        generate_bar_chart(df)

def test_generate_bar_chart_single_row():
    """Tests the function with a DataFrame containing only a single row."""
    data = {
        'Key Driver': ['Own-asset predictability'],
        'Contribution': [0.5]
    }
    df = pd.DataFrame(data)
    fig = generate_bar_chart(df)
    assert isinstance(fig, go.Figure)

def test_generate_bar_chart_large_contribution_values(sample_data):
    """Tests with large values in the 'Contribution' column."""
    sample_data['Contribution'] = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000]
    fig = generate_bar_chart(sample_data)
    assert isinstance(fig, go.Figure)
