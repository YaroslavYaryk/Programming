import asyncio


async def main():
    print("hello")
    task = asyncio.create_task(print_text("some text"))
    # will be after the next line, this time while we're
    # waiting for working pint_text we print 'finished'
    print("finished")


async def print_text(text):
    print(text)
    await asyncio.sleep(1)  # wait until this task finished


asyncio.run(main())
