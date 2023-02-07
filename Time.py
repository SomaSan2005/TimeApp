import tkinter as tk
import time

def show_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, show_time)

root = tk.Tk()
root.configure(bg='black')
root.geometry("500x500")

label = tk.Label(root, text="", font=("Helvetica", 20), bg="black", fg="white")
label.place(relx=0.5, rely=0.5, anchor="center")

show_time()
root.mainloop()

root.mainloop()


