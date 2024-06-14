def my_range(start, stop, step):
    if type(start) != int or type(stop) != int or type(step) != int or step==0 or stop < start:
        raise ValueError
    else:
        for i in range(start, stop, step):
            yield i


a = list(my_range(1.2, 10, 2))
print(a)
# for i in a:
#     print(i)
