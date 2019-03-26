import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Hello, world", 
                              background="black", foreground="white")
        self.label.pack(side="top", fill="both", expand=True)
        self.flash()

    def flash(self):
        bg = self.label.cget("background")
        fg = self.label.cget("foreground")
        self.label.configure(background=fg, foreground=bg)
        self.after(250, self.flash)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
