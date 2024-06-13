def is_palindrome(str1):

    if str1 == str1[::-1]:
        print("yes")
    else:
        print("no")


str1 = input()
is_palindrome(str1)
