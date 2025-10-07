# create a count variable
# loop over input
# if letter.isupper = aeiou
# increase count by 1
# return count
import string
from operator import truediv
from xml.etree.ElementTree import tostring

print("Get Count")


def get_count(sentence):
    vowel_count = 0
    for letter in sentence:
        if letter in "aeiouAEIOU":
            vowel_count += 1
    return vowel_count


print(get_count("b for bacon and eggies"))

# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

# take number and modulo it by 2
# add result to a list
# continue to do so until it is no longer a whole number
# return list
print(" ")
print("Count Bits")


def count_bits(n):
    binary_holder = []
    bit_counter = 0
    while n > 0:
        binary_holder.append(n % 2)
        n = n // 2
    for numbers in binary_holder:
        if numbers == 1:
            bit_counter += 1
    return bit_counter


#
print(count_bits(460))

# first letter capped
# every letter after a space capped
# saved to empty string
# string returned
print(" ")
print("To Jaden Case")


def to_jaden_case(string):
    newstring = ""
    space_checker = False
    for letters in range(len(string)):
        if letters >= 0:
            if newstring == "":
                newstring += (string[letters]).upper()
            elif string[letters] == " ":
                space_checker = True
                newstring += (string[letters])
            elif space_checker == True:
                newstring += (string[letters]).upper()
                space_checker = False
            else:
                newstring += (string[letters]).lower()

    return newstring


print(to_jaden_case("how can mirrors be real?"))

print(" ")
print("Descending Order")


def descending_order(num):
    nums = str(num)
    sort = sorted(nums, reverse=True)
    return int("".join(sort))


print(descending_order(1257894521))

# break number into digits
# multiply those digits by each other
# repeat until there is only 1 digit

# def persistence(n):
#     result = 0
#     for digits in n:
#         if digits == 1:
#             result += 1
#
#     return result

# print (persistence(999))

print(" ")
print("Square Digits")


def square_digits(num):
    result = ""
    result2 = ""
    nums = str(num)
    for digit in nums:
        result += digit

    for dig in result:
        result2 += str(int(dig) * int(dig))

    return int(result2)


print(square_digits(9119))

# create empty result list
# create string pair holder
# Create boolean tracker
# for each character in the string
# add it to the pair holder and flip the bool
# next one, add to the holder, add the holder to the list, clear the holder and flip the bool back
# if the bool is true, then its the first number
# if it's false, its the second
# if the bool is false, end the group and start a new one
print(" ")
print("Count Letter(s)")


def count_letter(s):
    result = []
    holder = ""
    tracker = True
    for letter in s:
        if tracker:
            holder += letter
            tracker = False
        elif not tracker:
            holder = holder + letter
            result += holder
            holder = ""
            tracker = True

    return result


print(count_letter("abcd"))

print(" ")
print("Disemvowel")


def disemvowel(string):
    disemvoweled = ""
    for letter in string:
        if letter not in "aeiouAEIOU":
            disemvoweled += letter
    return disemvoweled


print(disemvowel("b for bacon and eggies"))

print(" ")
print("Valid Braces")


# def valid_braces(string):
#     valid = False
#     left_paren = 0
#     right_paren = 0
#     left_sq = 0
#     right_sq = 0
#     left_curl = 0
#     right_curl = 0
#
#     for letter in string:
#         if letter not in "()[]{}":
#             return "Invalid. Bad job."
#         elif letter == "(":
#             left_paren = string.index(letter)
#         elif letter == ")":
#             right_paren = string.index(letter)
#         elif letter == "[":
#             left_sq = string.index(letter)
#         elif letter == "]":
#             right_sq = string.index(letter)
#         elif letter == "{":
#             left_curl = string.index(letter)
#         elif letter == "}":
#             right_curl = string.index(letter)
#
#     if left_paren <= right_paren and left_sq <= right_sq and left_curl <= right_curl:
#         valid = True
#     else:
#         valid = False
#
#     return valid


# def valid_braces(string):
#     valid = True
#     invalid = "Invalid. Bab job."
#     left_paren = 0
#     right_paren = 0
#     left_sq = 0
#     right_sq = 0
#     left_curl = 0
#     right_curl = 0
#
#     if ((string.find("[") == -1 and string.find("]") == -1) or (string.find("{") == -1 and string.find("}") == -1) or
#             (string.find("(") == -1 and string.find(")") == -1)):
#         valid = False
#
#     for letter in string:
#
#         if letter not in "()[]{}":
#             return invalid
#         elif letter == "(":
#             left_paren = string.index(letter)
#         elif letter == ")":
#             right_paren = string.index(letter)
#         elif letter == "[":
#             left_sq = string.index(letter)
#         elif letter == "]":
#             right_sq = string.index(letter)
#         elif letter == "{":
#             left_curl = string.index(letter)
#         elif letter == "}":
#             right_curl = string.index(letter)
#
#     if left_paren <= right_paren and left_sq <= right_sq and left_curl <= right_curl:
#         valid = True
#     else:
#         valid = False
#
#     return valid

def valid_braces(string):
    holder = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in "([{":
            holder.append(char)
        elif char in ")]}":
            if not holder or holder[-1] != brackets[char]:
                return False
            holder.pop()
        else:
            return "Invalid. Bad job."

    return not holder


print(valid_braces("HamTime4Ham"))
print("Should Be Invalid")
print(valid_braces("(){}[]"))
print("Should Be True")
print(valid_braces(")][[]](}"))
print("Should Be False")
print(valid_braces("{{}}[[]][{()]}"))
print("Should Be False")
print(valid_braces("(}"))
print("Should Be False")
print(valid_braces("[(])"))
print("Should Be False")

# Does the string contain the matching characters?
# () and or [] and or {}
# If not, fail
# If yes, is the order of them correct?
# L index lower than R index
# if not, fail
# if yes, what is between them?
# if it's nto another complete pair, fail
# If it is a complete pair, The string is valid



print(" ")
print("In Array")
def in_array(array1, array2):
    result = []
    for word1 in array1:
        for word2 in array2:
            if word1 in word2:
                result.append(word1)
    # for each string in a1
    # loop over the strings in a2 to see if it is present
    # if it is, add it to results array
    # return results array
    return sorted(set(result))


a1 = ["harp", "live", "strong"]

a2 = ["harp", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))