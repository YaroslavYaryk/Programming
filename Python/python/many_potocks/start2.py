import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    results.append(result)


results = []

params = {'finished': 2**24}

task1 = threading.Thread(target=handler, kwargs={'finished': 2**12})
task2 = threading.Thread(
    target=handler,
    kwargs={'started': 2**12, 'finished': 2**24})

started_at = time.time()
print("RESULT 1")
task1.start()
task2.start()

task1.join()
task2.join()
print(f'TIME: {time.time() - started_at}')


started_at = time.time()
print("RESULT 2")
handler(**params)
print(f'TIME: {time.time() - started_at}')
