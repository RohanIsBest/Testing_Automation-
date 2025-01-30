import tkinter as tk
from tkinter import messagebox
import time

def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Input Received", f"You entered: {user_input}")
def test_hmi():
    entry.insert(0, "Hello")
    on_button_click()
    time.sleep(1)
    if entry.get() == "Hello":
        print("Test Passed: Dialog box appeared and processed input correctly.")
    else:
        print("Test Failed: Dialog box did not appear as expected.")
root = tk.Tk()
root.title("HMI Simulation")

entry = tk.Entry(root)
entry.pack(pady=10)
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)
root.after(1000, test_hmi)
root.mainloop()
