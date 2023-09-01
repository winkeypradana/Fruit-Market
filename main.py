# Stock buah
sApel = 20
sJeruk = 40
sAnggur = 60

# Init harga
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

# Input jumlah buah
while True:
    nApel = int(input('Input jumlah apel: '))
    if nApel <=sApel:
        break
    else:
        print(f'Stock apel yang tersedia hanya {sApel}')
while True:
    nJeruk = nJeruk = int(input('Input jumlah jeruk: '))
    if nJeruk <= sJeruk:
        break
    else: 
        print(f'Stock jeruk yang tersedia hanya {sJeruk}')
while True:
    nAnggur = int(input('Input jumlah anggur: '))
    if nAnggur <= sAnggur:
        break 
    else:
        print (f'Stock jeruk yang tersedia hanya {sAnggur}')


# Hitung harga per buah
totalPriceApel = nApel * priceApel
totalPriceJeruk = nJeruk * priceJeruk
totalPriceAnggur = nAnggur * priceAnggur

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