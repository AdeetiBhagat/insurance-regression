# Project Title
insurance-regression
## Project Description
We created a regression model for the insurance dataset and saved it as a 
Python file. 
## Dataset
- **Name**: insurance-1.csv
- **Description**: This dataset contains information about insurance charges, including features such as age, sex, BMI, children, smoker status, region, and charges.
## Project Structure
The structure of your project directory. 
├── .github
│ └── workflows
│ └── ci-cd.yml
├── Data
│ └── insurance-1.csv
├── Model
│ ├── regression_model.py
│ ├── test_regression_model.py
├── Test
│ ├── insurance-1.csv
│ ├── test_regression_model.py
└── .gitignore
└── README.md

## Installation
Instructions on how to set up the project.
1. **Clone the repository:**
   git clone https://github.com/AdeetiBhagat/insurance-regression
   cd your-repo
2. **Create a virtual environment and activate it:**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

CI/CD Pipeline
CI/CD Tool: GitHub Actions
Stages:
Linting: Uses flake8 to check for syntax errors and code quality.
Testing: Runs unit tests using pytest.
Deployment: Placeholder for deployment steps.




