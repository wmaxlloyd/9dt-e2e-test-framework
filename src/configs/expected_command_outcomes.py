from typing import List

from src.lib.cli_execution_result import CLIExecutionResult
from src.lib.game_board_constructor import GameBoardConstructor

class ExpectedCommandOutcomes:
    class ProgramStart(CLIExecutionResult):
        def __init__(self) -> CLIExecutionResult:
            super().__init__(
                command="python2 9dt-app/9dt.py",
                output = [],
                is_alive = True)
    
    class PutValid(CLIExecutionResult):
        def __init__(self, column_number: int) -> CLIExecutionResult:
            super().__init__(
                command = f"PUT {column_number}",
                output = ["OK"],
                is_alive = True)
        
    class PutWin(CLIExecutionResult):
        def __init__(self, column_number: int) -> CLIExecutionResult:
            super().__init__(
                command = f"PUT {column_number}",
                output = ["WIN"],
                is_alive = True)
    
    class PutDraw(CLIExecutionResult):
        def __init__(self, column_number: int) -> CLIExecutionResult:
            super().__init__(
                command = f"PUT {column_number}",
                output = ["DRAW"],
                is_alive = True)

    class PutInvalidColumn(CLIExecutionResult):
        def __init__(self, column_number: int) -> CLIExecutionResult:
            super().__init__(
                command=f"PUT {column_number}",
                output = ["ERROR"],
                is_alive = True
            )
    
    class PutColumFilled(CLIExecutionResult):
        def __init__(self, column_number: int) -> CLIExecutionResult:
            super().__init__(
                command=f"PUT {column_number}",
                output = ["ERROR"],
                is_alive = True
            )

    class PutAlreadyWon(CLIExecutionResult):
        def __init__(self, column_number: int) -> CLIExecutionResult:
            super().__init__(
                command=f"PUT {column_number}",
                output = ["ERROR"],
                is_alive = True
            ) 

    class PutAlreadyDraw(CLIExecutionResult):
        def __init__(self, column_number: int) -> CLIExecutionResult:
            super().__init__(
                command=f"PUT {column_number}",
                output = ["ERROR"],
                is_alive = True
            )   

    class BoardEmpty(CLIExecutionResult):
        def __init__(self) -> CLIExecutionResult:
            super().__init__(
                command="BOARD",
                output = GameBoardConstructor().construct(),
                is_alive = True
            )
    
    class BoardUsed(CLIExecutionResult):
        def __init__(self, expected_non_empty_rows: List[List[str]] = [[]]) -> CLIExecutionResult:
            super().__init__(
                command="BOARD",
                output = GameBoardConstructor().construct(expected_non_empty_rows),
                is_alive = True
            ) 

    class GetEmpty(CLIExecutionResult):
        def __init__(self) -> CLIExecutionResult:
            super().__init__(
                command="GET",
                output = [],
                is_alive = True
            )
    
    class GetUsed(CLIExecutionResult):
        def __init__(self, expected_history) -> CLIExecutionResult:
            super().__init__(
                command="GET",
                output = expected_history,
                is_alive = True
            )
    
    class InvaidCommand(CLIExecutionResult):
        def __init__(self, invalid_command: str) -> CLIExecutionResult:
            super().__init__(
                command=invalid_command,
                output = ["ERROR"],
                is_alive = True
            )   
    