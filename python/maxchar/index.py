def maxChar(string: str) -> str:
    charMap = {}
    maxChar = ''
    max = 0
    for char in string:
        if char in charMap.keys():
            charMap[char] = charMap[char] + 1
        else:
         charMap[char] = 1
    for char in charMap:
        if charMap[char] > max:
            max =  charMap[char]
            maxChar = char
    return max, maxChar

print(maxChar('assadddd'))
