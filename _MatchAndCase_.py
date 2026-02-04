# input rating
# rating == 5 rating == 4  print('VERY GOOD')
# rating == 3 print('GOOD')
# rating == 2 print('NEEDS IMPROVEMENT')
# rating == 1 print('REALLY NEEDS IMPROVEMENT')
# else print('NOT IN RANGE')

rating = int(input('rate between 1 and 5: '))
match rating:
    case 1:
        print('REALLY NEEDS IMPROVEMENT')
    case 2:
        print('NEEDS IMPROVEMENT')
    case 3:
        print('GOOD')
    case 4 | 5:
        print('VERY GOOD')
    case _:
        print('NOT IN RANGE')