# Advanced Calculator Midterm

## Project Overview

This project is an advanced calculator application built in Python. It includes a command-line interface (REPL), multiple arithmetic operations, calculation history tracking, CSV save/load functionality, environment-based configuration, logging, unit testing, GitHub Actions, and several software design patterns.

The goal of this project was to create a calculator that is more than just basic arithmetic. It was designed to be structured, modular, testable, and easier to maintain by using object-oriented programming and design patterns.

---

## Features

The calculator supports the following arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division
- Power
- Root
- Modulo
- Integer Division
- Percentage Difference
- Percentage Change

The calculator also includes:

- Command-line REPL interface
- Calculation history tracking
- Save history to CSV
- Load history from CSV
- Undo and redo functionality
- Logging to a file
- Configuration using `.env`
- Automated unit testing with pytest
- Coverage reporting
- GitHub Actions CI workflow

---

## Project Structure

```text
advanced_calculator_midterm/
│
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── command.py
│   ├── config.py
│   ├── exceptions.py
│   ├── facade.py
│   ├── history.py
│   ├── logger_setup.py
│   ├── memento.py
│   ├── observers.py
│   ├── operation_factory.py
│   ├── operations.py
│   └── repl.py
│
├── data/
│   └── calculator_history.csv
│
├── logs/
│
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_config.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   └── test_repl.py
│
├── .github/
│   └── workflows/
│       └── python-app.yml
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── pytest.ini
├── README.md
└── requirements.txt