def compare_chars_case(first_char, second_char):
    """
    Helper function for compare second char to first one
    :param first_char - main char
    :param second_char - char to compare
    :return compared char
    """
    return second_char.lower() if first_char.islower() else second_char
