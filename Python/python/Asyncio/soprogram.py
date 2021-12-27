from functools import wraps


def coroutine(funk):  # in ordr not to write 'res.send(None'

	@wraps(funk)
	def wrapper(*args, **kwargs):
		res = funk(*args, **kwargs)
		res.send(None)
		return res
	return wrapper


@coroutine
def is_divider(number):

	while True:
		res = yield
		if number % res == 0:
			print(res)


cor = is_divider(100)
cor.send(3)
cor.send(15)
cor.send(10)
cor.send(25)
cor.send(24)
cor.close()