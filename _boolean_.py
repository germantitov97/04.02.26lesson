# input rating from the user, the range should be 1-5
#   is_valid should be True if in range and False if not in range
#   if is_valid:
#      print('in range')
#   else:
#      print('not in range')
#
# is_best should be True if the rating was 5
#   if is_valid and is_best:
#      print('highest score')
#   else:
#      print('not highest score')
#
# is_medium should be True if the rating was between 2-4
#   if is_valid and not is_medium:
#      print('score high or low')
#   else:
#      print('medium score')
#
# input number from user
#   is_positive should be True if number >= 0
#   write if with print
#
# input number from user
#   is_even should be True if number % 2 == 0
#   write if with print
is_valid = bool
is_best = bool
is_medium = bool
is_positive = bool

number = int(input('Enter a number between 1-5 : '))
if number >= 1 and number <= 5:
    is_valid = True
    print('in range')
elif number < 1 or number > 5:
    is_valid = False
    print('not in range')
if is_valid == True and number == 5:
    is_best = True
    print('highest score')
elif is_valid == True and number != 5:
    is_best = False
    print('not highest score')
if number >= 2 and number < 5:
    is_medium = True
else:
    is_medium = False
if is_valid == True and is_medium == False:
    print('score high or low')
elif is_valid == True and is_medium == True:
    print('medium score')
if number >= 0:
    is_positive = True
    print('number is positive')
else:
    is_positive = False
    print('number is negative')
if number % 2 == 0:
    print('even')
else:
    print('odd')





