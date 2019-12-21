import random
import os
import string
import pickle

def run(filename, drive, verbosity):
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

	if verbosity == 1:
		print("read manifest")

	filenameNoEx = (os.path.splitext(filename))[0]

	keyFileName = data[filenameNoEx][0]

	try:
		keyFile = open(keyFileName+".dkey", "rb")
	except FileNotFoundError:
		return "FileNotFoundError - nokeyfile"
	bytesKey = pickle.load(keyFile)
	keyFile.close()

	if verbosity == 1:
		print("read key file")

	os.chdir(cwd)

	lockedBytes = []
	try:
		with open(filename, "rb") as f:
			    bytesRead = f.read()
			    for b in bytesRead:
			    	lockedBytes.append(b)
	except FileNotFoundError:
		return "FileNotFoundError - missingfile"

	if verbosity == 1:
		print("read locked bytes")

	unlockedBytes = []
	for key in bytesKey:
		unlockedBytes.append(lockedBytes[bytesKey[key]])

	if verbosity == 1:
		print("decoded locked file")

	unlockedBytesToWrite = bytes(unlockedBytes)
	try:
		print(unlockedBytesToWrite.decode("utf-8"))
	except UnicodeDecodeError:
		print(unlockedBytesToWrite)

	return "OK"