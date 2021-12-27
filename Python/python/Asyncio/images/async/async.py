import asyncio
import aiohttp
import time


def write(data):
    file_name = f"{int(time.time() * 1000)}.jpeg"
    with open(file_name, 'wb') as file:
        file.write(data)


async def fetch_data(url, session):

    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write(data)


async def main2():

    url = "https://loremflickr.com/320/240"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch_data(url, session)))

        await asyncio.wait(tasks)


if __name__ == "__main__":
    t0 = time.time()
    asyncio.run(main2())
    print(time.time() - t0)
