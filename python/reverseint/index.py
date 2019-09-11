def reverse_int_method_1(number: int) -> int:
    num = abs(number)
    string_num = str(num)
    reversed_string = string_num[::-1]
    if number > 0:
        return int(reversed_string)
    else:
        return int(reversed_string) * -1

print(reverse_int_method_1(-134))

def reverse_int_method_2(number: int) -> int:
    num = abs(number)
    rev = 0
    while num > 0:
        dig = num%10
        rev = rev * 10 + dig
        num = num//10
    if number > 0:
        return rev
    else:
        return rev * -1


print(reverse_int_method_2(-10))