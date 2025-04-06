# Python Calculator with GUI

This is a calculator program written in Python, featuring both a command-line interface and a graphical user interface (GUI) built with Tkinter.

## Features

*   **Graphical User Interface (`gui.py`)**:
    *   Intuitive button layout for all operations.
    *   Display area showing the current number and calculation history.
    *   Keyboard support for digits, operators, Enter (equals), Escape (clear), and Backspace.
    *   Visual feedback with button animations on click/keypress.
*   **Command-Line Interface (`main.py`)**:
    *   Menu-driven interface for basic calculations.
*   **Core Operations (`operations.py`)**:
    *   Basic arithmetic: Addition, Subtraction, Multiplication, Division.
    *   Advanced operations: Exponentiation (Power), Square Root, Modulo.
    *   Error handling for invalid inputs and operations (e.g., division by zero).

## How to Run

### GUI Version

1.  Make sure you have Python installed (Tkinter is usually included).
2.  Navigate to the project directory in your terminal.
3.  Run the GUI script using the command:
    ```bash
    python gui.py
    ```
4.  Use the mouse or keyboard to perform calculations.

### Command-Line Version (Legacy)

1.  Navigate to the project directory in your terminal.
2.  Run the main script using the command:
    ```bash
    python main.py
    ```
3.  Follow the prompts to select an operation and enter numbers.

## Available Operations (Both Interfaces)

*   Add (+)
*   Subtract (-)
*   Multiply (*)
*   Divide (/)
*   Power (^)
*   Square Root (sqrt)
*   Modulo (%)

## File Structure

*   `gui.py`: The main script for the graphical user interface.
*   `main.py`: The main script for the command-line interface.
*   `operations.py`: Module containing functions for mathematical operations.
*   `README.md`: This file. 