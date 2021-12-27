import asyncio
import time


async def asinc_vorker(seconds):
    print(f"start worker - {seconds}")
    await asyncio.sleep(seconds)
    print(f'end worker - {seconds}')


async def stop_event_loop(loop, second):
    print(f'Stop in {second}s')
    await asyncio.sleep(second)
    loop.stop()  # stop for run_forever
    print("Stopped")


async def resolve_future(future):
    await asyncio.sleep(5)
    print("Future set result")
    future.set_result(10)


async def wait_for_future(future):
    result = await future
    print(f"Future result: {result}")


loop = asyncio.get_event_loop()
fut = asyncio.Future()

loop.create_task(asinc_vorker(3))
loop.create_task(asinc_vorker(4))
loop.create_task(stop_event_loop(loop, 10))
loop.create_task(resolve_future(fut))
loop.create_task(wait_for_future(fut))
loop.run_forever()
loop.close()
