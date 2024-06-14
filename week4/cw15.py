def do_multi_times(iterations=2):
    def factory(func):
        def wrapper(*args):
            for i in range(iterations):
                func(*args)
        return wrapper
    return factory


@do_multi_times(iterations=4)
def print_message(name):
    print("Hello, World!", name)


print_message('*')
