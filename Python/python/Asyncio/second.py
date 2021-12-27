import asyncio


async def find_data():

	print("start fetching")
	await asyncio.sleep(2)
	print("done fetching")
	return {'data': 1}


async def print_numbers():

	for i in range(10):
		print(i)
		await asyncio.sleep(0.25)


async def main():

	task1 = asyncio.create_task(find_data())
	task2 = asyncio.create_task(print_numbers())

	value = await task1  # we make 'print_numbers'
	# 2 seconds and then end process
	print(value)
	await task2  # we complete print_numbers til the end


asyncio.run(main())
