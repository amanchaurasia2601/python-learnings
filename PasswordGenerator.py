import random
print("Password length should be between 9 to 15")
n=int(input("Input password length: "))
if(n>=9 and n<=15):
    Inc="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$&*"
    Password=(random.choice(Inc) for i in range(n))
    Password_Generator="".join(Password)
    print(Password_Generator)

else:
    print("Illegal attempt")