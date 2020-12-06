# RollTables

A flexible Python package for creating and using random tables with your favorite TTRPG.

## Usage

RollTables can be run from the command line. It takes two text files as input: one with tables and one with text to be formatted with random choices from the tables.

### Tables

Tables are designed to be simple to use. Each table is made up of lines in a text file. The first line is the name of the table and all following lines are the different options to choose from. For example:

```shell
creature
dragon
yeti
hellhound
vampire
kobold
```

Multiple tables can placed in the same file, seperated by blank lines:

```shell
dungeon creator
abberation
cultists
forgotten empire
natural formation

dungeon history
abandoned by creators
abandoned due to plague
conquered by invaders
destroyed by attacking raiders
```

### Formatting Text

Text between curly braces, like `{creature}`, is replaced with a random choice from the table with the same name.

For example:

```shell
This dungeon was created long ago by {dungeon creator}, but has since been {dungeon history}. A fearsome {creature} now uses it as its lair.
```

Becomes:

```shell
This dungeon was created long ago by cultists, but has since been abandoned due to plague. A fearsome vampire now uses it as its lair.
```

### Command

The command looks something like this:

```shell
rolltables text.txt tables.txt
```

### Importing

RollTables can also be imported as a Python package.

```python
import rolltables

database = rolltables.load('/path/to/db.txt')
text = database.query("A wild {creature} leaps out and attacks!")
```
