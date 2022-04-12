'''
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
'''

def check_permutation(str1, str2):
    if(len(str1) != len(str2)):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if(str1[i] != str2[i]):
            return False
    
    return True

print(check_permutation('123123', '332211'))
print(check_permutation('1231123', '3322211'))