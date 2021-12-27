import asyncio


# async def spider(site_name):
#     for page in range(1, 4):
#         await asyncio.sleep(1)
#         print(site_name, page)


# loop = asyncio.get_event_loop()
# tasks = asyncio.wait([
#     loop.create_task(spider("Blog")),
#     loop.create_task(spider("News")),
#     loop.create_task(spider("Forum")),
# ])

# loop.run_until_complete(tasks)
# loop.close()


from tqdm import tqdm
import time


async def spider(site_name):

    for page in range(1, 4):
        await asyncio.sleep(1)
        print(site_name, page)


async def tqdm_line():
    for i in tqdm(range(100)):
        await asyncio.sleep(0.007)


def tqdm_line2():
    print("_callback")   


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    loop.create_task(spider("Blog")),
    loop.create_task(spider("News")),
    loop.create_task(spider("Forum")),
    loop.create_task(tqdm_line())
])

# loop.call_soon(tqdm_line2)  # will work as soon as possible
loop.call_later(2, tqdm_line2)  # work in the time functions wait
loop.call_later(3, tqdm_line2)
# if it's more than function time it won't be working
# loop.call_at(loop.now() + 2, tqdm_line2)  # will work in exact that time
loop.run_until_complete(tasks)
loop.close()
