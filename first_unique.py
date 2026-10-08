#Given a string s, return the first character that appears exactly once in the string.
#If there is no such character, return None.

#Example 1:

#Input:  "amazon"
#Output: "m"

def first_unique(s):
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in s:
        if counts[char] == 1:
            return char

    return None

print(first_unique("amazon"))  # Output: "m"
print(first_unique("aabbcc"))  # Output: None