#TipDat 'Set' menggunakan kurung kurawal '{'  '}'
#cara penulisan SAMA dengan List ataupun Tuple

#TipDat 'Set' tidak memilliki index, isinya berantakan (tidak bisa diurutkan)
foo = {"Belajar", "Python", 200, 6.99, True, 5j}
print(foo)
print(type(foo))

#isinya mengandung nilai Unik (Tidak bisa diubah dan tidak boleh sama)
print('\n')
uta = {"Belajar", "Belajar", 200, 200, True, 5j}
print(uta)
print('----------------')

#Set dipakai untuk operasi himpunan = gabungan(union), irisan(intersection)
uni = {1, 2, 3, 4, 5}
ins = {3, 4, 5, 6, 7}
print(uni | ins) #union
print(uni & ins) #intersection
