def sed(file_input):
    with open(file_input, 'r') as r:
        with open('words.txt', 'w') as w:
            k = r.read().split()
            d ={'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
            for i in k:
                if i in d.keys():
                    w.write(d[i])
                    w.write(' ')
                else:
                    w.write(i)
                    w.write(' ')



sed('project5.txt')

