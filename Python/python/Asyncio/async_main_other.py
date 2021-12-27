import asyncio


async def main():
	task = asyncio.create_task(other_function())
	print('A')
	await asyncio.sleep(1)
	print('B')
	result = await task
	print(f"result was {result}")


async def other_function():
	print(1)
	await asyncio.sleep(1)
	print(2)
	return 10


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
	loop.create_task(main()),
	# loop.create_task(other_function()),
])

loop.run_until_complete(tasks)
loop.close()