import os


def application():
	try:	
		os.remove("OD_data.txt")
	except OSError:
		pass
	try:
		os.remove("data.json")
	except OSError:
		pass
	return


