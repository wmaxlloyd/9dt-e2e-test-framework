from __future__ import annotations
from typing import List, TYPE_CHECKING
from src.configs.expected_command_outcomes import ExpectedCommandOutcomes
if TYPE_CHECKING:
	from src.lib.cli_execution_result import CLIExecutionResult

def generate_expected_output(game: List[int], output_key: object) -> List[CLIExecutionResult]:
	expected_output = [None] * len(game)
	for output_type in output_key:
		expectedPlayOutcome = getattr(ExpectedCommandOutcomes, output_type)
		for output_line_number in output_key[output_type]:
			game_column_played = game[output_line_number]
			expected_output[output_line_number] = expectedPlayOutcome(game_column_played)
	return expected_output

def generate_draw_game(game_board_height: int, game_board_width: int) -> List[int]:
	"""
	Generates draw game based on the following algorithm:
	If Even number of columns -> 
		1. Make two identical rows of alternating player tokens from right to left.
		2. Make two identical rows of alternating player tokens from left to right
		3. Repeat until all rows filled
	If Odd number columns ->
		1. Fill all but one column using even number of columns strategy
		2. Fill remaining column with alternating player tokens
	"""
	even_game_board_width = game_board_width - (game_board_width % 2)
	fill_row_left_right = lambda: list(range(1, even_game_board_width + 1))
	fill_row_right_left = lambda: fill_row_left_right()[::-1]
	game = []
	for current_row_index in range(game_board_height):
		new_row = fill_row_left_right() if current_row_index % 4 in [0,1] else fill_row_right_left()
		game += new_row
	if game_board_width % 2: # If odd number of columns
		game += [game_board_width] * game_board_height
	return game

def generate_draw_game_board(game_board_height: int, game_board_width: int) -> List[List[str]]:
	"""Generates game using `generate_draw_game` and then creates the board to mimic that algorithm"""
	game = generate_draw_game(game_board_height, game_board_width)
	return generate_game_board_from_game(game_board_height, game_board_width, game)

def generate_game_board_from_game(game_board_height: int, game_board_width: int, game: List[int]) -> List[List[str]]:
	"""Starts with an empty board (of "0"'s) and fills in appropriate player token as it iterates through game"""
	generate_empty_game_board_row = lambda: ["0"] * game_board_width
	game_board = [generate_empty_game_board_row() for i in range(game_board_height)]
	token_height_index_in_row = [game_board_height - 1] * game_board_width
	for (index, column) in enumerate(game):
		column_index = column - 1
		player = "1" if index % 2 == 0 else "2"
		game_board[token_height_index_in_row[column_index]][column_index] = player
		token_height_index_in_row[column_index] -= 1
	return game_board