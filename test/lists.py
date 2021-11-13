#3.8 Seeing the world: think of at least five places in the world you'd like to visit.

places = ['Paris', 'Venice', 'florance', 'Madrid', 'Amsterdam']
print(places)

print(sorted(places))

print(places)

places.sort(reverse=True)
print(places)

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)

len(places)
print(f"I have been in {len(places)} different places.")

#4-1. Pizzas:
pizzas = ['peperoni', 'regular', 'mashroom']
for pizza in pizzas:
    print(f"My favourite kind of Pizza is {pizza} pizza!")
print("I just LOVE PIZZA!!!")

animals = ['lion', 'tiger', 'leopard']
for animal in animals:
    print(f"{animal} is very dangerous animal,")
print("but so beautiful to look at them.")

#4-3. Counting to 20.
for nums in range(1, 21):
    print(nums)

nums = list(range(1, 1000001))
print(f"min of million: {min(nums)}")
print(f"max of million: {max(nums)}")
print(f"sum of million: {sum(nums)}")

nums = list(range(1, 20, 2))
print(nums)














