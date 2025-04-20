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