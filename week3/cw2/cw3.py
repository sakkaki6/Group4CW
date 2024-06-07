def capitalize_last_name(name):
    if not isinstance(name, str):
        raise TypeError()

    name_parts = name.split()
    if len(name_parts) != 2:
        raise ValueError()

    f_name = name_parts[0][0].upper() + name_parts[0][1:]
    l_name = name_parts[1].upper()

    return f_name + ' ' + l_name


try:
    user_input = input("Enter full name:")
    result = capitalize_last_name(user_input)
    print(result)
except TypeError:
    print("Input should be a string.")
except ValueError:
    print("Input should consist of exactly two words.")


