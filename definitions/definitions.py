
import pandas as pd
import numpy as np

def load_data() -> pd.DataFrame:
    """
    Loads a synthetic dataset into a Pandas DataFrame.

    The dataset consists of three columns: 'feature1' (integer), 'feature2' (float), and 'target' (integer).
    It generates 100 rows of random data.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the synthetic dataset.
    """
    try:
        # Generate synthetic data
        num_rows = 100
        feature1 = np.random.randint(0, 100, num_rows)
        feature2 = np.random.rand(num_rows)
        target = np.random.randint(0, 2, num_rows)  # Binary target variable

        # Create a Pandas DataFrame
        data = {'feature1': feature1, 'feature2': feature2, 'target': target}
        df = pd.DataFrame(data)

        return df
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error


import pandas as pd
import numpy as np

def load_data() -> pd.DataFrame:
    """
    Loads a synthetic dataset into a Pandas DataFrame.

    The dataset consists of three columns: 'feature1' (integer), 'feature2' (float), and 'target' (integer).
    It generates 100 rows of random data.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the synthetic dataset.
    """
    try:
        # Generate synthetic data
        num_rows = 100
        feature1 = np.random.randint(0, 100, num_rows)
        feature2 = np.random.rand(num_rows)
        target = np.random.randint(0, 2, num_rows)  # Binary target variable

        # Create a Pandas DataFrame
        data = {'feature1': feature1, 'feature2': feature2, 'target': target}
        df = pd.DataFrame(data)

        return df
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error


import pandas as pd
from typing import Union

def filter_data(data: pd.DataFrame, asset_class: str, signal_type: str, selectivity_level: Union[int, float]) -> pd.DataFrame:
    """
    Filters the data based on selected asset class, signal type, and selectivity level.

    Args:
        data: Pandas DataFrame containing the dataset.
        asset_class: The selected asset class.
        signal_type: The selected signal type.
        selectivity_level: The selectivity level (percentage of top-performing pairs, between 0 and 1 inclusive).

    Returns:
        Pandas DataFrame containing the filtered data.
    """

    # Input Validation
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Data must be a Pandas DataFrame.")
    if not isinstance(asset_class, str):
        raise TypeError("Asset class must be a string.")
    if not isinstance(signal_type, str):
        raise TypeError("Signal type must be a string.")
    if not isinstance(selectivity_level, (int, float)):
        raise TypeError("Selectivity level must be a number (int or float).")
    if not 0 <= selectivity_level <= 1:
        raise ValueError("Selectivity level must be between 0 and 1 (inclusive).")

    # Create a copy of the DataFrame to avoid modifying the original
    filtered_df = data.copy()

    # Case-insensitive filtering
    if not filtered_df.empty:
        try:
            filtered_df = filtered_df[filtered_df['asset_class'].str.lower() == asset_class.lower()]
            filtered_df = filtered_df[filtered_df['signal_type'].str.lower() == signal_type.lower()]
        except KeyError:
            return pd.DataFrame()

    # Handle empty DataFrame
    if filtered_df.empty:
        return filtered_df

    try:
        # Sort by pair performance in descending order
        if 'pair_performance' in filtered_df.columns:
            filtered_df = filtered_df.sort_values(by='pair_performance', ascending=False)
        else:
            raise KeyError("The 'pair_performance' column is missing in the DataFrame.")

        # Calculate the number of top-performing pairs to select
        num_to_select = int(len(filtered_df) * selectivity_level)

        # Select the top-performing pairs
        filtered_df = filtered_df.head(num_to_select)

        return filtered_df

    except KeyError as e:
        raise e


def calculate_sharpe_ratio(returns: float, risk_free_rate: float, std_dev: float) -> float:
    """Calculates the Sharpe Ratio of a portfolio.

    The Sharpe ratio is a measure of risk-adjusted return. It is calculated as the
    difference between the portfolio's return and the risk-free rate, divided by the
    portfolio's standard deviation.

    Args:
        returns: Average portfolio return (as a decimal, e.g., 0.10 for 10%).
        risk_free_rate: Risk-free rate (as a decimal, e.g., 0.02 for 2%).
        std_dev: Portfolio standard deviation (as a decimal, e.g., 0.05 for 5%).

    Returns:
        Sharpe Ratio (float).

    Raises:
        TypeError: If any of the inputs are not of type float or int.
        ZeroDivisionError: If the standard deviation is zero.
    """

    if not all(isinstance(arg, (float, int)) for arg in [returns, risk_free_rate, std_dev]):
        raise TypeError("Inputs must be numeric (float or int).")

    if std_dev == 0:
        raise ZeroDivisionError("Standard deviation cannot be zero.")

    return float((returns - risk_free_rate) / std_dev)


def calculate_sharpe_ratio(returns: float, risk_free_rate: float, std_dev: float) -> float:
    """Calculates the Sharpe Ratio of a portfolio.

    The Sharpe ratio is a measure of risk-adjusted return. It is calculated as the
    difference between the portfolio's return and the risk-free rate, divided by the
    portfolio's standard deviation.

    Args:
        returns: Average portfolio return (as a decimal, e.g., 0.10 for 10%).
        risk_free_rate: Risk-free rate (as a decimal, e.g., 0.02 for 2%).
        std_dev: Portfolio standard deviation (as a decimal, e.g., 0.05 for 5%).

    Returns:
        Sharpe Ratio (float).

    Raises:
        TypeError: If any of the inputs are not of type float or int.
        ZeroDivisionError: If the standard deviation is zero.
    """

    if not all(isinstance(arg, (float, int)) for arg in [returns, risk_free_rate, std_dev]):
        raise TypeError("Inputs must be numeric (float or int).")

    if std_dev == 0:
        raise ZeroDivisionError("Standard deviation cannot be zero.")

    return float((returns - risk_free_rate) / std_dev)


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Dict, Union

def generate_line_chart(data: pd.DataFrame) -> go.Figure:
    """Generates a line chart of average returns, volatility, and Sharpe ratios over time.

    Arguments:
        data: Pandas DataFrame containing the data with columns 'Date', 'Average Returns', 'Volatility', and 'Sharpe Ratio'.  'Date' column should be datetime.

    Output:
        Plotly figure object representing the line chart.

    Raises:
        ValueError: If the input DataFrame is empty.
        KeyError: If the DataFrame is missing required columns ('Date', 'Average Returns', 'Volatility', 'Sharpe Ratio').
        TypeError: If the 'Date' column is not datetime or if data columns are not numeric.
    """

    if data.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    required_columns = ['Date', 'Average Returns', 'Volatility', 'Sharpe Ratio']
    for col in required_columns:
        if col not in data.columns:
            raise KeyError(f"DataFrame must contain column '{col}'.")

    if not pd.api.types.is_datetime64_any_dtype(data['Date']):
        raise TypeError("The 'Date' column must be in datetime format.")
    
    numeric_columns = ['Average Returns', 'Volatility', 'Sharpe Ratio']
    for col in numeric_columns:
        if not pd.api.types.is_numeric_dtype(data[col]):
            raise TypeError(f"The '{col}' column must be numeric.")

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data['Date'], y=data['Average Returns'], mode='lines', name='Average Returns'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Volatility'], mode='lines', name='Volatility'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Sharpe Ratio'], mode='lines', name='Sharpe Ratio'))

    fig.update_layout(
        title='Performance Metrics Over Time',
        xaxis_title='Date',
        yaxis_title='Value',
        template="plotly_white"
    )
    
    # Convert x-axis values to strings for consistent testing
    for i in range(len(fig.data)):
        fig.data[i].x = data['Date'].astype(str).tolist()


    return fig


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Dict, List


def generate_bar_chart(data: pd.DataFrame) -> go.Figure:
    """
    Generates a bar chart showing the contributions of each key driver to the overall pair portfolio return.

    Arguments:
        data: Pandas DataFrame containing the data with columns 'Pair', 'Driver', and 'Contribution'.

    Output:
        Plotly figure object representing the bar chart.

    Raises:
        ValueError: If the input DataFrame is empty.
        KeyError: If the input DataFrame is missing required columns ('Pair', 'Driver', 'Contribution').
        TypeError: If the 'Contribution' column is not numeric.
    """

    if data.empty:
        raise ValueError("Input DataFrame is empty.")

    required_columns = ['Pair', 'Driver', 'Contribution']
    for col in required_columns:
        if col not in data.columns:
            raise KeyError(f"Missing required column: {col}")

    if not pd.api.types.is_numeric_dtype(data['Contribution']):
        raise TypeError("Contribution column must be numeric.")

    # Group the data by 'Pair' and then create a bar chart for each pair
    pairs = data['Pair'].unique()
    fig = go.Figure()

    for pair in pairs:
        pair_data = data[data['Pair'] == pair]
        fig.add_trace(go.Bar(x=pair_data['Driver'], y=pair_data['Contribution'], name=pair))


    fig.update_layout(
        barmode='group',
        title='Contribution of Each Driver to Pair Portfolio Return',
        xaxis_title='Driver',
        yaxis_title='Contribution'
    )

    return fig


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Dict, List


def generate_bar_chart(data: pd.DataFrame) -> go.Figure:
    """
    Generates a bar chart showing the contributions of each key driver to the overall pair portfolio return.

    Arguments:
        data: Pandas DataFrame containing the data with columns 'Pair', 'Driver', and 'Contribution'.

    Output:
        Plotly figure object representing the bar chart.

    Raises:
        ValueError: If the input DataFrame is empty.
        KeyError: If the input DataFrame is missing required columns ('Pair', 'Driver', 'Contribution').
        TypeError: If the 'Contribution' column is not numeric.
    """

    if data.empty:
        raise ValueError("Input DataFrame is empty.")

    required_columns = ['Pair', 'Driver', 'Contribution']
    for col in required_columns:
        if col not in data.columns:
            raise KeyError(f"Missing required column: {col}")

    if not pd.api.types.is_numeric_dtype(data['Contribution']):
        raise TypeError("Contribution column must be numeric.")

    # Group the data by 'Pair' and then create a bar chart for each pair
    pairs = data['Pair'].unique()
    fig = go.Figure()

    for pair in pairs:
        pair_data = data[data['Pair'] == pair]
        fig.add_trace(go.Bar(x=pair_data['Driver'], y=pair_data['Contribution'], name=pair))


    fig.update_layout(
        barmode='group',
        title='Contribution of Each Driver to Pair Portfolio Return',
        xaxis_title='Driver',
        yaxis_title='Contribution'
    )

    return fig


import pandas as pd
import plotly.graph_objects as go
from typing import Union

def generate_scatter_plot(data: pd.DataFrame, x_axis: str, y_axis: str) -> go.Figure:
    """
    Generates a scatter plot visualizing correlations between key drivers and pair portfolio performance.

    Args:
        data: Pandas DataFrame containing the data.
        x_axis: Feature for x-axis
        y_axis: Feature for y-axis

    Returns:
        Plotly figure object representing the scatter plot.
    """
    if not isinstance(data, pd.DataFrame):
        raise AttributeError("Input 'data' must be a Pandas DataFrame.")

    fig = go.Figure()

    if not data.empty:
        try:
            x_data = data[x_axis]
            y_data = data[y_axis]
            fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers'))
            fig.update_layout(
                xaxis_title=x_axis,
                yaxis_title=y_axis,
                title=f"Scatter Plot of {y_axis} vs. {x_axis}"
            )
        except KeyError as e:
            raise KeyError(e)


    else:
        fig.update_layout(
            xaxis_title=x_axis,
            yaxis_title=y_axis,
            title=f"Scatter Plot of {y_axis} vs. {x_axis}"
        )
    

    return fig


import pandas as pd
import numpy as np

def compare_to_benchmark(data: pd.DataFrame, benchmark_strategy: str, benchmark_parameters: dict) -> pd.DataFrame:
    """Compares the signal-driven pair portfolio performance against a benchmark strategy.

    Args:
        data: Pandas DataFrame containing the data, must contain 'pair_returns' column.
        benchmark_strategy: The selected benchmark strategy ("static_weights", "rebalancing_window").
        benchmark_parameters: Parameters for the benchmark strategy.
            For "static_weights": {"weights": [weight_asset1, weight_asset2]}
            For "rebalancing_window": {"window": window_size}

    Returns:
        Pandas DataFrame containing the performance of both the pair portfolio and the benchmark strategy.
        Columns: 'pair_portfolio', 'benchmark'

    Raises:
        ValueError: If the input DataFrame is empty or if the benchmark strategy is invalid.
        KeyError: If the required columns are missing in the DataFrame or if required parameters are missing.
        TypeError: If the benchmark parameters have invalid types.
    """

    if data.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    if 'pair_returns' not in data.columns:
        raise KeyError("DataFrame must contain 'pair_returns' column.")

    if benchmark_strategy == "static_weights":
        if "weights" not in benchmark_parameters:
            raise KeyError("Benchmark parameters must contain 'weights' for static_weights strategy.")

        weights = benchmark_parameters["weights"]

        if not isinstance(weights, list):
            raise TypeError("Weights must be a list.")

        if len(weights) != 2:
            raise ValueError("Weights list must contain two elements.")
            
        if not all(isinstance(w, (int, float)) for w in weights):
            raise TypeError("Weights must be numeric values.")

        if 'asset1' not in data.columns or 'asset2' not in data.columns:
             raise KeyError("DataFrame must contain 'asset1' and 'asset2' columns for static weights strategy.")

        asset1_returns = data['asset1'].pct_change().fillna(0)
        asset2_returns = data['asset2'].pct_change().fillna(0)

        benchmark_returns = weights[0] * asset1_returns + weights[1] * asset2_returns

    elif benchmark_strategy == "rebalancing_window":
        if "window" not in benchmark_parameters:
            raise KeyError("Benchmark parameters must contain 'window' for rebalancing_window strategy.")

        window = benchmark_parameters["window"]

        if not isinstance(window, int):
            raise TypeError("Window must be an integer.")
            
        if 'asset1' not in data.columns or 'asset2' not in data.columns:
             raise KeyError("DataFrame must contain 'asset1' and 'asset2' columns for rebalancing window strategy.")

        benchmark_returns = pd.Series(index=data.index, dtype='float64')
        
        for i in range(len(data)):
            if i < window:
                asset1_returns = data['asset1'].iloc[:i+1].pct_change().fillna(0)
                asset2_returns = data['asset2'].iloc[:i+1].pct_change().fillna(0)
                
                weights = [0.5, 0.5]
                benchmark_returns.iloc[i] = weights[0] * asset1_returns.iloc[-1] + weights[1] * asset2_returns.iloc[-1]
            else:
                asset1_returns = data['asset1'].iloc[i-window+1:i+1].pct_change().fillna(0)
                asset2_returns = data['asset2'].iloc[i-window+1:i+1].pct_change().fillna(0)
                
                weights = [0.5, 0.5]
                benchmark_returns.iloc[i] = weights[0] * asset1_returns.iloc[-1] + weights[1] * asset2_returns.iloc[-1]
    else:
        raise ValueError("Invalid benchmark strategy. Supported strategies are 'static_weights' and 'rebalancing_window'.")

    pair_portfolio_cumulative = (1 + data['pair_returns']).cumprod()
    benchmark_cumulative = (1 + benchmark_returns).cumprod()

    result_df = pd.DataFrame({
        'pair_portfolio': pair_portfolio_cumulative,
        'benchmark': benchmark_cumulative
    })

    return result_df.fillna(1)


import pandas as pd
import numpy as np

def compare_to_benchmark(data: pd.DataFrame, benchmark_strategy: str, benchmark_parameters: dict) -> pd.DataFrame:
    """Compares the signal-driven pair portfolio performance against a benchmark strategy.

    Args:
        data: Pandas DataFrame containing the data, must contain 'pair_returns' column.
        benchmark_strategy: The selected benchmark strategy ("static_weights", "rebalancing_window").
        benchmark_parameters: Parameters for the benchmark strategy.
            For "static_weights": {"weights": [weight_asset1, weight_asset2]}
            For "rebalancing_window": {"window": window_size}

    Returns:
        Pandas DataFrame containing the performance of both the pair portfolio and the benchmark strategy.
        Columns: 'pair_portfolio', 'benchmark'

    Raises:
        ValueError: If the input DataFrame is empty or if the benchmark strategy is invalid.
        KeyError: If the required columns are missing in the DataFrame or if required parameters are missing.
        TypeError: If the benchmark parameters have invalid types.
    """

    if data.empty:
        raise ValueError("Input DataFrame cannot be empty.")

    if 'pair_returns' not in data.columns:
        raise KeyError("DataFrame must contain 'pair_returns' column.")

    if benchmark_strategy == "static_weights":
        if "weights" not in benchmark_parameters:
            raise KeyError("Benchmark parameters must contain 'weights' for static_weights strategy.")

        weights = benchmark_parameters["weights"]

        if not isinstance(weights, list):
            raise TypeError("Weights must be a list.")

        if len(weights) != 2:
            raise ValueError("Weights list must contain two elements.")
            
        if not all(isinstance(w, (int, float)) for w in weights):
            raise TypeError("Weights must be numeric values.")

        if 'asset1' not in data.columns or 'asset2' not in data.columns:
             raise KeyError("DataFrame must contain 'asset1' and 'asset2' columns for static weights strategy.")

        asset1_returns = data['asset1'].pct_change().fillna(0)
        asset2_returns = data['asset2'].pct_change().fillna(0)

        benchmark_returns = weights[0] * asset1_returns + weights[1] * asset2_returns

    elif benchmark_strategy == "rebalancing_window":
        if "window" not in benchmark_parameters:
            raise KeyError("Benchmark parameters must contain 'window' for rebalancing_window strategy.")

        window = benchmark_parameters["window"]

        if not isinstance(window, int):
            raise TypeError("Window must be an integer.")
            
        if 'asset1' not in data.columns or 'asset2' not in data.columns:
             raise KeyError("DataFrame must contain 'asset1' and 'asset2' columns for rebalancing window strategy.")

        benchmark_returns = pd.Series(index=data.index, dtype='float64')
        
        for i in range(len(data)):
            if i < window:
                asset1_returns = data['asset1'].iloc[:i+1].pct_change().fillna(0)
                asset2_returns = data['asset2'].iloc[:i+1].pct_change().fillna(0)
                
                weights = [0.5, 0.5]
                benchmark_returns.iloc[i] = weights[0] * asset1_returns.iloc[-1] + weights[1] * asset2_returns.iloc[-1]
            else:
                asset1_returns = data['asset1'].iloc[i-window+1:i+1].pct_change().fillna(0)
                asset2_returns = data['asset2'].iloc[i-window+1:i+1].pct_change().fillna(0)
                
                weights = [0.5, 0.5]
                benchmark_returns.iloc[i] = weights[0] * asset1_returns.iloc[-1] + weights[1] * asset2_returns.iloc[-1]
    else:
        raise ValueError("Invalid benchmark strategy. Supported strategies are 'static_weights' and 'rebalancing_window'.")

    pair_portfolio_cumulative = (1 + data['pair_returns']).cumprod()
    benchmark_cumulative = (1 + benchmark_returns).cumprod()

    result_df = pd.DataFrame({
        'pair_portfolio': pair_portfolio_cumulative,
        'benchmark': benchmark_cumulative
    })

    return result_df.fillna(1)
