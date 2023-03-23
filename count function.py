full_number = []


def countfor(full):
    n = full  # Takes a number called full and calls it n
    number = 0  # This number is going to represent the number of times the number we are looking for appears
    while n > 0:  # This repeats the process of counting 4s until int(n/10) = 0
        r = n % 10  # The modulo will say if n has a 4 in it
        n = int(n / 10)  # This decreases the size of n by 1 digit
        if r == 4:  # Aka if a 4 is found
            number += 1  # says the number of 4s found in the full number
        if r == 4:
            full_number.append(full)  # add the full number that had a 4 to a list

    return number


sum1 = 0  # Initialize sum1 as the sum of all times the number 4 appears
for i in range(1235):  # iterates over numbers 1 to 1234
    sum1 = sum1 + countfor(i)  # continuously adds the number of 4s countfor has found

print('#' * 60)
print(f'le chiffre 4 apparait [ {sum1} ] fois de 1 à 1234')
print('#' * 60)
print(full_number)
# This is fucking genius!
