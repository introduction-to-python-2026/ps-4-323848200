def split_before_each_uppercase(formula):
    """Splits a string before every uppercase letter."""
    if not formula:
        return []
    
    result = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            result.append(formula[start:i])
            start = i
            
    result.append(formula[start:])
    return result


def split_at_digit(formula):
    """Splits a string into a prefix and the first digit onward as an integer."""
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
            
    return formula, 1
