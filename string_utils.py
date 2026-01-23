def split_before_each_uppercase(formula):
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
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            number_part = formula[i:]
            return prefix, int(number_part)
            
    return formula, 1
