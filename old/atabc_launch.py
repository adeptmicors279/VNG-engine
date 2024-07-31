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
    #新建项目
    create_new_project_label=ttk.Label(root_canvas,text='•新建项目',style='show.TLabel',cursor="hand2")
    create_new_project_label.place(relx=0.15,rely=0.4)
    
    #全局设置
    global_setting=ttk.Label(root_canvas,text='•设置',style='show.TLabel',cursor="hand2")
    global_setting.place(relx=0.7,rely=0.4)
    #加载项目
    load_project=ttk.Label(root_canvas,text='•加载项目',style='show.TLabel',cursor="hand2")
    load_project.place(relx=0.42,rely=0.4)

    #函数堆放
    #控制label绘制的按钮颜色
    def listening_label(label_name,click_event):
        label_name.bind('<Enter>',lambda event: label_name.configure(style='listening.TLabel'))#关联鼠标经过事件
        label_name.bind('<Leave>', lambda event: label_name.config(style='show.TLabel'))  
        label_name.bind('<Button-1>',lambda event: click_event(event))

    def choose_path(entry):
        folder_path = filedialog.askdirectory()
        entry.delete(0, tkinter.END)
        entry.insert(0, f"{folder_path}")

    def click_create_project(event):#创建项目的函数
        
        def create_root_cavans_start():
            back=ttk.Label(root_canvas,text='<<返回',font=('微软雅黑',20),background='AliceBlue')
            back.place(relx=0.001,rely=0.8)
            
            setting=ttk.Frame(root_canvas,style='settingFrame.TFrame')
            setting.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.72)

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
            
            def create_project(event):
                setname_project=setname_project_enrty.get()
                project_path=set_path.get()
                resolution=set_resolution.get()
                if setname_project!='' and project_path!='' and resolution!='请选择分辨率':
                    if os.path.exists(f'{project_path}'):
                        shutil.copytree('template/',rf'{project_path}/{setname_project}')
                        data={'path':rf'{project_path}/{setname_project}','resolution':f'{resolution}','GUI':'default','content':'default'}
                        with open(rf'{project_path}/{setname_project}/config/config.conf','w',encoding='utf-8')as f:
                            f.write(str(data))
                        with open(rf'load_project/{setname_project}.load','w',encoding='utf-8')as f:
                            f.write(rf'{project_path}/{setname_project}')

                        
                        root.destroy()
                        from gameeditor import launch_editor
                        launch_editor()
                        
                    else:
                        messagebox.showerror('ERROR','文件夹不存在')
                else:
                    if setname_project=='' and project_path=='' and resolution=='请选择分辨率':
                        with open('default.gset','r',encoding='utf-8')as f:
                            f.readlines()
                        pass
                        
                    else:
                        messagebox.showerror('ERROR','请检查输入是否缺漏')



            listening_label(next,click_event=create_project)

            create_new_project_label.unbind('<Button-1>')
            def back_to_main(event):
                back.destroy()
                setting.destroy()
                move_label(window=root_canvas,label=create_new_project_label,new_relx=0.15,new_rely=0.4)
                create_new_project_label.bind('<Button-1>',lambda event: click_create_project(event))
            
            listening_label(back,click_event=back_to_main)

        move_label(window=root_canvas,label=create_new_project_label,new_relx=0.001,new_rely=0.1,callback=create_root_cavans_start)
        

    def click_global_setting(event):

        def create_root_canvas_global_setting():
            
            back=ttk.Label(root_canvas,text='<<返回',font=('微软雅黑',20),background='AliceBlue')
            back.place(relx=0.001,rely=0.8)
            
            setting=ttk.Frame(root_canvas,style='settingFrame.TFrame')
            setting.place(relx=0.2,rely=0.1,relheight=0.8,relwidth=0.72)


            def back_to_main(event):
                back.destroy()
                setting.destroy()
                move_label(window=root_canvas,label=create_new_project_label,new_relx=0.15,new_rely=0.4)
                create_new_project_label.bind('<Button-1>',lambda event: click_create_project(event))


            global_setting.unbind('<Button-1>')
            
            back.bind('<Enter>',lambda event: back.configure(style='listening.TLabel'))#关联鼠标经过事件
            back.bind('<Leave>', lambda event: back.config(style='show.TLabel'))
            back.bind('<Button-1>',lambda event:back_to_main(event))



        move_label(window=root_canvas,label=global_setting,new_relx=0.001,new_rely=0.1,callback=create_root_canvas_global_setting)

    #监听label
    listening_label(create_new_project_label,click_create_project)
    listening_label(global_setting,click_event=click_global_setting)
    listening_label(load_project,click_event=None)
    '''暂时设置为None'''
    
    root.mainloop()



if __name__=='__main__':
    root_window()