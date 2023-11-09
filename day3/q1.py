Fruits1 = set()
Fruits2 = set()
num_of_fruits = int(input("how many no. of fruits = "))
for i in range(num_of_fruits):
    Fruit = (input("Fruit = "))
    Fruits1.add(Fruit)
print(Fruits1)

fruit_to_add = int(input("how many no. of fruits = "))
for i in range(fruit_to_add):
    Fruit = (input("Fruit = "))
    Fruits2.add(Fruit)
Fruits_new = Fruits1 | Fruits2
print(Fruits_new)
