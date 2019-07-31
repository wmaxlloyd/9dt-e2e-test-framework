from src.lib.game_scenario_base import GameScenarioBase
from src.configs.expected_command_outcomes import ExpectedCommandOutcomes
from src.lib.game_board_constructor import GameBoardConstructor
from src.utils import game_scenario_utilities

class ExpectedGameScenarios:
    class HorizontalWinPlayer1(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,1,2,2,3,3,4]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(6),
                    "PutWin": [6]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["2","2","2"],
                    ["1","1","1","1"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","1","2","2","3","3","4"]
                )
            )
    
    class HorizontalWinPlayer2(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,1,2,2,3,3,1,4,1,4]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(9),
                    "PutWin": [9]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["1"],
                    ["1"],
                    ["2","2","2","2"],
                    ["1","1","1","2"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","1","2","2","3","3","1","4","1","4"]
                )
            )
    
    class VerticalWinPlayer1(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,2,1,2,1,2,1]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(6),
                    "PutWin": [6]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["1"],
                    ["1","2"],
                    ["1","2"],
                    ["1","2"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","2","1","2","1","2","1"]
                )
            )
    
    class VerticalWinPlayer2(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,2,1,2,1,2,3,2]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(7),
                    "PutWin": [7]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["0","2"],
                    ["1","2"],
                    ["1","2"],
                    ["1","2","1"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","2","1","2","1","2","3","2"]
                )
            )
    
    class DiagonalDownWinPlayer1(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [4,3,3,2,1,2,2,1,1,4,1]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(10),
                    "PutWin": [10]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["1"],
                    ["1","1"],
                    ["2","2","1","2"],
                    ["1","2","2","1"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["4","3","3","2","1","2","2","1","1","4","1"]
                )
            )

    class DiagonalDownWinPlayer2(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,4,3,3,2,1,2,2,1,1]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(9),
                    "PutWin": [9]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["2"],
                    ["1","2"],
                    ["2","1","2"],
                    ["1","1","1","2"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","4","3","3","2","1","2","2","1","1"]
                )
            )
    
    class DiagonalUpWinPlayer1(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,2,2,3,4,3,3,4,4,1,4]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(10),
                    "PutWin": [10]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["0","0","0","1"],
                    ["0","0","1","1"],
                    ["2","1","2","2"],
                    ["1","2","2","1"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","2","2","3","4","3","3","4","4","1","4"]
                )
            )

    class DiagonalUpWinPlayer2(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [4,1,2,2,3,4,3,3,4,4]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(9),
                    "PutWin": [9]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["0","0","0","2"],
                    ["0","0","2","1"],
                    ["0","2","1","2"],
                    ["2","1","1","1"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["4","1","2","2","3","4","3","3","4","4"]
                )
            )
    
    class Draw(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game_board_constructor = GameBoardConstructor()
            game_board_height = game_board_constructor.board_height
            game_board_width = game_board_constructor.board_width
            game = game_scenario_utilities.generate_draw_game(game_board_height, game_board_width)
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(len(game) - 1),
                    "PutDraw": [len(game) - 1]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed(game_scenario_utilities.generate_draw_game_board(game_board_height, game_board_width)),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(str(column_int) for column_int in game)
            )

    class KeepPlayingOnFilledColumn(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game_board_height = GameBoardConstructor().board_height
            game = [1] * game_board_height + [1]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(game_board_height),
                    "PutColumFilled": [game_board_height]
                }),
                # Creates game board with one row and alternating ["1"], ["2"] ex [["1"],["2"],["1"]] for game_board_height = 3
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([["1"] if (game_board_height - current_row_int) % 2 == 0 else ["2"] for current_row_int in range(1, game_board_height + 1)]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(["1"] * game_board_height)
            )
    
    class KeepPlayingAfterWinPlayer1(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,1,2,2,3,3,4,1,1]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(6),
                    "PutWin": [6],
                    "PutAlreadyWon": range(7,9)
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["2","2","2"],
                    ["1","1","1","1"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","1","2","2","3","3","4"]
                )
            )
    
    class KeepPlayingAfterWinPlayer2(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game = [1,1,2,2,3,3,1,4,1,4,1,1]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(9),
                    "PutWin": [9],
                    "PutAlreadyWon": range(10,12)
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed([
                    ["1"],
                    ["1"],
                    ["2","2","2","2"],
                    ["1","1","1","2"]
                ]),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(
                    ["1","1","2","2","3","3","1","4","1","4"]
                )
            )
    
    class KeepPlayingAfterDraw(GameScenarioBase):
        def __init__(self) -> GameScenarioBase:
            game_board_constructor = GameBoardConstructor()
            game_board_height = game_board_constructor.board_height
            game_board_width = game_board_constructor.board_width
            game = game_scenario_utilities.generate_draw_game(game_board_height, game_board_width) + [1]
            super().__init__(
                game_to_play = game,
                expected_game_results = game_scenario_utilities.generate_expected_output(game, {
                    "PutValid": range(len(game) - 2),
                    "PutDraw": [len(game) - 2],
                    "PutAlreadyDraw": [len(game) - 1]
                }),
                expected_board_result = ExpectedCommandOutcomes.BoardUsed(game_scenario_utilities.generate_draw_game_board(game_board_height, game_board_width)),
                expected_history_result = ExpectedCommandOutcomes.GetUsed(str(column_int) for column_int in game[:-1])
            )
    

