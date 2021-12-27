import asyncio


# @asyncio.coroutine
async def test_cor(cor_index, number):
	result = 0
	for i in range(number):
		result += i
		# yield
		await asyncio.sleep(0)
		print(f"index {cor_index} -> {i}")
	return result


loop = asyncio.get_event_loop()
tasks = asyncio.wait([
	loop.create_task(test_cor(1, 3)),
	loop.create_task(test_cor(2, 4))
])

loop.run_until_complete(tasks)
loop.close()