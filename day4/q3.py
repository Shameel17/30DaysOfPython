a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
root1 = 0
root2 = 0
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1 = (-b + (discriminant ** 0.5)) / (2 * a)
    root2 = (-b - (discriminant ** 0.5)) / (2 * a)
    print(root1, root2)
elif discriminant == 0:
    root1 = -b / (2 * a)
    root2 = root1
    print(root1, root2)
else:
    root1 = (-b + (discriminant ** 0.5)) / (2 * a)
    root2 = (-b - (discriminant ** 0.5)) / (2 * a)
    print(root1, root2)
