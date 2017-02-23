import os
import sys
import thread
import signal
path = None
open_file = []

class commands:
	def open(filename):
		global path, open_file
		path = filename

		open_file[:] = ""
		with open(path) as f:
			for l in f:
				line = []
				for c in l:
					line.append(c)
				open_file.append("".join(line))

	def save(filename = path):
		with open(filename, "w") as f:
			for l in open_file:
				f.write(l)

	def get_path():
		print("\t",path)

class text2():
	def __init__(self, args):
		os.system("cls")
		#thread.start_new_thread(monitor_file, ()) #not working
		signal.signal(signal.SIGINT, self.destroy_temp)
		signal.signal(signal.SIGTERM, self.destroy_temp)
		self.command_line()

	def command_line(self):
		while True:
			command = input("~")
			command_terms = command.split(" ")
			if command_terms[0] == "open":
				commands.open(command_terms[1])
			elif command_terms[0] == "filename":
				commands.get_path()
			elif command_terms[0] == "save":
				if len(command_terms) > 1:
					commands.save(command_terms[1])
				else:
					commands.save()
					
			self.reload()

	def reload(self):
		commands.save("text2.temp")

	def destroy_temp(self):
		os.remove("text2.temp")

text2(None)