from configparser             import ConfigParser
from logging                  import info, exception, error
from shared.Command           import Command
from shared.ConnectionCommand import ConnectionCommand
from shared.SelectionCommand  import SelectionCommand
from shared.Report            import Report
from shared.ConnectionReport  import ConnectionReport
from shared.Operation         import Operation
from myutils.TypeLibrary      import SectionProxy
from logic.Receiver           import Receiver
from cutie                    import select
from os                       import system
from shared.SelectionReport import SelectionReport
from prettytable import PrettyTable
from prettytable import SINGLE_BORDER
from prettytable import MARKDOWN
from prettytable.colortable import ColorTable

class View:

    DB_OPTIONS = {}
    SETTINGS : SectionProxy = None
    BANNER : str = None
    MENU : str = None
    
    tables : list[str] = None
    mode : str = 'SQL'
    
    @classmethod
    def initialize(cls) -> None:
        info("Intializing View (loading settings)")
        config = ConfigParser(interpolation=None)
        config.read('config.ini')
        for k,v in config['Databases'].items():
            cls.DB_OPTIONS[k] = v
        cls.SETTINGS = config['ViewSettings']
        cls.load_banner()
        cls.load_menu()
    
    @classmethod
    def start(cls) -> None:
        cls.initialize()
        print("Select database:\n")
        list_of_options = list(cls.DB_OPTIONS.keys())
        idx = select(list_of_options,deselected_prefix="   ",selected_prefix=" \033[92m>\033[0m ")
        selected_option = list_of_options[idx]
        selected_database = cls.DB_OPTIONS[selected_option]
        command = ConnectionCommand(selected_database)
        report = Receiver.execute(command)
        cls.consume(report)
        cls.main_loop()       
    
    @classmethod
    def load_settings(cls) -> None:
        config = ConfigParser(interpolation=None)
        config.read('config.ini')
        cls.SETTINGS = config['ViewSettings']

    @classmethod
    def load_banner(cls):
        info("loading banner")
        banner = open(cls.SETTINGS['banner']).read()
        color = cls.SETTINGS['banner_color']
        cls.BANNER = f"\033[{color}m{banner}\033[0m"
    
    @classmethod
    def load_menu(cls):
        info("loading menu")
        menu = open(cls.SETTINGS['menu']).read()
        color = cls.SETTINGS['menu_color']
        cls.MENU = f"\033[{color}m{menu}\033[0m"
         
    @classmethod
    def banner(cls) -> None:
        """Prints the banner"""
        print(cls.BANNER)
        
    @classmethod
    def menu(cls):
        """Prints the menu"""
        print(cls.MENU)
        
    @classmethod
    def main_loop(cls):
        over = False
        cls.banner()
        cls.menu()
        while not over:
            user_input = input("> ")
            command = cls.process(user_input)
            report = Receiver.execute(command)
            system('cls')
            cls.banner()
            cls.consume(report)
    
    @classmethod
    def process(cls, raw_input) -> Command:
        """
        Take raw input, refine it, creates command
        """
        try:
            refined_input = raw_input.strip().lower().split()
            if cls.mode == 'SQL' and refined_input[0] in cls.tables:
                command = SelectionCommand(
                    target=refined_input[0],
                    columns=['*']
                    )
        except Exception as e:
            exception(f"ERROR: SEEK HELP ||| {e}")
        finally:
            return command
        
    @classmethod
    def consume(cls, report : Report) -> Report:
        match report.TYPE_OF_REPORT:
            case Operation.CONNECTION:
                return cls.consume_connection_report(report)
            case Operation.SELECTION:
                return cls.consume_selection_report(report)
            case Operation.INSERTION:
                return cls.consume_insertion_report(report)
            case Operation.ALTERATION:
                return cls.consume_alteration_report(report)
            case Operation.DELETION:
                return cls.consume_deletion_report(report)
            case Operation.GENERIC:
                exception("\033[31mUNKNOWN REPORT TYPE\033[0m")
                raise ValueError
    
    @classmethod
    def consume_connection_report(cls,report:ConnectionReport) -> None:
        cls.tables = report.list_of_tables
        msg = f"Success! Connected to SQLite version {report.sqlite_version}"
        info(msg)
        
    @classmethod
    def consume_selection_report(cls,report:SelectionReport) -> None:
        table = report.table # string
        columns = report.headers # list of strings
        rows = report.query_results # list of list of strings and int
 
        table = PrettyTable()
        table.field_names = columns
        table.add_rows(rows)
        table.set_style(15)

        print(table)

    @classmethod
    def __str__(cls):
        """
        String representation of the class.
        """
        return f"{cls}"