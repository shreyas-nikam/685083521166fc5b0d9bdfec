
import pytest
import pandas as pd
import plotly.graph_objects as go
from definition_92a9ce70739a4dd3b4856970420333ce import generate_scatter_plot

# Sample Data for testing
@pytest.fixture
def sample_data():
    data = {
        'x_axis_feature': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        'y_axis_feature': [2, 4, 1, 3, 5, 3, 1, 4, 2, 5],
        'other_feature': [6, 7, 8, 9, 10, 6, 7, 8, 9, 10]
    }
    return pd.DataFrame(data)

def test_generate_scatter_plot_valid_data(sample_data):
    """Test with valid data and column names."""
    fig = generate_scatter_plot(sample_data, 'x_axis_feature', 'y_axis_feature')
    assert isinstance(fig, go.Figure), "Should return a Plotly figure object."
    assert len(fig.data) > 0, "The figure should contain data."
    assert fig.data[0]['type'] == 'scatter', "The figure should be a scatter plot."
    assert fig.data[0]['x'][0] == 1, "X-axis data mismatch"
    assert fig.data[0]['y'][0] == 2, "Y-axis data mismatch"

def test_generate_scatter_plot_empty_dataframe():
    """Test with an empty DataFrame."""
    empty_df = pd.DataFrame()
    fig = generate_scatter_plot(empty_df, 'x_axis', 'y_axis')
    assert isinstance(fig, go.Figure), "Should return a Plotly figure object even for empty DataFrame."
    assert len(fig.data) == 0, "The figure should not contain data for empty dataframe."

def test_generate_scatter_plot_invalid_x_axis(sample_data):
    """Test with an invalid x-axis column name."""
    with pytest.raises(KeyError):
        generate_scatter_plot(sample_data, 'invalid_x', 'y_axis_feature')

def test_generate_scatter_plot_invalid_y_axis(sample_data):
    """Test with an invalid y-axis column name."""
    with pytest.raises(KeyError):
        generate_scatter_plot(sample_data, 'x_axis_feature', 'invalid_y')

def test_generate_scatter_plot_non_numeric_data(sample_data):
    """Test with non-numeric data."""
    sample_data['x_axis_feature'] = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
    with pytest.raises(TypeError):  # Or potentially ValueError, depending on Plotly's handling
        generate_scatter_plot(sample_data, 'x_axis_feature', 'y_axis_feature')

def test_generate_scatter_plot_missing_data(sample_data):
    """Test with missing data (NaN values)."""
    sample_data['x_axis_feature'][0] = float('nan')
    fig = generate_scatter_plot(sample_data, 'x_axis_feature', 'y_axis_feature')
    assert isinstance(fig, go.Figure), "Should still return a Plotly figure object."

def test_generate_scatter_plot_inf_data(sample_data):
    """Test with infinite data (inf values)."""
    sample_data['x_axis_feature'][0] = float('inf')
    fig = generate_scatter_plot(sample_data, 'x_axis_feature', 'y_axis_feature')
    assert isinstance(fig, go.Figure), "Should still return a Plotly figure object."

def test_generate_scatter_plot_mixed_data_types(sample_data):
    """Test with mixed data types in a column."""
    sample_data['x_axis_feature'][0] = 'string'
    with pytest.raises(TypeError):
         generate_scatter_plot(sample_data, 'x_axis_feature', 'y_axis_feature')

def test_generate_scatter_plot_large_numbers(sample_data):
    """Test with very large numbers."""
    sample_data['x_axis_feature'] = [1e10, 2e10, 3e10, 4e10, 5e10, 1e10, 2e10, 3e10, 4e10, 5e10]
    fig = generate_scatter_plot(sample_data, 'x_axis_feature', 'y_axis_feature')
    assert isinstance(fig, go.Figure)

def test_generate_scatter_plot_negative_numbers(sample_data):
    """Test with negative numbers."""
    sample_data['x_axis_feature'] = [-1, -2, -3, -4, -5, -1, -2, -3, -4, -5]
    fig = generate_scatter_plot(sample_data, 'x_axis_feature', 'y_axis_feature')
    assert isinstance(fig, go.Figure)
