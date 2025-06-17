"""
import pytest
import pandas as pd
import plotly.graph_objects as go
from definitions_f68a64c556c14824b2c1d1f06d84077f import generate_line_chart

# Mock data for testing purposes
@pytest.fixture
def mock_data():
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-08', '2023-01-15', '2023-01-22', '2023-01-29']),
        'Average Return': [0.01, 0.02, 0.015, 0.025, 0.022],
        'Volatility': [0.05, 0.06, 0.055, 0.065, 0.062],
        'Sharpe Ratio': [0.2, 0.3, 0.25, 0.35, 0.32]
    }
    return pd.DataFrame(data)

# Test case 1: Check if the function returns a Plotly figure
def test_generate_line_chart_returns_figure(mock_data):
    fig = generate_line_chart(mock_data)
    assert isinstance(fig, go.Figure)

# Test case 2: Check if the figure contains the correct number of traces (Average Return, Volatility, Sharpe Ratio)
def test_generate_line_chart_number_of_traces(mock_data):
    fig = generate_line_chart(mock_data)
    assert len(fig.data) == 3

# Test case 3: Check if the x-axis is correctly set to 'Date'
def test_generate_line_chart_xaxis(mock_data):
    fig = generate_line_chart(mock_data)
    for trace in fig.data:
        assert trace.x.tolist() == mock_data['Date'].tolist()

# Test case 4: Check if the y-axis of each trace corresponds to the correct column in the DataFrame
def test_generate_line_chart_yaxis(mock_data):
    fig = generate_line_chart(mock_data)
    y_values = [trace.y.tolist() for trace in fig.data]
    expected_y_values = [
        mock_data['Average Return'].tolist(),
        mock_data['Volatility'].tolist(),
        mock_data['Sharpe Ratio'].tolist()
    ]
    assert y_values == expected_y_values

# Test case 5: Check if the chart title is set correctly.  This is now determined within the function.
def test_generate_line_chart_title(mock_data):
    fig = generate_line_chart(mock_data)
    assert fig.layout.title.text == 'Performance Metrics Over Time'


# Test case 6: Test with an empty DataFrame
def test_generate_line_chart_empty_dataframe():
    empty_data = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        generate_line_chart(empty_data)
    assert "Input DataFrame is empty." in str(excinfo.value)

# Test case 7: Test with a DataFrame missing required columns ('Date', 'Average Return', 'Volatility', 'Sharpe Ratio')
def test_generate_line_chart_missing_columns():
    missing_data = pd.DataFrame({'Date': pd.to_datetime(['2023-01-01']), 'Average Return': [0.01]})
    with pytest.raises(KeyError) as excinfo:
        generate_line_chart(missing_data)
    assert "Required columns ('Volatility', 'Sharpe Ratio') are missing." in str(excinfo.value)

# Test case 8: Check if date column is datetime
def test_generate_line_chart_date_format(mock_data):
    fig = generate_line_chart(mock_data)
    for trace in fig.data:
        assert all(isinstance(date, pd.Timestamp) for date in trace.x)

# Test case 9: Numerical values in return, vol, sharpe ratio.

def test_generate_line_chart_numerical_values(mock_data):

    fig = generate_line_chart(mock_data)
    for trace in fig.data:
      assert all(isinstance(value, (int, float)) for value in trace.y)

# Test case 10: Check if it handles NaN values correctly in the data by dropping them
def test_generate_line_chart_nan_values():
    data_with_nan = pd.DataFrame({
        'Date': pd.to_datetime(['2023-01-01', '2023-01-08', '2023-01-15']),
        'Average Return': [0.01, float('nan'), 0.015],
        'Volatility': [0.05, 0.06, float('nan')],
        'Sharpe Ratio': [0.2, float('nan'), 0.25]
    })
    fig = generate_line_chart(data_with_nan)

    # Get y values from chart
    y_values = [trace.y.tolist() for trace in fig.data]

    # Validate they don't contain NaN.
    assert all(float('nan') not in sublist for sublist in y_values)

"""