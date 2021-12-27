import asyncio


async def print_numbers():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds passed")
        count += 1
        await asyncio.sleep(1)


def main():
    event_loop = asyncio.get_event_loop()
    tasks = asyncio.wait([
        event_loop.create_task(print_numbers()),
        event_loop.create_task(print_time())
    ])

    event_loop.run_until_complete(tasks)
    event_loop.close()


if __name__ == '__main__':
    main()
