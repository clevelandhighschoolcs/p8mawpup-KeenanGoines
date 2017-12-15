import urllib2

import time



def webdata():

	timeT = 0

	lengthB = ''

	while timeT < 5:

		URL = urllib2.urlopen ('https://twitter.com/YoYoGames?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor')
		data = URL.read()
		datastring = str(data)
		lengthA = len(datastring)
		
		print (lengthA)
		if lengthB != '' and lengthA != lengthB:
			print ('This tweeter feed has changed')
			return
		else:
			lengthB = lengthA
		timeT +- 1
		time.sleep(5)
		print "Restarting"
webdata()
