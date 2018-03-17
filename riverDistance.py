#!/usr/bin/python
import csv
from collections import OrderedDict
import math


dataTypes = [
'Flow Rate (m/s)',
'Phosphates (mol/L)',
'Temperature (deg C)',
'pH',
'Conductivity (uS/cm)',
'Ammonium (mg/L)',
' Nitrates (mg/L)',
'Turbidity (NTU)',
'DO'
]



rivers = [
"Rocky Creek",
"Wards Creek",
"Buck Mtn",
"Old House Run ",
"Deer Creek",
"Greenbriar at Cass",
"Shavers Fork",
"West Greenbrier at Durbin",
"East Greenbrier",
"Bullpasture",
"CHM, E. Greenbriar",
"Leatherbark Run",
"Riverview",
"Deer Run"
]

riverDict = OrderedDict()



def display(dic):
	for river in rivers:
		if river in dic:
			print river
			for dataType in dataTypes:
				print '   ',dataType, ': ', dic[river][dataType][0]  


with open('riverData.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['River'] in riverDict:
			for dataType in dataTypes:
				if dataType in riverDict[row['River']]:
					data = row[dataType]
					if (any(i.isdigit() for i in data)):
						print data
						data = float(data)
						
						riverDict[row['River']][dataType][0]+=data
						riverDict[row['River']][dataType][1]+=1
		else:
			riverDict[row['River']] = OrderedDict()
			for dataType in dataTypes:
				data = row[dataType]
				
				riverDict[row['River']][dataType]=[0.0,1]
				if (any(i.isdigit() for i in data)):
					data = float(data)
					riverDict[row['River']][dataType][0]+=data
		#display(riverDict)

for river in rivers:
		if river in riverDict:
			for datatype in dataTypes:
				average = riverDict[river][datatype][0]/riverDict[river][datatype][1]
				riverDict[river][datatype] = average

minimum = [float('inf'),'','']
for a in rivers:
	for b in rivers:
		if a != b:
			sumOfDiffSquared  = 0
			for dataType in dataTypes:
				diff = riverDict[a][dataType]-riverDict[b][dataType]
				diffSquared = diff**2
				sumOfDiffSquared+= diffSquared
			distance = math.sqrt(sumOfDiffSquared)
			
			print "distance from ", a, " to ", b, ': ',distance

			if distance < minimum[0] and distance > 0.0 :
				minimum[0] = distance
				minimum[1] = a
				minimum[2] = b
	