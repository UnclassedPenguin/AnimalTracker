# AnimalTracker
Program for keeping track of animals.

## Requirements

- Python3
    - PyQt5
    - Pandas
    - sqlite3
    - ConfigParser
    - xlsxwriter

## Usage
Clone the repository.
```shell
$ cd AnimalTracker
$ python AnimalTracker.py
```

When ran, the program reads the config.ini file which only has to contain three lines:

```init
[DEFAULT]
database = ATDataBase.dat
savedir = ./Saves/ 
```

The database will be created if it doesn't exist, and the default save directory (savedir) is included in the repository, but can be changed to whatever folder you want that you have write access to. 
