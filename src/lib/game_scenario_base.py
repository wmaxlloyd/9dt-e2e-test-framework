from typing import List
from src.lib.cli_execution_result import CLIExecutionResult
from src.configs.expected_command_outcomes import ExpectedCommandOutcomes

class GameScenarioBase:
    
    def __init__(
        self,
        game_to_play: List[str] = [],
        expected_game_results: List[CLIExecutionResult] = [],
        expected_board_result: CLIExecutionResult = ExpectedCommandOutcomes.BoardEmpty(),
        expected_history_result: CLIExecutionResult = ExpectedCommandOutcomes.GetEmpty()
    ):
        self.game_to_play = game_to_play
        self.expected_game_results = expected_game_results
        self.expected_board_result = expected_board_result
        self.expected_history_result = expected_history_result
