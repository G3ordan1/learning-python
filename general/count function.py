# Originally created to answer the question: How many times does 
# the number 4 appear between 1 and 1234?
full_number = []


def countfor(full):
    n = full  # Takes a number called full and calls it n
    number = 0  # This number is going to represent the number of times the number we are looking for appears
    if digit == 0 and n == 0:  # This is a special case for 0
        number += 1
        full_number.append(0)
    while n > 0:  # This repeats the process of counting the digits until int(n/10) = 0
        r = n % 10  # The modulo will say if n has the digit in it
        n = int(n / 10)  # This decreases the size of n by 1 digit
        if r == digit:  # Aka if the digit is found
            number += 1  # says the number of the digits found in the full number
            if full not in full_number:
                full_number.append(full) # add the full number that had a 4 to a list
    return number


digit = int(input('Enter the digit you want to count (between 0 and 9): '))  # Asks for a digit to count
num = int(input('Enter the max of your range (between 0 and 2^31+1): '))  # Asks for a range of numbers

sum1 = 0  # Initialize sum1 as the sum of all times the digit appears
for i in range(num+1):  # iterates over numbers 1 to num
# continuously adds the number of digits countfor has found
    sum1 = sum1 + countfor(i)

print('#' * 60)
print(f'le chiffre {digit} apparait {sum1} fois de 0 à {num}')
print('#' * 60)
print(full_number)
# This is fucking genius!
