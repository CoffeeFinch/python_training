# create a count variable
# loop over input
# if letter.isupper = aeiou
# increase count by 1
# return count

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

print (to_jaden_case("how can mirrors be real?"))



def descending_order(num):
    nums = str(num)
    sort = sorted(nums, reverse=True)
    return int("".join(sort))

print (descending_order(1257894521))