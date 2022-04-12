'''
1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
'''

def urlIFY(input):
    replace = '%20'
    output = []
    for i in range(len(input)):
        if(input[i] == ' '):
            output.append(replace)
        else:
            output.append(input[i])
    return ''.join(output)

print(urlIFY('give me spaces'))