import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')  
    clock_label.config(text=current_time)   
    clock_label.after(1000, update_time)   

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=('Arial', 40, 'bold'), background='black', foreground='lightgreen')
clock_label.pack(anchor='center')
update_time()

root.mainloop()
