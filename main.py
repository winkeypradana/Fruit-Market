# Init harga
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

# Input jumlah buah
nApel = int(input('Input jumlah apel: '))
nJeruk = int(input('Input jumlah jeruk: '))
nAnggur = int(input('Input jumlah anggur: '))

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

Apel : {nApel} x {priceApel}
Jeruk : {nJeruk} x {priceJeruk}
Anggur : {nAnggur} x {priceAnggur}
Total : {priceTotal}
'''
)