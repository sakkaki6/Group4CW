def sed(file_input, file_output):
    with open(file_input, 'r') as r:
        with open(file_output, 'a') as a:
            k = r.read().split()
            for i in k:
                a.write(i)
                a.write(' ')

sed('file1.txt', 'project2.txt')
sed('file2.txt', 'project2.txt')
sed('file3.txt', 'project2.txt')