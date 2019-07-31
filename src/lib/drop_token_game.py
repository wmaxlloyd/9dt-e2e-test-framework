from typing import List, TYPE_CHECKING
from src.lib.cli_executor import CLIExecutor
if TYPE_CHECKING:
    from src.lib.cli_execution_result import CLIExecutionResult

class DropTokenGame:
    def __init__(self) -> CLIExecutionResult:
        self.executor = CLIExecutor("python2 9dt-app/9dt.py")
    
    def start(self) -> CLIExecutionResult:
        return self.executor.start()
    
    def restart(self) -> CLIExecutionResult:
        return self.executor.restart()

    def run_command(self, command: str) -> CLIExecutionResult:
        return self.executor.execute(command)

    def put_token(self, row_number: int) -> CLIExecutionResult:
        return self.run_command(f"PUT {str(row_number)}")
    
    def get_board(self) -> CLIExecutionResult:
        return self.run_command("BOARD")
    
    def play_game(self, columns_to_put: [str]) -> List[CLIExecutionResult]:
        command_results = []
        for column_to_put in columns_to_put:
            command_results.append(self.put_token(column_to_put))
        return command_results
    
    def get_history(self) -> CLIExecutionResult:
        return self.run_command("GET")
    
    def end(self) -> None:
        self.executor.end()
    