# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

try:
    numbers = read_numbers()
except:
    sys.exit("Error: no numbers provided")

numbers.sort()
length = (len(numbers)-1)
if length == -1:
    sys.exit("Error: no numbers provided")

#minimum
print(f"Minimum = {numbers[0]}")
#max
print(f"Maximum = {numbers[length]}")
#mean
sum_mean = sum(numbers)
mean = sum_mean / (length +1)
print(f"Mean = {mean}")
#median
if length % 2 == 0:
    median = numbers[length // 2]
else:
    first_number = numbers[length // 2]
    second_number = numbers[(length // 2) + 1]
    sum_median = second_number + first_number
    median = sum_median/2
print(f"Median = {median}")