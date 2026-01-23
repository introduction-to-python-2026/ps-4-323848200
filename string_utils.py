def split_before_each_uppercase(formula):
    if not formula:
        return []
    
    split_formula = []
    start = 0
    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end
            
    split_formula.append(formula[start:])
    return split_formula


def split_at_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            return prefix, int(formula[i:])
            
    return formula, 1
