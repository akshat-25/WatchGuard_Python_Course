import  tkinter as tk

root = tk.Tk()

tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")
tk.Label(root, text="Label 1", bg="red").pack(side="top",fill="both",expand=True)
tk.Label(root, text="Label 2", bg="red").pack(side="top", fill="both", expand=True)
 

root.mainloop()