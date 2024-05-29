def grading(grade):
    if 2 <= grade < 3:
        return 'Fail'
    elif grade < 3.5:
        return 'Poor'
    elif grade < 4.5:
        return 'Good'
    elif grade < 5.5:
        return 'Very Good'
    elif grade < 6.00:
        return 'Excellent'


grade = float(input())

print(grading(grade))