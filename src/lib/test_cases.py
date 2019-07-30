from unittest import TestCase
from src.lib.drop_token_game import DropTokenGame
from src.configs.expected_command_outcomes import ExpectedCommandOutcomes
from src.configs.expected_game_scenarios import ExpectedGameScenarios
from src.lib.game_board_constructor import GameBoardConstructor
from src.lib import cli_execution_validator

class DropTokenTestCase(TestCase):
    def setUp(self):
        self.drop_token_game = DropTokenGame()
        self.ExpectedCommandOutcomes = ExpectedCommandOutcomes
        self.ExpectedGameScenarios = ExpectedGameScenarios
        self.cli_execution_validator = cli_execution_validator
        self.GameBoardConstructor = GameBoardConstructor()
    
    def tearDown(self):
        self.drop_token_game.end()
    
    def shortDescription(self):
        return self._testMethodDoc

