import tkinter
from tkinter import ttk
from tkinter import *
import webbrowser
from tkinter import messagebox
from tkinter.simpledialog import askinteger, askfloat, askstring
def save_edit():
    print ('test')
    pass

def editor_quit():
    pass

def editor_update(event):
    messagebox.showinfo('tips','暂未完工')

def launch_editor():
    editor=Tk()
    editor.title('GalGame editor')
    editor.state("zoomed")
    screen_width=editor.winfo_screenwidth()
    screen_height=editor.winfo_screenheight()

    editor.geometry(f'{int(screen_width*0.7)}x{int(screen_height*0.8)}')
    editor.minsize(int(screen_width*0.7),int(screen_height*0.8))

#设置顶栏菜单
    menu=Menu(editor)

    filemenu=Menu(menu,tearoff=0)
    menu.add_cascade(label='文件', menu=filemenu)
    filemenu.add_command(label='保存        Ctrl+S', command=save_edit)
    filemenu.add_command(label='退出        Alt+F4',command=editor_quit)

    edit_menubar=Menu(menu,tearoff=0)
    menu.add_cascade(label='编辑',menu=edit_menubar)
    edit_menubar.add_command(label='复制        Ctrl+C')
    edit_menubar.add_command(label='粘贴        Ctrl+V')
    edit_menubar.add_command(label='剪贴        Ctrl+X')

    runproject=Menu(menu,tearoff=0)
    menu.add_cascade(label='调试',menu=runproject)
    runproject.add_command(label='运行        Ctrl+Alt+R')
    runproject.add_command(label='预览        Ctrl+Alt+Y')

    UI=Menu(menu,tearoff=0)
    menu.add_cascade(label='UI设定',menu=UI)
    UI.add_command(label='设计主界面UI')  
    
    def show_about():
        show_about=Toplevel()
        show_about.transient(editor)
        show_about.title('About')
        show_about.resizable(0,0)
        show_about.geometry(f'{int(screen_width*0.3)}x{int(screen_height*0.4)}+{int(screen_width*0.5-screen_width*0.3/2)}+{int(screen_height*0.5-screen_height*0.4/2)}')
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
        update.bind('<Button-1>',lambda event:editor_update(event))
        show_about.grab_set()  # 捕捉所有的交互事件
        show_about.wait_window()

    
    menu.add_command(label='关于',command=show_about)

#创建一个画布进行布局
    editor_Canvas=Canvas(editor)
    editor_Canvas.pack(fill='both',expand=True)
    def show_context_menu(event):
        global_button3_menu.post(event.x_root, event.y_root)

    def create_plot():
        create=Toplevel()
        create.title('创建剧情点')
        create.resizable(0,0)
        create.geometry(f'{int(screen_width*0.2)}x{int(screen_height*0.1)}+{int(screen_width*0.5-screen_width*0.2/2)}+{int(screen_height*0.5-screen_height*0.1/2)}')
        create.transient(editor)
        ttk.Label(create,text='输入名称').grid(row=1,column=1)
        name=ttk.Entry(create,width=30)
        name.grid(row=2,column=1,pady=5)
        ttk.Label(create,text='输入描述').grid(row=3,column=1)
        description=ttk.Entry(create,width=30)
        description.grid(row=4,column=1)
        def definite():
            with open (rf'plot/{name.get()}.pl','w',encoding='utf-8')as f:
                text=f'''name=={name.get()}\ndescription=={description.get()}'''
                f.write(text)
            create.destroy()
                
        ttk.Button(create,text='保存',command=lambda:definite()).grid(row=2,column=2,padx=5,sticky=E)
        ttk.Button(create,text='取消',command=lambda:create.destroy()).grid(row=4,column=2,padx=5,sticky=E)

        create.grab_set()  # 捕捉所有的交互事件
        create.wait_window

        
    
    def create_choose():
        pass

    def link():
        pass




    global_button3_menu=Menu(editor_Canvas,tearoff=0)
    global_button3_menu.add_command(label='创建剧情点',command=lambda:create_plot())
    global_button3_menu.add_command(label='创建选择枝',command=lambda:create_choose())
    global_button3_menu.add_command(label='连接剧情点',command=lambda:link())
    editor.bind("<Button-3>", show_context_menu)


















    editor.config(menu=menu)
    editor.mainloop()

#调试用，等会删
launch_editor()