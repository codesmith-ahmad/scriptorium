import sqlite3
from sqlite3 import Row
from enum import Enum

# sqlite3.register_adapter... #TODO put that in separate file

class SQL:
    
    class Operation(Enum):
        SELECT = "SELECT"
        INSERT = "INSERT"
        UPDATE = "UPDATE"
        DELETE = "DELETE"
        
    def __init___(self,
        operation: str, # required regardless of op
        table: str,     # required regardless of op
        columns: list = [],
        # TODO if len = 0, then replace by '*' IFF SELECT, by '' IFF INSERT, error if UPDATE, irrelevant for DELETE
        # TODO required for UPDATE
        # TODO special case for INSERT and DELETE        
        values: list[tuple] = [],
        # TODO required for UPDATE as a list of singular tuple of size 1
        # TODO required for INSERT
        conditions: list[str] = None,  # WHERE, optional
        order: str = None     # ORDER BY, optional
        ):
            self.operation = operation,
            self.table = table,
            self.columns = columns,
            self.values = values,
            self.conditions = conditions,
            self.order = order
            
            self.__query = None
    
    def build_sql(self) -> int:
        #TODO USE DATA ABOVE TO CONSTRUCT QUERY BASED ON OPERATION TYPE
        pseudo = """
        if self.operation.upper() any of the Operatio enum, op = self.operation, 
        return 0 if successful,
        return 1 if not
        """
    
    def __str__(self):
        if self.__query is None:
            self.query = self.build_sql()
        return self.__query

class Result:
    def __init__(self,
        error = ValueError("Empty Result"),
        version: str = None,      # to test CONNECT # TODO consider sqlcipher??????
        rows: list[Row] = None,   # to test SELECT
        lastrowid: int = None,    # to test INSERT
        rowcount: int = None,     # to test UPDATE
        tablecount: dict[str,int] # to test DELETE
        = {"before": None, "after": None}, 
        query: SQL = None
        ):
            self.error = error,
            self.version = version,
            self.rows = rows,
            self.lastrowid = lastrowid,
            self.rowcount = rowcount
            self.query = query
    
class Database:
    # TODO add password for authentification
    # TODO combine all db ops into one function: execute(sql)
    # TODO create function: build_sql() -> SQL which creates an sql query object
    
    source: str = None
    con: Connection = None
    
    @classmethod # NOT STATIC
    def connect(cls,database: str) -> None: #TODO CHANGE TO connect(source,password)
        cls.config_sqlite3()
        cls.source = database
        cls.con = sqlite3.connect(
            database=database,
            detect_types=sqlite3.PARSE_DECLTYPES)
        cls.con.row_factory = sqlite3.Row # will now return Rows instead of tuples.
        # info
    
    @classmethod
    def execute(cls,sql: SQL) -> Result:
        """Executes SQL query"""
        try:
            r = Result()
            code = sql.build_sql()
            if successful, sql.__str
            c = cls.con.execute(sql.__)
            if query[0:6].lower() == 'select':
                result = self.cursor.fetchall()
                self.conn.close()
                return result
        except SQLException as e:
            Result.error = e
        except Error as e:
            Result.error = e
        finally:
            return r
        
    def has_error(self) -> bool:
        """Check if the result contains an error."""
        return self.error is not None
    
    @classmethod
    def close(cls):
        """close this bitch"""
        cls.con.close()
    
    @classmethod
    def select(cls,
        dql: str = None,
        table: str = None,  # FROM
        columns: list[str] = None,     # SELECT
        conditions: list[str] = None,  # WHERE
        ordering_terms: str = None     # ORDER BY
    ) -> list[Row]:
        """
        SELECT [columns] FROM table
        WHERE condition1 AND condition2 ...AND conditionN
        ORDER BY ordering_terms
        """
        query = ""
        
        if dql is not None:
            query = dql
        elif table is not None and columns is not None:
            query = f"SELECT {', '.join(columns)} FROM {table}"
            
            if conditions:
                query += f" WHERE {' AND '.join(conditions)}"
            
            if ordering_terms:
                query += f" ORDER BY {ordering_terms}"
        else:
            raise ValueError("Table and columns must be provided for SELECT operation.")
        
        # Execute the query using the database connection
        # Example: rows = cls.execute_query(query)
        # Remember to handle exceptions and return appropriate results
        # e.g., return list of Row objects, etc.

        # Replace `pass` with appropriate execution code
        pass


    @classmethod
    def insert(cls,
        dml: str = None,
        table: str = None,
        columns: list[str] = None,
        values: list[tuple] = None
    ) -> Status:
        """INSERT INTO table columns VALUES tuples]"""
        query = f"INSERT INTO {table}"

        if dql:
            query += f" {dql}"
        elif table and columns and values:
            query += f" ({', '.join(columns)}) VALUES "
            value_strings = []
            for value_set in values:
                value_strings.append(f"({', '.join(map(str, value_set))})")
            query += ", ".join(value_strings)
        else:
            raise ValueError("Either `values` or `dql` must be provided for INSERT operation.")

        # Execute the query using the database connection
        # Example: cls.execute_query(query)
        # Remember to handle exceptions and return appropriate results
        # e.g., return number of rows affected, inserted IDs, etc.

        # Replace `pass` with appropriate execution code
        pass
    
    @classmethod
    def update(cls,
        dml: str = None,
        table: str = None,
        columns: list[str] = None,
        value: int | str = None,
        conditions: list[str] = None
    ) -> Status:
        """Execute an UPDATE operation on the database."""
        query = ""
        
        if dml is not None:
            query = dml
        elif table is not None and columns is not None and value is not None and conditions is not None:
            query = f"UPDATE {table} SET {', '.join([f'{col} = {value}' for col in columns])} WHERE {' AND '.join(conditions)}"
        else:
            raise ValueError("Table, columns, value, and conditions must be provided for UPDATE operation.")
        
        # Execute the query using the database connection
        # Example: status = cls.execute_query(query)
        # Remember to handle exceptions and return appropriate results
        # e.g., return a Status object indicating success or failure, etc.

        # Replace `pass` with appropriate execution code
        pass

        
    @classmethod
    def delete(cls,
        dml: str = None,
        table: str = None,
        conditions: list[str] = None
    ) -> Status:
        """Execute a DELETE operation on the database."""
        query = ""
        
        if dml is not None:
            query = dml
        elif table is not None and conditions is not None:
            query = f"DELETE FROM {table} WHERE {' AND '.join(conditions)}"
        else:
            raise ValueError("Table and conditions must be provided for DELETE operation.")
        
        # Execute the query using the database connection
        # Example: status = cls.execute_query(query)
        # Remember to handle exceptions and return appropriate results
        # e.g., return a Status object indicating success or failure, etc.

        # Replace `pass` with appropriate execution code
        pass
    
    @classmethod
    def config_sqlite3(cls) -> None:
        sqlite3.register_converter
        sqlite3.register_adapter
        ...

from pysqlcipher3 import dbapi2 as sqlite3


class Database(object):
    def __init__(self, dbname):
        self.dbname = dbname

    def connDB(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA key='mypassword'")

    def createDB(self):
        self.connDB()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            login TEXT NOT NULL,
            passwd TEXT);
            '''
        )

        self.cursor.execute(
            '''
            INSERT INTO users (name, login, passwd)
            VALUES ("Admininstrator", "admin", "12345")
            '''
        )
        self.conn.commit()
        self.conn.close()

    def queryDB(self, sql):
        self.connDB()
        self.cursor.execute(sql)

        if sql[0:6].lower() == 'select':
            result = self.cursor.fetchall()
            self.conn.close()
            return result
        else:
            self.conn.commit()
            self.conn.close()