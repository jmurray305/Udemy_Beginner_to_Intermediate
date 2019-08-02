'''1. Write a program in python which finds a letter in a string?
Example: String = "Example String", letter = "S" returns True.

2. Write a program in python to reverse a string using slicing method?

Example: String = "helloworld", Returns reversed string = "dlrowolleh" '''

def search(inputstring, letter):
    if (inputstring.find(letter) != -1): 
        return True
    else: 
        return False 

        
def rev(x): 
    x = x[::-1] 
    return x 