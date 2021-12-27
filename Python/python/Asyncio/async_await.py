import asyncio
import time


async def asinc_vorker(number, divide):
    print(f"asinx worker -  {number}, {divide}")
    await asyncio.sleep(1)
    print(number / divide)


async def gather_worker():

    result = await asyncio.gather(  # just create couple of task
        asinc_vorker(30, 10),
        asinc_vorker(40, 10),
        asinc_vorker(50, 10),
        asinc_vorker(60, 10),
        asinc_vorker(70, 10),
        asinc_vorker(80, 10),
    )


event_loop = asyncio.get_event_loop()  # work simultaniuously
task_list = [
    event_loop.create_task(gather_worker()),
]

task = asyncio.wait(task_list)
event_loop.run_until_complete(task)
event_loop.close()
