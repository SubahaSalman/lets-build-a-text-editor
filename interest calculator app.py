# Write a Python program to create an application to take inputs 
# of the principal amount, time period, and rate of interest from 
# the user, and return the simple interest and compound interest on 
# the same principle using the Python Tkinter library.



from tkinter import *

import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest
        si = (principal * rate * time) / 100

        # Compound Interest
        amount = principal * ((1 + rate / 100) ** time)
        ci = amount - principal

        result_label.config(
            text=f"Simple Interest = {si:.2f}\nCompound Interest = {ci:.2f}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")


root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

tk.Label(root, text="Principal Amount:").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()


tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()


tk.Label(root, text="Time Period (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()


tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()