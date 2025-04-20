#Python Standard Libraries
import itertools
import hashlib
import pickle
import math
import random

def GenRainbowTblofPassword():
    rainbowTable = {}
    pwLen = int(input("input desired password length: "))
    pwContent = input("What characters would you like your password to pull from: ")
    for variations in range(pwLen, pwLen + 1): # Defines length as user's input
        #Generates all possible combos of characters used in string below
        for pwTuple in itertools.product(pwContent, repeat=variations): #iterates over each combination of string provided by user
            pw = ""
            md5Hash = hashlib.md5()
            for eachChr in pwTuple:
                pw = pw+"".join(eachChr)
            pw = bytes(pw, 'ascii')
            md5Hash.update(pw) # creates MD5 hash of the password
            md5Digest = md5Hash.hexdigest()
            rainbowTable[pw.decode('ascii')] = md5Digest
    return rainbowTable

def PickleNSerialize(rainbowTable):
    # Open (and create if file does not exist) the destination File (write binary)
    pickleFileWrite = open('./rainbow.db', 'wb') 
    pickle.dump(rainbowTable, pickleFileWrite) #serialize the list and DUMP to file                    
    pickleFileWrite.close() 
    pickleFileRead = open('./rainbow.db', 'rb') # Open the pickle file (read binary)
    retrievedDict = pickle.load(pickleFileRead) # LOAD the serialized data into a list
    retrievedList= list(retrievedDict.items())
    return retrievedList

def PullRandomPasswords(retrievedList):
    count = 0
    randomNumList = []
    randomPwList = []
    while count < 15:
        randomNumList.append(random.randint(1, len(retrievedList)))
        count += 1
    for eachNum in randomNumList:
        randomPwList.append(retrievedList[eachNum])
    return randomPwList

def PrintResults(randomPwList):
    count = 0
    for eachPw in randomPwList:
        count += 1
        print(count, eachPw)    

rainbowTable = GenRainbowTblofPassword()
retrievedList = PickleNSerialize(rainbowTable)
randomPwList = PullRandomPasswords(retrievedList)
PrintResults(randomPwList)