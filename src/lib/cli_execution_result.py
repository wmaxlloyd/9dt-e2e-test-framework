from typing import List


class CLIExecutionResult:
    def __init__(self, command: str = "", output: List[str] = [], is_alive: bool = True) -> CLIExecutionResult:
        self.command = command
        self.output = output
        self.is_alive = is_alive
