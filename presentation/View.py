from configparser                import ConfigParser
from logging                     import info, exception, error
from typing                      import Self, TypeVar
from os                          import system
from prettytable                 import PrettyTable # Does rich have one already?
from presentation.ConnectCommand import ConnectCommand
from logic.Receiver              import Receiver

class View:
    
    # type declaration
    SectionProxy = TypeVar("SectionProxy")
    Command = TypeVar("Command")
    Report = TypeVar("Report")

    # constants declaration
    SETTINGS : SectionProxy = None
    BANNER : str = None
    MENU : str = None
    
    @classmethod
    def start(cls:Self) -> None:
        cls.initialize()
        db = cls.select_database()
        command = ConnectCommand(connect_to=db)
        report =  Receiver.execute(command)
        print(report)

    @classmethod
    def initialize(cls) -> None:
        cls.load_settings()
        cls.load_banner()
        cls.load_menu()
    
    @classmethod
    def select_database(cls) -> str:
        #todo cutie menu here
        print(
    """
    <cutie menu>
        > OmniRecords
        dummy
    """
        )
        return "omni"
    
    @classmethod
    def load_settings(cls) -> None:
        info("Loading settings")
        config = ConfigParser(interpolation=None)
        config.read('config.ini')
        cls.SETTINGS = config['ViewSettings']

    @classmethod
    def load_banner(cls):
        info("Loading banner")
        banner = open(cls.SETTINGS['banner']).read()
        color = cls.SETTINGS['banner_color']
        cls.BANNER = f"\033[{color}m{banner}\033[0m"
    
    @classmethod
    def load_menu(cls):
        info("Loading menu")
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
    
    # @classmethod
    # def process(cls, raw_input):
    #     """
    #     Take raw input, refine it, and extract action and id where id could be null.
    #     """
    #     action_set = {  # TODO REPLACED BY COMMAND
    #         "action": None,
    #         "arg": None
    #     }
    #     try:
    #         refined_input = raw_input.strip().lower().split()
    #         action_set["action"] = refined_input[0]
    #         action_set["arg"] = refined_input[1]
    #     except IndexError:
    #         if action_set["action"] is None:
    #             error("\033[31mERROR: CANNOT BE EMPTY, SEEK HELP\033[0m")
    #         else:
    #             pass
    #     except:
    #         exception("ERROR: SEEK HELP")  # Send exception info to both file AND console
    #     finally:
    #         return action_set
    
    # @classmethod
    # def execute_action(cls, action_set):
    #     """
    #     Execute the action based on user input.
    #     """
    #     exit = False
    #     try:
    #         action = action_set.get("action")
    #         match action:
    #             case "exit":
    #                 exit = True
    #             case "help":
    #                 print(cls.MENU_TEXT)
    #             case "update":
    #                 cls.prompt_update() 
    #             case _:
    #                 info(f"Executing action {action.upper()}...\n")
    #                 display_info = FishService.execute_action(action_set)  # The only connection to FishService
    #                 cls.execute(display_info)  # Either PrettyTable or string, both printable
    #     except ValueError:
    #         pass
    #     except Exception as e:
    #         exception("ERROR IN FishConsoleView.execute_action")
    #     finally:
    #         return exit
    
    # @classmethod
    # def execute(cls, display_info: DisplayInfo):
    #     """
    #     Execute based on the display information.
    #     """
    #     if display_info.is_table:
    #         pt = display_info.pretty_table
    #         row_count = display_info.row_count
    #         i = 0
    #         while True:
    #             print(pt.get_string(start=i, end=i + 10))
    #             sign()
    #             if i > row_count - 10:
    #                 break
    #             else:
    #                 i += 10

    # @classmethod
    # def prompt_update(cls):
    #     """
    #     Prompt the user for input to update data.
    #     """
    #     try:
    #         index = input("Enter the ID to update: ")
    #         column = input("Enter the column to update: ")
    #         new_value = input("Enter the new value: ")

    #         action_set = {"action": "update", "arg": index, "column": column, "new_value": new_value}
    #         display_info = FishService.execute_action(action_set)
    #         cls.execute(display_info)
    #     except Exception as e:
    #         exception("ERROR IN prompt_update")

    # @classmethod
    # def __str__(cls):
    #     """
    #     String representation of the class.
    #     """
    #     return f"{cls}"