def validate_phone_number(ph_num):
    if ph_num[0] not in ['6', '7', '8', '9']:
        return "invalid"
    if len(ph_num) != 10:
        return "invalid"
    for digit in set(ph_num):
        if ph_num.count(digit) > 7:
            return "invalid"
    consecutive_count = 1
    for i in range(1, len(ph_num)):
        if ph_num[i] == ph_num[i - 1]:
            consecutive_count += 1
            if consecutive_count > 5:
                return "invalid"
        else:
            consecutive_count = 1
    return "valid"


phone_number = input("Enter a 10-digit phone number: ")
result = validate_phone_number(phone_number)
print(result)
