import asyncio
from asyncio.coroutines import coroutine
import time


def sync_worker(number, divide):  # work one by one
    print(f"asinx worker -  {number}, {divide}")
    time.sleep(1)
    print(number / divide)


sync_worker(30, 10)
sync_worker(15, 5)


async def asinc_vorker(number, divide):

    print(f"asinx worker -  {number}, {divide}")
    await asyncio.sleep(1)
    print(number / divide)


event_loop = asyncio.get_event_loop()  # work simultaniuously
task_list = [
    event_loop.create_task(asinc_vorker(30, 10)),
    event_loop.create_task(asinc_vorker(15, 5)),
]

task = asyncio.wait(task_list)
event_loop.run_until_complete(task)
event_loop.close()
