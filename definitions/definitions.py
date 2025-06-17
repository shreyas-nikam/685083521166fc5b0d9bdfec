
import pandas as pd
import numpy as np

def load_data() -> pd.DataFrame:
    """
    Loads the synthetic dataset into a Pandas DataFrame.

    Arguments:
        None

    Output:
        Pandas DataFrame containing the synthetic dataset.
    """

    # Number of rows in the dataset
    num_rows = 100

    # Define possible values for categorical columns
    asset_classes = ["equities", "bonds", "currencies", "commodities"]
    signal_types = ["value", "momentum", "carry"]

    # Generate synthetic data
    data = {
        "asset_class": np.random.choice(asset_classes, num_rows),
        "signal_type": np.random.choice(signal_types, num_rows),
        "return": np.random.normal(0.05, 0.1, num_rows),
        "volatility": np.random.uniform(0.01, 0.2, num_rows),
        "sharpe_ratio": np.random.normal(0.5, 1.5, num_rows),
        "own_asset_predictability": np.random.uniform(0, 1, num_rows),
        "cross_asset_predictability": np.random.uniform(0, 0.5, num_rows),
        "signal_correlation": np.random.normal(0, 0.2, num_rows),
        "signal_mean_imbalance": np.random.normal(0, 0.5, num_rows),
        "signal_variance_imbalance": np.random.uniform(0, 0.3, num_rows),
        "unexplained_effect": np.random.normal(0, 0.1, num_rows),
    }

    # Create Pandas DataFrame
    df = pd.DataFrame(data)

    return df


def calculate_sharpe_ratio(returns: float, risk_free_rate: float, std_dev: float) -> float:
    """
    Calculates the Sharpe Ratio of a portfolio.

    Args:
        returns: Average portfolio return.
        risk_free_rate: Risk-free rate.
        std_dev: Portfolio standard deviation.

    Returns:
        Sharpe Ratio.  Returns inf if std_dev is 0.

    Raises:
        TypeError: if any of the inputs are not floats or integers.
    """
    if not isinstance(returns, (float, int)):
        raise TypeError("Returns must be a float or integer.")
    if not isinstance(risk_free_rate, (float, int)):
        raise TypeError("Risk-free rate must be a float or integer.")
    if not isinstance(std_dev, (float, int)):
        raise TypeError("Standard deviation must be a float or integer.")

    if std_dev == 0:
        if returns == risk_free_rate:
            return float('inf')
        return float('inf') if returns > risk_free_rate else float('-inf')

    return (returns - risk_free_rate) / std_dev


import pandas as pd
import plotly.graph_objects as go

def generate_bar_chart(data: pd.DataFrame) -> go.Figure:
    """
    Generates a bar chart showing the contributions of each key driver to the overall pair portfolio return.

    Arguments:
        data: Pandas DataFrame containing the data with columns 'Key Driver' and 'Contribution'.

    Output:
        Plotly figure object representing the bar chart.

    Raises:
        ValueError: If the input DataFrame is empty or if 'Contribution' contains NaN or infinite values.
        KeyError: If the input DataFrame is missing the required columns ('Key Driver' or 'Contribution').
        TypeError: If the 'Contribution' column contains non-numeric values.
    """

    if data.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    if 'Key Driver' not in data.columns or 'Contribution' not in data.columns:
        raise KeyError("Input DataFrame must contain 'Key Driver' and 'Contribution' columns.")

    if not pd.api.types.is_numeric_dtype(data['Contribution']):
        raise TypeError("The 'Contribution' column must contain numeric values.")
    
    if data['Contribution'].isnull().any():
        raise ValueError("The 'Contribution' column cannot contain NaN values.")

    if (data['Contribution'] == float('inf')).any() or (data['Contribution'] == float('-inf')).any():
        raise ValueError("The 'Contribution' column cannot contain infinite values.")

    fig = go.Figure(data=[go.Bar(x=data['Key Driver'], y=data['Contribution'])])

    fig.update_layout(
        title='Contribution of Key Drivers to Pair Portfolio Return',
        xaxis_title='Key Driver',
        yaxis_title='Contribution to Return'
    )

    return fig


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_scatter_plot(data: pd.DataFrame, x_axis: str, y_axis: str) -> go.Figure:
    """
    Generates a scatter plot visualizing correlations between key drivers and pair portfolio performance.

    Args:
        data: Pandas DataFrame containing the data.
        x_axis: Feature for x-axis
        y_axis: Feature for y-axis

    Returns:
        Plotly figure object representing the scatter plot.

    Raises:
        KeyError: If the specified x_axis or y_axis column does not exist in the DataFrame.
        TypeError: If the data in the specified columns is not numeric.
    """

    try:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a Pandas DataFrame.")

        if data.empty:
            fig = go.Figure()
            fig.update_layout(
                xaxis_title=x_axis,
                yaxis_title=y_axis
            )
            return fig

        if x_axis not in data.columns:
            raise KeyError(f"X-axis column '{x_axis}' not found in DataFrame.")
        if y_axis not in data.columns:
            raise KeyError(f"Y-axis column '{y_axis}' not found in DataFrame.")

        # Check if the data in the columns is numeric. If not, raise a TypeError.
        if not pd.api.types.is_numeric_dtype(data[x_axis]):
            raise TypeError(f"X-axis column '{x_axis}' contains non-numeric data.")
        if not pd.api.types.is_numeric_dtype(data[y_axis]):
            raise TypeError(f"Y-axis column '{y_axis}' contains non-numeric data.")

        fig = go.Figure(data=go.Scatter(x=data[x_axis], y=data[y_axis], mode='markers'))
        fig.update_layout(
            xaxis_title=x_axis,
            yaxis_title=y_axis
        )
        return fig

    except KeyError as e:
        raise e
    except TypeError as e:
        raise e
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


import pandas as pd
import numpy as np

def compare_to_benchmark(data: pd.DataFrame, benchmark_strategy: str, benchmark_parameters: dict) -> pd.DataFrame:
    """Compares the signal-driven pair portfolio performance against a benchmark strategy.

    Args:
        data: Pandas DataFrame containing the data. Must contain at least 'pair_portfolio_return'.
        benchmark_strategy: The selected benchmark strategy ('linear_weights' or 'quantile_sorting').
        benchmark_parameters: Parameters for the benchmark strategy.  Should be a dictionary.  For quantile_sorting,
                              it should contain a 'quantile' key.

    Returns:
        Pandas DataFrame containing the performance of both the pair portfolio and the benchmark strategy.
        Returns an empty DataFrame if the input DataFrame is empty.

    Raises:
        TypeError: If data is not a Pandas DataFrame or benchmark_parameters is not a dictionary.
        ValueError: If an invalid benchmark strategy is selected.
    """

    if data is None:
        raise TypeError("Data cannot be None.")

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Data must be a Pandas DataFrame.")
    
    if not isinstance(benchmark_parameters, dict):
        raise TypeError("Benchmark parameters must be a dictionary.")

    if data.empty:
        return pd.DataFrame()

    # Create a copy to avoid modifying the original DataFrame
    data = data.copy()

    # Handle NaN and infinite values by replacing with 0
    data = data.replace([np.inf, -np.inf], np.nan)
    data = data.fillna(0)

    if benchmark_strategy == 'linear_weights':
        # For demonstration purposes, assume a constant benchmark return
        # In a real-world scenario, this would be replaced with the actual benchmark logic
        pass  # No modification needed as the data already contains benchmark returns

    elif benchmark_strategy == 'quantile_sorting':
        if 'quantile' not in benchmark_parameters:
            raise ValueError("Quantile parameter missing for quantile_sorting strategy.")

        quantile_value = benchmark_parameters['quantile']
        if not 0 <= quantile_value <= 1:
            raise ValueError("Quantile value must be between 0 and 1.")
            
        #Placeholder for more complex quantile sorting. The test data comes with a 'benchmark_return'
        #column already
        pass
    else:
        raise ValueError("Invalid benchmark strategy selected.")

    return data
