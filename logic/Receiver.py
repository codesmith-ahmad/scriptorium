from logging                import info, exception
from data.SQLiteOperator    import SQLiteOperator
from presentation.Command   import Command
from logic.Report           import Report

class Receiver:

    @classmethod
    def execute(cls, command : Command) -> Report:
        match command.command_type:
            case Command.Type.CONNECTION:
                return cls.execute_connection(command)
            case Command.Type.SELECTION:
                return cls.execute_selection(command)
            case Command.Type.INSERTION:
                return cls.execute_insertion(command)
            case Command.Type.ALTERATION:
                return cls.execute_alteration(command)
            case Command.Type.DELETION:
                return cls.execute_deletion(command)
            case "unknown":
                exception("\033[31mUNKNOWN COMMAND TYPE\033[0m")
                raise ValueError
    
    @classmethod
    def execute_connection(cls, command : Command) -> Report:
        """Send connection instructions to database"""
        SQLiteOperator.initialize(command.connect_to)
        report = SQLiteOperator.test_connection()
        tables = []
        for tpl in report.table_list:
            tables += [tpl[0]]
        report.table_list = tables
        return report
    
    @classmethod
    def execute_selection(cls, command : Command) -> Report:
        table = command.target
        columns = command.columns
        try:
            if table == "assignments" or "expenses":
                command.target = table + "view"
            if command.columns == "all":
                command.columns = ['*'] # TODO FIND OUT WHAT THE HEADERS ARE CALLED
            report = SQLiteOperator.select(
                command.target,
                command.columns
            )
            report = cls.analyze(report)
            return report
        except Exception as e:
            # Handle exceptions
            print(f"Error executing selection: {e}")
    
    @classmethod
    def execute_insertion(cls) -> Report:
        raise NotImplementedError
    
    @classmethod
    def execute_alteration(cls) -> Report:
        raise NotImplementedError
    
    @classmethod
    def execute_deletion(cls) -> Report:
        raise NotImplementedError
    
    @classmethod
    def analyze(cls,report:Report) -> Report:
        match report.report_type:
            case Report.Type.CONNECTION:
                return cls.analyze_connection(report)
            case Report.Type.SELECTION:
                return cls.analyze_selection(report)
            case Report.Type.INSERTION:
                return cls.read_insertion(report)
            case Report.Type.ALTERATION:
                return cls.read_alteration(report)
            case Report.Type.DELETION:
                return cls.read_deletion(report)
            case "unknown":
                exception("\033[31mUNKNOWN REPORT TYPE\033[0m")
                raise ValueError
            
    @classmethod
    def analyze_selection(cls,report:Report):
        if report.table == "assignments":
            # TODO ADD TEST DATES AND APPLY COLOR TO ROWS TO SHOW PRIORITY