def get_input():
    str1 = input("enter a number: ")
    try:
        number = int(str1)
        print(f"Successfully converted input to integer: {number}")
        return number
    except (ValueError,TypeError):
        print("Error: The input could not be converted to an integer.")
    except Exception as f:
        print(f.__class__.__name__)
    finally:
        print("complete.")
print(get_input)

get_input()