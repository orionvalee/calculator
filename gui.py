import tkinter as tk
import operations
import math

# Global variables to store calculator state
first_number = None
operation = None
is_new_number = True # Flag to check if the next digit should start a new number

# --- Function Definitions ---

def button_click(number):
    """Handles clicks for digit buttons (0-9) and decimal point."""
    global is_new_number
    current = entry.get()
    if is_new_number:
        entry.delete(0, tk.END)
        entry.insert(0, str(number))
        is_new_number = False
    else:
        entry.insert(tk.END, str(number))

def button_clear():
    """Clears the entry field and resets calculator state."""
    global first_number, operation, is_new_number
    entry.delete(0, tk.END)
    first_number = None
    operation = None
    is_new_number = True

def button_operator(op):
    """Handles clicks for binary operator buttons (+, -, *, /, ^, %)."""
    global first_number, operation, is_new_number
    try:
        f_num = float(entry.get())
        first_number = f_num
        operation = op
        is_new_number = True # Ready for the next number
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        is_new_number = True


def button_sqrt():
    """Handles the square root operation."""
    global first_number, operation, is_new_number
    try:
        num = float(entry.get())
        result = operations.square_root(num)
        entry.delete(0, tk.END)
        if isinstance(result, str): # Check for error message
            entry.insert(0, result)
        else:
             # Format to avoid unnecessary .0
             entry.insert(0, str(int(result)) if result.is_integer() else str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    is_new_number = True # Ready for a new calculation or input


def button_equal():
    """Handles the equals button click, performs calculation."""
    global first_number, operation, is_new_number
    if first_number is None or operation is None:
        # Nothing to calculate if no first number or operation stored
        return 
        
    try:
        second_number = float(entry.get())
        entry.delete(0, tk.END)
        result = None

        if operation == '+':
            result = operations.add(first_number, second_number)
        elif operation == '-':
            result = operations.subtract(first_number, second_number)
        elif operation == '*':
            result = operations.multiply(first_number, second_number)
        elif operation == '/':
            result = operations.divide(first_number, second_number)
        elif operation == '^':
             result = operations.power(first_number, second_number)
        elif operation == '%':
             result = operations.modulo(first_number, second_number)

        if isinstance(result, str): # Check for error messages from operations
             entry.insert(0, result)
        elif result is not None:
            # Format to avoid unnecessary .0
            entry.insert(0, str(int(result)) if result.is_integer() else str(result))
        else:
             entry.insert(0, "Error") # Should not happen with current logic, but safeguard

    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    
    # Reset state after calculation, ready for new input
    first_number = None 
    operation = None
    is_new_number = True


# --- GUI Setup ---
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500") # Adjust size as needed
root.resizable(False, False) # Optional: Make window non-resizable

# Entry widget for display
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10) # ipady for internal padding

# --- Button Creation & Placement ---
# Define button texts in order
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '^', '+',
    'C', '=', '%', 'sqrt'
]

# Create and grid buttons dynamically
row_val = 1
col_val = 0
for text in button_texts:
    # Choose command based on button type
    if text.isdigit() or text == '.':
        cmd = lambda t=text: button_click(t)
    elif text in ['+', '-', '*', '/', '^', '%']:
        cmd = lambda t=text: button_operator(t)
    elif text == 'sqrt':
         cmd = button_sqrt
    elif text == 'C':
        cmd = button_clear
    elif text == '=':
        cmd = button_equal
    else: # Should not happen
        cmd = None

    # Create button
    button = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 12), command=cmd)
    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew") # sticky makes buttons expand

    # Update row/column counters
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid column/row weights so buttons resize nicely (optional but good)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, row_val + 1): # +1 because row_val stops after last button is placed
    root.grid_rowconfigure(i, weight=1)


# Start the Tkinter event loop
root.mainloop() 