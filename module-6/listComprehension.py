# doubles = [expression for value in iterable if condition]

doubles = [x*2 for x in range(1, 11)]
triples = [x*3 for x in range(1, 11)]
squares = [z*z for z in range(1, 11)]

fruits = ["apple", "orange", "banana", "mango"]
fruits = [ fruit[0].upper() for fruit in fruits]

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num <=0]
even_nums = [num for num in numbers if num %2==0]
odd_nums = [num for num in numbers if num %2 == 1]


grades = [80, 46, 67 ,98, 87, 76, 54, 65]
passing_grades = [ grade for grade in grades if grade >= 60]

print(passing_grades)