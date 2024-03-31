import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Function to calculate the real arrival time
def calculate_arrival(event=None):
    try:
        planned_time = datetime.strptime(planned_time_entry.get(), "%H:%M")
        delay = int(delay_entry.get())
        real_arrival_time = planned_time + timedelta(minutes=delay)
        result_var.set(real_arrival_time.strftime("%H:%M"))
        result_label.configure(foreground='red')  # Set the result text to red
    except ValueError:
        result_var.set("Invalid input")

# Function to copy the result to the clipboard
def copy_result(event=None):
    root.clipboard_clear()
    root.clipboard_append(result_var.get())

# Function to reset all fields
def reset_fields(event=None):
    planned_time_entry.delete(0, tk.END)
    delay_entry.delete(0, tk.END)
    result_var.set("")

# Setting up the UI
root = tk.Tk()
root.title("Train Arrival Calculator")

# Bind the Enter key to the calculate_arrival function
root.bind('<Return>', calculate_arrival)
# Bind Ctrl+Backspace to the reset_fields function
root.bind('<Control-BackSpace>', reset_fields)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Planned arrival time
ttk.Label(root, text="Planned Arrival Time (HH:MM):").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
planned_time_entry = ttk.Entry(root)
planned_time_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

# Delay in minutes
ttk.Label(root, text="Delay (in minutes):").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
delay_entry = ttk.Entry(root)
delay_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

# Button to calculate the real arrival time
calculate_button = ttk.Button(root, text="Calculate Real Arrival Time", command=calculate_arrival)
calculate_button.grid(column=0, row=2, columnspan=2, sticky=tk.EW, padx=5, pady=5)

# Displaying the result
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, foreground='red')  # Default text color set to red
result_label.grid(column=0, row=3, columnspan=2, sticky=tk.EW, padx=5, pady=5)
result_label.bind('<Button-1>', copy_result)  # Bind clicking on the label to copy_result function

# Button to reset the fields
reset_button = ttk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(column=0, row=4, columnspan=2, sticky=tk.EW, padx=5, pady=5)

root.mainloop()
