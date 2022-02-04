import csv
import os
import random


nameIter = 0
beginText = "name,number,address \n"
csvFile = open('./output.txt', 'w')
csvFile.write(beginText)
while nameIter <= 100:
    randNum = random.randrange(1000000000, 9999999999, 100)
    randAddr = random.randrange(100, 9999, 15)
    dataName = "Test Name" + str(nameIter) 
    dataNumber = str(randNum)
    dataAddress = str(randAddr)  + ' Sesame St.'
    fullData = dataName + ',' + dataNumber + ',' + dataAddress + '\n'
    csvFile.write(fullData)
    nameIter+=1
csvFile.close()