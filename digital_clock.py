import tkinter as tk
import time

root = tk.Tk()
root.title("Clock")

def update_time():
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(1000, update_time)


label = tk.Label(root, font=("Arial", 60), \
                 fg="cyan", bg="black")
label.pack(padx=10, pady=10)

update_time()
root.mainloop()