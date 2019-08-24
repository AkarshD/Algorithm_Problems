def sentencePalindrome(s):
    l, h = 0, len(s) - 1

    # Lowercase string
    s = s.lower()

    # Compares character until they are equal
    while (l <= h):

        # If there is another symbol in left
        # of sentence
        if (not (s[l] >= 'a' and s[l] <= 'z')):
            l += 1

        # If there is another symbol in right
        # of sentence
        elif (not (s[h] >= 'a' and s[h] <= 'z')):
            h -= 1

        # If characters are equal
        elif (s[l] == s[h]):
            l += 1
            h -= 1

        # If characters are not equal then
        # sentence is not palindrome
        else:
            return False
    # Returns true if sentence is palindrome
    return True


# Driver program to test sentencePalindrome()
s = "Was it a cat I saw?"
if (sentencePalindrome(s)):
    print 
else:
    print "Sentence is not palindrome."