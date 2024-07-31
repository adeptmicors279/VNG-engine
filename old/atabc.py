import tkinter as ttk
from tkinter import *

import math
def move_label(window,label,target_x,target_y,time,callback=None):
    # 更新 label 的位置
    current_x=label.winfo_x()
    current_y=label.winfo_y()
    dx=current_x-int(target_x)
    dy=current_y-int(target_y)
    dx=-dx
    dy=-dy
    decimal_ratio=round(dx/dy,2)
    dx_temporary=(dx**2)**0.5
    dy_temporary=(dy**2)**0.5
    dx=(dx_temporary/dx)*decimal_ratio
    dy=(dy_temporary/dy)*1
    new_x=current_x+dx
    new_y=current_y+dy
    # 如果 label 还没有到达目标位置，则继续移动  
    if not (new_x==target_x and new_y==target_y):
        # 将 label 移动到新的位置
        window.update_idletasks()  # 更新标签的位置（但不重绘整个窗口）
        label.place(x=new_x,y=new_y)
        # 使用 after 方法在一段时间后再次调用此函数
        window.after(time,move_label,window,label,target_x,target_y,time,callback)  # time 毫秒后再次调用
    else: 
        if callback is not None:
            callback()
            return
        else:
            return


def root_window():
    root=Tk()
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    screen_height=int(screen_height*0.6)
    screen_width=int(screen_width*0.5)
    root.geometry(f'{screen_width}x{screen_height}')
    root.minsize(screen_width, screen_height)
    root.maxsize(1920,1080)
    root_canvas=ttk.Canvas(root,highlightthickness=0,bg='AliceBlue')
    root_canvas.pack(fill='both',expand=True,side='top')
    start_label=ttk.Label(root_canvas,text='•新建项目',font=('微软雅黑',20),background='AliceBlue')
    start_label.place(x=200,y=300)
    
    def click(event):
        def create_root_cavans_start():
            back=ttk.Label(root_canvas,text='<<返回',font=('微软雅黑',20),background='AliceBlue')
            back.place(x=20,y=500)
            setting=ttk.Frame(root_canvas,background='AliceBlue')
            setting.place(x=200,y=80,width=670,height=480)
            name_project_lab=ttk.Label(setting,text='请输入创建的项目名:',font=('微软雅黑',8),background='AliceBlue',fg='grey')
            name_project_lab.grid(row=1,column=1,sticky=W)
            name_project=Entry(setting,bg='AliceBlue',width=30)
            name_project.grid(row=2,column=1,pady=10,sticky=W)
            setting_isolation_label=Label(setting,text='设置(如果开启此项优先使用该设置而不是全局设置)',bg='AliceBlue',fg='grey')
            setting_isolation_label.grid(row=3,column=1,sticky=W,pady=10)
            #setting_isolation_open=Radiobutton(setting,font=('微软雅黑',8),background='AliceBlue')
            #setting_isolation_open.grid(row=4,column=1)

            start_label.unbind('<Button-1>')
            def back_to_main(event):
                move_label(window=root_canvas,label=start_label,target_x=200,target_y=300,time=2)
                back.destroy()
                setting.destroy()
                start_label.bind('<Button-1>',lambda event: click(event))
            
            back.bind('<Enter>',lambda event: back.configure(fg='blue'))#关联鼠标经过事件
            back.bind('<Leave>', lambda event: back.config(fg='black'))  
            back.bind('<Button-1>',lambda event:back_to_main(event))


        move_label(window=root_canvas,label=start_label,target_x=20,target_y=90,time=2,callback=create_root_cavans_start)

    start_label.bind('<Enter>',lambda event: start_label.configure(fg='blue'))#关联鼠标经过事件
    start_label.bind('<Leave>', lambda event: start_label.config(fg='black'))  
    start_label.bind('<Button-1>',lambda event: click(event))
    root.mainloop()

if __name__=='__main__':
    root_window()