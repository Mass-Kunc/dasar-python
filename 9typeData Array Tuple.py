#Hampir mirip tipe List. Tipe data Tuplr isinya tidak bisa diganti

#tipe data List menggunakan kurung siku '['  ']' , dan isi bisa diubah
foo = ['Belajar', "Python", "di", "Duniailkom"]
print(foo)

#tipe data Tuple menggunakan kurung bulat '('  ')' , dan isi TIDAK bisa diubah
uta = ('Belajar', "Python", "di", "Duniailkom")
print(uta)

print('\n',type(foo))
print( type(uta), '\n')


#update
foo[0] = 'Latihan'
print(foo)

uta[0] = 'Latihan' #error karena isi data Tuple tidak bisa diubah

#cara akses/menampilkan sama dengan list
