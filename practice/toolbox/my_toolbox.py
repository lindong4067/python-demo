import tkinter as tk
from tkinter import ttk
import ctypes

myappid = "my.toolbox"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


root = tk.Tk()
root.title("我的工具箱V1.0")
the_width, the_height = root.maxsize()
root.geometry("%dx%d" %(the_width, the_height))
root.resizable(1, 1)
root.state("zoomed")

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='ws')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')
f1 = tk.Frame(notebook, bg='red', width=the_width, height=the_height)

l = tk.Label(f1, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
e1 = tk.Entry(f1, show='*', font=('Arial', 14)) # 显示成密文形式

e2 = tk.Entry(f1, show=None, font=('Arial', 14)) # 显示成明文形式

e1.pack()

e2.pack()
l.pack()

f2 = tk.Frame(notebook, bg='blue', width=the_width, height=the_height)
notebook.add(f1, text='JSON格式化')
notebook.add(f2, text='XML格式化')
notebook.pack()


root.wm_iconbitmap("my_toolbox_32x32.ico")
root.mainloop()

# def gui_start():
#     init_window = Tk()
#     MyGUI(init_window)