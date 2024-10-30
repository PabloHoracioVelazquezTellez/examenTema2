import tkinter as tk
from getInformation import GetInformation
from showInformation import ShowInformation
from windows import Windows

if __name__ == "__main__":
    root = tk.Tk()
    data_source = GetInformation()
    display_source = ShowInformation(data_source, root)
    app = Windows(root, show_information=display_source)
    root.mainloop()
