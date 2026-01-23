def split_at_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
            
    return formula, 1


def split_before_each_uppercase(formula):
    if not formula:
        return []
    
    indices = []
    for i in range(len(formula)):
        if formula[i].isupper():
            indices.append(i)
            
    indices.append(len(formula))
    
    parts = []
    for j in range(len(indices) - 1):
        start = indices[j]
        end = indices[j+1]
        parts.append(formula[start:end])
        
    return parts
            
    return formula, 1
