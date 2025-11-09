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