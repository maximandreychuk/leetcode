def average(salary):
    max_salary = min_salary = salary[0]
    summary = 0
    for i in salary:
        if i > max_salary:
            max_salary = i
        if i < min_salary:
            min_salary = i
        summary += i
    summary = summary - max_salary - min_salary
    length = len(salary)-2
    return round(summary / length, 5)

print(average(salary = [4000,3000,1000,2000]))
print(average(salary = [1000,2000,3000]))
