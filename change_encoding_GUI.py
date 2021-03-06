
import os
import chardet
from tkinter import *
from tkinter.filedialog import *

items = []
change = {}
app = Tk()
app.title("编码格式转换")
app.geometry("900x600+150+60")


def choose_file():
	global items 
	file_name = askopenfilename(initialdir="f:\\")
	items.append(file_name)
	print("已选择文件>>> " + str(items))
	show_items(items)

def choose_dir():
	global items
	path = askdirectory()
	lst = os.listdir(path)
	for item in lst:
		new_path = path + os.sep + item
		if os.path.isfile(new_path) and new_path.endswith(".txt"):
			items.append(new_path)
	print("已选择文件夹>>> " + str(items))
	show_items(items)


def delete_list():
	global items
	items = []
	print("列表已清空>>> " + str(items))
	show_items(items)


def chage_file(mat="utf-8"):
	global items
	global change
	for file in items:
		if file:
			fo = open(file, "rb")
			encod = chardet.detect(fo.read())['encoding']
			fo.close()
			# print(encod)
			with open(file, "r", encoding=encod) as f:
				content = f.readlines()
				content = "".join(content)
			with open(file, "w", encoding=mat) as w:
				w.write(content)
			change[file] = encod
			show_change(change)


def show_items(items):
	items = "\n".join(items)
	label = app.children["content"]
	label['text'] = str(items)

def show_change(change):
	total = []
	for key in change.keys():
		text  = key+" 成功由 "+change[key]+" 转换为 utf-8 格式。"
		total.append(text)
	label = app.children["content"]
	total = "\n".join(total)
	label['text'] = total


Label(name="content", text=">>>已选文件汇总<<<", font=('楷体',15)).pack(fill=BOTH,expand=1)

Button(name='choose_file', text='选择文件', bg='pink', font=('楷体', 25), command=choose_file).pack(fill=X,expand=1,padx=10,side=LEFT)
Button(name='choose_dir', text='选择文件夹', bg='pink', font=('楷体', 25), command=choose_dir).pack(fill=X,expand=1,padx=10,side=LEFT)
Button(name='delete_list', text='清空已选文件', bg='pink', font=('楷体', 25), command=delete_list).pack(fill=X,expand=1,padx=10,side=LEFT)

Label(name="zero", text="↓ ↓ 选择转换编码格式 ↓ ↓", font=(15)).place(x=620,y=500)
# .pack(fill=BOTH,expand=True)
Button(name="code1", text="utf-8", bg='orange', command=lambda:chage_file("utf-8")).pack(fill=BOTH,expand=1,side=RIGHT)
Button(name="code2", text="gbk", bg='orange', command=lambda:chage_file("gbk")).pack(fill=BOTH,expand=1,side=RIGHT)
Button(name="code3", text="ANSI", bg='orange', command=lambda:chage_file("ANSI")).pack(fill=BOTH,expand=1,side=RIGHT)
Button(name="code4", text="Unicode", bg='orange', command=lambda:chage_file("unicode")).pack(fill=BOTH,expand=1,side=RIGHT)

app.mainloop()
