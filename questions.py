strings

What is a string in Python?
How do you concatenate two or more strings in Python?
How do you convert a string to uppercase or lowercase in Python?
What is string formatting in Python?
What is the difference between a string and a list in Python?
How do you access individual characters in a string in Python?
What is the 'split' method in Python?
How do you check if a string contains a certain substring in Python?
How do you replace a substring in a string in Python?
What is the 'strip' method in Python?
How do you reverse a string in Python?
How do you convert a string to an integer in Python?
How do you find the length of a string in Python?
How do you remove whitespace from the beginning or end of a string in Python?
How do you check if a string is empty in Python?
How do you find the index of a substring in a string in Python?
How do you convert a list of strings to a single string in Python?
What is the difference between 'find' and 'index' methods in Python?
How do you split a string into a list of characters in Python?
How do you convert a string to a list in Python?
What is the 'join' method in Python?
How do you remove a specific character from a string in Python?
How do you count the occurrence of a substring in a string in Python?
How do you check if a string starts with or ends with a certain substring in Python?
How do you format a string with multiple placeholders in Python?
How do you remove all occurrences of a substring in a string in Python?
How do you check if a string is a palindrome in Python?
How do you sort a list of strings in Python?
How do you replace multiple substrings in a string in Python?
How do you convert a string to a datetime object in Python?
How do you compare two strings in Python?
How do you convert a string to a float in Python?
How do you capitalize the first letter of a string in Python?
What is the difference between a string and a byte string in Python?
How do you encode and decode strings in Python?
How do you remove all leading zeros from a string in Python?
How do you check if a string is numeric in Python?
How do you remove non-alphanumeric characters from a string in Python?
How do you reverse the order of words in a string in Python?
How do you split a string into multiple substrings based on a delimiter in Python?
How do you check if a string is a valid email address in Python?
How do you remove duplicate characters from a string in Python?
How do you extract a substring between two characters in a string in Python?
How do you replace a string with another string in a file in Python?
How do you remove the last character of a string in Python?
How do you compare two strings in Python?
How do you convert a string to a float in Python?
How do you capitalize the first letter of a string in Python?
What is the difference between a string and a byte string in Python?
How do you encode and decode strings in Python?
How do you remove all leading zeros from a string in Python?
How do you check if a string is numeric in Python?
How do you remove non-alphanumeric characters from a string in Python?
How do you reverse the order of words in a string in Python?
How do you split a string into multiple substrings based on a delimiter in Python?
How do you check if a string is a valid email address in Python?
How do you remove duplicate characters from a string in Python?
How do you extract a substring between two characters in a string in Python?
How do you remove all whitespace characters from a string in Python?
How do you convert a string to a boolean in Python?
How do you remove all punctuation characters from a string in Python?re
How do you concatenate a list of strings into a single string using a separator in Python?
How do you pad a string with zeros or other characters in Python?
How do you count the number of words in a string in Python?
How do you extract a substring from the end of a string in Python?
How do you check if a string contains only letters or only numbers in Python?
How do you convert a string to a dictionary in Python?
How do you convert a string to a list of integers in Python?
How do you remove all occurrences of a character from a string in Python?
How do you extract the first letter of each word in a string in Python?
How do you truncate a string to a certain length in Python?
How do you convert a string to a set in Python?



bitwise operators


What are bitwise operators in Python?
How many bitwise operators are there in Python?
What is the use of the & operator in Python?
What is the use of the | operator in Python?
What is the use of the ^ operator in Python?
What is the use of the ~ operator in Python?
How can you perform left shift and right shift operations in Python?
Can you give an example of how you would use a bitwise operator to check if a number is even or odd in Python?
How can you use a bitwise operator to set a bit to 1 in Python?
How can you use a bitwise operator to clear a bit to 0 in Python?

What is the difference between == and is operators in Python?
    Answer: The == operator checks if two values are equal, while the is operator checks if two objects are the same object in memory.

    What is the order of precedence for operators in Python?
    Answer: The order of precedence for operators in Python is as follows: parentheses, exponentiation, multiplication and division (left to right), addition and subtraction (left to right), comparison operators, logical operators.

    What are the logical operators in Python?
    Answer: The logical operators in Python are and, or, and not. They are used to combine and manipulate boolean values.

    What is the ternary operator in Python?
    Answer: The ternary operator is a shorthand way of writing an if-else statement in Python. It has the syntax "value_if_true if condition else value_if_false".

    What are the bitwise operators in Python?
    Answer: The bitwise operators in Python are & (and), | (or), ^ (xor), ~ (not), << (left shift), and >> (right shift). They are used to perform bitwise operations on integer values.


What is the difference between "is" and "==" operators in Python?
    Answer: "is" operator is used to compare the memory locations of two objects, while "==" operator is used to compare the values of two objects.

    Can we use "is" operator to compare values of two objects?
    Answer: No, "is" operator is used to compare the memory locations of two objects. To compare the values of two objects, we should use the "==" operator.

    What is the return type of "is" and "is not" operators?
    Answer: The return type of both "is" and "is not" operators is a boolean value - True or False.

    How do you check if two variables refer to the same object in Python?
    Answer: We can use the "is" operator to check if two variables refer to the same object in Python. For example:

css

a = [1, 2, 3]
b = a
print(a is b)  # Output: True

    What is the difference between "is" and "id" functions in Python?
    Answer: "is" operator is used to compare the memory locations of two objects, while "id" function is used to get the unique identifier of an object. The "id" function returns an integer value, while "is" operator returns a boolean value.


Can we use "is" operator with strings in Python?
    Answer: Yes, we can use "is" operator with strings in Python. However, it is recommended to use "==" operator to compare the values of two strings.

    What happens when we use "is" operator with mutable objects like lists and dictionaries?
    Answer: When we use "is" operator with mutable objects like lists and dictionaries, it compares the memory locations of the objects. If two mutable objects have the same values but are stored in different memory locations, the "is" operator will return False.

    What is the use of "is not" operator in Python?
    Answer: "is not" operator is used to check if two objects are not the same object. It returns True if the two objects have different memory locations, and False if they have the same memory location.

    How can we check if a variable is None using identity operator in Python?
    Answer: We can use the "is" operator to check if a variable is None in Python. For example:

python

a = None
print(a is None)  # Output: True

    Is "is" operator faster than "==" operator in Python?
    Answer: Yes, "is" operator is faster than "==" operator in Python because it only compares the memory locations of two objects, while "==" operator compares the values of two objects, which may involve more operations. However, the difference in speed is usually negligible in most cases.

Write source in Python code for assignment operators.

Give example to understand operator precedence available in Python programming language

Write a program in Python to explain relational operators.

Write source in Python code for bitwise operators.

Write a program in Python to explain logical operators.

Write source in Python code for identity operators.

Write source in Python code for membership operators.

Write a program in Python to explain assignment operators.


loops

Example 1: Print the first 10 natural numbers using for loop.
Example 2: Python program to print all the even numbers within the given range.
Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
Example 4: Python program to calculate the sum of all the odd numbers within the given range.
Example 5: Python program to print a multiplication table of a given number
Example 6: Python program to display numbers from a list using a for loop.
Example 7: Python program to count the total number of digits in a number.
Example 8: Python program to check if the given string is a palindrome.
Example 9: Python program that accepts a word from the user and reverses it.
Example 10: Python program to check if a given number is an Armstrong number
Example 11: Python program to count the number of even and odd numbers from a series of numbers.
Example 12: Python program to display all numbers within a range except the prime numbers.
Example 13: Python program to get the Fibonacci series between 0 to 50.
Example 14: Python program to find the factorial of a given number.
Example 15: Python program that accepts a string and calculates the number of digits and letters.
Example 16: Write a Python program that iterates the integers from 1 to 25.
Example 17: Python program to check the validity of password input by users.
Example 18: Python program to convert the month name to a number of days.


https://csiplearninghub.com/questions-of-while-loop-in-python/



lists

1 : Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

Given: list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output: [5, 10, 15, 200, 25, 50, 20]
 
2. write a program to remove all occurrences of item 20.

Given:  list1 = [5, 20, 15, 20, 25, 50, 20]

Expected output:  [5, 15, 25, 50]
3:Write a program to add item 7000 after 6000 in the following Python List

Given:	list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

Expected output:  [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
4:write a program to turn every item of a list into its square.

Given:	numbers = [1, 2, 3, 4, 5, 6, 7]

Expected output:  [1, 4, 9, 16, 25, 36, 49]
5 : write a program to remove negative numbers in list

given list : [2,-5,23,6,-22,0,-1,5]

Expected Output : [2,23,6,0,5]
1.How to remove duplicates in list
2.Reverse List except Last Element using Slicing
3. find out the sum of element present in list 
you can use sum function or without sum function.
l1= [3,5,6,7,3,5,7,10]
find out the sum of above element.

4. Within a list print duplicate and unique value
5. Write a program to reverse strings in a given list of string values
Eg. [One,Two,Three]
O/p [enO, owT, eerhT]

6. Print even an odd number in a list without using list comprehension
7. program to count positive and negative numbers in a List
Print second largest element in a list
9. 3rd largest element in a list
