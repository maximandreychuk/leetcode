def my_range(start, stop, step=None):
    while start < stop:
        yield start
        if step:
            start += step
        else:
            start += 1

print(list(my_range(1,10)))