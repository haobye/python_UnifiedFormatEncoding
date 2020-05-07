import os
import chardet

table = []

def read_table(path):
	if os.path.isdir(path):
		lst = os.listdir(path)
		for item in lst:
			new_path = path + os.sep + item
			if os.path.isdir(new_path):
				read_table(new_path)
			elif os.path.isfile(new_path) and new_path.endswith(".txt"):
				table.append(new_path)		
	elif os.path.isfile(path) and path.endswith(".txt"):
		table.append(path)


def chage_file(file):
	fo = open(file, "rb")
	encod = chardet.detect(fo.read())['encoding']
	fo.close()
	# print(encod)
	with open(file, "r", encoding=encod) as f:
		content = f.readlines()
		content = "".join(content)
	with open(file, "w", encoding="UTF-8") as w:
		w.write(content)
	print(file+" 成功由 "+encod+" 转换为 utf-8 格式。")


def main():
	# path = input("input need read path : ")
	path = r"F:\scala\21高阶函数.txt"
	read_table(path)
	print(table)
	for file in table:
		chage_file(file)


main()

