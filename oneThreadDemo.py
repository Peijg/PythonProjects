from time import ctime,sleep


def music():
	for i in range(2):
		print "I was listening to music. %s" % ctime()
		sleep(1)


def movie():

	for i in range(3):
		print "I want to watch movie! %s" % ctime()

if __name__ == '__main__':
	music()
	movie()
	print "all over %s" % ctime()		