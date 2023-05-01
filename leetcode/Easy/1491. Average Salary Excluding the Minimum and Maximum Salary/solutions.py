def average(salary: list[int]) -> float:
    return 1.0*(sum(salary)-min(salary)-max(salary))/(len(salary)-2)

# salary = [4000,3000,1000,2000]
# salary = [1000,2000,3000]
salary = [8000,9000,2000,3000,6000,1000]
print(average(salary=salary))