import pytest
import pandas as pd
import plotly.graph_objects as go
from definition_b731dfcbba3b488bbf9cf92643e6a0e7 import generate_scatter_plot

@pytest.fixture
def sample_dataframe():
    data = {'x': [1, 2, 3, 4, 5],
            'y': [2, 4, 1, 3, 5],
            'z': [3, 1, 4, 2, 5]}
    return pd.DataFrame(data)

def test_generate_scatter_plot_valid_input(sample_dataframe):
    fig = generate_scatter_plot(sample_dataframe, 'x', 'y')
    assert isinstance(fig, go.Figure)
    assert fig.data[0]['type'] == 'scatter'
    assert fig.data[0]['x'].tolist() == sample_dataframe['x'].tolist()
    assert fig.data[0]['y'].tolist() == sample_dataframe['y'].tolist()

def test_generate_scatter_plot_different_axes(sample_dataframe):
    fig = generate_scatter_plot(sample_dataframe, 'y', 'z')
    assert isinstance(fig, go.Figure)
    assert fig.data[0]['x'].tolist() == sample_dataframe['y'].tolist()
    assert fig.data[0]['y'].tolist() == sample_dataframe['z'].tolist()

def test_generate_scatter_plot_empty_dataframe():
    empty_df = pd.DataFrame()
    fig = generate_scatter_plot(empty_df, 'x', 'y')
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 0

def test_generate_scatter_plot_missing_x_axis(sample_dataframe):
    with pytest.raises(KeyError):
        generate_scatter_plot(sample_dataframe, 'nonexistent_column', 'y')

def test_generate_scatter_plot_missing_y_axis(sample_dataframe):
    with pytest.raises(KeyError):
        generate_scatter_plot(sample_dataframe, 'x', 'nonexistent_column')

def test_generate_scatter_plot_non_dataframe_input():
    with pytest.raises(AttributeError):
        generate_scatter_plot([1, 2, 3], 'x', 'y')

def test_generate_scatter_plot_x_axis_is_not_numeric(sample_dataframe):
    sample_dataframe['a'] = ['a', 'b', 'c', 'd', 'e']
    fig = generate_scatter_plot(sample_dataframe, 'a', 'y')
    assert isinstance(fig, go.Figure)

def test_generate_scatter_plot_y_axis_is_not_numeric(sample_dataframe):
    sample_dataframe['a'] = ['a', 'b', 'c', 'd', 'e']
    fig = generate_scatter_plot(sample_dataframe, 'x', 'a')
    assert isinstance(fig, go.Figure)

def test_generate_scatter_plot_null_values(sample_dataframe):
    sample_dataframe['x'][2] = None
    fig = generate_scatter_plot(sample_dataframe, 'x', 'y')
    assert isinstance(fig, go.Figure)
    
def test_generate_scatter_plot_inf_values(sample_dataframe):
    sample_dataframe['x'][2] = float('inf')
    fig = generate_scatter_plot(sample_dataframe, 'x', 'y')
    assert isinstance(fig, go.Figure)

def test_generate_scatter_plot_nan_values(sample_dataframe):
    import numpy as np
    sample_dataframe['x'][2] = np.nan
    fig = generate_scatter_plot(sample_dataframe, 'x', 'y')
    assert isinstance(fig, go.Figure)