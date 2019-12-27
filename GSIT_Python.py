# 1. greeting and after 10 years
'''
name = input('What is your name? ')
print('Nice to meet you,', name, '!')
age = int(input('How old are you? '))
print('So after decade, you are', age+10, 'years old.' )
'''

# 2. Coin change program
# the kinds of coin are 10, 50, 100, 500
'''
money = int(input('How much do you have? '))

money_500 = money // 500; money %= 500
money_100 = money // 100; money %= 100
money_50 = money // 50; money %= 50
money_10 = money // 10; money %= 10

print('You can change with %d pieces of 500' % money_500)
print('You can change with %d pieces of 100' % money_100)
print('You can change with %d pieces of 50' % money_50)
print('You can change with %d pieces of 10' % money_10)
'''

# 3. Calculate which is leap year
'''
year = int(input('What year is it? '))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 ==100) :
    print('%d is leap year' % year);

else :
    print('%d is not leap year' % year);
'''

# 4. APLLE
'''
fresh = input('Are the apples fresh? \nYou can choose Y/N ')

if fresh == 'Y':
    apple_cost = int(input('How much an apple is? '))

    if apple_cost <=1000:
        quantity = 10
    else:
        quantity = 5
    print('You buy %d apples' % quantity)

elif fresh == 'N':
    print("You don't buy an apple")

else:
    print("Chose wrong letter")
'''

# 5. input num
'''
num = int(input('What is your number? '))

if num > 0:
    print('Your number, %d, is positive.' % num)

elif num == 0:
    print('Your number, %d, is zero.' % num)

else:
    print('Your number, %d, is negative.' % num)
'''

# 6. Score process
'''
score = int(input('What is your score? '))

if score >= 90:
    print('Your grade is A')

elif score >= 80:
    print('Your grade is B')

elif score >= 70:
    print('Your grade is C')

elif score >= 60:
    print('Your grade is D')

else:
    print('Your grade is F')

print('\nYour semester is done, GOOD JOB')
'''

# 7. Rock Scissors Paper
'''
import random # 난수 생성 위해
You = input('Choose Yours from\n 1. Rock\n 2. Scissors\n 3. Paper\n')
num = random.randint(1,3)

if num == 1:
    Com = 'Rock'
elif num == 2:
    Com = 'Scissors'
elif num == 3:
    Com = 'Paper'

if You == Com:
    result = 'Tie'
elif You == 'Rock':
    if Com == 'Scissors':
        result = 'You WIN'
    else:
        result = 'You LOSE'
elif You == 'Scissors':
    if Com == 'Paper':
        result = 'You WIN'
    else:
        result = 'You LOSE'
elif You == 'Paper':
    if Com == 'Rock':
        result = 'You WIN'
    else:
        result = 'You LOSE'

print('%s, Your is %s, and Computers is %s' % (result, You, Com))
'''

# 8. sum of integer
'''
num = int(input('What is your number? '))
sum = 0

for i in range(1, num+1):
    sum += i

print('Your Sum from 1 to %d, is %d.' % (num, sum))
'''

# 9. factorial
'''
num = int(input('What is your number? '))
fac = 1

for i in range(1, num+1):
    fac *= i

print('%d! is %f.' % (num, fac))
'''

# 10. summation of position number
'''
num = int(input('What is your number? '))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print('The summation of the digit for %d, is %d.' % (num, sum))
'''

# 11. Guess number!
'''
import random # 난수 생성 위해

num = random.randint(1, 100)
temp = 0
guess = 0

while num != guess:
    guess = int(input('Guess the number! '))
    temp += 1
    if num > guess:
        print('Higher!')
        continue
    else:
        print('Lower!')
        continue
    temp += 1

print('Congratulation! You Guess right number, %d, in %d tries.' % (num, temp))
'''

# 12. square
'''
def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

print(power(10,2))
'''

# 13. swap and average
'''
def add(x, y):
    return x + y


def swap(x, y):
    if x < y:
        x, y = y, x
        return x, y
    else:
        return x, y


x = int(input('what is your 1st number? '))
y = int(input('what is your 2nd number? '))
x, y = swap(x, y)
sum = add(x, y)
average = sum/2

print('your numbers are %d, %d, sum is %d, average is %.3f.' % (x, y, sum, average))
'''

# 14. address organizing program
'''
menu = 0
Friends = []

while menu != 9:
    print("1. Print friends list\n2. Add friend\n3. Delete friend\n4. Change name\n9. Exit")
    menu = int(input('\nPress the number. '))

    if menu == 1:
        print(Friends)
    elif menu == 2:
        name_add = input('What is the name of friend? ')
        Friends.append(name_add)
    elif menu == 3:
        name_del = input('What is the name of friend? ')
        if name_del in Friends:
            Friends.remove(name_del)
        else:
            print('There is no %s in your list' % name_del)
    elif menu == 4:
        name_chan = input('What is the name of friend? ')
        if name_chan in Friends:
            name_2 = input('What is the new name of friend?')
            remove = Friends.index(name_chan)
            Friends.remove(name_chan)
            Friends.insert(remove, name_2)
        else:
            print('There is no %s in your list' % name_del)
'''