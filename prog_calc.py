#! /usr/bin/python3
# python program to convert and calculate values for Assembly programming
# TODO: implement signed and unsigned arithmetic
#       validate user input

import tkinter as tk

class App:
    def __init__(self, master):

        self.menubar = tk.Menu(master)
        master.config(menu=self.menubar)

        self.entry = tk.Entry(master)

        self.lstbx1 = tk.Listbox(master, selectmode=tk.BROWSE, exportselection=0)
        self.lstbx2 = tk.Listbox(master, selectmode=tk.BROWSE, exportselection=0)

        for i in [ "Binary", "Octal", "Decimal", "Hexadecimal" ]:
            self.lstbx1.insert(tk.END, i)
            self.lstbx2.insert(tk.END, i)

        self.result = tk.Label(master, text="0")

        self.quit_button = tk.Button(master, text="Quit", fg="red",
            command=master.quit)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit )

        self.layout()


    def layout(self):
        self.lstbx1.grid(row=0, column=0)
        self.lstbx2.grid(row=0, column=1)
        self.entry.grid(row=1, column=0)
        self.result.grid(row=1, column=1)
        self.submit_button.grid(row=2, column=0)
        self.quit_button.grid(row=2, column=1)


    def submit(self):
        tmp = self.entry.get()
        calc_src = self.lstbx1.curselection()
        calc_dst = self.lstbx2.curselection()

        if (calc_src[0] == 0): # "Binary"
            tmp = int(tmp, 2)
        elif (calc_src[0] == 1): # "Octal"
            tmp = int(tmp, 8)
        elif (calc_src[0] == 2): # "Decimal"
            tmp = int(tmp)
        elif (calc_src[0] == 3): # "Hexadecimal"
            tmp = int(tmp, 16)

        if (calc_dst[0] == 0): # "Binary"
            tmp = bin(tmp)
        elif (calc_dst[0] == 1): # "Octal"
            tmp = oct(tmp)
        elif (calc_dst[0] == 2): # "Decimal"
            tmp = int(tmp)
        elif (calc_dst[0] == 3): # "Hexadecimal"
            tmp = hex(tmp)

        self.result.configure(text=tmp)


root = tk.Tk()
app = App(root)
root.mainloop()
root.destroy()
