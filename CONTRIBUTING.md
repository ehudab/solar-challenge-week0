# Contributing to Solar Challenge Week 0

Thank you for considering contributing to this project! We welcome contributions that improve the repository's functionality, structure, and documentation.

## Repository Structure

- **`src/`**: Contains reusable Python modules for EDA tasks.
  - `eda_utils.py`: Core utility functions for data analysis.
- **`notebooks/`**: Jupyter notebooks for country-specific EDA.
- **`scripts/`**: Entry-point scripts for orchestrating the EDA process.
- **`tests/`**: Unit tests for the `src/` modules.
- **`data/`**: Contains raw and cleaned datasets (excluded from version control).

## Naming Conventions

- **Branches**: Use the format `eda-<country>` (e.g., `eda-benin`).
- **Files**: Use lowercase with underscores (e.g., `eda_utils.py`).
- **Commits**: Follow the convention `<type>: <description>` (e.g., `fix: correct CI workflow`).

## Contribution Guidelines

1. **Fork the Repository**: Create a fork of the repository on GitHub.
2. **Create a Branch**: Create a new branch for your changes.
   ```bash
   git checkout -b <branch-name>
   ```
3. **Make Changes**: Implement your changes, ensuring they align with the project's structure and guidelines.
4. **Run Tests**: Ensure all tests pass before submitting your changes.
   ```bash
   python -m unittest discover -s tests
   ```
5. **Submit a Pull Request**: Open a pull request with a clear title and description.

## Mapping of Notebooks to Outputs

| Notebook               | Output Files                     |
|------------------------|----------------------------------|
| `benin_eda.ipynb`      | `benin_clean.csv`               |
| `sierraleone_eda.ipynb`| `sierraleone_clean.csv`         |
| `togo_eda.ipynb`       | `togo_clean.csv`                |

## Code Style

- Use `black` for code formatting:
  ```bash
  black .
  ```
- Use `flake8` for linting:
  ```bash
  flake8 .
  ```

Thank you for contributing!