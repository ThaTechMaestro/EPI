def test_valid_parenthesis(s):


    open_symbol = []
    symbol_lookup_table = {'{':'}', '(':')', '[':']'}

    for symbol in s:

        if symbol in symbol_lookup_table:
            open_symbol.append(symbol)
        elif symbol != symbol_lookup_table[open_symbol.pop()]
            return False
        elif not open_symbol:
            return False
    
    

