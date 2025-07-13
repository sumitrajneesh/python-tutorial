# def fun():
#     print("Hello")
#
# fun()

# def substraction(x, y):
#     return (x - y)
#
# a = 90
# b = 50
#
# res = substraction(a, b)
# print(res)

#Python program to print first 10 prime numbers

# def fun(n):
#     x = 2
#     count = 0
#     while count < n:
#         for d  in range(2, int(x ** 0.5) + 1):
#             if x % d == 0:
#                 break
#         else:
#             print(x)
#             count +=1
#         x +=1
# n = 10
# fun(n)

#passing function as an Argument

# def fun(func, arg):
#     return func(arg)
#
# def square(x):
#     return x ** 2
#
# res = fun(square, 5)
# print(res)

# def fun(*args):
#     for arg in args:
#         print(arg)
# fun(1,2,3,4,5)

# def fun(**kwargs):
#     for k, val in kwargs.items():
#         print(f"{k}: {val}")
#
# fun(name="sumit", age =30, city="Kolkata")

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Name - {self.name} and Age - {self.age} . ")
#
# p1 = Person("sumit", 25)
#
# p1.greet()

#empty function with pass

# def fun():
#     pass
#
# fun()

# i = 0
#
# while i < 10:
#     pass
#     i += 1

#python return statement

# def add(a, b):
#     return a + b
#
# def is_true(a):
#     return bool(a)
#
# res = add(2, 3)
# print(res)
#
# res = is_true( 2 < 5)
#
# print(res)

#return multiple values

# def fun():
#     name = "sumit"
#     age = 30
#     return name, age
#
# name, age = fun()
# print(name)
# print(age)

# def fun1(msg):
#     def fun2():
#         return f"Message: {msg}"
#     return fun2
#
# fun3 = fun1("Hello world")
#
# print(fun3())

# s1 = "codinggyan"
# s2 = lambda func: func.upper()
# print(s2(s1))

# s = ['1', '2', '3' ,'4']
# res = map(int, s)
# print(list(res))

from functools import reduce

# def add(x, y):
#     return x + y
#
# a = [1,2 ,3,4,5]
# res = reduce(add, a)
#
# print(res)

a = [1, 2, 3, 4, 5, 6]
res = reduce(lambda x, y: x + y, a)

print(res)