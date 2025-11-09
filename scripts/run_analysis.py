import sys
import os
import pandas as pd

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from eda_utils import EDAUtils

def main():
    """
    Orchestrates the EDA process by loading data, performing analysis, and generating outputs.
    """
    # Initialize the EDA utility
    eda = EDAUtils()

    # Load the dataset (example: Benin dataset)
    data_path = "src/data/benin_clean.csv"
    df = pd.read_csv(data_path)

    # Perform EDA operations
    print("Summary Statistics:")
    print(eda.calculate_summary_statistics(df))

    eda.plot_correlation_heatmap(df)
    eda.plot_scatter(df, x="A", y="B")
    eda.plot_histogram(df, column="A")

    # Handle missing values
    df_cleaned = eda.handle_missing_values(df, strategy="median")

    # Export cleaned data
    eda.export_cleaned_data(df_cleaned, "src/data/benin_cleaned_output.csv")

if __name__ == "__main__":
    main()