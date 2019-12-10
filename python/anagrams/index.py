# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
# anagrams('rail safety', 'fairy tales') --> True
# anagrams('RAIL! SAFETY!', 'fairy tales') --> True
# anagrams('Hi there', 'Bye there') --> False
import re
def anagrams(stringA, stringB):
    return cleanString(stringA) == cleanString(stringB)


def cleanString(str):
    str = str.lower()
    return "".join(sorted(re.findall('\w', str)))

print(anagrams('rail safety', 'fairy tales'))
print(anagrams('RAIL! SAFETY!', 'fairy tales'))
print(anagrams('Hi there', 'Bye there'))
