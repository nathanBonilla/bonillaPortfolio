# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique(str):
    str = sorted(str)
    for i in range(len(str) - 1):
        str[i] = str[i].lower()
        if(str[i] == str[i+1]):
            return False
    return True

print(is_unique('true'))
print(is_unique('not true'))
