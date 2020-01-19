import random
import os
import ntpath
import string
import json


def run(filename, drive, output, verbosity):
    letters = string.ascii_lowercase
    fileBytes = []
    try:
        with open(filename, "rb") as f:
            bytesRead = f.read()
            for b in bytesRead:  # iterate through the individual bytes and put them in a list
                fileBytes.append(b)
    except FileNotFoundError:
        return "FileNotFoundError - missingfile"

    if verbosity == 1:
        print("read file bytes")

    # generate an empty list of random length
    lockedBytes = [None] * round(len(bytesRead) + (len(bytesRead) * random.uniform(2, 5)))
    bytesKey = {}
    bKeyIndex = 0
    for b in bytesRead:
        unique = False
        while unique is False:
            index = random.randint(0, (len(lockedBytes) - 1))
            if lockedBytes[index] is not None:  # if the random index already has something in it that isnt None
                pass
            else:
                unique = True  # exit the while
                bytesKey[bKeyIndex] = index  # set the position in the Key
                lockedBytes[index] = b  # assign the byte to the lockedBytes list at the given index
                bKeyIndex += 1

    if verbosity == 1:
        print("scrambled file bytes")

    for i in range(len(lockedBytes)):
        if lockedBytes[i] is None:  # If the index is None
            lockedBytes[i] = random.randint(1, 255)  # generate random data to fill it
        else:
            pass

    if verbosity == 1:
        print("added random data")

    filenameNoEx = ntpath.splitext(ntpath.basename(filename))[0]  # Get the filename path
    filenameEx = (ntpath.splitext(filename))[1]  # Get the file extenstion

    lockedFileData = []
    lockedFileIndentifier = "".join(random.sample(letters, 16))
    lockedFileData.append(lockedFileIndentifier)
    lockedFileData.append(lockedBytes)

    if output == "":  # If the user hasn't specified a custom file output name
        lockedFileName = filenameNoEx
    else:
        lockedFileName = output

    lockedFile = open(lockedFileName + ".dblt", "w")
    json.dump(lockedFileData, lockedFile)
    lockedFile.close()

    if verbosity == 1:
        print("wrote locked file")

    keyFileName = "".join(random.sample(letters, 16))  # generate a random name for the key file

    try:
        os.chdir(drive + ":\\deadbolt\\")
    except FileNotFoundError:  # deadbolt dir does not exist
        os.mkdir(drive + ":\\deadbolt\\")
        os.chdir(drive + ":\\deadbolt\\")

    keyFile = open(keyFileName + ".dkey", "w")
    json.dump(bytesKey, keyFile)
    keyFile.close()

    if verbosity == 1:
        print("wrote key file")

    try:
        manifestFile = open("manifest.json", "r")
    except FileNotFoundError:
        manifestFile = open("manifest.json", "w")
        json.dump({}, manifestFile)  # create empty dictionary
        manifestFile.close()
        manifestFile = open("manifest.json", "r")
    data = json.load(manifestFile)
    manifestFile.close()

    data[lockedFileIndentifier] = [filenameNoEx, filenameEx, keyFileName]  # add new entry to manifest.txt

    manifestFile = open("manifest.json", "w")
    json.dump(data, manifestFile)
    manifestFile.close()

    if verbosity == 1:
        print("updated manifest")

    return "OK"
