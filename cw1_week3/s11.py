def pascal_1(n: int):
    if n <= 0:
        return

    li1 = [1]
    if n > 1:
        li2 = [1, 1]

    print(li1)

    if n > 1:
        print(li2)

    for i in range(2, n+1):
        if i % 2 == 0:

            li1 = [1] + [li2[j] + li2[j + 1]
                         for j in range(len(li2) - 1)] + [1]
            print(li1)
        else:

            li2 = [1] + [li1[j] + li1[j + 1]
                         for j in range(len(li1) - 1)] + [1]
            print(li2)


num_rows = int(input("Enter the number of rows: "))
pascal_1(num_rows)
