available=5
n=int(input('Enter no of candies you want: '))
for i in range(available):
    if n>available:
        print('Sorry')
    else:
        print('Candy')