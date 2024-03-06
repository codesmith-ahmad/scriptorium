# SCRIPTORIUM

## OmniRecords Keeper

Here begins the creation of a new database CLI manager for my files. Successor of "OMNIRECORDS" (name passed to the actual database) which was originally written in PowerShell.

### **Architecture**: [Three-tier](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture])

#### Responsabilities

User creates input
~View~ (New name: <u>Screen</u>) generates **Command** (interprets what user wants)
View sends Command to ~Receiver~ (new name: <u>Control</u>)
Control sends **Instructions** to SQLiteOperator in the form of arguments
SQLiteOperator returns **Package** (Executed query as string, errors if any, table name as string, column names as list[str], rows as list[list])
Control unpacks Package. And generates a **Report** logging all tranformations applied to the table. If a column requires special treatment, flag it and treat it.
Control sends Report to **Screen**
Screen places appropriate data from report into pre-defined areas, will use `__str__(self)` to print the screen 

(Screen -> Control) **Command**:
- Operation: CONNECT, SELECT, INSERT, UPDATE, DELETE, TRANSACT add more when needed... (add to menu)
  - If CONNECT:
    - target = database
  - If SELECT:
    - target = table
    - columns = columns
    - filters = WHERE ...
    - ordering_terms = ORDER BY ...
  - If UPDATE:
    - target = table
    - columns = array of 1
    - filters = WHERE ...
    - values = array of 1
  - If INSERT:
    - target = table
    - columns = columns to add value
    - values = array of 1 or more
  - If DELETE:
    - target = table
    - filters = what comes after the where

(Control -> Data) **Instructions**:
    From **Command**, select appropriate function and pass appropriate arguments as keywords
  
(Data -> Control) **Package**:
- error = put exception variable here if any
- self.sqlite_version = sqlite_version
- list_of_tables = list_of_tables from sqlite_master
- table_info = table_info (do not filter)
- table = table
- columns = headers
- rows = query_results (as list of list or otherwise for easy handling)
  
    DENEST AND CONVERT TUPLES INTO LIST OR DICTIONARIES BEFORE SENDING TO CONTROL

(Control -> Screen) **Report**:
- ...

(Screen -> console) **Screen**:
This class allocates spaces for certain things to display.
For example. the banner will ALWAYS  be displayed at the top,
menu below banner, input below menu, and maybe have a sidebar in the future.
Need appropriate API for this.
List of class attributes:
- banner
- menu
- mode_indicator
- status_bar
- datetime_area
- input_area
- sidebar

<u>Sequence of transformation of input</u>
input > Command > Instructions > queries
queries > Package > Report > Display

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

None.

#### Presentation

- *cutie* or *questionary*: Navigatable options menu
- *prettytable*: Display results in table (tried rich, bad output)

### TODO

In order:

- [ ] encrypt / decrypt db file
- [ ] basic CRUD operations
