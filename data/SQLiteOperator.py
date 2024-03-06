
from sqlite3 import connect as connect_to
from shared.Report import Report
from myutils.TypeLibrary import Connection, Cursor
from logging import info, exception, debug
from shared.SelectionReport import SelectionReport
from shared.ConnectionReport import ConnectionReport

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
    def test_connection(cls) -> ConnectionReport:
        r = ConnectionReport()
        c = cls.cursor
        r.sqlite_version = c.execute("SELECT sqlite_version()").fetchone()[0]
        r.list_of_tables = c.execute(r"""
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
            structure_query = f"SELECT name,type FROM pragma_table_info('{table}');"
            data_query = f""
            
            if len(columns) == 1:
                data_query += f"SELECT {columns[0]} from {table}"
            else:
                data_query += f"SELECT {', '.join(columns)} FROM {table}"

            # Add WHERE clause if filters are provided
            if filters:
                data_query += f" WHERE {' AND '.join(filters)}"

            # Add ORDER BY clause if ordering_terms are provided
            if ordering_terms:
                data_query += f" ORDER BY {ordering_terms}"

            # Execute queries
            report = SelectionReport(
                table=table,
                table_info=(cls.cursor.execute(structure_query)).fetchall(),
                query_results=(cls.cursor.execute(data_query)).fetchall()
            )

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
