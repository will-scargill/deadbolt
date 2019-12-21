import random
import os
import string
import pickle

def run(filename, drive, verbosity):
	fileBytes = []
	try:
		with open(filename, "rb") as f:
		    bytesRead = f.read()
		    for b in bytesRead:
		    	#print(b)
		    	fileBytes.append(b)
	except FileNotFoundError:
		return "FileNotFoundError - missingfile"

	if verbosity == 1:
		print("read file bytes")

	lockedBytes = [None] * round(len(bytesRead) + (len(bytesRead) * random.uniform(1, 4)))
	bytesKey = {}
	bKeyIndex = 0
	for b in bytesRead:
		unique = False
		while unique == False:
			index = random.randint(0, (len(lockedBytes) - 1))
			if lockedBytes[index] != None:
				pass
			else:
				unique = True
				bytesKey[bKeyIndex] = index
				lockedBytes[index] = b
				bKeyIndex += 1

	if verbosity == 1:
		print("scrambled file bytes")

	for i in range(len(lockedBytes)):
		if lockedBytes[i] == None:
			lockedBytes[i] = random.randint(1, 255)
		else:
			pass

	if verbosity == 1:
		print("added random data")

	filenameNoEx = (os.path.splitext(filename))[0]
	filenameEx = (os.path.splitext(filename))[1]


	lockedFile = open(filenameNoEx + ".dblt", "wb")
	lockedFile.write(bytes(lockedBytes))
	lockedFile.close()

	if verbosity == 1:
		print("wrote locked file")

	letters = string.ascii_lowercase
	keyFileName = "".join(random.sample(letters,16))

	try:
		os.chdir(drive + ":\\deadbolt\\" )
	except FileNotFoundError:
		os.mkdir(drive + ":\\deadbolt\\")
		os.chdir(drive + ":\\deadbolt\\" )

	keyFile = open(keyFileName + ".dkey", "wb")
	pickle.dump(bytesKey, keyFile)
	keyFile.close()

	if verbosity == 1:
		print("wrote key file")

	try:
		manifestFile = open("manifest.txt", "rb")
	except FileNotFoundError:
		manifestFile = open("manifest.txt", "wb")
		pickle.dump({}, manifestFile)
		manifestFile.close()
		manifestFile = open("manifest.txt", "rb")
	data = pickle.load(manifestFile)
	manifestFile.close()

	data[filenameNoEx] = [keyFileName, filenameEx]

	manifestFile = open("manifest.txt", "wb")
	pickle.dump(data, manifestFile)
	manifestFile.close()

	if verbosity == 1:
		print("updated manifest")

	return "OK"