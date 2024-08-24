# Question 1 
# arb_args - Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for arg in args:
        print(arg) 

arb_args(1, "apple", 3.14, True)

# Question 2
# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.


def inner_func(a, b):
    def add():
        return a + b
    
    def multiply():
        return a * b
    
    result1 = add()
    result2 = multiply()

    total = result1 + result2

    print(total)

inner_func(7,5)

# Question 3
# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.


def lunch_lady(students_name, lunch_preference="Mystery Meat"):
    print(f'Students Name": {students_name}')
    print(f'Lunch Preference: {lunch_preference}')

lunch_lady("daddy", "burger")

# Question 4
# sum_n_product - Accepts two integers and returns both the sum and the product.


def sum_n_product(a, b):
    sum_result = a + b 
    product_result = a * b
    return sum_result, product_result

sum_value, product_value = sum_n_product(5,4)
print(f"Sum: {sum_value}, Product: {product_value}")


# Question 5
# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.


def arb_args(*args):
    for arg in args:
        print(arg) 

alias_arb_args = arb_args

alias_arb_args(1, "apple", 3.14, True)


# Question 6 
# arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*numbers):
    if len(numbers) ==0:
        print("no numbers provided.")
    else:
        total = sum(numbers)
        average = total / len(numbers)
        print(f'The Average is: {average}')

arb_mean(1, 2, 3, 4, 5)
arb_mean(10, 20, 30)
arb_mean()


# Question 7
# arb_longest_string - Accepts any number of strings and returns the longest one.


def arb_longest_string(*strings):
    if len(strings) == 0:
        return None
    
    longest_string = max(strings, key=len)
    return longest_string

print(arb_longest_string("apple", "banana", "cherry", "blueberry"))
print(arb_longest_string("cat", "dog", "elephant"))
print(arb_longest_string())  # No strings provided


