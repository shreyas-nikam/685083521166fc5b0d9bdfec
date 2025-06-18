import pytest
import pandas as pd
import plotly.graph_objects as go
from definition_882361b862964d70bbfc44c68eb58e9d import generate_line_chart

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
        'Average Returns': [0.01, 0.02, -0.01, 0.03, 0.015],
        'Volatility': [0.05, 0.06, 0.04, 0.07, 0.055],
        'Sharpe Ratio': [0.5, 0.7, -0.2, 0.8, 0.6]
    }
    return pd.DataFrame(data)

def test_generate_line_chart_valid_data(sample_data):
    """Tests the function with valid DataFrame input."""
    fig = generate_line_chart(sample_data)
    assert isinstance(fig, go.Figure), "The function should return a Plotly figure object."
    assert len(fig.data) == 3, "The figure should contain three traces (Average Returns, Volatility, Sharpe Ratio)."
    assert fig.data[0]['name'] == 'Average Returns', "The first trace should be named 'Average Returns'."
    assert fig.data[1]['name'] == 'Volatility', "The second trace should be named 'Volatility'."
    assert fig.data[2]['name'] == 'Sharpe Ratio', "The third trace should be named 'Sharpe Ratio'."
    assert all(isinstance(x, str) for x in fig.data[0]['x']), "X-axis values should be strings (dates)."
    assert all(isinstance(y, float) or isinstance(y, int) for y in fig.data[0]['y']), "Y-axis values should be numerical."

def test_generate_line_chart_empty_data():
    """Tests the function with an empty DataFrame."""
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        generate_line_chart(empty_df)

def test_generate_line_chart_missing_columns():
    """Tests the function with a DataFrame missing required columns."""
    data = {'Date': pd.to_datetime(['2023-01-01', '2023-01-02'])}
    df = pd.DataFrame(data)
    with pytest.raises(KeyError):
        generate_line_chart(df)

def test_generate_line_chart_non_datetime_date_column():
    """Tests the function when the 'Date' column is not in datetime format."""
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Average Returns': [0.01, 0.02, -0.01],
        'Volatility': [0.05, 0.06, 0.04],
        'Sharpe Ratio': [0.5, 0.7, -0.2]
    }
    df = pd.DataFrame(data)
    with pytest.raises(TypeError):
        generate_line_chart(df)

def test_generate_line_chart_non_numeric_data():
    """Tests the function with non-numeric data in the value columns."""
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'Average Returns': ['a', 'b', 'c'],
        'Volatility': ['d', 'e', 'f'],
        'Sharpe Ratio': ['g', 'h', 'i']
    }
    df = pd.DataFrame(data)

    with pytest.raises(TypeError):
         generate_line_chart(df)

def test_generate_line_chart_inf_values():
    """Tests the function when the data contains infinite values."""
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'Average Returns': [0.01, float('inf'), -0.01],
        'Volatility': [0.05, 0.06, 0.04],
        'Sharpe Ratio': [0.5, 0.7, -0.2]
    }
    df = pd.DataFrame(data)
    fig = generate_line_chart(df)
    assert isinstance(fig, go.Figure), "The function should return a Plotly figure object even with inf values."

def test_generate_line_chart_nan_values():
    """Tests the function when the data contains NaN values."""
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'Average Returns': [0.01, float('nan'), -0.01],
        'Volatility': [0.05, 0.06, 0.04],
        'Sharpe Ratio': [0.5, 0.7, -0.2]
    }
    df = pd.DataFrame(data)
    fig = generate_line_chart(df)
    assert isinstance(fig, go.Figure), "The function should return a Plotly figure object even with NaN values."