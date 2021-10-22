foo = ['Belajar', "Python", "di", "Duniailkom"]
bar = [100, 200, 93]

baz = ["Python", 200, 6.99, True,5j]
  
print(foo)
print(bar)
print(baz)
print('-------------------')

#print type
print(type(foo))
print(type(bar))
print(type(baz))

print('-------------------')

#cara akses type data List
#Data pertama bernomor index 0, data kedua 1, dst

print(baz[2])
print(baz[0])
print('-------------------')

#cara update isi List
print (baz)

#update
baz[0] = 9000
baz[1] = 'setelah diganti ini'
print(baz)
print('-------------------')
print('-------------------')

#menampilkan sebaian data
baz = ["Python", 200, 6.99, True,5j]
print(baz[2:5])
print(baz[:3])
print(baz[3:])
print(baz[:]) # = menampilkan semua isi

