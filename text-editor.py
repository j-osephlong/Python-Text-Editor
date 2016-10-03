##Created by Joseph Long 2016
##First python project
##Simple Text Editor
	##github.com/whatHappenedToBrendanFraser/Text-Editor

import os
import sys

text = []
loaded = []
filename = "file.txt"
autosave = False

def open_text(name=filename):
	global text

	f = open(name, "rU")
	text[:] = []
	for line in f:
		text.append(line.replace("\n",""))
	f.close()

def print_text():
	x = 0
	for line in text:
		print("    ", x, line)
		x+=1

def save_text(name=filename):
	f = open(name, "w")
	for line in text:
		f.write(line + "\n")
	f.close()

def interperit(command):
	global text
	global filename
	global autosave
	command_list = command.split(",")

	if command_list[0] == "change":
		try: text[int(command_list[1])] = command_list[2][1:]
		except: print("\tCommand either missing arguments or one of the arguments are out of range")
	elif command_list[0] == "open":
		if len(command_list) > 1:
			filename = command_list[1][1:]
			open_text(filename)
		else:
			open_text()
	elif command_list[0] == "save":
		if(len(command_list) > 1):
			save_text(command_list[1][1:])
		else:
			save_text()
	elif command_list[0] == "autosave":
		if autosave:
			autosave = False
			print("\tAutosave disabled")
		else:
			autosave = True
			print("\tAutosave enabled")
	elif command_list[0] == "new":
		filename = command_list[1][1:]
		save_text(command_list[1])
		text[:] = []
	elif command_list[0] == "print":
		if len(command_list) > 1:
			print(text[int(command_list[1])])
		else:
			print_text()
	elif command_list[0] == "nl" or command_list[0] == r"\n" or command_list[0] == "new line":
		if len(command_list) > 2:
			text.insert(int(command_list[1]), command_list[2][1:])
		else:
			text.append(command_list[1][1:])
	elif command_list[0] == "find":
		for b in range(0, len(text)):
			if text[b].find(command_list[1][1:]) != -1:
				print("    ", b, text[b])
	elif command_list[0] == "clear": os.system("cls")
	elif command_list[0] == "remove":
		for b in range(0, len(text)):
			if not len(command_list) > 2: 
				text[b] = text[b].replace(command_list[1][1:], "")
			else:
				text[b] = text[b].replace(command_list[1][1:], command_list[2][1:])
	elif command_list[0] == "load":
		try: 
			f = open(command_list[1][1:] + ".py", "r")
			f.close
			loaded.append(command_list[1][1:])
		except: print("\tCouldn't load " + command_list[1] + ",\n\t\tPlugin does not exist")
		print(loaded)
	elif command_list[0] in loaded:
		save_text("text.temp")
		args = " ".join(command_list[1:])
		os.system(".\\" + command_list[0] + ".py " + args)
		open("text.temp")
		os.remove("text.temp")
def main():
	os.system("cls")
	global filename

	if len(sys.argv) > 1:
		filename = sys.argv[1]

	global text
	try: open_text(filename)
	except: print("Default file not found\n\t\"file.txt\" is missing")

	while 1:
		interperit(input(">>>"))
		if autosave: save_text()

main()