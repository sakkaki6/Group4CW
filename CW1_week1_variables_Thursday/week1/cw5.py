previous_number = 0
for current_number in range(10):
    sum = previous_number+current_number

    print("current number", current_number,
          "previous number", previous_number, "sum:", sum)
    previous_number = current_number
