from logging                    import info, exception
from data.SQLiteOperator        import SQLiteOperator
from shared.Command             import Command
from shared.ConnectionCommand   import ConnectionCommand
from shared.SelectionCommand    import SelectionCommand
from shared.Report              import Report
from shared.ConnectionReport    import ConnectionReport
from shared.SelectionReport     import SelectionReport
from shared.Operation           import Operation

class Receiver:

    @classmethod
    def execute(cls, command : Command) -> Report:
        match command.TYPE_OF_COMMAND:
            case Operation.CONNECTION:
                return cls.execute_connection(command)
            case Operation.SELECTION:
                return cls.execute_selection(command)
            case Operation.INSERTION:
                return cls.execute_insertion(command)
            case Operation.ALTERATION:
                return cls.execute_alteration(command)
            case Operation.DELETION:
                return cls.execute_deletion(command)
            case "unknown":
                exception("\033[31mUNKNOWN COMMAND TYPE\033[0m")
                raise ValueError
    
    @classmethod
    def execute_connection(cls, command : ConnectionCommand) -> ConnectionReport:
        """Send connection instructions to database"""
        SQLiteOperator.initialize(command.connect_to)
        report = SQLiteOperator.test_connection()
        tables = []
        for tpl in report.list_of_tables:
            tables += [tpl[0]]
        report.list_of_tables = tables
        return report
    
    @classmethod
    def execute_selection(cls, command : SelectionCommand) -> Report:
        table = command.target
        try:
            if table == "assignments" or "expenses":
                command.target = table + "view"
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
        match report.TYPE_OF_REPORT:
            case Operation.CONNECTION:
                return cls.analyze_connection(report)
            case Operation.SELECTION:
                return cls.analyze_selection(report)
            case Operation.INSERTION:
                return cls.read_insertion(report)
            case Operation.ALTERATION:
                return cls.read_alteration(report)
            case Operation.DELETION:
                return cls.read_deletion(report)
            case "unknown":
                exception("\033[31mUNKNOWN REPORT TYPE\033[0m")
                raise ValueError
            
    @classmethod
    def analyze_selection(cls,report:SelectionReport) -> Report:
        # unpack report
        table = report.table
        table_info = report.table_info
        query_results = [list(x) for x in report.query_results]
        try:
            if table == "assignmentsview":
                for row in query_results:
                    lifetime = row[4]
                    if lifetime <= 3:
                        row[4] = f"\033[31m{lifetime}\033[0m"
                    for i in range(len(row)):
                        if row[i] is not None:
                            row[i] = str(row[i]) # must convert to string prior to display, View must not handle numbers
                report.table = "ASSIGNMENTS"
                report.headers = [tpl[0] for tpl in table_info]
                report.query_results = query_results
            else:
                report.table = report.table.upper()
                report.headers = [tpl[0] for tpl in table_info] 
        except Exception as e:
            exception(e)
        finally:
            return report