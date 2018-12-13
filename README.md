# AnimalTracker
Program for keeping track of animals, a basic herd management software.
Keep track of animal body condition, weight, parents, children, and more.

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

When ran, the program reads the config.ini file which only has to contain four lines:

```init
[DEFAULT]
database = ATDataBase.dat
savedir = ./Saves/
ui = UI3
```

The database will be created if it doesn't exist, and the default save directory (savedir) is included in the repository, but can be changed to whatever folder you want that you have write access to. You can change these values in the config file directly or through the "options" menu in the program. 
