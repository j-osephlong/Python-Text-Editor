import os

file = []

def check_for_changes():
	global file
	temp = []
	with open("text2.temp") as f:
		for l in f:
			temp.append(l)
	if len(file) != len(temp):
		file = temp
		print_file()
	else:
		for f, t in zip(file, temp):
			if f != t:
				file = temp
				print_file()
				break

def print_file():
	os.system("cls")
	for l in file:
		print(l, end = "")
	print("")

def wait_for_load():
	if os.path.isfile("text2.temp"):
		pass
	else:
		print("Please load file in text2")
		while not os.path.isfile("text2.temp"):
			pass

def main():
	global file
	os.system("cls")
	wait_for_load()
	os.system("cls")
	with open("text2.temp") as f:
		for l in f:
			file.append(l)

	print_file()

	while True:
		check_for_changes()

main()