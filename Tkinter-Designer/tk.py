import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("多标签页示例")

# 创建 Notebook 控件
notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10)

# 定义标签页内容和标题
tab1 = tk.Frame(notebook, width=400, height=300)
tab2 = tk.Frame(notebook, width=400, height=300)
tab3 = tk.Frame(notebook, width=400, height=300)

# 添加标签页到 Notebook
notebook.add(tab1, text='标签页 1')
notebook.add(tab2, text='标签页 2')
notebook.add(tab3, text='标签页 3')

# 示例内容：每个标签页放置不同的内容
label1 = tk.Label(tab1, text="这是标签页 1 的内容", font=('Helvetica', 12))
label1.pack(pady=20)

label2 = tk.Label(tab2, text="这是标签页 2 的内容", font=('Helvetica', 12))
label2.pack(pady=20)

label3 = tk.Label(tab3, text="这是标签页 3 的内容", font=('Helvetica', 12))
label3.pack(pady=20)

# 运行主循环
root.mainloop()