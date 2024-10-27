import tkinter as tk
from getInformation import GetInformation
from showInformation import ShowInformation
if __name__ == "__main__":
    root = tk.Tk()
    data_source = GetInformation()
    app = ShowInformation(root, data_source)
    root.mainloop()
