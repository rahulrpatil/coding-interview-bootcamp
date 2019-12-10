# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
# capitalize('a short sentence') --> 'A Short Sentence'
# capitalize('a lazy fox') --> 'A Lazy Fox'
# capitalize('look, it is working!') --> 'Look, It Is Working!'

def capitalize(str):
    word_list = []
    for word in str.split(' '):
        word_list.append(word[0].upper() + word[1::])
    return ' '.join(word_list)

print(capitalize('a short sentence'))
print(capitalize('a lazy fox'))
print(capitalize('look, it is working!'))
