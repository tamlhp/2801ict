def is_palindrome(s, length):
    """
    This function recursively determines whether the given string is a palindrome.
    
    :param s: string to check
    :param length: length of the string
    :return: True if the string is a palindrome, False otherwise
    """
    if length <= 1:
        # Base case: a string of length 0 or 1 is always a palindrome
        return True
    
    if s[0] != s[length-1]:
        # Base case: if the first and last characters don't match, the string is not a palindrome
        return False
    
    # Recursive case: check if the substring between the first and last characters is a palindrome
    return is_palindrome(s[1:length-1], length-2)

# Check if "racecar" is a palindrome
s = "racecar"
length = len(s)
print(is_palindrome(s, length))  # True

# Check if "hello" is a palindrome
s = "hello"
length = len(s)
print(is_palindrome(s, length))  # False

# Check if "A man, a plan, a canal, Panama!" is a palindrome
s = "A man, a plan, a canal, Panama!"
length = len(s)
print(is_palindrome(s, length))  # True