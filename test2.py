import os
from tkinter import Tk, messagebox

# 确保路径正确
folder_path = r'C:\Users\1\Desktop\default_name\plot\line'

# 更改工作目录
os.chdir(folder_path)

# 检查文件夹是否存在
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # 遍历文件夹
    for root, dirs, files in os.walk('.'):
        if files:  # 只有当files非空时才执行
            for file in files:
                if file == '123.gl':
                    messagebox.showwarning('Warning', '该名称已存在')
                    print('该名称不可用')
                else:
                    messagebox.showinfo('Info', '该名称可用')
                    print('该名称可用')
        else:
            # 如果文件夹为空
            messagebox.showinfo('Info', '文件夹为空')
            print('文件夹为空')
else:
    messagebox.showerror('Error', '路径不存在或不是文件夹')
    print('路径不存在或不是文件夹')