# SCRIPTORIUM

## OmniRecords Keeper

Here begins the creation of a new database CLI manager for my files. Successor of "OMNIRECORDS" (name passed to the actual database) which was originally written in PowerShell.

**Architecture**: Model-View-Controller or Layered or else?

**Development approach**: Test-driven (begin by creating unit-tests, implement iff successful)

**Project layout**: (ask ChatGPT for best project layout)
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

- *rich* : this will be used to make the output attractive
- *prettytable* : to output attractive tables, but how to handle conditional styles? See if otehr libraries does both

### TODO

In order:

- [ ] determine project layout, understand the exact purpose of each area
- [ ] create dummy database for training
- [ ] connect to database
- [ ] encrypt / decrypt db file
- [ ] basic CRUD operations
