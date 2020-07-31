def remowood(n):
    if (n % 3 == 0 and n%5==0):
        return ("remo_wood")
    elif(n % 3==0):
        return("remo")
    elif(n%5==0):
        return ("wood")
    else:
        return (n)


n=int(input("Enter no: "))
t=remowood(n)
print(t)
