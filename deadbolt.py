import argparse

from modules import locker
from modules import unlocker
from modules import reader

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()


group.add_argument("-l", "--lock", help="lock the file", action="store_true")
group.add_argument("-u", "--unlock", help="unlock the file", action="store_true")
group.add_argument("-r", "--read", help="read the file", action="store_true")
parser.add_argument("file", help="file to use")
parser.add_argument("drive", help="drive number to read/save the key file to/from")


args = parser.parse_args()

if args.lock:
    response = locker.run(args.file, args.drive)
    if response == "FileNotFoundError - missingfile":
        pass
    elif reponse == "OK":
        pass
elif args.unlock:
    response = unlocker.run(args.file, args.drive)
    if response == "FileNotFoundError - missingfile":
        print("Specified file " + args.file + " could not be found")
    elif response == "FileNotFoundError - nodirectory":
        print("No deadbolt directory could be found on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nokeyfile":
        print("No corresponding key file exists on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nomanifest":
        print("No manifest could be found on the specified drive " + args.drive)
    elif reponse == "OK":
        pass
elif args.read:
    response = reader.run(args.file, args.drive)
    if response == "FileNotFoundError - missingfile":
        print("Specified file " + args.file + " could not be found")
    elif response == "FileNotFoundError - nodirectory":
        print("No deadbolt directory could be found on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nokeyfile":
        print("No corresponding key file exists on the specified drive " + args.drive)
    elif response == "FileNotFoundError - nomanifest":
        print("No manifest could be found on the specified drive " + args.drive)
    elif reponse == "OK":
        pass


