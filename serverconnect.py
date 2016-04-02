import os
import psycopg2
import urlparse
import time
from serial import Serial

ser = Serial('/dev/ttyAMA0',9600,timeout=0.005)
ser.close()
ser.open()

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse('<postgres database details>')

conn = psycopg2.connect(
	database = url.path[1:],
	user = url.username,
	password = url.password,
	host = url.hostname,
	port = url.port
)

cur = conn.cursor()

while 1:
	cur.execute("""SELECT * FROM devices WHERE rpi_id='<mac_address>' ORDER BY id""")
	rows = cur.fetchall()
	deviceStates = dict()
	deviceName = []
	for row in rows:
		deviceStates[row[1]] = row[2]
		deviceName.append(row[1])
	d1 = deviceStates[deviceName[0]]
	d2 = deviceStates[deviceName[1]]
	d3 = deviceStates[deviceName[2]]
	print deviceStates
	if(d1 == True):
		ser.write('1')
		time.sleep(2)
		print "Device 1 on"
	if(d1 == False):
		ser.write('2')
		time.sleep(2)
		print "Device 1 off"
	if(d2 == True):
		ser.write('3')
		time.sleep(2)
		print "Device 2 on"
	if(d2 == False):
		ser.write('4')
		time.sleep(2)
		print "Device 2 off"
	if(d3 == True):
		ser.write('5')
		time.sleep(2)
		print "Device 3 on"
	if(d3 == False):
		ser.write('6')
		time.sleep(2)
		print "Device 3 off"
	time.sleep(5) 
