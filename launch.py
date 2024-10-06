"""
This is a game editor for VNG

"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import pickle


class Mainwondow(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VNG Game Editor")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{int(self.screen_width*0.3)}x{int(self.screen_height*0.2)}"
        )
        self.root.resizable(False, False)
        self.main_window()
        self.start()

    def main_window(self):
        def choose_path():
            Folderpath = filedialog.askdirectory()
            path.configure(state='normal')
            path.insert(0, f"{Folderpath}")
            path.configure(state='readonly')

        ttk.Label(self.root, text='请输入项目名称').grid(
            row=0, column=0, padx=4, pady=5)
        name = ttk.Entry(self.root, width=30)
        name.grid(row=0, column=1, padx=4, pady=5)

        ttk.Label(self.root, text='请选择路径').grid(
            row=1, column=0, padx=4, pady=5)
        path = ttk.Entry(self.root, width=30, state='readonly')
        path.grid(row=1, column=1, padx=4, pady=5)
        ttk.Button(self.root, text='选择路径', command=lambda: choose_path()).grid(
            row=1, column=2, padx=4, pady=5)

        ttk.Label(self.root, text='请选择分辨率').grid(
            row=2, column=0, padx=4, pady=5)
        resolution = ttk.Combobox(self.root, width=26, state='readonly', values=[
                                  '请选择分辨率', '1280x720', '1920x1080', '2560x1440'])
        resolution.current(0)
        resolution.grid(row=2, column=1, padx=4, pady=5)

        def next(name, path, resolution):
            if os.path.exists(path+'/'+name):
                messagebox.showwarning('Wrong', '项目已存在')
                return
            else:
                os.mkdir(path+'/'+name)
                os.mkdir(path+'/'+name+'/res')
                os.mkdir(path+'/'+name+'/res/ogg')
                os.mkdir(path+'/'+name+'/res/img')

                with open(path+'/'+name+'/'+'info.glg', 'wb') as f:
                    lst = [f'name=={name}', f'resolution=={resolution}']
                    pickle.dump(lst, f)

                self.root.destroy()

        ttk.Button(self.root, text='下一步>>', command=lambda: next(name=name.get(), resolution=resolution.get(), path=path.get()) if name.get() and resolution.get(
        ) != '请选择分辨率' and path.get() else messagebox.showwarning('Wrong', '请确认填写完整')).grid(row=2, column=2, padx=4, pady=5)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    main = Mainwondow()
