# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# pseudocode

# create a list of random number
list_numbers = (105, 123, 135, 285, 356, 515, 1004, 1075, 3104)

# print the list of number
print ("Given list:", list_numbers)
print ("All number divisible by 5 are")

# check if the number is divisible by 5
for number in list_numbers:
    if (number % 5) == 0:
# print all the list of number divisible by 5
      print (number)
