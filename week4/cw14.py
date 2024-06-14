def do_before(before_func):
    def decorator(function):
        
        def pre_func(*args, **kwargs):
            pre_func()
            function(*args,**kwargs)
            print("Hello, this runs before the main function!")
        return pre_func
    return decorator


@do_before
def wrapped_function():
        print("executing the wrapper function.")








