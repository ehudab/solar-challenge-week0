"""
Unit tests for EDA Utilities Module

This script contains unit tests for the functions in the eda_utils module.
"""

import unittest
import pandas as pd
import numpy as np
from src.eda_utils import EDAUtils

class TestEDAUtils(unittest.TestCase):

    def setUp(self):
        """
        Set up a sample DataFrame for testing.
        """
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, np.nan, 2, 1],
            'C': [10, 20, 30, 40, 50],
            'D': [100, 200, 300, 400, 500]
        })

    def test_calculate_summary_statistics(self):
        """
        Test summary statistics calculation.
        """
        summary = EDAUtils.calculate_summary_statistics(self.df)
        self.assertEqual(summary.loc['mean', 'A'], 3)

    def test_detect_outliers(self):
        """
        Test outlier detection.
        """
        outliers = EDAUtils.detect_outliers(self.df, ['A', 'B'], threshold=2)
        self.assertTrue(outliers['A'].sum() == 0)

    def test_handle_missing_values(self):
        """
        Test missing value handling.
        """
        df_filled = EDAUtils.handle_missing_values(self.df, strategy="median", columns=['B'])
        self.assertEqual(df_filled['B'].isna().sum(), 0)

    def test_export_cleaned_data(self):
        """
        Test exporting cleaned data.
        """
        EDAUtils.export_cleaned_data(self.df, "test.csv")
        loaded_df = pd.read_csv("test.csv")
        self.assertTrue(loaded_df.equals(self.df))

    def test_plot_correlation_heatmap(self):
        """
        Test plotting correlation heatmap.
        """
        try:
            EDAUtils.plot_correlation_heatmap(self.df)
        except Exception as e:
            self.fail(f"plot_correlation_heatmap raised an exception: {e}")

    def test_plot_scatter(self):
        """
        Test plotting scatter plot.
        """
        try:
            EDAUtils.plot_scatter(self.df, 'A', 'B')
        except Exception as e:
            self.fail(f"plot_scatter raised an exception: {e}")

    def test_plot_histogram(self):
        """
        Test plotting histogram.
        """
        try:
            EDAUtils.plot_histogram(self.df, 'A')
        except Exception as e:
            self.fail(f"plot_histogram raised an exception: {e}")

    def test_plot_time_series(self):
        """
        Test plotting time series.
        """
        self.df['Timestamp'] = pd.date_range(start='2023-01-01', periods=len(self.df), freq='D')
        try:
            EDAUtils.plot_time_series(self.df, 'Timestamp', ['A', 'B'])
        except Exception as e:
            self.fail(f"plot_time_series raised an exception: {e}")

    def test_create_bubble_chart(self):
        """
        Test creating bubble chart.
        """
        try:
            EDAUtils.create_bubble_chart(self.df, 'A', 'B', 'C')
        except Exception as e:
            self.fail(f"create_bubble_chart raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()