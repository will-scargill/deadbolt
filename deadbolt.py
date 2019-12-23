import argparse

from modules import locker
from modules import unlocker
from modules import reader

parser = argparse.ArgumentParser(description="secure your files")
operationType = parser.add_mutually_exclusive_group() # user shouldnt be able to run multiple different operations at once
volumeType = parser.add_mutually_exclusive_group() # cant be quiet and verbose at the same time


operationType.add_argument("-l", "--lock", help="lock the file", action="store_true")
operationType.add_argument("-u", "--unlock", help="unlock the file", action="store_true")
operationType.add_argument("-r", "--read", help="read the file", action="store_true")
volumeType.add_argument("-q", "--quiet", help="decrease output verbosity", action="count", default=0)
volumeType.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)
parser.add_argument("file", help="file to be locked/unlocked")
parser.add_argument("drive", help="drive number to read/save the key file to/from")


args = parser.parse_args()

if args.lock:
    response = locker.run(args.file, args.drive, args.verbose)
    if response == "FileNotFoundError - missingfile" and args.quiet < 1:
        print("deadbolt.py: error: specified file " + args.file + " could not be found")
    elif response == "OK" and args.quiet < 2:
        print("file locked")
elif args.unlock:
    response = unlocker.run(args.file, args.drive, args.verbose)
    if response == "FileNotFoundError - missingfile" and args.quiet < 1:
        print("deadbolt.py: error: specified file " + args.file + " could not be found")
    elif response == "FileNotFoundError - nodirectory" and args.quiet < 1:
        print("deadbolt.py: error: no deadbolt directory could be found on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nokeyfile" and args.quiet < 1:
        print("deadbolt.py: error: no corresponding key file exists on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nomanifest" and args.quiet < 1:
        print("deadbolt.py: error: no manifest could be found on the specified drive " + args.drive)
    elif response == "OK" and args.quiet < 2:
        print("file unlocked")
elif args.read:
    response = reader.run(args.file, args.drive, args.verbose)
    if response == "FileNotFoundError - missingfile" and args.quiet < 1:
        print("deadbolt.py: error: specified file " + args.file + " could not be found")
    elif response == "FileNotFoundError - nodirectory" and args.quiet < 1:
        print("deadbolt.py: error: no deadbolt directory could be found on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nokeyfile" and args.quiet < 1:
        print("deadbolt.py: error: no corresponding key file exists on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nomanifest" and args.quiet < 1:
        print("deadbolt.py: error: no manifest could be found on the specified drive " + args.drive)
    elif response == "OK" and args.quiet < 2:
        print("\nfile output displayed above")
else:
    print("deadbolt.py: error: no mode of operation was specified [-l | -u | -r]")


