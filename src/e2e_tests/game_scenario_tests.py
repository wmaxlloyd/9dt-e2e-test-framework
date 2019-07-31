import unittest
from src.lib.test_cases import DropTokenTestCase

class GameScenarios(DropTokenTestCase):
    def test_game_scenario_0001(self):
        """
        @test Vertical win - Plyer 1
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.VerticalWinPlayer1()
        )
        if comparison_errors:
            self.fail(comparison_errors)
    
    def test_game_scenario_0002(self):
        """
        @test Vertical win - Player 2
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.HorizontalWinPlayer2()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0003(self):
        """
        @test Horizontal win - Player 1
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.HorizontalWinPlayer1()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0004(self):
        """
        @test Horizontal win - Player 2
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.HorizontalWinPlayer2()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0005(self):
        """
        @test Diagonal down win - Player 1
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.DiagonalDownWinPlayer1()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0006(self):
        """
        @test Diagonal down win - Player 2
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.DiagonalDownWinPlayer2()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0007(self):
        """
        @test Diagonal up win - Player 1
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.DiagonalUpWinPlayer1()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0008(self):
        """
        @test Diagonal up win - Player 2
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.DiagonalUpWinPlayer2()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0009(self):
        """
        @test Draw (Filled up board)
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.Draw()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0010(self):
        """
        @test Column Filled
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.KeepPlayingOnFilledColumn()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0011(self):
        """
        @test Keep Playing after a draw
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.KeepPlayingAfterDraw()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0012(self):
        """
        @test Keep playing after win Player 1
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.KeepPlayingAfterWinPlayer1()
        )
        if comparison_errors:
            self.fail(comparison_errors)

    def test_game_scenario_0013(self):
        """
        @test Keep playing after win Player 2
        """
        comparison_errors = self.cli_execution_validator.test_game_scenario_and_get_errors(
            self.drop_token_game,
            self.ExpectedGameScenarios.KeepPlayingAfterWinPlayer2()
        )
        if comparison_errors:
            self.fail(comparison_errors)