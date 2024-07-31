import tkinter
from tkinter import ttk
from tkinter import *
import webbrowser
from tkinter import messagebox
from tkinter.simpledialog import askinteger, askfloat, askstring
import os
class Game_editor():
    
    def __init__(self,editor):
        self.editor=editor
        self.editor.title('GalGame editor')
        self.editor.state("zoomed")

        #style
        style=ttk.Style()



        self.screen_width=editor.winfo_screenwidth()
        self.screen_height=editor.winfo_screenheight()
        self.editor.geometry(f'{int(self.screen_width*0.7)}x{int(self.screen_height*0.8)}')
        self.editor.minsize(int(self.screen_width*0.7),int(self.screen_height*0.8))
        self.paned_window=PanedWindow(self.editor,orient='horizontal',bg='grey')
        self.paned_window.pack(fill='both',expand=True)
        #左frame
        self.left_frame=Frame(self.paned_window,width=300,bg='white')
        self.paned_window.add(self.left_frame)
        #paned
        self.right_paned=PanedWindow(self.paned_window,orient='vertical',bg='grey')
        self.paned_window.add(self.right_paned)

        #右frame
        self.right_top_frame=Frame(self.right_paned,bg='white',height=750)
        self.right_paned.add(self.right_top_frame)

        self.right_buttom_frame=Frame(self.right_paned,bg='white')
        self.right_paned.add(self.right_buttom_frame)
        self.set_menu()
        self.outline()
        
        
        self.start()


    def set_menu(self):
        self.menu=Menu(self.editor)
        #文件
        self.filemenu=Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label='文件', menu=self.filemenu)
        self.filemenu.add_command(label='保存        Ctrl+S')
        self.filemenu.add_command(label='退出        Alt+F4')
        #编辑
        self.edit_menubar=Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label='编辑',menu=self.edit_menubar)
        self.edit_menubar.add_command(label='复制        Ctrl+C')
        self.edit_menubar.add_command(label='粘贴        Ctrl+V')
        self.edit_menubar.add_command(label='剪贴        Ctrl+X')
        #调试
        self.runproject=Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label='调试',menu=self.runproject)
        self.runproject.add_command(label='运行        Ctrl+Alt+R')
        self.runproject.add_command(label='预览        Ctrl+Alt+Y')
        #UI
        self.UI=Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label='UI设定',menu=self.UI)
        self.UI.add_command(label='设计主界面UI')
        self.editor.config(menu=self.menu)
        #关于
        self.menu.add_command(label='关于',command=self.show_about)

    def show_about(self):
        show_about=Toplevel()
        show_about.transient(editor)
        show_about.title('About')
        show_about.resizable(0,0)
        show_about.geometry(f'{int(self.screen_width*0.3)}x{int(self.screen_height*0.4)}+{int(self.screen_width*0.5-self.screen_width*0.3/2)}+{int(self.screen_height*0.5-self.screen_height*0.4/2)}')
        Label(show_about,text='该软件为创作Galgame而制作的游戏开发工具',font=('微软黑体','12')).grid(row=1,column=1,sticky=W)
        check_github=Label(show_about,text='查看作者Github',fg='grey',cursor='hand2')
        check_github.grid(row=2,column=1,pady=30,sticky=W)
        check_github.bind('<Button-1>',lambda event:webbrowser.open("https://github.com/txptxp1"))
        check_github.bind('<Enter>',lambda event:check_github.configure(fg='blue'))
        check_github.bind('<Leave>',lambda event:check_github.configure(fg='grey'))
        update=Label(show_about,text='检查更新',fg='grey')
        update.grid(row=2,column=2,pady=30)
        update.bind('<Enter>',lambda event:update.configure(fg='blue'))
        update.bind('<Leave>',lambda event:update.configure(fg='grey'))
        update.bind('<Button-1>',lambda event:messagebox.showinfo('tips','未完成'))
        show_about.grab_set()  # 捕捉所有的交互事件
        show_about.wait_window()        

    def outline(self):

        def create_outline():
            
            pass

        cre_but=Label(self.left_frame, text='    +    ',bg='white',font=('微软黑雅',10,'bold'))
        cre_but.pack(fill='x',side='top')
        cre_but.bind('<Enter>',lambda event:cre_but.configure(bg='#DADADA'))
        cre_but.bind('<Leave>',lambda event:cre_but.configure(bg='white'))

        self.outline_frame=Frame(self.left_frame,bg='white',width=150)
        self.outline_frame.pack(fill='both',side='bottom',expand=True)

        self.outline_tree=ttk.Treeview(self.outline_frame)


        self.outline_tree.pack(fill='both',expand=True)

        
        
        
        """cre_but.grid(row=0, column=0)
        
        # 确保left_frame能够根据需要扩展其内部控件
        '''self.left_frame.grid_rowconfigure(0,weight=1)'''
        self.left_frame.grid_columnconfigure(0,weight=1)
        self.left_frame.grid_columnconfigure(1,weight=1)# 如果需要，也可以设置列权重"""


    
    def start(self):
        self.editor.mainloop()


if __name__=='__main__':
    editor=Tk()
    game_editor=Game_editor(editor)
