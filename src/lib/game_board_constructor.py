from typing import List
from src.utils.exceptions import InvalidBoardException

class GameBoardConstructor:
    def __init__(self) -> GameBoardConstructor:
        self.board_width = 40
        self.board_height = 40
        self.empty_board_row = "| " + " ".join(["0"] * self.board_width)
        self.board_bottom = [
            "+" + "-" * 2 * self.board_width,
            "  " + " ".join([str(item) for item in range(1, self.board_width + 1)])
        ]

    def construct(self, non_empty_rows_as_list: List[List[str]] = []) -> List[str]:
        empty_rows_to_insert = self.board_height - len(non_empty_rows_as_list)
        if empty_rows_to_insert < 0:
            raise InvalidBoardException(f"Received too many rows to insert. Can be no more than {self.board_height}. Received: {len(non_empty_rows_as_list)}")
        
        non_empty_rows = [self.__convert_row_list_to_string(row_as_list) for row_as_list in non_empty_rows_as_list]
        return [self.empty_board_row] * empty_rows_to_insert + non_empty_rows + self.board_bottom

    def __convert_row_list_to_string(self, row_list: List[List[str]]):
        if self.board_width < len(row_list):
            raise InvalidBoardException(f"Received row that is too large to insert for board width {self.board_width}. Received {row_list}")
        
        remaining_0s_in_row = ["0"] * (self.board_width - len(row_list))
        row_string = "| " + " ".join(row_list + remaining_0s_in_row)
        return row_string