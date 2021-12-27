import asyncio


def high_operation(value):

	result = 0
	for i in range(value):
		result += i
	return result


async def main(value):
	""" for better performance """
	result = await loop.run_in_executor(None, high_operation, value)
	# if it's high perfomance work
	print(f"the value is - {result}")


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
	loop.create_task(main(1_000_000)),
	loop.create_task(main(1_000_001)),
])

loop.run_until_complete(tasks)
loop.close()