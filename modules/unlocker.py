import os
import json
import pickle


def run(filename, drive, output, verbosity):
    cwd = os.getcwd()  # store this for later while we read the manifest file

    try:
        lockedFile = open(filename, "r")
    except FileNotFoundError:
        return "FileNotFoundError - missingfile"
    data = json.load(lockedFile) 
    lockedFile.close()

    bytesRead = data[1]
    fileIndentifier = data[0]

    lockedBytes = []

    for b in bytesRead:
        lockedBytes.append(b)

    try:
        os.chdir(drive + ":\\deadbolt\\")
    except FileNotFoundError:
        return "FileNotFoundError - nodirectory"

    try:
        manifestFile = open("manifest.json", "rb")
    except FileNotFoundError:
        return "FileNotFoundError - nomanifest"

    manifestData = json.load(manifestFile)
    manifestFile.close()

    if verbosity == 1:
        print("read manifest")

    keyFileName = manifestData[fileIndentifier][2]
    try:
        keyFile = open(keyFileName + ".dkey", "r")
    except FileNotFoundError:
        return "FileNotFoundError - nokeyfile"
    bytesKey = json.load(keyFile)
    keyFile.close()

    if verbosity == 1:
        print("read key file")

    os.chdir(cwd)  # go back to original directory

    if verbosity == 1:
        print("read locked bytes")

    unlockedBytes = []
    for key in bytesKey:
        unlockedBytes.append(lockedBytes[bytesKey[key]])  # by iterating through bytesKey in order, the order of the original data is preserved.

    if verbosity == 1:
        print("decoded locked file")

    if output == "":
        unlockedFileName = manifestData[fileIndentifier][0] + "_deadbolt"
    else:
        unlockedFileName = output

    unlockedBytesToWrite = bytes(unlockedBytes)
    newFile = open(unlockedFileName + manifestData[fileIndentifier][1], "wb")
    newFile.write(unlockedBytesToWrite)
    newFile.close()

    if verbosity == 1:
        print("wrote unlocked file")

    return "OK"
