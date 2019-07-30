from src.lib.test_cases import DropTokenTestCase

class SmokeTests(DropTokenTestCase):
    def test_smoke_0001(self):
        """
        @test Program starts without Error
        """
        execution_result = self.drop_token_game.start()
        comparison_error = self.cli_execution_validator.get_execution_result_comparison_error(
            execution_result,
            self.ExpectedCommandOutcomes.ProgramStart())
        if comparison_error:
            self.fail(comparison_error)

    def test_smoke_0002(self):
        """
        @test Program returns appropriate output with input - PUT X (in bounds)
        """
        self.drop_token_game.start()
        valid_column = 1
        execution_result = self.drop_token_game.put_token(valid_column)
        comparison_error = self.cli_execution_validator.get_execution_result_comparison_error(
            execution_result,
            self.ExpectedCommandOutcomes.PutValid(valid_column))
        if comparison_error:
            self.fail(comparison_error)        
    
    def test_smoke_0003(self):
        """
        @test Program returns appropriate output with input - PUT X (out of bounds)
        """
        self.drop_token_game.start()
        invalid_column = self.GameBoardConstructor.board_width + 1
        execution_result = self.drop_token_game.put_token(invalid_column)
        comparison_error = self.cli_execution_validator.get_execution_result_comparison_error(
            execution_result,
            self.ExpectedCommandOutcomes.PutInvalidColumn(invalid_column))
        if comparison_error:
            self.fail(comparison_error)

    def test_smoke_0004(self):
        """
        @test Program returns appropriate output with input - BOARD
        """
        self.drop_token_game.start()
        execution_result = self.drop_token_game.get_board()
        comparison_error = self.cli_execution_validator.get_execution_result_comparison_error(
            execution_result,
            self.ExpectedCommandOutcomes.BoardEmpty())
        if comparison_error:
            self.fail(comparison_error)

    def test_smoke_0005(self):
        """
        @test Program returns appropriate output with input - GET
        """
        self.drop_token_game.start()
        execution_result = self.drop_token_game.get_history()
        comparison_error = self.cli_execution_validator.get_execution_result_comparison_error(
            execution_result,
            self.ExpectedCommandOutcomes.GetEmpty())
        if comparison_error:
            self.fail(comparison_error)

    def test_smoke_0006(self):
        """
        @test Program returns error output with any unexpected input - Invalid
        """
        self.drop_token_game.start()
        invalid_command = "Invalid"
        execution_result = self.drop_token_game.run_command(invalid_command)
        comparison_error = self.cli_execution_validator.get_execution_result_comparison_error(
            execution_result,
            self.ExpectedCommandOutcomes.InvaidCommand(invalid_command))
        if comparison_error:
            self.fail(comparison_error)
