import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        show_custom_error("Input Error", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        show_custom_error("Input Error", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        show_custom_error("Input Error", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 != 0:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
        else:
            show_custom_error("Math Error", "Division by zero is not allowed")
    except ValueError:
        show_custom_error("Input Error", "Please enter valid numbers")

def on_enter_key(event):
    if entry1.focus_get() == entry1:
        entry2.focus()
        return "break"
    elif entry2.focus_get() == entry2:
        if op.get() == 'Add':
            add()
        elif op.get() == 'Subtract':
            subtract()
        elif op.get() == 'Multiply':
            multiply()
        elif op.get() == 'Divide':
            divide()
        entry1.focus()
        return "break"

def show_custom_error(title, message):
    error_dialog = tk.Toplevel(root)
    error_dialog.title(title)
    error_dialog.geometry("300x150")
    error_dialog.resizable(False, False)
    
    label = tk.Label(error_dialog, text=message, wraplength=250, padx=10, pady=10)
    label.pack(padx=10, pady=10)
    
    button = tk.Button(error_dialog, text="OK", command=error_dialog.destroy)
    button.pack(pady=5)

def show_custom_input(prompt):
    input_dialog = tk.Toplevel(root)
    input_dialog.title(prompt)
    input_dialog.geometry("300x150")
    input_dialog.resizable(False, False)
    
    label = tk.Label(input_dialog, text=f"Enter {prompt}:", wraplength=250, padx=10, pady=10)
    label.pack(padx=10, pady=10)
    
    entry = tk.Entry(input_dialog, width=30)
    entry.pack(padx=10, pady=10)
    entry.focus()

    def on_ok():
        value = entry.get()
        input_dialog.destroy()
        return value

    button = tk.Button(input_dialog, text="OK", command=on_ok)
    button.pack(pady=5)
    
    root.wait_window(input_dialog)
    return entry.get()

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x350")  # Adjusted initial window size
root.configure(bg="#f0f0f0")  # Light gray background

# Font styles
font_style = ("Arial", 12)
title_font = ("Arial", 16, "bold")  # Increased title font size for better emphasis
button_font = ("Arial", 12, "bold")  # Increased button font size

# Title label
tk.Label(root, text="Simple Calculator", font=title_font, bg="#f0f0f0", pady=10).grid(row=0, column=0, columnspan=2, padx=15, pady=15)

# First number input
tk.Label(root, text="Enter first number:", font=font_style, bg="#f0f0f0", anchor='w').grid(row=1, column=0, padx=20, pady=10, sticky='w')
entry1 = tk.Entry(root, font=font_style)
entry1.grid(row=1, column=1, padx=20, pady=10, sticky='ew')

# Second number input
tk.Label(root, text="Enter second number:", font=font_style, bg="#f0f0f0", anchor='w').grid(row=2, column=0, padx=20, pady=10, sticky='w')
entry2 = tk.Entry(root, font=font_style)
entry2.grid(row=2, column=1, padx=20, pady=10, sticky='ew')

# Operation selection
op = tk.StringVar(value='Add')
operations = ['Add', 'Subtract', 'Multiply', 'Divide']
for i, operation in enumerate(operations):
    tk.Radiobutton(root, text=operation, variable=op, value=operation, font=font_style, bg="#f0f0f0", anchor='w').grid(row=3+i//2, column=i%2, padx=20, pady=5, sticky='w')

# Calculate button
tk.Button(root, text="Calculate", command=lambda: on_enter_key(None), font=button_font, bg="#4CAF50", fg="white", relief=tk.RAISED).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Result label
result_label = tk.Label(root, text="Result: ", font=font_style, bg="#f0f0f0")
result_label.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky='ew')  # Adjusted padding

# Configure grid weights to ensure resizing
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(6, weight=1)

# Set focus on the first entry box
entry1.focus()

# Bind the Enter key to the calculation function
root.bind('<Return>', on_enter_key)

# Start the main loop
root.mainloop()
