T = int(input())
if 0 <= T <= 23:
    if 0 <= T <= 5:
        print("NIGHT")
    elif 6 <= T <= 11:
        print("MORNING")
    elif 12 <= T <= 17:
        print("AFTERNOON")
    elif 18 <= T <= 23:
        print("EVENING")
    else:
        print("INVALID")
else:
    print("INVALID")
