a= [ 5, 6, 2, 9, 6, 4 ]
for i in a:
    square=lambda a:a*a
    print(square(i),end=" ")
print()
for i in a:
    cube=lambda a:a*a*a
    print(cube(i),end=" ")