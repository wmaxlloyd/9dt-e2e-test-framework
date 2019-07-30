class MissingRequiredAttributeException(Exception):
    """Raised when required attribute is missing from class"""
    pass

class AttributeWrongTypeException(Exception):
    """Raised when required attribute is incorrect type"""
    pass

class ExecutionResultsDoNotMatchException(Exception):
    """Raised when two cli execution results do not match"""
    pass

class InvalidBoardException(Exception):
    """Raised when creating a board that does not fit expected dimensions"""
    pass

# TODO: Remove fluff