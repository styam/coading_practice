#========================method 1=================
def is_palindrome(name):
    s = ""
    for i in name:
        s = i + s

    if s == name:
        print("True")

    else:
        print("False")


is_palindrome("nitin")



#========================method 2=================
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

# ============================method 3===============
def isPalindrome(s):

    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False

s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
