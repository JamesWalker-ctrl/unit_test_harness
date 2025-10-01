# utils/string_utils.py
def capitalize(text):
    """
    Capitalizes the first character of the string and lowers the rest.
    Example: 'hello WORLD' → 'Hello world'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[:1].upper() + text[1:].lower()
