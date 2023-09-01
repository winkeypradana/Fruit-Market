
# Input jumlah buah
def input_fruit (name, stock, price):
    while True:
        n = int(input(f'Input jumlah {name.capitalize()}: '))
        if n <= stock:
            price = n * price
            break
        else:
            print (f'Jumlah terlalu banyak. {name.capitalize()} sisa stock {stock}')
    return price, n
  
# Stock buah
sApel = 20
sJeruk = 40
sAnggur = 60

# Init harga
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

# Hitung harga per buah
totalPriceApel, nApel = input_fruit('Apel',sApel,priceApel)
totalPriceJeruk, nJeruk = input_fruit('Jeruk',sJeruk,priceJeruk)
totalPriceAnggur, nAnggur = input_fruit('Anggur',sAnggur,priceAnggur)

# Hitung harga total buah
priceTotal = totalPriceAnggur + totalPriceApel + totalPriceJeruk

# show
print (
    f'''
Detail Belanja

Apel : {nApel} x {priceApel} = Rp {totalPriceApel}
Jeruk : {nJeruk} x {priceJeruk} = Rp {totalPriceJeruk}
Anggur : {nAnggur} x {priceAnggur} = Rp {totalPriceAnggur}
Total : Rp {priceTotal}
'''
)

while True:
    npembayaran = (int(input('Silahkan masukan nominal uang untuk membayar: ')))
    selisihpembayaran = npembayaran - priceTotal
    if npembayaran < priceTotal:
        print (f'Maaf jumlah kekurangan yang anda harus bayar adalah: Rp. {selisihpembayaran}')
    elif npembayaran > priceTotal:
        print(f'Terimakasih, berikut jumlah kembaliannya:Rp. {selisihpembayaran}')
        break
    else:
        npembayaran == selisihpembayaran
        print(f'Terimakasih')
        break