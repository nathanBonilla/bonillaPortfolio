'''
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
'''

def is_unique(string):
    new_list = []
    for i in string:
        i = i.lower()
        if(i in new_list):
            return False
        new_list.append(i)
    
    return True

def without_data_structures(string):
    string = sorted(string.lower())

    for i in range(1, len(string)):
        if(string[i - 1] == string[i]):
            return False
    
    return True

print(is_unique("true"))
print(is_unique("not True"))
print(without_data_structures("true"))
print(without_data_structures("not True"))