import tkinter as tk
import operations
import math

# Global variables to store calculator state
first_number = None
operation = None
is_new_number = True # Flag to check if the next digit should start a new number

# --- Animation Logic ---
ANIMATION_COLOR = "lightblue"
ANIMATION_TIME = 100 # milliseconds

def animate_button(button_widget):
    """Temporarily change button background and revert after a delay."""
    original_color = button_widget.cget("background")
    button_widget.config(background=ANIMATION_COLOR)
    # Revert color after ANIMATION_TIME ms
    root.after(ANIMATION_TIME, lambda: button_widget.config(background=original_color))

# Map keysyms/chars to button texts for animation lookup
key_to_button_map = {
    # Digits
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    'KP_0': '0', 'KP_1': '1', 'KP_2': '2', 'KP_3': '3', 'KP_4': '4',
    'KP_5': '5', 'KP_6': '6', 'KP_7': '7', 'KP_8': '8', 'KP_9': '9',
    # Operators
    '+': '+', '-': '-', '*': '*', '/': '/', '^': '^', '%': '%',
    'KP_Add': '+', 'KP_Subtract': '-', 'KP_Multiply': '*', 'KP_Divide': '/',
    # Decimal
    '.': '.', 'KP_Decimal': '.', 'KP_Separator': '.',
    # Equals
    'Return': '=', 'KP_Enter': '=',
    # Clear
    'Escape': 'C',
    # Backspace (Not directly mapped to a button, handled separately)
    # Sqrt
    # (No direct key for sqrt, handle via button click animation)
}

# --- Function Definitions ---

def button_click(number):
    """Handles clicks/keypress for digit buttons and decimal point."""
    global is_new_number

    # Animation
    if str(number) in buttons:
        animate_button(buttons[str(number)])

    current = entry.get()
    # Prevent multiple decimal points
    if number == '.' and '.' in current and not is_new_number:
        return
    if is_new_number:
        # Clear potential previous result from entry if starting new number
        if operation is None and first_number is not None:
            history_label.config(text="") # Also clear history if it was just a result
        entry.delete(0, tk.END)
        entry.insert(0, str(number))
        is_new_number = False
    else:
        entry.insert(tk.END, str(number))

def button_clear():
    """Clears the entry field, history, resets state, animates 'C'."""
    global first_number, operation, is_new_number
    animate_button(buttons['C'])
    entry.delete(0, tk.END)
    history_label.config(text="") # Clear history label
    first_number = None
    operation = None
    is_new_number = True

def button_operator(op):
    """Handles operator clicks/keypress, updates history, animates."""
    global first_number, operation, is_new_number
    animate_button(buttons[op])

    current_text = entry.get()
    if not current_text or current_text == "Error":
        if current_text == "Error": # Clear error state if operator is pressed after error
             history_label.config(text="")
             first_number = None
             operation = None
        is_new_number = True
        return

    if not is_new_number and first_number is not None:
        button_equal() # Calculate previous operation first
        current_text = entry.get()
        if current_text == "Error":
            history_label.config(text="Error") # Show error in history too
            is_new_number = True
            return
        # After chaining, the result is in entry, ready to be the first_number

    try:
        f_num = float(current_text)
        first_number = f_num
        operation = op
        # Format first number for history (remove .0)
        history_text = f"{int(f_num) if f_num.is_integer() else f_num} {op}"
        history_label.config(text=history_text)
        is_new_number = True # Ready for the next number (will clear entry on next digit)
        # Don't clear entry here, allow seeing the first number until next digit starts
    except ValueError:
        button_clear()
        entry.insert(0, "Error")
        history_label.config(text="Error")
        is_new_number = True

def button_sqrt():
    """Handles sqrt button click, updates history, animates."""
    global first_number, operation, is_new_number
    animate_button(buttons['sqrt'])
    current_text = entry.get()
    if not current_text or current_text == "Error":
        return

    try:
        num = float(current_text)
        history_label.config(text=f"sqrt({num})") # Show operation in history
        result = operations.square_root(num)
        entry.delete(0, tk.END)
        if isinstance(result, str): # Error message
            entry.insert(0, result)
            history_label.config(text="Error") # Update history on error
        else:
            result_str = str(int(result)) if result.is_integer() else str(result)
            entry.insert(0, result_str)
            # Leave history as sqrt(num), result is in entry
    except ValueError:
        button_clear()
        entry.insert(0, "Error")
        history_label.config(text="Error")

    is_new_number = True
    first_number = None # sqrt is a unary operation, reset state
    operation = None

def button_equal():
    """Handles equals click/keypress, updates history, animates."""
    global first_number, operation, is_new_number
    animate_button(buttons['='])

    current_text = entry.get()
    if first_number is None or operation is None or is_new_number or not current_text or current_text == "Error":
        return

    try:
        second_number = float(current_text)
        # Update history before calculation
        history_text = f"{history_label.cget('text')} {int(second_number) if second_number.is_integer() else second_number} ="
        history_label.config(text=history_text)

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

        if isinstance(result, str): # Error message from operations
             entry.insert(0, result)
             history_label.config(text="Error") # Show error in history
        elif result is not None:
            result_str = str(int(result)) if isinstance(result, float) and result.is_integer() else str(result)
            entry.insert(0, result_str)
            # History already shows the full expression
        else:
             entry.insert(0, "Error")
             history_label.config(text="Error")

    except ValueError:
        button_clear()
        entry.insert(0, "Error")
        history_label.config(text="Error")

    # Reset state, result is in entry, history shows the calculation
    # Result becomes the potential first number for chaining (handled by button_operator)
    is_new_number = True
    first_number = None # Reset first_number after '=' completes the operation
    operation = None


# --- Keyboard Input Handling ---
def key_press(event):
    """Handles keyboard input, filtering, animating, and calling actions."""
    key = event.char
    keysym = event.keysym
    # print(f"Key pressed: char='{key}', keysym='{keysym}'")

    button_text_to_animate = None

    # Let specific bindings (Enter, Escape, Backspace) handle their keys first
    if keysym in ['Return', 'KP_Enter', 'Escape']:
        # These are handled by root.bind, which call the main functions
        # Animation is handled within button_equal/button_clear called by the lambda
        return
    elif keysym == 'BackSpace':
        # Backspace doesn't have a direct button to animate
        handle_backspace(event) # Call backspace logic
        return "break"

    # Map key to action and button text for animation
    target_button = None
    action = None

    # Digits
    if key.isdigit():
        target_button = key
        action = lambda: button_click(key)
    elif keysym.startswith('KP_') and keysym[3:].isdigit():
        digit = keysym[3:]
        target_button = digit
        action = lambda: button_click(digit)

    # Operators
    elif key in ['+', '-', '*', '/', '^', '%']:
        target_button = key
        action = lambda: button_operator(key)
    elif keysym == 'KP_Add':
        target_button = '+'
        action = lambda: button_operator('+')
    elif keysym == 'KP_Subtract':
        target_button = '-'
        action = lambda: button_operator('-')
    elif keysym == 'KP_Multiply':
        target_button = '*'
        action = lambda: button_operator('*')
    elif keysym == 'KP_Divide':
        target_button = '/'
        action = lambda: button_operator('/')

    # Decimal Point
    elif key == '.':
        target_button = '.'
        action = lambda: button_click('.')
    elif keysym in ['KP_Decimal', 'KP_Separator']:
        target_button = '.'
        action = lambda: button_click('.')

    # Perform action and animation if a valid key was pressed
    if target_button and target_button in buttons and action:
        # animate_button(buttons[target_button]) # Animation is now handled inside button_click/op
        action()
        return "break" # Stop further processing

    # Ignore other keys by stopping further processing
    if keysym not in ['Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Alt_L', 'Alt_R']:
        return "break"
    # Allow modifiers to pass


# --- GUI Setup ---
root = tk.Tk()
root.title("Calculator")
# Increased height slightly for history label
root.geometry("400x550")
root.resizable(False, False)

# History Label (New)
history_label = tk.Label(root, text="", width=35, font=('Arial', 12), anchor='e', justify='right', fg='grey')
history_label.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 0), sticky='ew') # Place above entry

# Entry widget for display (Shifted down one row)
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16), justify='right')
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=(5, 10), ipady=10)
entry.focus_set()

# --- Button Creation & Placement ---
# Dictionary to store button widgets (New)
buttons = {}

# Define button texts in order
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '^', '+',
    'C', '=', '%', 'sqrt'
]

# Create and grid buttons dynamically (Start from row 2)
row_val = 2 # Start buttons below history and entry
col_val = 0
for text in button_texts:
    # Define command WITH animation trigger
    if text.isdigit() or text == '.':
        # Pass the digit/dot itself to button_click
        cmd = lambda t=text: button_click(t)
    elif text in ['+', '-', '*', '/', '^', '%']:
        # Pass the operator symbol to button_operator
        cmd = lambda t=text: button_operator(t)
    elif text == 'sqrt':
         cmd = button_sqrt # sqrt function now handles animation
    elif text == 'C':
        cmd = button_clear # clear function now handles animation
    elif text == '=':
        cmd = button_equal # equal function now handles animation
    else:
        cmd = None

    # Create button
    button = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 12), command=cmd)
    buttons[text] = button
    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid column/row weights (Adjust row range)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
# Adjust row configure range for new layout (rows 2 onwards for buttons)
for i in range(2, row_val):
    root.grid_rowconfigure(i, weight=1)

# --- Bind Keyboard Events ---
# Root bindings for global keys (Enter, Escape)
# Lambdas now just call the main functions; animation is inside those functions
root.bind('<Return>', lambda event: (button_equal(), "break")[1])
root.bind('<KP_Enter>', lambda event: (button_equal(), "break")[1])
root.bind('<Escape>', lambda event: (button_clear(), "break")[1])

# Entry bindings for Backspace and general keys
def handle_backspace(event):
    # (No animation for backspace currently)
    # ... existing backspace logic ...
    global is_new_number, first_number, operation
    if entry.get() == "Error":
        button_clear() # Use button_clear to handle state and potentially animate C
        return "break"

    should_clear = False
    if not is_new_number:
        current = entry.get()
        if not current:
            return "break"
        entry.delete(len(current)-1, tk.END)
        if not entry.get():
             if first_number is not None and operation is not None:
                 should_clear = True # Mark for full clear
             else:
                 is_new_number = True

    if should_clear:
         # Clear state fully but don't animate 'C' for backspace-to-empty scenario
         entry.delete(0, tk.END)
         history_label.config(text="")
         first_number = None
         operation = None
         is_new_number = True
    return "break"

entry.bind('<BackSpace>', handle_backspace)
entry.bind('<KeyPress>', key_press) # key_press now calls action & handles animation via those actions

# Start the Tkinter event loop
root.mainloop() 