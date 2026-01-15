"""
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""

a = int(input("Enter the first num: "))
b = int(input("Enter the second num: "))


a_sum_b = a + b
a_diff_b = a - b
a_prod_b = a * b

print(f"sum of 2 nums = {a_sum_b}")
print(f"difference of 2 nums = {a_diff_b}")
print(f"product of 2 nums = {a_prod_b}")