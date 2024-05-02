import tkinter as tk
from tkinter import filedialog
import os

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            # Display content in a text widget or process it as needed
            print(content)

def execute_function():
    # Define the Python function you want to execute here
    print("Executing Python function...")


def submit():
    # Get the text from the entry boxes and print them
    print("Name:", name_entry.get())
    print("Age:", age_entry.get())

# Create Tkinter window
root = tk.Tk()
root.title("File Loader and Function Executor")

# Button to load a text file
load_button = tk.Button(root, text="Load Text File", command=load_file)
load_button.grid()

# Button to execute Python function
execute_button = tk.Button(root, text="Execute Function", command=execute_function)
execute_button.grid()

# Create and pack Entry widgets
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=2)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=2)


# Create and pack a submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2)

# Run the event loop
root.mainloop()