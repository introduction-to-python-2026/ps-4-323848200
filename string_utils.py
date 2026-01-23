def split_at_digit(formula):
    # מחפשים את האינדקס של הספרה הראשונה
    for i in range(len(formula)):
        if formula[i].isdigit():
            # כל מה שלפני הספרה הוא ה-Prefix
            # מהספרה ועד הסוף הוא ה-Number
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number
            
    # אם לא נמצאה אף ספרה (כמו ב-NaCl)
    return formula, 1


def split_before_each_uppercase(formula):
    if not formula:
        return []
    
    parts = []
    start = 0
    
    # עוברים על המחרוזת מהתו השני והלאה
    for i in range(1, len(formula)):
        # אם מצאנו אות גדולה, חותכים את מה שהיה לפניה
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i
            
    # הוספת החלק האחרון שנשאר (חובה)
    parts.append(formula[start:])
    
    # בדיקה למקרה שהחלק הראשון ריק (קורה אם המחרוזת מתחילה באות גדולה,
    # אבל הלוגיקה שלנו עם start=0 וטווח מ-1 מונעת זאת)
    return [p for p in parts if p]
