def palindrome_method_1(string: str) -> bool:
    reversed_string = ''.join(list(reversed(string)))
    return reversed_string == string

print(palindrome_method_1('abaa'))

def palindrome_method_2(string: str) -> bool:
    string_length = len(string)
    for i in range(0, string_length//2):
        if string[i] != string[string_length - i - 1]:
            return False
    return True

print(palindrome_method_2("malayalam"))