import json
from src.utils.exceptions import MissingRequiredAttributeException, AttributeWrongTypeException

def expected_command_outcome(cls):
    expected_attributes = {
        "expected_process_terminated": bool,
        "expected_output": list
    }
    __check_class_for_expected_attributes(cls, expected_attributes)
    return cls

def expected_game_scenario(cls):
    expected_attributes = {
        
    }

def __check_class_for_expected_attributes(cls, expected_attributes):
    for expected_attribute in expected_attributes:
        if not hasattr(cls, expected_attribute):
            raise MissingRequiredAttributeException(f"Class '{cls}' missing required attribute '{expected_attribute}'")
        attribute_type = type(getattr(cls, expected_attribute))
        if not attribute_type == expected_attributes[expected_attribute]:
            raise AttributeWrongTypeException(f"Attribute '{expected_attribute}' wrong type in class '{cls}': Expected - {expected_attributes[expected_attribute]}| Found - {attribute_type} ")