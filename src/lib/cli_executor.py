from __future__ import annotations
import pexpect
from pexpect.exceptions import TIMEOUT as PExpectTimeout, EOF as PExpectEOF
from src.utils.cli_executor_utilities import convert_array_elements_to_str
from src.lib.cli_execution_result import CLIExecutionResult

STDOUT_LINE_DELIMETER = "\r\n"
DEFAULT_TIMEOUT_FOR_OUTPUT_SECONDS = .1

class CLIExecutor:

    def __init__(self, seed_command: str) -> None:
       self.process_terminated = None
       self.process = None
       self.seed_command = seed_command
    
    def start(self) -> CLIExecutionResult:
        self.process = pexpect.spawn(self.seed_command)
        self.process.timeout = DEFAULT_TIMEOUT_FOR_OUTPUT_SECONDS
        return self.get_command_result(self.seed_command)
    
    def get_new_output(self) -> [bytes]:
        read_full_output = False
        output = []

        while not read_full_output:
            try:
                self.process.expect(STDOUT_LINE_DELIMETER)
                output.append(self.process.before)
            except PExpectTimeout:
                read_full_output = True
            except PExpectEOF:
                read_full_output = True

        return output
    
    def get_command_result(self, command: str) -> CLIExecutionResult:
        new_output_raw = self.get_new_output()
        new_output_string_array = convert_array_elements_to_str(new_output_raw)
        self.is_alive = self.process.isalive()
        return CLIExecutionResult(command=command, output=new_output_string_array, is_alive=self.is_alive)

    def wait_for_command_execution(self, command: str) -> CLIExecutor:
        self.process.expect(f"{command}{STDOUT_LINE_DELIMETER}")
        return self

    def execute(self, command: str) -> CLIExecutionResult:
        if not self.is_alive:
            raise Exception(f"Unable to execute command: {command} - Process has been terminated")

        self.process.sendline(command)
        self.wait_for_command_execution(command)
        return self.get_command_result(command)
    
    def end(self) -> CLIExecutor:
        if self.process:
            self.process.kill(0)
        return self
    
    def restart(self) -> CLIExecutor:
        if self.process:
            self.end()
        return self.start()

