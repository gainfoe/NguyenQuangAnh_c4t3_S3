prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

print("List of fruits:")
number = 1
for fruit in prices:
    print(str(number) + ".")
    print(fruit)
    print("price:", prices[fruit])
    print("stock:", stock[fruit])
    print()
    number += 1

print("Total:")
total = 0
for fruit in prices:
    print(fruit + 's', "cost", prices[fruit] * stock[fruit])
    total += prices[fruit] * stock[fruit]

print("Total Prices:", total)



