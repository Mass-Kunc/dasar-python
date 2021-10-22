#Format TipDat Dictionary 
#nama_variabel = { "key1": "value1", "key2": "value2", "key3": "value3" }
#menggunakan kurung Kurawal '{'  '}' atau constructor dict():

foo = { 1: "Belajar", 2: "Python", 3: "di rumah" }
print(type(foo)); print(foo)
print('\n')

uta = { 1: "Latihan", "apa": "Nendang", "berapa": 2, "dimana": "di sini" }
print(type(uta)); print(uta)
print('-----------------------')

#construct dict key string tanpa tanda petik dan menggunakan sama denga (=)
goo = dict (say = "Latihan",
            apa = "Nendang",
            berapa = 2,
            dimana= "di sini"
            )
print(goo)

print('-----------------------')


#nilai dari setiap element dict bisa terdiri berbagai tipe data
yui = { 1: 'Belajar',
        2: ['Pascal', 'Python', 'PHP'],  #tipdat List
        'Dimana?' : 'Rumah',
        'semangat' : True,  #boolean
        'target': 2020,     
        'riwayat sekolah': {    #tipdat dict
            'SD' : 'SDN ok',
            'SMP' : 'SMP ko',
            'SMA' : 'SMA okok'
            },
        'dengan' : ('presiden', 'ronaldo') #tipdat Tuple
        }
print(type(yui)) ; print(yui) ; print('\n')

print('Targetnya', yui['target'])

print('-----------')

#update
foo = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }
 
foo["kegiatan"] = "Value jadi Belajar Bahasa Pemrograman"
print(foo)

#tambah data
foo = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }

foo["target"] = 2020
print(foo)

#delete data
foo = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }
 
del foo["website"]
print(foo)
