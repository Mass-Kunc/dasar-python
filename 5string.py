#Spenulisan string
#tanda petik ('), petik 2 ("), (''')/(""")
#tanda petik 3  (''')/(""") dipakai untuk membuat multiline string

teks = 'OK coy'
teks2 = "0k coy coy"
teks3 = '''ok 3
bro
rock
0ooooooooooooooooo '''


print(teks, teks2)
print(teks3)

print("""Langsung print juga bisa""")

print('==========================')

# fungsi (\n) untuk pindah baris, fungsi (\t) untuk tab_paragraf
paragraf = '\t Awal'
enter = 'Kata pertama \n kata ke dua'

print(paragraf)
print(enter)
print('kata \t awal')

print('==============LATIHAN============')

print('''\t Awal tahun aku makan air putih.
Air Putih <> air tawar \n Benar kan?''')

print('\n\n')


#ARRAY = kumpulan tipe data yang saling terhubung
print(teks[0])

print(teks3[5])

print(teks[3:6])
