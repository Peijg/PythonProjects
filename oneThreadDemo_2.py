# -*- coding: utf-8 -*-

from time import ctime,sleep

def music(func):
	for i in range(2):
		print "I was listening to %s. %s" % (func,ctime())
		sleep(1)


def movie(func):

	for i in range(3):
		print "I want to watch %s! %s" % (func,ctime())

if __name__ == '__main__':
	music(u'大风吹')
	movie(u'阿凡达')

	print "all over %s" % ctime()