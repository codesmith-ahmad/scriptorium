from configparser           import ConfigParser
from logging                import info, exception, error
from logic.Report import Report
from myutils.TypeLibrary    import SectionProxy, ReportType
from os                     import system
from presentation.Command   import Command
from logic.Receiver         import Receiver
from cutie                  import select

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
        command = Command(Command.Type.CONNECTION)
        command.connect_to = selected_database
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
        while not over:
            cls.banner()
            cls.menu()
            user_input = input("> ")
            command = cls.process(user_input)
            report = Receiver.execute(command)
            cls.consume(report)
    
    @classmethod
    def process(cls, raw_input) -> Command:
        """
        Take raw input, refine it, creates command
        """
        command = Command()
        try:
            refined_input = raw_input.strip().lower().split()
            if refined_input[0] in cls.tables:
                command.command_type = Command.Type.SELECTION
                command.target = refined_input[0]
                command.columns = "all"
                command.filters = None
                command.ordering_terms = None #todo BAD, RETURN TO MAKING PREDEFINED REPORTS CAUSE I KEEP FORGETTING WHAT'S IN THEM
        except Exception as e:
            exception(f"ERROR: SEEK HELP ||| {e}")
        finally:
            return command
        
    @classmethod
    def consume(cls, report : ReportType):
        match report.report_type:
            case Report.Type.CONNECTION:
                return cls.read_connection_report(report)
            case Report.Type.SELECTION:
                return cls.read_selection_report(report)
            case Report.Type.INSERTION:
                return cls.read_insertion_report(report)
            case Report.Type.ALTERATION:
                return cls.read_alteration_report(report)
            case Report.Type.DELETION:
                return cls.read_deletion_report(report)
            case "unknown":
                exception("\033[31mUNKNOWN REPORT TYPE\033[0m")
                raise ValueError
    
    @classmethod
    def read_connection_report(cls,report) -> None:
        cls.tables = report.table_list
        msg = f"Success! Connected to SQLite version {report.sqlite_version}"
        info(msg)

    @classmethod
    def __str__(cls):
        """
        String representation of the class.
        """
        return f"{cls}"