class ExecutionResultsDoNotMatchException(Exception):
    """Two cli execution results do not match"""
    pass

class InvalidBoardException(Exception):
    """Creating a board that does not fit expected dimensions"""
    pass
