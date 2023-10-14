def is_equal_string(utf8_string, utf16_string):
    utf8_decoded = utf8_string.decode('utf-8')
    utf16_decoded = utf16_string.decode('utf-16')
    
    return utf8_decoded.casefold() == utf16_decoded.casefold()

