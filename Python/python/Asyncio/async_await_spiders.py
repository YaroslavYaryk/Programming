import asyncio


async def get_pages(site_name):
	await asyncio.sleep(0.5)
	print(f"Get pages for {site_name}")
	return range(1, 4)


async def get_page_data(site_name, page):
	await asyncio.sleep(1)
	print(f"Get data for {site_name} - ({page})")


async def spider(site_name):
	pages = await get_pages(site_name)
	for i in pages:
		await get_page_data(site_name, i)

loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    loop.create_task(spider("Blog")),
    loop.create_task(spider("News")),
    loop.create_task(spider("Forum")),
])

loop.run_until_complete(tasks)
loop.close()