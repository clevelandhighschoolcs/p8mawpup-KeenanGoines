import urllib2
import time
import re
import requests
from twilio.rest import Client

#To ge this to work, do these following things while in your virtualenv scripts folder, whilst having virtualenv enabled:

#pip install twilio
#pip install Client
#pip install requests

account_sid = 'your account sid here'
auth_token = 'your auth token here'
twilio_phone_number = '+your twilio phone number here'
my_phone_number = '+your phone number here'


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
			body = "This tweeter feed has changed!"
			client = Client(account_sid, auth_token)
			client.messages.create(
			body=body,
			to=my_phone_number,
			from_=twilio_phone_number
			)
			return
		else:
			lengthB = lengthA
		timeT +- 1
		time.sleep(5)
		print "Restarting"
webdata()
