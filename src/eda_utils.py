"""
EDA Utilities Module

This module contains reusable functions for exploratory data analysis tasks.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

class EDAUtils:
    """
    A utility class for performing exploratory data analysis (EDA) tasks.
    
    This class contains static methods for various EDA operations, such as calculating summary statistics,
    detecting outliers, plotting visualizations, and handling missing values. Each method is designed to
    work with pandas DataFrames and provides flexibility for different use cases.
    """

    @staticmethod
    def calculate_summary_statistics(df):
        """
        Calculate summary statistics for a DataFrame.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: Summary statistics.
        """
        # Calculate summary statistics for the DataFrame
        return df.describe()

    @staticmethod
    def detect_outliers(df, columns, threshold=3):
        """
        Detect outliers in specified columns using Z-scores.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            columns (list): List of column names to check for outliers.
            threshold (float): Z-score threshold for outlier detection.

        Returns:
            pd.DataFrame: DataFrame with outliers flagged.
        """
        # Calculate Z-scores of the specified columns
        z_scores = df[columns].apply(zscore)
        # Flag outliers based on the Z-score threshold
        return (z_scores.abs() > threshold)

    @staticmethod
    def plot_correlation_heatmap(df):
        """
        Plot a correlation heatmap for a DataFrame.

        Parameters:
            df (pd.DataFrame): The input DataFrame.

        Returns:
            None
        """
        # Plot a heatmap of the correlation matrix
        plt.figure(figsize=(12, 8))
        correlation_matrix = df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Correlation Heatmap")
        plt.show()

    @staticmethod
    def plot_scatter(df, x, y):
        """
        Plot a scatter plot for two variables.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            x (str): Column name for the x-axis.
            y (str): Column name for the y-axis.

        Returns:
            None
        """
        # Create a scatter plot for the specified variables
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=x, y=y)
        plt.title(f"Scatter Plot: {x} vs {y}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid()
        plt.show()

    @staticmethod
    def handle_missing_values(df, strategy="median", columns=None):
        """
        Handle missing values in a DataFrame.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            strategy (str): Strategy for handling missing values ("median", "mean", "drop").
            columns (list): List of columns to apply the strategy. If None, applies to all columns.

        Returns:
            pd.DataFrame: DataFrame with missing values handled.
        """
        # Determine columns to process
        if columns is None:
            columns = df.columns

        # Handle missing values based on the specified strategy
        if strategy == "median":
            for col in columns:
                df[col] = df[col].fillna(df[col].median())
        elif strategy == "mean":
            for col in columns:
                df[col] = df[col].fillna(df[col].mean())
        elif strategy == "drop":
            df = df.dropna()
        else:
            raise ValueError("Invalid strategy. Choose from 'median', 'mean', or 'drop'.")

        return df

    @staticmethod
    def plot_histogram(df, column, bins=30):
        """
        Plot a histogram for a specific column.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            column (str): Column name to plot.
            bins (int): Number of bins for the histogram.

        Returns:
            None
        """
        # Plot a histogram of the specified column
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True, bins=bins)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()

    @staticmethod
    def export_cleaned_data(df, file_path):
        """
        Export cleaned DataFrame to a CSV file.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            file_path (str): Path to save the CSV file.

        Returns:
            None
        """
        # Export the DataFrame to a CSV file
        df.to_csv(file_path, index=False)
        print(f"Cleaned data saved to {file_path}")

    @staticmethod
    def plot_time_series(df, timestamp_column, value_columns):
        """
        Plot time series for specified value columns.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            timestamp_column (str): Column name for timestamps.
            value_columns (list): List of column names to plot.

        Returns:
            None
        """
        # Convert the timestamp column to datetime format
        df[timestamp_column] = pd.to_datetime(df[timestamp_column])
        # Plot each value column as a separate time series
        for column in value_columns:
            plt.figure(figsize=(10, 6))
            plt.plot(df[timestamp_column], df[column], label=column)
            plt.title(f"Time Series of {column}")
            plt.xlabel("Timestamp")
            plt.ylabel(column)
            plt.legend()
            plt.grid()
            plt.show()

    @staticmethod
    def create_bubble_chart(df, x, y, bubble_size, color_column=None):
        """
        Create a bubble chart.

        Parameters:
            df (pd.DataFrame): The input DataFrame.
            x (str): Column name for the x-axis.
            y (str): Column name for the y-axis.
            bubble_size (str): Column name for bubble sizes.
            color_column (str): Column name for bubble colors (optional).

        Returns:
            None
        """
        # Create a bubble chart with optional color coding
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(
            df[x], df[y], s=df[bubble_size], alpha=0.6,
            c=df[color_column] if color_column else df[bubble_size], cmap='viridis', edgecolor='k'
        )
        plt.colorbar(scatter, label=color_column if color_column else bubble_size)
        plt.title(f"Bubble Chart: {x} vs {y} with Bubble Size Representing {bubble_size}")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid()
        plt.show()