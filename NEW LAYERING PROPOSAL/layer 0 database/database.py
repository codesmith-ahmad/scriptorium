import sqlite3
from sqlite3 import Row

# sqlite3.register_adapter...

class Database:
    
    source: str = None
    con: Connection = None
    
    @classmethod # NOT STATIC
    def connect(cls,database: str) -> None:
        cls.config_sqlite3()
        cls.source = database
        cls.con = sqlite3.connect(
            database=database,
            detect_types=sqlite3.PARSE_DECLTYPES)
        cls.con.row_factory = sqlite3.Row # will now return Rows instead of tuples.
        # info
    
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
