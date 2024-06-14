words = ["apple", "banana", "cherry", "date", "elderberry"]
words.sort(key=lambda x: x.count('a')+ x.count('e')+  x.count('i') + x.count('y') + x.count('u')+  x.count('o'), reverse=True)
print(words)