import random
import os
import string
import pickle

def run(filename, drive):
	cwd = os.getcwd()
	try:
		os.chdir(drive + ":\\deadbolt\\" )
	except FileNotFoundError:
		return "FileNotFoundError - nodirectory"

	try:
		manifestFile = open("manifest.txt", "rb")
	except FileNotFoundError:
		return "FileNotFoundError - nomanifest"
	data = pickle.load(manifestFile)
	manifestFile.close()

	filenameNoEx = (os.path.splitext(filename))[0]

	keyFileName = data[filenameNoEx][0]
	try:
		keyFile = open(keyFileName+".dkey", "rb")
	except FileNotFoundError:
		return "FileNotFoundError - nokeyfile"
	bytesKey = pickle.load(keyFile)
	keyFile.close()

	os.chdir(cwd)

	lockedBytes = []
	try:
		with open(filename, "rb") as f:
			    bytesRead = f.read()
			    for b in bytesRead:
			    	lockedBytes.append(b)
	except FileNotFoundError:
		return "FileNotFoundError - missingfile"

	unlockedBytes = []
	for key in bytesKey:
		unlockedBytes.append(lockedBytes[bytesKey[key]])

	unlockedBytesToWrite = bytes(unlockedBytes)
	newFile = open(filenameNoEx + "_deadbolt" + data[filenameNoEx][1], "wb")
	newFile.write(unlockedBytesToWrite)
	newFile.close()

	return "OK"