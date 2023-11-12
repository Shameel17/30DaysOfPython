sham = int(input())
sri = int(input())
mans = int(input())
kri = int(input())
if sri > 0 and mans > 0 and kri > 0:
    if sri + mans + kri == sham:
        if sri == mans or mans == kri or sri == kri:
            print("not fair")
        else:
            print("fair")
    else:
        print("not fair")
else:
    print("not fair")
