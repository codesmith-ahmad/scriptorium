# SCRIPTORIUM

## OmniRecords Keeper

Here begins the creation of a new database manager for my files. Successor of "OMNIRECORDS" (name passed to the actual database) which was written in PowerShell.

To use sqlite3 package from Python.

Architecture: Model-View-Controller (uncomitted choice)

Development approach: Test-driven (begin by creating unit-tests, implement iff successful)

Project layout: (ask ChatGPT for best project layout)

1. `modules`: keep my logger here, set it up first thing and other things
2. `tests`: where unit tests will be written using `pytest`
3. `model`: ?
4. `controller`: ?
5. `view`: thinking about using `Rich` API for terminal dashboard layout

### TODO

In order:

- [ ] determine project layout, understand the exact purpose of each area
- [ ] create dummy database for training
- [ ] connect to database
- [ ] encrypt / decrypt db file
- [ ] basic CRUD operations
