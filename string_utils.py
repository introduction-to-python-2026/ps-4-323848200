def split_at_digit(formula):
    # מחפשים את האינדקס של הספרה הראשונה
    for i, char in enumerate(formula):
        if char.isdigit():
            # prefix: הכל לפני הספרה
            prefix = formula[:i]
            # number: מהספרה והלאה כ-integer
            number = int(formula[i:])
            return prefix, number
            
    # אם לא נמצאו ספרות, מחזירים את המחרוזת המקורית ו-1
    return formula, 1


def split_before_each_uppercase(formula):
    if not formula:
        return []
    
    parts = []
    start = 0
    # רצים מהתו השני כדי לזהות אותיות גדולות שמתחילות איבר חדש
    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i
            
    # הוספת החלק האחרון שנשאר
    parts.append(formula[start:])
    return parts
