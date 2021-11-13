# 10/30/2021
# lists: looping

cars = ['bmw', 'tesla', 'lexus', 'ferrari']

"""
for tempVariable in iterativeObjects:
    code here using tempVariable
"""

for car in cars:
    print(f"I love {car} a lot!")
pizzas = ['peperoni', 'mushroom', 'cheese', 'grandma']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really like pizzaaaaaaa!")

animals = ['lion', 'tiger', 'leopard']
for animal in animals:
    print(f"{animal} would be the cutest animal without huge teeth")
print("but you can't change it")

print("############ Making numerical list##########")
# range(start, end, step)
# range(start)
#range(start, stop)
for num in range(6, 15, 3):
    print(num)
# print the numbers from 22-50 that is dividable by 3
for num in range(20, 51, 3):
    print(num)
nums_by_3 = list(range(21, 51, 3))
print(nums_by_3)

# print th squares of numbers between 10-20
squares = []
for num in range(10, 21):
    print(num*num)
    print(num**2)
    print(num*num*num)
    squares.append(num**2)
print(squares)

print("$$$$$$$$$ statistics $$$$$$$$$$")
print(f"min of squares: {min(squares)}")
print(f"max of squares: {max(squares)}")
print(f"sum of squares: {sum(squares)}")

print("####### List Comprehensions########")
squares = [num**2 for num in range(5, 10)]
print(squares)

cars = ['BmW', 'Lexus', 'FerraRi', 'Tesla']

for car in cars:
    if car.lower() == 'ferrari':
        print(f"Wooow you must really love your {car.upper()}!")
    else:
        print(f"{car.title()} is a good car, good for you.")


nums1 = range(1, 11)
nums2 = range(1, 11)
for row in nums1:
    for col in nums2:
        print(f"\t{col}*{row}={row*col}", end='\t')
    print()
    # ljust - left side
    # rjust - right side
    #




