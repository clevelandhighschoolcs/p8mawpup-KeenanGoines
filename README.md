# p8mawpup-KeenanGoines
p8mawpup-KeenanGoines created by GitHub Classroom

Made in Python 3.6

import urllib2 import time

def webdata(): timeT = 0 length = ' ' while timeT < 5: URL = urllib2.urlopen ('https://twitter.com/YoYoGames?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor') data = URL.read() datastring = str(data) lengthA = len(datastring)

	print (lengthA)
	if lengthB != ' ' amd lengthA != lengthB:
		print ('This tweeter feed has changed')
		return
	else:
		lengthB - lengthA
	timeT +- 1
	time.sleep(5)
webdata()
