def do_before(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            pre_func()
            function(*args, **kwargs)
        return wrapper
    return decorator


def pre_func(): 
        print("Executing the pre-function...")

@do_before(pre_func) 
def wrapped_function(): 
    print("Executing the wrapped function...")

wrapped_function()