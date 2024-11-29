# Problem

#  write a function to check if two strings are anagrams of each other. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, CBDA is an anagram of ABCD.

# Algorithmn
# step 1: Define a function  that handles this problem

# step 2 : input first string and second string

# step 3 : sort the characters in both strings

# step 4 : compare the sorted strings

# step 5 : return true if the strings are anagrams, false otherwise

# step 6 : end

#code

def anagrams():

    # defining  varibale

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # remove any white space and convert strings to lowerclass

    str1 = str.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

    




    


