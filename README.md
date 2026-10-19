
# Python Log Analyzer

A lightweight Python tool for analyzing application logs and identifying common issues during incident troubleshooting.

## Features

- Counts total log entries.
- Identifies ERROR, WARNING, and INFO messages.
- Detects repeated error messages while ignoring timestamps.
- Filters log entries by severity.
- Generates a text report.
- Includes automated unit tests.

## Project Structure

Python-Log-Analyzer/
├── sample_logs/
│   └── application.log
├── reports/
├── tests/
│   └── test_log_analyzer.py
├── log_analyzer.py
├── requirements.txt
├── .gitignore
└── README.md

## Requirements

- Python 3.10 or later recommended.
- No external Python packages required.

## Run the Analyzer

Clone or download the repository, then open a terminal in the project folder.

powershell
py log_analyzer.py


The generated report is saved to: reports/analysis_report.txt


## Filter Log Entries

Show only ERROR entries:

powershell
py -c "from log_analyzer import analyze_log; print(*analyze_log('sample_logs/application.log', severity='ERROR')['filtered_lines'], sep='\n')"


Change `ERROR` to `WARNING` or `INFO` to filter other levels.

## Run Automated Tests

powershell
py -m unittest discover -s tests -v


## Skills Demonstrated

- Python programming
- File handling and text processing
- Log analysis and incident troubleshooting
- Error pattern detection
- Report generation
- Automated testing
- Git and GitHub fundamentals

## Future Improvements

- Support for additional log formats.
- CSV and JSON report exports.
- Date and time range filtering.
- Command-line arguments.
- More robust parsing of structured application logs.
