#1. Find even_num and odd_numm
#orginal list with 8 number
numbers = [10, 105, 22, 39, 100, 999, 87, 351]

# Lists to hold even and odd numbers
even_num = []
odd_num = []

for num in number:
    if num % 2 == 0:
        even_num.append(num)
    else :
        odd_num.append(num)

# Output the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Answer:
even_num: [10, 22, 100]
odd_num: [105, 39, 999, 87, 351]


#2.Find Prime Number in List 

#funtion to find the prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range (2, int(num ** 0.5) +1):
        if num % i == 0 :
            return False
    return True

# Original list
numbers = [10, 105, 22, 39, 100, 999, 87, 351]
prime_numbers = []

for num in numbers:
    if (is_prime(num)):
        prime_numbers.append(num)

# Output the result
print("Prime numbers in the list:", prime_numbers)
print("Total prime numbers:", len(prime_numbers))

#3. Find Happy_number
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

# Original list
numbers = [10, 105, 22, 39, 100, 999, 87, 351]
happy_numbers = []

for num in numbers:
    if is_happy(num):
        happy_numbers.append(num)

# Output the results
print("Happy numbers in the list:", happy_numbers)
print("Total happy numbers:", len(happy_numbers))

#4.Sum First last digit
def sum_first_last_digit(number):
    # Convert the number to string to access digits
    num_str = str(abs(number))  # abs() handles negative numbers
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit
    num = 12345
result = sum_first_last_digit(num)
print("Sum of first and last digit:", result)


#5. Loop through all possible combinations of Rs.1, Rs.2, Rs.5, Rs.10 coins
for c10 in range(0, 2):          # Rs.10 coin: max 1
    for c5 in range(0, 3):       # Rs.5 coin: max 2
        for c2 in range(0, 6):   # Rs.2 coin: max 5
            for c1 in range(0, 11):  # Rs.1 coin: max 10
                total = c10*10 + c5*5 + c2*2 + c1*1
                if total == 10:
                    print(f"Rs.10:{c10}, Rs.5:{c5}, Rs.2:{c2}, Rs.1:{c1}")


#6. Find  duplicates in the list
# Sample lists (you can change these)
list1 = [1, 2, 3, 4, 5, 10]
list2 = [3, 5, 7, 10, 11]
list3 = [0, 3, 5, 9, 10]

# Find duplicates (common elements) in all three lists
duplicates = set(list1) & set(list2) & set(list3)

# Output the result
print("Duplicates in all three lists:", list(duplicates))


#7.Find Repeating number
# Given list
numbers = [1, 2, 3, 4, 5, 2, 1, 4, 3, 5]

# Count occurrences of each number
from collections import Counter
count = Counter(numbers)

# Find the first non-repeating element
for num in numbers:
    if count[num] == 1:
        print("First non-repeating element is:", num)
        break
else:
    print("No non-repeating element found.")


#8.find the minimum element in a rated and sorted list
def find_min_in_rotated_sorted_list(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return arr[low]


# rotated sorted list
numbers = [4, 5, 6, 1, 2, 3]
# Find and print minimum element
min_element = find_min_in_rotated_sorted_list(numbers)
print("Minimum element in the rotated sorted list is:", min_element)

# output of the result
# Minimum element in the rotated sorted list is: 1


#9.Find sum of Target 
# Given list and target value
numbers = [10, 20, 30, 9]
target = 59

# Find triplets
found = False
n = len(numbers)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if numbers[i] + numbers[j] + numbers[k] == target:
                print(f"Triplet found: {numbers[i]}, {numbers[j]}, {numbers[k]}")
                found = True

if not found:
    print("No triplet found with the given sum.")
    

#10. find if there is asub-list with sum equal to zero
def has_zero_sum_sublist(arr):
    seen_sums = set()
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)
    return False

# Given list
numbers = [4, 2, -3, 1, 6]

# Check and print result
if has_zero_sum_sublist(numbers):
    print("Sub-list with zero sum exists.")
else:
    print("No sub-list with zero sum exists.")


