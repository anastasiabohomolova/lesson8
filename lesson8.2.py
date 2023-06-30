def func_gen(limit):
    for i in range(limit):
        if i % 2 == 1:

            yield i       


my_gen = func_gen(10)
for i in range(3):
    print(next(my_gen))




