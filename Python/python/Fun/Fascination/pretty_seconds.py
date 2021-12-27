import time


def get_pretty_seconds(second):
	days = second // (24 * 60 * 60)
	hours = (second - (days * 24*3600))//3600
	minutes = (second - (days*24 * 60 * 60 + hours*3600)) // 60
	seconds = second % 60
	print(f"{round(days)} : {round(hours)} : {round(minutes)} : {round(seconds)}")


get_pretty_seconds(time.time())

