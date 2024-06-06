def sorted_list(list1, list2):
    combined_list = []
    for item in range(len(list1)):
        combined_list.append((list1[item], list2[item]))
    tuple2 = dict(combined_list)

    print(sorted(tuple2.items(), key=lambda item: item[1], reverse=True))


sorted_list(["Mike", "Danny", "Jim", "Annie"], [4, 12, 7, 19])
