def reverse_string_method_1(string: str) -> str:
    return string[::-1]

print(reverse_string_method_1("Hello"))

def reverse_string_method_2(string: str) -> str:
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

print(reverse_string_method_2("hello"))

def reverse_string_method_3(string: str) -> str:
    return ''.join(list(reversed(string)))

print(reverse_string_method_3("hello"))