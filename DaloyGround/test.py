from threading import Thread

class Test:
	def __init__(self):
		pass

	def run(self):
		print("Hello world!")

	def start(self):
		thread = Thread(target = self.run, args=())
		thread.start()

test = Test()
test.start()