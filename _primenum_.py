# **Bonus: input number from user, is_prime should be True if the number is prime otherwise False
number = int(input('Enter a number: '))
is_prime = bool
if number <= 1:
    is_prime = False
elif number <= 3:
    is_prime = True
elif number % 2 == 0 or number % 3 == 0:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
    else:
        is_prime = True

print('prime is ',is_prime)