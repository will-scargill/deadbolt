# deadbolt

[![Build Status](https://travis-ci.com/will-scargill/deadbolt.svg?branch=master)](https://travis-ci.com/will-scargill/deadbolt)

A command-line tool for securing your files via external media. By keeping the encrypted file seperated from the key file, it can only be decrypted when the external media is plugged into the computer.

## usage

python deadbolt.py [-h] [-l | -u | -r] [-q | -v] file drive

### positional parameters

file - path of the file to be locked/unlocked
drive - drive to read/write the key file from/to

### mode of operation (required)

-l (--lock) - lock the specified file

-u (--unlock) - unlock the specified file

-r (--read) - read the contents of the specified file

### optional parameters

-v (--verbose) - increases output verbosity

-q (--quiet) - decreases output verbosity

-o (--output) - specifies output file name

-R (--remove) - removes original file

## example

`testfile.txt` contains `Hello world`

The command `python deadbolt.py -l testfile.txt e` is run to lock the file

A file `testfile.dblt` is created in the current directory, and the key file will be generated in the deadbolt directory in the base of the specified drive, in this case `E:\deadbolt`

To unlock the file, the command `python deadboly.py -u testfile.dblt e` is run

This will create the file `testfile_deadbolt.txt` which will have the same content as the original file

## todo

- Secure RNG?
