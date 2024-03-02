from configparser                import ConfigParser
from logging                     import info, exception, error
from utils.TypeLibrary           import SectionProxy, Self
from os                          import system
from presentation.ConnectCommand import ConnectCommand
from logic.Receiver              import Receiver
from cutie                       import select

class View:

    # constants declaration
    DB_OPTIONS = {}
    SETTINGS : SectionProxy = None
    BANNER : str = None
    MENU : str = None
    
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
    def start(cls:Self) -> None:
        cls.initialize()
        print("Select database:\n")
        list_of_options = list(cls.DB_OPTIONS.keys())
        idx = select(list_of_options,deselected_prefix="   ",selected_prefix=" \033[92m>\033[0m ")
        selected_option = list_of_options[idx]
        selected_database = cls.DB_OPTIONS[selected_option]
        print("Connect to " + selected_database)
        command = ConnectCommand(connect_to=selected_database)
        report = Receiver.execute(command)
        print(report)
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
        cls.banner()
        cls.menu()
    
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