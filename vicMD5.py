"""
facelessg00n 2020

Exports all MD5 values from a VICS formatted JSON file

Place this file in the same folder as a VICS JSON file
and run with 'python3 vicMD5.py'
"""
#------ Load Dependencies-----------------------
import os
import json

#------ Setup Variables-------------------------
line = 0
hash=[]
jsonFile=[]

#--- Locate JSON file---------------------------
fileList = os.listdir(os.getcwd())
print("Locating Json file in current directory")
for y in fileList:
    if y.endswith('.json'):
        jsonFile.append(y)

#------ Load file-------------------------------
print("\nLoading file, this may take some time")
json = json.loads(open(jsonFile[0]).read())
value = json['value']
length = len(value)

#------ Extract values to a list----------------
for x in value:
    #print  (json['value'][line]['MD5'])
    hash.append(json['value'][line]['MD5'])
    line = line +1
    if line >=(length):
        break
print ("\n"+str(line)+" lines have been added to the list.")
print ("\nWriting file now")

#------Write an output file---------------------
outF= open("Hashes.txt" , "w")
for z in hash:
    outF.write(z)
    outF.write("\n")
outF.close()
print ("\nWriting file is complete")
