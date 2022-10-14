NumList = [9,3,5,4,-7,9,0,3,-10]
print("List Of Numbers : ",NumList)
print()
# 1.Using filter() function filter the list so that only negative numbers are left.

NegNums = list(filter(lambda x: x<0,NumList))

print("Negative Numbers : ",NegNums)
print()
#2. Using filter function, filter the even numbers so that only odd numbers are passed to the new list.

OddNums = list(filter(lambda x: x%2!=0,NumList))

print("Odd Numbers : ",OddNums)
print()
#3. Using filter() and list() functions and .lower() method filter all the vowels in a given string.

list1 = ["A","B","C","D","e","F","g","H","I","j","k","l","m"]

vowels = list(filter(lambda x: True if x.lower() in "aeiou" else False, list1))

print("Vowels in the list : ", vowels)

#4. This time using filter() and list() functions filter all the positive integers in the string.
print()

posInts = list(filter(lambda x: True if x>0 else False, NumList))

print("Positive integers in the list : ", posInts)

print()

#5. Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.[Try using map inside filter]


Change = list(filter(lambda x: x>0 ,map(lambda x: x*-1,NumList)))

print("The Changed list : ", Change)