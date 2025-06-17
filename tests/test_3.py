
import pytest
import pandas as pd
import plotly.graph_objects as go
from definition_e07e41ad21a2463cacdff2d21bf88615 import generate_line_chart


def create_sample_dataframe():
    """Creates a sample Pandas DataFrame for testing."""
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
        'Average Return': [0.01, 0.02, 0.015, 0.025, 0.022],
        'Volatility': [0.005, 0.006, 0.0055, 0.007, 0.0065],
        'Sharpe Ratio': [2.0, 3.0, 2.7, 3.5, 3.4]
    }
    return pd.DataFrame(data)



def test_generate_line_chart_valid_data():
    """Tests the function with valid data and checks the output type."""
    data = create_sample_dataframe()
    fig = generate_line_chart(data)
    assert isinstance(fig, go.Figure), "The function should return a Plotly figure."


def test_generate_line_chart_empty_dataframe():
    """Tests the function with an empty DataFrame."""
    data = pd.DataFrame()  # Empty DataFrame
    fig = generate_line_chart(data)
    assert isinstance(fig, go.Figure), "The function should return a Plotly figure even with empty data."
    assert len(fig.data) == 0, "The figure should have no traces when the input DataFrame is empty."


def test_generate_line_chart_missing_columns():
    """Tests the function when the DataFrame is missing required columns."""
    data = pd.DataFrame({'Date': pd.to_datetime(['2023-01-01', '2023-01-02']), 'Returns': [0.01, 0.02]})
    with pytest.raises(KeyError):
        generate_line_chart(data)


def test_generate_line_chart_non_numeric_data():
    """Tests the function with non-numeric data in numeric columns."""
    data = create_sample_dataframe()
    data['Average Return'] = ['a', 'b', 'c', 'd', 'e']
    with pytest.raises(TypeError):
        generate_line_chart(data)


def test_generate_line_chart_incorrect_date_format():
    """Tests the function with incorrect date format in the 'Date' column."""
    data = create_sample_dataframe()
    data['Date'] = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'] # Dates as strings
    fig = generate_line_chart(data)
    assert isinstance(fig, go.Figure), "The function should handle dates as strings and return a Plotly figure."


def test_generate_line_chart_nan_values():
    """Tests the function with NaN values in the DataFrame."""
    data = create_sample_dataframe()
    data.loc[2, 'Average Return'] = float('NaN')
    fig = generate_line_chart(data)
    assert isinstance(fig, go.Figure), "The function should handle NaN values and return a Plotly figure."


def test_generate_line_chart_inf_values():
    """Tests the function with infinite values in the DataFrame."""
    data = create_sample_dataframe()
    data.loc[2, 'Average Return'] = float('inf')
    fig = generate_line_chart(data)
    assert isinstance(fig, go.Figure), "The function should handle infinite values and return a Plotly figure."

def test_generate_line_chart_zero_volatility():
    """Tests the function when volatility is zero."""
    data = create_sample_dataframe()
    data['Volatility'] = [0, 0, 0, 0, 0]
    fig = generate_line_chart(data)
    assert isinstance(fig, go.Figure), "The function should handle zero volatility and return a Plotly figure."

def test_generate_line_chart_negative_sharpe_ratio():
    """Tests the function when Sharpe Ratio is negative."""
    data = create_sample_dataframe()
    data['Sharpe Ratio'] = [-1, -2, -3, -4, -5]
    fig = generate_line_chart(data)
    assert isinstance(fig, go.Figure), "The function should handle negative Sharpe ratios and return a Plotly figure."
