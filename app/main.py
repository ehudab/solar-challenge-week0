import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Update DATA_PATH to use an absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "src", "data")

# Dashboard styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #e3f2fd;
    }
    h1 {
        color: #0d47a1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a header image or logo (optional)
st.image(
    "https://via.placeholder.com/800x200?text=Solar+Potential+Dashboard",
    use_container_width=True
)

def main():
    data_files = {
        'Benin': os.path.join(DATA_PATH, "benin_clean.csv"),
        'Sierra Leone': os.path.join(DATA_PATH, "sierraleone-bumbuna.csv"),
        'Togo': os.path.join(DATA_PATH, "togo-dapaong_qc.csv")
    }

    st.title("Solar Potential Dashboard")

    # Check for missing files
    missing_files = [file for file in data_files.values() if not os.path.exists(file)]
    if missing_files:
        st.error(f"The following files are missing: {', '.join(missing_files)}")
        return

    # Country selection widget
    st.sidebar.header("Select Country")
    selected_countries = st.sidebar.multiselect(
        "Choose countries to visualize:",
        options=list(data_files.keys()),
        default=list(data_files.keys())
    )

    # Metric selection widget
    st.sidebar.header("Select Metric")
    selected_metric = st.sidebar.selectbox(
        "Choose a metric to visualize:",
        options=['GHI', 'DNI', 'DHI']
    )

    # Load and display selected data
    if selected_countries:
        combined_data = []
        for country in selected_countries:
            df = pd.read_csv(data_files[country])
            df['Country'] = country
            combined_data.append(df)

        combined_data = pd.concat(combined_data)

        # Boxplot visualization
        st.subheader(f"Boxplot of {selected_metric} Across Selected Countries")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=combined_data, x='Country', y=selected_metric, palette='Set2', ax=ax)
        ax.set_title(f"{selected_metric} Comparison Across Countries")
        st.pyplot(fig)

        # Top regions table (updated to exclude 'Region')
        st.subheader(f"Top 10 {selected_metric} Values Across Selected Countries")
        top_regions = combined_data[[selected_metric, 'Country']].sort_values(by=selected_metric, ascending=False).head(10)
        st.write(top_regions)

if __name__ == "__main__":
    main()