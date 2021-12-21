# def my_decorator(func):
#     def wrapper(a, b):
#         print("hello")
#         func(a, b)
#         print("world")
#
#     return wrapper
#
#
# @my_decorator
# def foo(a, b):
#     #print("Hello")
#     print(a + b)
#     print("Python")
#     #print("world")
#
#
# def baz():
#     # print("Hello")
#     print("Artem")
#     # print("world")
#
#
# foo(2,3)

def fibonachi(n):
    last_num = 0
    next_num = 1
    if n == 1:
        print(last_num)
    else:
        print(last_num, next_num, end=" ")
        for i in range(n - 2):
            last_num, next_num = next_num, last_num + next_num
            print(next_num, end= " ")

fibonachi(5)
