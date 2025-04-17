"""
tkinter.TkVersion     #检查当前 Tkinter版本

StringVar()用于与TK控件(按钮、标签)进行交互,实现数据的双向绑定,get()、set(value)获取与设置StringVar对象的值


使窗口在屏幕正中间的方法

import tkinter as tk

root = tk.Tk()

width,height = 400,300

crw,crh  = root.winfo_screenwidth(),root.winfo_screenheight()

x,y = (crw - width) // 2,(crh - height) // 2

root.geometry(f'{width}x{height}+{x}+{y}')

root.mainloop()



1.pack()         默认情况下,每个选项都放在前一个选项的下面,并按照它们分配给窗口的顺序排列

#根据需要调整窗口大小,框架将响应式扩展并填充窗口
frame1 = tk.Frame(master=root, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=root, width=100, bg="yellow")      #Frame是一个容器,用于容纳其他组件(按钮、文本框、标签),是GUI应用程序中用户与程序交互的主要界面
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=root, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

设置 fill关键字参数来指定框架的填充方向,选项包括水平填充、垂直填充和双向填充.以下是堆叠三个框架的方法,以便每个框架都水平填充整个窗口:tk.X、tk.Y、tk.BOTH
填充窗口的一个好处是,填充会响应窗口大小的调整,但小组件不会在垂直方向上扩展

缺点:
1.组件的位置取决于调用的顺序


2.grid()        拆分窗口或将其拆分为行和列来工作

for i in range(3):

    root.columnconfigure(i, weight=1, minsize=75)

    root.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):

        frame = tk.Frame(master=root,relief=tk.RAISED,borderwidth=1)

        frame.grid(row=i, column=j,padx=5, pady=5)         #padx:水平方向添加填充   pady:垂直方向添加填充

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")

        label.pack(padx=5, pady=5)



root.columnconfigure(0, minsize=250)

root.rowconfigure([0, 1], minsize=100)


label1 = tk.Label(text="A")

label1.grid(row=0, column=0, sticky="ns")        #'n'与单元格的顶部中心部分对齐 's'与单元格的底部中心部分对齐 'w'与单元格的左中侧对齐 'e'与单元格的右中侧对齐

                                                            grid()            grid()
label2 = tk.Label(text="B")                              sticky="ew" -->     fill=tk.X

label2.grid(row=1, column=0, sticky="we")                sticky="ns" -->     fill=tk.Y
                                                         sticky="nsew" -->   fill=tk.BOTH




3.place()      用于控制窗口小部件在窗口中应占据的精确位置

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)

提供两个关键字参数指定窗口小部件左上角的x坐标和y坐标,两者均以像素为单位

缺点:
1.布局可能难以管理,如果应用程序有很多widget则尤其如此
2.创建的布局不是响应式的,它们不会随着窗口大小的调整而改变





tk.Button(root,text = 'Hello Tkinter',        #控制标签的宽度和高度:width,height(对于宽度和高度测量,Tkinter使用文本单位);文本和背景颜色foreground,background
          foreground = 'purple',
          background = 'white',
          width = 10,height = 2).pack()



label = tk.Label(root,text = 'Name',fg="black", bg="white",width = 5)
entry = tk.Entry()                        #从用户那里获取少量文本(如姓名或电子邮件地址),使用Entry小部件,它将显示一个小文本框,用户可以在其中输入一些文本
label.pack()
entry.pack()

entry.get()      检索文本get()
entry.delete(0,4)     删除文本delete()
entry.insert(0,'pycharm')     插入文本insert()



text_box = tk.Text()
text_box.pack()
                                     #1.字符的行号   2.字符在该行上的索引位置     get("1.0", tk.END) 表示获取文本框中的所有文本
text_box.get("1.0","1.5")            #需要传递start索引和end索引,从文本框中获取整个单词,结束索引必须比要读取的最后一个字符的索引多1
text_box.delete("1.0","1.5")
text_box.insert("1.0","hello")
text_box.insert("2.0","\nworld")     #新行中插入文本,则需要在要插入的字符串中手动插入换行符



border_effects = {
    "flat": tk.FLAT,       # FLAT:没有边框效果
    "sunken": tk.SUNKEN,   # SUNKEN:创建下沉效果
    "raised": tk.RAISED,   # RAISED:创建凸起的效果
    "groove": tk.GROOVE,   # GROOVE:创建凹槽边框效果
    "ridge": tk.RIDGE,     # RIDGE:创建脊状效果
}

for relief_name, relief in border_effects.items():

    frame = tk.Frame(master=root, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)

    label = tk.Label(master=frame, text=relief_name)
    label.pack()



import tkinter as tk

window = tk.Tk()

def handle_keypress(event):

    print(event.char)

btn = tk.Button(text="Click me!")

window.bind("<Button>", handle_keypress)      #接受两个参数:1.字符串表示的事件  2.事件处理程序

window.mainloop()
"""

