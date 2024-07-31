from tkinter import *
from tkinter import ttk,messagebox
import tkinter
import math
import os
import os.path
from tkinter import filedialog
import shutil

def move_label(window,label,new_relx,new_rely,callback=None):
    window.update_idletasks()  # 更新标签的位置（但不重绘整个窗口）
    label.place(relx=new_relx,rely=new_rely)
    if callback==None:
        return
    else:
        callback()
        return
    

def listening_label(label_name,click_event):#监听label
    label_name.bind('<Enter>',lambda event: label_name.configure(style='listening.TLabel'))#关联鼠标经过事件
    label_name.bind('<Leave>', lambda event: label_name.config(style='show.TLabel'))  
    label_name.bind('<Button-1>',lambda event: click_event(event))

def choose_path(entry):#选择路径
    folder_path = filedialog.askdirectory()
    entry.delete(0, tkinter.END)
    entry.insert(0, f"{folder_path}")

def root_window():
    root=Tk()
    global style
    style = ttk.Style()
    '''style堆放'''
    #button
    style.configure('setting.TButton',font=('微软雅黑',8),foreground='black')
    #FRAME
    style.configure('settingFrame.TFrame',background='AliceBlue')
    #全局
    style.configure('.',font=('微软雅黑',20),background='AliceBlue')
    #LABEL
    style.configure('show.TLabel',background='AliceBlue',font=('微软雅黑',20))#normal show
    style.configure('setting.TLabel',font=('微软雅黑',8),background='AliceBlue',foreground='grey')#setting show
    style.configure('listening.TLabel',font=('微软雅黑',20),background='AliceBlue',foreground="blue")#listening show

    '''创建主窗口'''
    root.title('atabc')
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    screen_height=int(screen_height*0.6)
    screen_width=int(screen_width*0.5)
    root.geometry(f'{screen_width}x{screen_height}')
    root.minsize(screen_width, screen_height)
    root.maxsize(1920,1080)
    root_canvas=Canvas(root,highlightthickness=0,bg='AliceBlue')
    root_canvas.pack(fill='both',expand=True,side='top')
    '''创建label'''
    #新建项目
    create_project=ttk.Label(root_canvas,text='•新建项目',style='show.TLabel',cursor="hand2")
    create_project.place(relx=0.15,rely=0.4)
    
    #全局设置
    global_setting=ttk.Label(root_canvas,text='•设置',style='show.TLabel',cursor="hand2")
    global_setting.place(relx=0.7,rely=0.4)
    #加载项目
    load_project=ttk.Label(root_canvas,text='•加载项目',style='show.TLabel',cursor="hand2")
    load_project.place(relx=0.42,rely=0.4)
    Label(root_canvas,text='•最近打开',bg='AliceBlue',fg='grey',font=('微软雅黑',15)).place(relx=0.57,rely=0.5)
    recent_open=Frame(root_canvas,bg='#e9eced',highlightbackground="#6B6B65",highlightthickness=1)
    recent_open.place(relx=0.57,rely=0.55,relwidth=0.33,relheight=0.35)
    
    '''点击label的函数'''

    def new_project(event):
        '''布置布局'''
        
        back=ttk.Label(root_canvas,text='<<返回',font=('微软雅黑',20),background='AliceBlue',cursor="hand2")
        back.place(relx=0.001,rely=0.8)#创建返回标签
        
        setting=ttk.Frame(root_canvas,style='settingFrame.TFrame')
        setting.place(relx=0.15,rely=0.1,relheight=0.8,relwidth=0.8)

        ttk.Label(setting,text='请输入创建的项目名:',style='setting.TLabel').grid(row=1,column=1,sticky=W)
        setname_project_enrty=ttk.Entry(setting,width=30,style='')
        setname_project_enrty.grid(row=2,column=1,pady=10,sticky=W)
        ttk.Label(setting,text='设置(留空则使用默认设置)',style='setting.TLabel').grid(row=3,column=1,sticky=W,pady=10)
        ttk.Separator(setting,orient='horizontal', style='red.TSeparator').grid(row=4,column=1, columnspan=2, sticky='EW', pady=5, padx=5)
        ttk.Label(setting,text='输入项目创建路径',style='setting.TLabel').grid(row=5,column=1,sticky='W')
        set_path=ttk.Entry(setting,width=30,style='')
        set_path.grid(row=6,column=1,pady=10,sticky=W)
        ttk.Button(setting,text='选取路径',width=8,style='setting.TButton',command=lambda : choose_path(entry=set_path)).grid(row=6,column=2,sticky='W')
        ttk.Label(setting,text='设置分辨率',style='setting.TLabel').grid(row=7,column=1,sticky='W',pady=10)
        set_resolution=ttk.Combobox(setting, width = 26,state='readonly',values=['请选择分辨率','1280x720','1920x1080','2560x1440'])
        set_resolution.current(0)
        set_resolution.grid(row=8,column=1,sticky='W')
        next=ttk.Label(setting,text='下一步>>',font=('微软雅黑',20),background='AliceBlue',cursor="hand2")
        next.grid(row=10,column=5,sticky='E',pady=10)

        def create_file(event):
            setname_project=setname_project_enrty.get()
            project_path=set_path.get()
            resolution=set_resolution.get()
            if setname_project!='' and project_path!='' and resolution!='请选择分辨率':
                if os.path.exists(f'{project_path}'):
                    try:
                        shutil.copytree('template/',rf'{project_path}/{setname_project}')
                        data=f'path=={project_path}/{setname_project}\nresolution=={resolution}\nGUI==default\ncontent==default'
                        with open(rf'{project_path}/{setname_project}/config/config.gset','w',encoding='utf-8')as f:
                            f.write(str(data))
                        with open(rf'load_project/{setname_project}.load','w',encoding='utf-8')as f:
                            f.write(rf'{project_path}/{setname_project}')

                        
                        root.destroy()
                        os.chdir(f'{project_path}')
                        from gameeditor import launch_editor
                        launch_editor()
                    except FileExistsError as fileerror:
                        messagebox.showerror('warning',f'{fileerror}')

                else:
                    messagebox.showerror('ERROR','文件夹不存在')
            elif setname_project=='' and project_path=='' and resolution=='请选择分辨率':
                try:
                    with open('default.gset','r',encoding='utf-8')as f:
                        default=f.readlines()
                    
                        project_path=str(default[0]).split('default_path==')[1].replace('\n','').replace('\\','\\\\').replace('/','\\\\')
                        resolution=str(default[1]).split('default_resolution==')[1].replace('\n','')
                        setname_project=str(default[2]).split('default_name==')[1].replace('\n','')
                        if os.path.exists(f'{project_path}'):
                            shutil.copytree('template/',rf'{project_path}/{setname_project}')
                            data=f'path=={project_path}/{setname_project}\nresolution=={resolution}\nGUI==default\ncontent==default'
                            with open(rf'{project_path}/{setname_project}/config/config.gset','w',encoding='utf-8')as f:
                                f.write(str(data))
                            with open(rf'load_project/{setname_project}.load','w',encoding='utf-8')as f:
                                f.write(rf'{project_path}/{setname_project}')
                            messagebox.showinfo('tips',f'默认创建在桌面\n名为{setname_project}')
                            root.destroy()
                            os.chdir(f'{project_path}')
                            from gameeditor import launch_editor
                            launch_editor()
                except FileExistsError as fileerror:
                    messagebox.showerror('warning',f'{fileerror}')
                    '''这里是默认设置使用'''

                    '''使用默认设置'''


            else:
                messagebox.showerror('ERROR','请检查输入是否缺漏')

        '''移动标签'''
        move_label(window=root_canvas,label=create_project,new_relx=0.001,new_rely=0.1)
        listening_label(next,click_event=create_file)#监听标签并执行回调函数
        def back_to_main(event):
            back.destroy()
            setting.destroy()
            move_label(window=root_canvas,label=create_project,new_relx=0.15,new_rely=0.4)
            create_project.bind('<Button-1>',lambda event: new_project(event))


        create_project.unbind('<Button-1>')
    
        listening_label(back,click_event=back_to_main)

    def setting_global(event):
        '''布置布局'''
        back=ttk.Label(root_canvas,text='<<返回',font=('微软雅黑',20),background='AliceBlue')
        back.place(relx=0.001,rely=0.8)#创建返回标签
        
        setting=ttk.Frame(root_canvas,style='settingFrame.TFrame')
        setting.place(relx=0.15,rely=0.1,relheight=0.8,relwidth=0.8)

        ttk.Label(setting,text='请输入项目默认创建路径',style='setting.TLabel').grid(row=1,column=1,sticky=W)
        set_path=ttk.Entry(setting,width=30,style='')
        set_path.grid(row=2,column=1,pady=10,sticky=W)
        ttk.Button(setting,text='选取路径',width=8,style='setting.TButton',command=lambda : choose_path(entry=set_path)).grid(row=2,column=2,sticky='W')
        ttk.Label(setting,text='请输入项目默认名称',style='setting.TLabel').grid(row=3,column=1,sticky=W)
        set_name=ttk.Entry(setting,width=30,style='')
        set_name.grid(row=4,column=1,pady=10,sticky=W)
        ttk.Label(setting,text='请设置默认分辨率',style='setting.TLabel').grid(row=5,column=1,sticky=W)
        set_resolution=ttk.Combobox(setting,width=26,state='readonly',values=['1280x720','1920x1080','2560x1440'])
        set_resolution.current(0)
        set_resolution.grid(row=6,column=1,pady=10)
        save=ttk.Label(setting,text='保存',font=('微软雅黑',20),background='AliceBlue')
        save.grid(row=7,column=1,pady=40,sticky=E)
        def save_default_setting(event):
            with open('default.gset','w',encoding='utf-8')as f:
                f.write(f'default_path=={str(set_path.get())}\ndefault_resolution=={str(set_resolution.get())}\ndefault_name=={str(set_name.get())}')
            save.configure(text='保存成功')
        listening_label(label_name=save,click_event=save_default_setting)
        
        #载入默认设置显示
        with open('default.gset','r',encoding='utf-8')as f:
            default=f.readlines()
        for i in default:
            default_set_name=i.split('==')[0]
            default_set_value=i.split('==')[1]
            if default_set_name=='default_path' and default_set_value!='\n':
                set_path.insert(0,f'{default_set_value}')
            elif default_set_name=='default_path' and default_set_value=='\n':
                set_path.insert(0,f'{os.path.expanduser("~/Desktop")}')
            if default_set_name=='default_name':
                set_name.insert(0,f'{default_set_value}')


        '''移动标签'''
        move_label(window=root_canvas,label=global_setting,new_relx=0.001,new_rely=0.1)
        def back_to_main(event):
            back.destroy()
            setting.destroy()
            move_label(window=root_canvas,label=global_setting,new_relx=0.7,new_rely=0.4)
            global_setting.bind('<Button-1>',lambda event: new_project(event))


        global_setting.unbind('<Button-1>')
    
        listening_label(back,click_event=back_to_main)

    def load(event):
        folder_path=str(filedialog.askdirectory())
        if os.path.exists(folder_path+'/config/config.gset'):
            root.destroy()
            os.chdir(f'{folder_path}')
            from gameeditor import launch_editor
            launch_editor()
            
        else:
            messagebox.showerror('warning','未检测到工程文件')





    #监听...
    listening_label(create_project,click_event=new_project)
    listening_label(global_setting,click_event=setting_global)
    listening_label(load_project,click_event=load)


    root.mainloop()






if __name__=='__main__':
    root_window()