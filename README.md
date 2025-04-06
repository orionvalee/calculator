# Simple Python Calculator

This is a command-line calculator program written in Python.

## Features

*   Performs basic arithmetic operations: Addition, Subtraction, Multiplication, Division.
*   Includes additional operations: Exponentiation (Power), Square Root, Modulo.
*   Handles potential errors like division by zero and invalid input.
*   Separates calculation logic (`operations.py`) from the main user interface (`main.py`).

## How to Run

1.  Make sure you have Python installed.
2.  Navigate to the directory containing the `calculator` folder in your terminal.
3.  Run the main script using the command:
    ```bash
    python calculator/main.py
    ```
4.  Follow the prompts to select an operation and enter the required numbers.
5.  The program will ask if you want to perform another calculation after each operation.

## Available Operations

1.  Add
2.  Subtract
3.  Multiply
4.  Divide
5.  Power (x^y)
6.  Square Root
7.  Modulo

## File Structure

*   `calculator/`
    *   `main.py`: The main script that handles user interaction and menu display.
    *   `operations.py`: A module containing the functions for each mathematical operation.
    *   `README.md`: This file. 