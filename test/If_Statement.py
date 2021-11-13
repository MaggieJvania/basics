#
cars = ['Bently', 'Ferrari', 'Mybach']
msg = [f"My {cars[1]} is the best!"]
print(msg)

nums = list(range(1, 101))
print(f"min : {min(nums)}")
print(f"max : {max(nums)}")
print(f"sum : {sum(nums)}")

animal = 'Tiger'
print("is animal == 'Tiger'? I predict True.")
print(animal == 'Tiger')

print("is animal == 'Lion'? I predict False.")
print(animal == 'Lion')

# checking for Inequality:
icecreams = ['cherry']
if icecreams != 'cherry':
    print("sorry, this option is not in stuck.")

# cheching for Equality:
icecream = 'cherry'
icecream == 'cherry'
icecream

# test for lower()
icecream = 'Cherry'
icecream.lower() == 'cherry'
icecream

# numerical test - equality and inequality:
age = 21
age == 21
True

age = 21
if age != 33:
    print("sorry, I can't help")

# numerical test - grater than, less than, grater than or equal to, less than or equal to.
age = 21
age > 10
True
age < 10
False
age >=22
False
age <= 33
True

# test using "AND" and "OR" keywords.
age_1 = 18
age_2 = 21
age_1 >= 19 and age_2 <= 23
False # False because age_1 is not more or equal to 19.

age_1 <= 21 and age_2 <=23
True # True because both are True.

age_1 <=18 or age_2 >=30
True # True because one of them is True.

# test wheather an item is or is not in the list
list = ['apple', 'cherry', 'watermelon']
'melon' in list
False # 'Melon' is not in the list

'apple' in list
True # 'apple' is in the list



# 5.3.
alien_color = 'green'
if alien_color == 'green':
    print("you earned 5 points!")

alien_color = 'yellow'
if alien_color == 'red':
    print("game over")

# 5.4.
alien_color = 'green'
if alien_color == 'green':
    print("You win the game!")
else:
    print("game over!")

alien_color = 'green'
if alien_color != 'green':
    print("you are looser.")
else:
    print("congratulations!")

# 5.5.
alien_color = 'green'
if alien_color == 'green':
    print('you earned 5 points.')
elif alien_color == 'yellow':
    print("you earnd 10 points!")
else:
    print("you earned 15 points.")


alien_color = 'yellow'
if alien_color == 'green':
    print('you earned 5 points.')
elif alien_color == 'yellow':
    print("you earnd 10 points!")
else:
    print("you earned 15 points.")


alien_color = 'red'
if alien_color == 'green':
    print('you earned 5 points.')
elif alien_color == 'yellow':
    print("you earnd 10 points!")
else:
    print("you earned 15 points.")


# 5.6.
age = 66
if age < 2:
    print("Person is a baby.")
elif age >=2 and age < 4:
    print("Person is a toddler.")
elif age >= 4 and age < 13:
    print("Person is a kid.")
elif age >= 13 and age < 20:
    print("Person is a teenager.")
elif age >= 20 and age < 65:
    print("person is an adult.")
else:
    print("Person is an elder.")

# 5.7.
fav_fruits = ['apple', 'orange', 'cherry']









