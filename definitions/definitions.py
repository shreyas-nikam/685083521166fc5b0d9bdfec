
import pandas as pd
import numpy as np

def load_data() -> pd.DataFrame:
    """Loads the synthetic dataset into a Pandas DataFrame.

    Arguments: None
    Output: Pandas DataFrame containing the dataset.
    """
    try:
        # Generate synthetic data
        data = {
            'col1': np.random.randint(0, 100, 10),
            'col2': np.random.rand(10),
            'col3': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
        }

        # Create Pandas DataFrame
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
