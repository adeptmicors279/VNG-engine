import tkinter
from tkinter import ttk
from tkinter import *
import webbrowser
from tkinter import messagebox 
import os
from tkinter.simpledialog import askstring,askinteger
import converter

class Game_editor():
    
    def __init__(self,editor):
        self.editor=editor
        self.editor.title('GalGame editor')
        self.editor.state("zoomed")
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
        self.refresh_treeview()
        self.listening()
        
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

        #右键
        self.click_menu=Menu(self.editor,tearoff=0)
        self.click_menu.add_command(label='打开',command=lambda:self.open_outline())
        self.click_menu.add_command(label='修改',command=lambda:self.change_outline())
        self.click_menu.add_command(label='删除',command=lambda:self.delete_outline())
        




    def show_about(self):
        show_about=Toplevel()
        show_about.transient(self.editor)
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


    def create_outline(self,event):
        set_outline=Toplevel()
        set_outline.transient(self.editor)
        set_outline.title('编辑')
        set_outline.resizable(0,0)
        set_outline.geometry(f'{int(self.screen_width*0.3)}x{int(self.screen_height*0.4)}+{int(self.screen_width*0.5-self.screen_width*0.3/2)}+{int(self.screen_height*0.5-self.screen_height*0.4/2)}')
        Label(set_outline,text='编辑大纲').pack(fill='x')
        choose_type=ttk.Combobox(set_outline,values=['请选择','主线','支线'],state='readonly')
        choose_type.pack(fill='x')
        choose_type.current(0)
        Label(set_outline,text='输入名称').pack(fill='x')
        name=ttk.Entry(set_outline)
        name.pack(fill='x')
        def confirm():
            verify_list=os.walk('plot\\line\\')
            for i,dirs,f in verify_list:
                if f:
                    for j in f:
                        if j==str(name.get())+'.gl':
                            messagebox.showwarning('warning','该名称已存在')
                            return
                        else:
                            if choose_type.get()=='请选择' or name.get()=='':
                                messagebox.showwarning('warning','请填写完整')
                                return
                            elif choose_type.get()=='主线' and name.get()!='':
                                self.outline_tree.insert('','end',text=str(name.get()),values=('主线'))
                                type='main'
                            elif choose_type.get()=='支线' and name.get()!='':
                                self.outline_tree.insert('','end',text=str(name.get()),values=('支线'))
                                type='branch'
                            with open(f'plot\\line\\{str(name.get())}.gl','w',encoding='utf-8') as f:
                                f.write('type=='+type+'\n'+'name=='+str(name.get()))
                                set_outline.destroy()
                else:
                    if choose_type.get()=='请选择' or name.get()=='':
                        messagebox.showwarning('warning','请填写完整')
                        return
                    elif choose_type.get()=='主线' and name.get()!='':
                        self.outline_tree.insert('','end',text=str(name.get()),values=('主线'))
                        type='main'
                    elif choose_type.get()=='支线' and name.get()!='':
                        self.outline_tree.insert('','end',text=str(name.get()),values=('支线'))
                        type='branch'
                    with open(f'plot\\line\\{str(name.get())}.gl','w',encoding='utf-8') as f:
                        f.write('type=='+type+'\n'+'name=='+str(name.get()))
                        set_outline.destroy()
                        

        ttk.Button(set_outline,text='取消',command=lambda:set_outline.destroy()).pack(fill='x',side='bottom')
        ttk.Button(set_outline,text='确定',command=lambda:confirm()).pack(fill='x',side='bottom')
        

        set_outline.grab_set()
        set_outline.wait_window()
        self.refresh_treeview()

    def outline(self):
        

        cre_but=Label(self.left_frame, text='    +    ',bg='white',font=('微软黑雅',10,'bold'))
        cre_but.pack(fill='x',side='top')
        cre_but.bind('<Enter>',lambda event:cre_but.configure(bg='#DADADA'))
        cre_but.bind('<Leave>',lambda event:cre_but.configure(bg='white'))
        cre_but.bind('<Button-1>',lambda event:self.create_outline(event))
        self.outline_frame=Frame(self.left_frame,bg='white',width=150)
        self.outline_frame.pack(fill='both',side='bottom',expand=True)

        self.outline_tree=ttk.Treeview(self.outline_frame,columns=['type','name'],show='headings')
        self.outline_tree.heading('type',text='类型')
        self.outline_tree.heading('name',text='名称')
        self.outline_tree.column('type',width=50,anchor=W)
        self.outline_tree.column('name',width=90,anchor=W)
        self.outline_tree.pack(fill='both',expand=True)
    
    def open_outline(self):
        if self.outline_tree.selection():
            print ('success')

        






    def refresh_treeview(self):
        self.outline_tree.delete(*self.outline_tree.get_children())
        #插入节点
        verify_list=os.walk('plot\\line\\')
        for i,dirs,f in verify_list:
            if f:
                for j in f:
                    type=converter.load_setting(f'plot\\line\\{j}','type')
                    name=converter.load_setting(f'plot\\line\\{j}','name')
                    self.outline_tree.insert('','end',values=(type,name))

    
    def change_outline(self):
        if self.outline_tree.selection():
            change=Toplevel()
            change.transient(self.editor)
            change.title(f'修改"{self.outline_tree.item(self.outline_tree.selection())["values"][1]}"')
            change.geometry(f'{int(self.screen_width*0.3)}x{int(self.screen_height*0.4)}+{int(self.screen_width*0.5-self.screen_width*0.3/2)}+{int(self.screen_height*0.5-self.screen_height*0.4/2)}')
            type=converter.load_setting(f'plot\\line\\{self.outline_tree.item(self.outline_tree.selection())["values"][1]}.gl','type')
            glname=converter.load_setting(f'plot\\line\\{self.outline_tree.item(self.outline_tree.selection())["values"][1]}.gl','name')
            Label(change,text='编辑大纲').pack(fill='x')
            choose_type=ttk.Combobox(change,values=['请选择','主线','支线'],state='readonly')
            choose_type.pack(fill='x')
            choose_type.current(1 if type=='main' else 2)
            Label(change,text='输入名称').pack(fill='x')
            name=ttk.Entry(change)
            name.insert(0,f'{glname}')
            name.pack(fill='x')
            def confirm():
                verify_list=os.walk('plot\\line\\')
                for i,dirs,f in verify_list:
                    if f:
                        for j in f:
                            if j==str(name.get())+'.gl':
                                if glname!=str(name.get()):
                                    messagebox.showerror('warning','该名称已存在')
                                elif glname==str(name.get()):
                                    messagebox.showwarning('warning','请做出更改')
                            elif j==str(name.get()+'.gl'):
                                os.remove(f'plot\\line\\{glname}.gl')
                                if choose_type.get()=='请选择' or name.get()=='':
                                    messagebox.showwarning('warning','请填写完整')
                                    return
                                elif choose_type.get()=='主线' and name.get()!='':
                                    type='main'
                                elif choose_type.get()=='支线' and name.get()!='':
                                    type='branch'
                                with open(f'plot\\line\\{str(name.get())}.gl','w',encoding='utf-8') as f:
                                    f.write('type=='+type+'\n'+'name=='+str(name.get()))
                                    
                                    change.destroy()
                                    
                    

            ttk.Button(change,text='取消',command=lambda:change.destroy()).pack(fill='x',side='bottom')
            ttk.Button(change,text='确定',command=lambda:confirm()).pack(fill='x',side='bottom')



            change.grab_set()
            change.wait_window()
            self.refresh_treeview()



        

    def delete_outline(self):
        if self.outline_tree.selection():
            ask=messagebox.askyesno('删除',f'是否删除  "{self.outline_tree.item(self.outline_tree.selection())["values"][1]}"')
            if ask==True:
                os.remove(f'plot\\line\\{self.outline_tree.item(self.outline_tree.selection())["values"][1]}.gl')
                self.refresh_treeview()
            else:
                pass
            pass
        else:
            pass
        



    def outline_menu(self,event):
        if self.outline_tree.selection():
            self.click_menu.post(event.x_root, event.y_root)
        else:
            pass

    def listening(self):
        self.outline_tree.bind('<Button-3>',self.outline_menu)




    
    def start(self):
        self.editor.mainloop()


if __name__=='__main__':
    folder_path = r'C:\Users\1\Desktop\default_name'
    os.chdir(folder_path)
    editor=Tk()
    game_editor=Game_editor(editor)
