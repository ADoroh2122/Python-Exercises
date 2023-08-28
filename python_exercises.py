# Question 1. 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def first_odds(username):
    """Want to print hello_Username as the function."""
    print("hello, " + username + '!')

first_odds('andrew')

    #input = input("Enter your username: ")
    #first_odds(input)
    
# Question 2. 
# Write a python function, first_odds that prints the odd numbers from 1-100 
# and returns nothing.

def first_odds():
    """Prints the odd numbers from 1-100"""
    for number in range(1,100,2):
        print(number)
print(first_odds())

# Question 3. 
# Please write a Python function, max_num_in_list to return the max number of a given list. 
    
def max_num_in_list():
    """Return max number of a given list"""
digits =[1,2,3]
print(max(digits))
max_num_in_list()

# Question 4. 
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(year):
    """Seeing if a given year is a leap year."""
    year = int(year)
    if (year % 4 ==0 and year % 100 != 0) or year % 400 ==0:
        return True
    else:
        return False
   
answer = is_leap_year(2000)
print(answer)

# Question 5. 
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    """Checking if numbers are consecutive or not"""
    if a_list == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False
    
a_list = [1,3,4,5]
print(is_consecutive(a_list))

    