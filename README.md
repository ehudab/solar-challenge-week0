# Solar Challenge Week 0

## How to Reproduce the Environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ehudab/solar-challenge-week0.git
   cd solar-challenge-week0
   ```

2. **Set Up Python Virtual Environment**
   - Using `venv`:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: .\venv\Scripts\activate
     ```
   - Using `conda` (if preferred):
     ```bash
     conda create -n solar-challenge python=3.9 -y
     conda activate solar-challenge
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run CI Locally (Optional)**
   ```bash
   python --version
   pip install -r requirements.txt
   ```

5. **Merge `setup-task` into `main` via a Pull Request**
   - Push the `setup-task` branch to GitHub:
     ```bash
     git push -u origin setup-task
     ```
   - Open a Pull Request on GitHub to merge `setup-task` into `main`.

## Exploratory Data Analysis Notebooks

### Overview
This repository contains EDA notebooks for analyzing solar datasets from different countries. Each notebook provides a structured approach to data cleaning, analysis, and visualization.

### Notebooks

#### Togo EDA Notebook
- **File**: `notebooks/togo_eda.ipynb`
- **Features**:
  - Summary statistics and missing value report
  - Outlier detection and cleaning
  - Time series analysis
  - Cleaning impact analysis
  - Correlation and relationship exploration
  - Wind distribution analysis
  - Temperature analysis

#### Sierra Leone EDA Notebook
- **File**: `notebooks/sierraleone_eda.ipynb`
- **Features**:
  - Summary statistics and missing value report
  - Outlier detection and cleaning
  - Time series analysis
  - Cleaning impact analysis
  - Correlation and relationship exploration
  - Wind distribution analysis
  - Temperature analysis
  - Bubble chart visualization

### How to Run
1. Ensure the environment is set up as described above.
2. Open the desired notebook in Jupyter or VS Code.
3. Execute the cells sequentially to reproduce the analysis and visualizations.