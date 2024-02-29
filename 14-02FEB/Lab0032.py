# reverse a string using function and check palindrome

def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


original_str = input("Enter the String to check")
original_str=original_str.lower()
String = reverse_string(original_str)
if String == original_str:
    print("This is a palindrome")
else:
    print(String," is Not a palindrome")

