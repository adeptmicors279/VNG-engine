from tkinter import ttk, filedialog
import tkinter as tk


class Editor(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('打包工具')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{int(self.screen_width*0.4)}x{int(self.screen_height*0.25)}")
        self.root.resizable(False, False)
        self.selected_path = None  # 初始化路径
        self.edit_window()
        self.start()

    def choose_path(self):
        self.selected_path = filedialog.askdirectory()
        

    def edit_window(self):
        ttk.Button(self.root, text='选择项目位置', command=lambda: self.choose_path()).grid(
            row=0, column=0, padx=4, pady=5)
        self.selected_path

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    Editor()
