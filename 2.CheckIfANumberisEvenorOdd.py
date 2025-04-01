# Algorithm-2: Check if a Number is Even or Odd

number = int(input('Enter a number: '))

if number == 0:
    print('Number is Zero which is a confusing number.')

elif number%2 == 0:
    print('Number is Even')

else:
    print('Number is Odd')