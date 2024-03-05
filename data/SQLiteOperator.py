
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
        r = Report()
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
    def select_all(cls):
        """
        Execute SELECT_ALL operation.

        Returns:
        - Dict[int, Otolith]: A dictionary containing selected data.
        """
        try:
            info("Executing SELECT_ALL...")
            if cls.dataframe is None:
                cls.load_dataframe()
            dataset = {}
            for i in range(len(cls.dataframe.index)):
                dataset[i] = cls.select(i)
            return dataset
        except Exception as e:
            exception(e)

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
