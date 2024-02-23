# Code by Ahmad Al-Jabbouri

import configparser
from logging import info, exception, error, debug
import os
from typing import *
import pandas as pd
from model.Otolith import Otolith

class DataStore():
    """
    A class representing a data store.

    Attributes:
    - CURRENT_PATH (str): The current working directory.
    - DATA_SOURCE (str): The path to the CSV file as the data source.
    - DATA_FIELDS (List[str]): Aliases for fields.
    - MAX_ROWS (int): The maximum number of rows to display.
    - dataframe (pd.DataFrame): The DataFrame containing the data.
    """

    CURRENT_PATH: str = os.getcwd()
    DATA_SOURCE: str = None
    DATA_FIELDS: List[str] = None  # aliases for fields
    MAX_ROWS: int = 100
    dataframe: pd.DataFrame = None

    @classmethod
    def load_dataframe(cls) -> None:
        """
        Load DataFrame from the CSV file.
        """
        info("Loading dataframe...")
        if cls.DATA_SOURCE is None:
            cls.connect_database()
        pd.options.display.max_rows = cls.MAX_ROWS  # Will not display more than 100 records
        cls.dataframe = pd.read_csv(cls.DATA_SOURCE)
        cls.DATA_FIELDS = list(cls.dataframe.columns)

    @classmethod
    def connect_database(cls) -> None:
        """
        Connect to the data source.
        """
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            cls.DATA_SOURCE = config.get('database', 'csv_path')
        except FileNotFoundError:
            error("\033[31mconfig.ini NOT FOUND! Place one next to launcher.py\033[0m")
        except:
            exception("\033[31mERROR: Something went wrong attempting to read [database] from config.ini\033[0m")
        else:
            info(f"\033[92mCONNECTED TO DATABASE\033[0m: {cls.CURRENT_PATH}\\{cls.DATA_SOURCE}")

    @classmethod
    def select_all(cls) -> Dict[int, Otolith]:
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
    def select(cls, index: int) -> Otolith:
        """
        Execute SELECT operation.

        Parameters:
        - index (int): The index of the data to select.

        Returns:
        - Otolith: An instance of the Otolith class.
        """
        try:
            debug("Executing SELECT...")
            series = cls.dataframe.loc[index]
            return Otolith(
                source=series.loc[cls.DATA_FIELDS[0]],
                latin_name=series.loc[cls.DATA_FIELDS[1]],
                english_name=series.loc[cls.DATA_FIELDS[2]],
                french_name=series.loc[cls.DATA_FIELDS[3]],
                year=series.loc[cls.DATA_FIELDS[4]],
                month=series.loc[cls.DATA_FIELDS[5]],
                number=series.loc[cls.DATA_FIELDS[6]]
            )
        except Exception as e:
            pass

    @classmethod
    def insert(cls, data: List[List]) -> None:
        """
        Execute INSERT operation.

        Parameters:
        - data (List[List]): The data to be inserted.
        """
        try:
            info("Executing INSERT...")
            new_df = pd.DataFrame(data, columns=list(cls.dataframe.columns))
            cls.dataframe = pd.concat([cls.dataframe, new_df])
            cls.dataframe.to_csv(cls.DATA_SOURCE, index=False)
            cls.load_dataframe()
        except Exception as e:
            pass

    @classmethod
    def update(cls, index: int, column: str, new_val: Union[str, int]) -> None:
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
            cls.dataframe.to_csv(cls.DATA_SOURCE, index=False)
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
            cls.dataframe.to_csv(cls.DATA_SOURCE, index=False)
            cls.load_dataframe()
        except Exception as e:
            pass
