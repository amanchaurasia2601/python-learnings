class A:
    def fun1(self):
        print("I am from Class A fun1")

    def fun2(self):
        print("I am from Class A fun2")


class B(A):    #Single level Inheritance
    def fun3(self):
        print("I am from Class B fun3")

    def fun4(self):
        print("I am from Class B fun4")


class C(B):    #Multilevel inheritance
    def fun5(self):
        print("I am from Class C fun5")

    def fun6(self):
        print("I am from Class C fun6")


class D(A):    #Hierarchical inheritance
    def fun7(self):
        print("I am from Class D fun7")

    def fun8(self):
        print("I am from Class D fun8")

class E(C,D):     #Multiple inheritance
    def fun9(self):
        print("I am from Class E fun9")

    def fun10(self):
        print("I am from Class E fun10")

a=A()
b=B()
c=C()
d=D()
e=E()

a.fun1()
a.fun2()
b.fun1()  #Single level inheritance
b.fun2()  #Single level inheritance
b.fun3()  #Single level inheritance
b.fun4()  #Single level inheritance
c.fun1()  #Multiple level inheritance
c.fun2()  #Multiple level inheritance
c.fun3()  #Multiple level inheritance
c.fun4()  #Multiple level inheritance
c.fun5()  #Multiple level inheritance
c.fun6()  #Multiple level inheritance
d.fun7()  #Hierarchcal inheritance
d.fun8()  #Hierarchcal inheritance
d.fun1()  #Hierarchcal inheritance
d.fun2()  #Hierarchcal inheritance
e.fun9()  #Multiple inheritance
e.fun10() #Multiple inheritance
e.fun1()  #Multiple inheritance
e.fun2()  #Multiple inheritance
e.fun3()  #Multiple inheritance
e.fun4()  #Multiple inheritance
e.fun5()
e.fun6()
e.fun7()
e.fun8()
e.fun9()
e.fun10()
