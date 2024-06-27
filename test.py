# import itertools
# from functools import lru_cache

# def generate_dice_faces():
#     return list(itertools.product(range(10), repeat=6))

# @lru_cache(maxsize=None)
# def can_cover_all_numbers_cached(die1, die2, max_number):
#     required_combinations = set()
#     for num in range(max_number + 1):
#         tens = num // 10
#         units = num % 10
#         required_combinations.add((tens, units))

#     possible_combinations = set()
#     for d1 in die1:
#         for d2 in die2:
#             possible_combinations.add((d1, d2))
#             possible_combinations.add((d2, d1))

#     return required_combinations.issubset(possible_combinations)

# def can_cover_all_numbers(die_faces, max_number):
#     for die1 in die_faces:
#         for die2 in die_faces:
#             if can_cover_all_numbers_cached(tuple(die1), tuple(die2), max_number):
#                 return tuple(die1), tuple(die2)
#     return None, None

# def main():
#     die_faces = generate_dice_faces()
#     max_number = int(input("Enter the maximum number to cover (0-99): "))

#     die1, die2 = can_cover_all_numbers(die_faces, max_number)
    
#     if die1 and die2:
#         print(f"Yes, the two dice can cover all numbers from 00 to {max_number}.")
#         print(f"Die 1 faces: {die1}")
#         print(f"Die 2 faces: {die2}")
#     else:
#         print(f"No, the two dice cannot cover all numbers from 00 to {max_number}.")

# if __name__ == "__main__":
#     main()

