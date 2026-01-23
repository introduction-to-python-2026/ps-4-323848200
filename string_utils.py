def split_at_first_digit(formula):
    # מחפשים את האינדקס של הספרה הראשונה
    for i, char in enumerate(formula):
        if char.isdigit():
            # הקידומת לפני הספרה, והמספר מהספרה והלאה
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
            
    # אם לא נמצאו ספרות
    return formula, 1


def split_before_each_uppercases(formula):
    if not formula:
        return []
    
    parts = []
    start = 0
    # רצים מהתו השני כדי לזהות אותיות גדולות
    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i
            
    # הוספת החלק האחרון
    parts.append(formula[start:])
    return parts
