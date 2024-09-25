# E-commerce Automation Framework

This repository contains an automation framework developed using Selenium with Python for testing an e-commerce website. The framework utilizes Pytest for test case management, generates HTML reports for test execution summaries, and interacts with Excel files for data-driven testing. It covers various test scenarios including search functionality, filters, sorting, header links, etc.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Selenium WebDriver
- Pytest
- pytest-html
- Openpyxl
- pytest-metadata
- pytest-xdist

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies.

## Usage

1. Navigate to the project directory.
2. Execute tests using **run_tests.bat**.
3. To generate HTML reports.

## Running Tests

To run the tests in your project, use the following commands:

### Run All Tests
Run all test cases located in the `testCases` folder:
```bash
pytest -v -s testCases/
```
To run all testcases in testCases folder and generate `html reports`
```bash
pytest -v -s --html=./Reports/automation_report.html testCases/ --browser=chrome
```
Run test cases marked with sanity. You can replace "`sanity`" with "`regression`" or "`smoke`" to run the respective test groups:
```bash
pytest -v -s -m "sanity" testCases/ --browser=chrome
```
## Structure
ecommerce-automation/

├── testCases/ # Test case files

├── pageObjects/ # Page object files

├── TestData/ # Test data files (Excel, CSV, etc.)

├── utilities/ # Utility files

├── Reports/ # Test execution reports

├── config.ini # Configuration file

├── requirements.txt # Python dependencies

└── README.md # Project documentation
