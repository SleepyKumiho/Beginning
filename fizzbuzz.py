"""
Programmer: Ryan Lee

Straightforward fizzbuzz program, accepts an integer and counts up to that number (inclusive) from 1
"""

count = int(input("Type an integer: ")) + 1
ran = range(count)
for x in ran:
    result = ""
    if x % 3 == 0:
        result += "Fizz"
    if x % 5 == 0:
        result += "Buzz"
    if result == "":
        print(x)
    else:
        print(result)
