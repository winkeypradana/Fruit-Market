import fruitmarket as fm

# Init database
db= [
    ['index', 'nama', 'stock', 'harga'],
    [ 0, 'Apel', 20, 10000],
    [ 1, 'Jeruk', 15, 15000],
    [ 2, 'Anggur', 25, 20000],
]

#define prompt display
PROMPT ='''
Selamat datang di pasar buah

List menu:
1. Menampilkan daftar buah
2. Menambah buah
3. Menghapus buah
4. Membeli buah
5. Exit
'''

def main():
    while True:
        print(PROMPT)
        menu = int(input('> Silahkan pilih menu: '))

        if menu == 1:
            fm.show(db)
        elif menu == 2:
            fm.add(db)
        elif menu == 3:
            fm.delete(db)
        elif menu == 4:
            fm.buy(db)
        elif menu == 5:
            print('Terima kasih telah berbelanja!')
            break
        else:
            print('Menu tidak ada')

if __name__ == '__main__':
    main()

