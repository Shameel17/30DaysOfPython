a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a == b and b == c and a == c:
    print("its an equilateral triangle")
elif a == b or b == c or a == c:
    print("its an isosceles triangle")
else:
    print("its a scalene triangle")
