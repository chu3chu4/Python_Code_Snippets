
#challenge use filter to list all even numbers

numbers = [1, 2, 3, 4, 5]

filtered_list = list(filter (lambda number: number % 2 == 0, numbers))

print (filtered_list)