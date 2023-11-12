E_1 = int(input())
E_2 = int(input())
E_3 = int(input())
E_4 = int(input())
E_5 = int(input())
if E_1 > 0 and E_2 > 0 and E_3 > 0 and E_4 > 0 and E_5 > 0:
    if E_1 % 2 == 0 and E_2 % 2 == 0 and E_3 % 2 == 0 and E_4 % 2 == 0 and E_5 % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
