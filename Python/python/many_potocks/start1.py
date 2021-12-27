import threading
import time


def handler(started=0, finished=0):
	result = 0
	for i in range(started, finished):
		result += i
	print(f"Value: {result}")
	

params = {'finished': 100000000}

task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print("RESULT 1")
task.start()
task.join()
print(f'TIME: {time.time() - started_at}')


started_at = time.time()
print("RESULT 2")
handler(**params)
print(f'TIME: {time.time() - started_at}')
