from math import factorial

squares = [i**2 for i in range(11)]
print(squares)
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
numweek = [1,2,3,4,5,6,7]
weekdict = {k: v for (k, v) in zip(numweek, week)}
print(weekdict)
libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
libs_set = [i.lower() for i in libs]
libs_set = set(libs_set)
print(libs_set)
nums = [1, 3, 4, 87, 98, 15, 7, 4]
nums_even = [i for i in nums if i%2==0]
print(nums_even)
fct_nums = [1, 2, 3, 4, 5]
fct = {i: factorial(i) for i in fct_nums}
print(fct)
