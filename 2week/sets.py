# 1 exercise

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# 2 exercise

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# 3 exercise

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

# 4 exercise

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# 5 exercise

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)