def func_gen():
    for i in [1, True, 2, 5, False, 8]:
        dicts = {}
        dicts[i] = i + 1
        print(dicts)
       
    yield dicts

a = func_gen()
print(next(a))



