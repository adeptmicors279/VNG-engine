from tkinter import Tk, Label
from PIL import ImageFont, ImageDraw, ImageTk,Image

root = Tk()

# 加载自定义字体文件
font_path = "iconfont.ttf"
font_size = 20
custom_font = ImageFont.truetype(font_path, font_size)

# 创建一个带有自定义字体的图片
width = 200
height = 50
image = Image.new("RGBA", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
draw.text((10, 10), "Custom Font", font=custom_font, fill=(0, 0, 0))

# 将图片转换为Tkinter支持的格式
tk_image = ImageTk.PhotoImage(image)

# 在Tkinter窗口中显示带有自定义字体的标签
label = Label(root, image=tk_image)
label.pack()

root.mainloop()
