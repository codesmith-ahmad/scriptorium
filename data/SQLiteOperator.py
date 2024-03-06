
from sqlite3 import connect as connect_to
from logic.Report import Report
from myutils.TypeLibrary import Connection, Cursor
from logging import info, exception, debug

class SQLiteOperator():

    data_source: str = None
    connection: Connection = None
    cursor: Cursor = None

    @classmethod
    def initialize(cls, data_source: str) -> None:
        """Establish a connection to the SQLite database."""
        cls.connection = connect_to(data_source)
        cls.cursor = cls.connection.cursor()
        info("Connected to " + data_source)
    
    @classmethod    
    def test_connection(cls) -> Report:
        r = Report(Report.Type.CONNECTION)
        c = cls.cursor
        r.sqlite_version = c.execute("SELECT sqlite_version()").fetchone()[0]
        r.table_list = c.execute(r"""
                               SELECT name FROM sqlite_master
                               WHERE
                               type = 'table' AND
                               name NOT LIKE '\_%' ESCAPE '\' AND
                               name NOT LIKE 'sqlite%';
                               """).fetchall()
        return r
        
    @classmethod
    def select(cls, table:str, columns:list[str], filters:list[str] = None, ordering_terms:str = None) -> Report:
        """Filters are valid SQL conditions without the WHERE"""
        try:
            report = Report(Report.Type.SELECTION)
            
            if len(columns) == 1:
                query = f"SELECT {columns[0]} from {table}"
            else:
                query = f"SELECT {', '.join(columns)} FROM {table}"

            # Add WHERE clause if filters are provided
            if filters:
                query += f" WHERE {' AND '.join(filters)}"

            # Add ORDER BY clause if ordering_terms are provided
            if ordering_terms:
                query += f" ORDER BY {ordering_terms}"

            # Execute the query
            cls.cursor.execute(query)

            # Fetch the results
            results = cls.cursor.fetchall()

            report.results = results

        except Exception as e:
            # Handle exceptions
            print(f"Error executing selection: {e}")
        finally:
            return report
    
    @classmethod
    def update(cls, index: int, column: str, new_val) -> None:
        """
        Execute UPDATE operation.

        Parameters:
        - index (int): The index of the data to be updated.
        - column (str): The column to be updated.
        - new_val (Union[str, int]): The new value to set in the specified column.
        """
        try:
            info("Executing UPDATE...")
            cls.dataframe.loc[index, column] = new_val
            cls.dataframe.to_csv(cls.data_source, index=False)
            cls.load_dataframe()
        except Exception as e:
            pass

    @classmethod
    def delete(cls, index: int) -> None:
        """
        Execute DELETE operation.

        Parameters:
        - index (int): The index of the data to be deleted.
        """
        try:
            info("Executing DELETE...")
            cls.dataframe = cls.dataframe.drop(index)
            cls.dataframe.to_csv(cls.data_source, index=False)
            cls.load_dataframe()
        except Exception as e:
            pass
