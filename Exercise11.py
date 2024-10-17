def anagrams(str1, str2):
    if sorted(list(str1)) == sorted(list(str2)):
        print("They are anagrams")
        return True
    else:
        return False

str1 = str(input("Enter a string: "))
str2 = str(input("Enter another string: "))

anagrams(str1, str2)
