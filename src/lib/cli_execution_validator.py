from __future__ import annotations
from typing import List, TYPE_CHECKING
from src.utils.exceptions import ExecutionResultsDoNotMatchException
if TYPE_CHECKING:
    from src.lib.cli_execution_result import CLIExecutionResult
    from src.lib.game_scenario_base import GameScenarioBase

def compare_execution_results(test_result: CLIExecutionResult, expected_result: CLIExecutionResult) -> None:
    commands_match = True
    if test_result.command != expected_result.command:
        commands_match = False
    
    if test_result.is_alive != expected_result.is_alive:
        commands_match = False
    
    if test_result.output != expected_result.output:
        commands_match = False
    
    if not commands_match:
        raise ExecutionResultsDoNotMatchException(f"""
Command Execution Results do not match!
Actual:
    Command - {test_result.command}
    Process Alive - {test_result.is_alive}
    Output - {test_result.output}
Expected:
    Command - {expected_result.command}
    Process Alive - {expected_result.is_alive}
    Output - {expected_result.output}""")

def get_game_execution_comparisons(game: List[int], test_outputs: List[CLIExecutionResult], expected_outputs: List[CLIExecutionResult]) -> List[str]:
    execution_errors = []
    for (index, test_output) in enumerate(test_outputs):
        column_execution_comparison_error = get_execution_result_comparison_error(
            test_output,
            expected_outputs[index],
            error_prefix = f"\nAt game index {index}:\n"
        )
        if column_execution_comparison_error:
            execution_errors.append(column_execution_comparison_error)
    return execution_errors


def get_execution_result_comparison_error(test_result: CLIExecutionResult, expected_result: CLIExecutionResult, error_prefix: str = "") -> str:
    try:
        compare_execution_results(
            test_result,
            expected_result
        )
    except ExecutionResultsDoNotMatchException as e:
        return f"{error_prefix}{str(e)}"
    return ""

def test_game_scenario_and_get_errors(drop_token_game: List[int], scenario: GameScenarioBase) -> str:
    """Plays game and compares execution result of: PUT commands, BOARD command and GET (history)"""
    drop_token_game.restart()
    game_output = drop_token_game.play_game(scenario.game_to_play)
    board_output = drop_token_game.get_board()
    history_output = drop_token_game.get_history()
    game_execution_comparisons = get_game_execution_comparisons(
        scenario.game_to_play,
        game_output,
        scenario.expected_game_results
    )
    board_execution_comparison = get_execution_result_comparison_error(
        board_output,
        scenario.expected_board_result
    )
    history_execution_comparison = get_execution_result_comparison_error(
        history_output,
        scenario.expected_history_result
    )
    all_comparisons = game_execution_comparisons + [board_execution_comparison, history_execution_comparison]
    comparison_errors = [comparison_error for comparison_error in all_comparisons if comparison_error]
    return "\n".join(comparison_errors)
