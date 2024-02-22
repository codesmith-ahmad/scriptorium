# SCRIPTORIUM

## OmniRecords Keeper

Here begins the creation of a new database CLI manager for my files. Successor of "OMNIRECORDS" (name passed to the actual database) which was originally written in PowerShell.

### **Development approach**: Test-driven

(begin by creating unit-tests, implement iff successful)

### **Architecture**: [Three-tier](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture])

#### Responsabilities

##### Presentation

1. To generate a `Command` from user input
2. To send `Command`s to Logic
3. To transform `Report`s into output

##### Logic

1. To generate a `Report` from `Command`s
2. To send `Report`s to Presentation
3. To send instructions to Data
4. To transform tables received from data

##### Data

1. To establish connections with databases
2. CRUD operations
3. File I/O

#### Project layout (ask ChatGPT for best project layout)

1. `modules`: keep my logger here, set it up first thing and other things
2. `tests`: where unit tests will be written using `pytest`
3. `model`: ?
4. `controller`: ?
5. `view`: thinking about using `Rich` API for terminal dashboard layout

### Libraries to use

#### Persistence

- *sqlite3* : this CLI is built around it, the core of this project

#### Control

- *click* : this will be used to build the CLI engine

#### Presentation

- *cutie* : Navigatable options menu
- *rich* : this will be used to make the output attractive
- *prettytable* : to output attractive tables, but how to handle conditional styles? See if otehr libraries does both

### TODO

In order:

- [ ] determine project layout, understand the exact purpose of each area
- [ ] create dummy database for training
- [ ] connect to database
- [ ] encrypt / decrypt db file
- [ ] basic CRUD operations
