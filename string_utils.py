def split_before_each_uppercase(formula):
    if not formula:
        return []
    
    indices = [i for i, char in enumerate(formula) if char.isupper()]
    
    indices.append(len(formula))
    
    result = []
    for j in range(len(indices) - 1):
        result.append(formula[indices[j]:indices[j+1]])
        
    return result


def split_at_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
            
    return formula, 1
