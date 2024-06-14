def do_multi_times(argument=2):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for i in range(argument):
                function(*args, **kwargs)
        return wrapper
    return decorator

@do_multi_times() 
def print_message(): 
    print("Hello, World!") 
 
print_message()