from datetime import date
from bs4 import BeautifulSoup
import urllib
# Download data from website of KMA
def getkmadata(date): 
	url = 'http://www.kma.go.kr/weather/observation/currentweather.jsp?auto_man=m&type=t99&tm=%d.%d.%d.20%%3A00&x=23&y=5' % (date.year, date.month, date.day)

	# Use BeautifulSoup to interpret htmp page
	content = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(content)
	trs = soup.find_all("tr")[2:]

	# Dictionary to store data, which is indexed with station names
	weatherdata = {}

	for tr in trs:
		# name of city (Korean), encoding is recommended to avoid potential problems.
		station = tr.contents[1].text.encode('utf-8', 'ignore')

		# temperature
		temperature = tr.contents[11].text

		# humidity
		humidity = tr.contents[21].text

		# windspeed
		windspeed = tr.contents[-4].text

		# Other weather condition
		# You may add your code here to get other conditions

		# wrap the data
		weatherdata[station] = (temperature, humidity, windspeed) 

	return weatherdata
		
# Downlaod data of 09/12/2012
casedate = date(year = 2012, month = 9, day = 12)
data = getkmadata(casedate)
print(data)

# print the data
for station, weatherdata in data.items():
	# Printing Korean may rise encoding problems.
	print('station name: %s' % station.decode('utf-8'))
	print('temperature: %s' % data[0])
	print('humidity: %s' % data[1])
	print('windspeed: %s' % data[2])