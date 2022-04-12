'''
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
'''

# to be a palindrome, it may only have one odd number of letters
# the rest to be even

def palindrome_permutation(input):
    new_dict = {}

    for i in input:
        if(i in new_dict):
            new_dict[i] += 1
        else:
            new_dict.update({i : 1})

    count = 0
    for i in new_dict:
        if(new_dict[i] % 2 != 0):
            count += 1
        if(count > 1):
            return False
    
    return True

print(palindrome_permutation('racecar'))
print(palindrome_permutation('not racecar'))