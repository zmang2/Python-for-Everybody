# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'

colonpos = str.find(":")
print(colonpos)

new_string = str[colonpos+1:]
print(new_string)
print(type(new_string))

new_string_float = float(new_string)
print(new_string_float)
print(type(new_string_float))