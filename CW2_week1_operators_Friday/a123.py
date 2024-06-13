a=[1,2]
print(a,id(a))
b=a
print(b,id(b))
a.append(3)
print(a,id(a),b,id(b))