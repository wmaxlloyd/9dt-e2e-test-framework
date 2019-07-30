def convert_array_elements_to_str(stdout_as_byte_array: [bytes]) -> [str]:
    return list(map(lambda stdout_line: stdout_line.decode(), stdout_as_byte_array))