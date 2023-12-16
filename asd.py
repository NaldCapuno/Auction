import tkinter as tk

main = tk.Tk()
list = tk.Listbox(main)
list.grid(row=0, column=0, padx=10, pady=10)
list.insert(0, 'nigga')

main.mainloop()