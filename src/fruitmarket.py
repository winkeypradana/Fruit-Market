from tabulate import tabulate

def show(database, title='Daftar Buah Tersedia'):
    #define header
    header = database [0]
    data = database [1:]
    
    #showtable
    print(tabulate(data, header, tablefmt="outLine"))

def add(database):
    # input buah baru
    name = input('Input nama buah: ').capitalize()
    stock = int(input('Input stock buah:'))
    price = int (input('Input harga buah:'))
    index = len(database) -1 

    # update database
    database = database.append([
        index, name, stock, price
    ])
    return database

def delete (database):
    # input index
    index = int(input('Input indeks buah yang akan dihapus:'))

    # hapus buah berdasarkan index
    for i, val in enumerate (database[1:]):
        if index == val [0]:
            del database [i+1]
            break
        elif index > len(database) - 1:
            print('Buah yang dicari tidak ada')
            break
    
    # update indeks buah
    for i, val in enumerate (database[1:]):
        database[i+1][0] = i

    return database

# Input jumlah buah
def input_fruit(name, stock, price):
    while True:
        n = int(input(f'Input jumlah {name.capitalize()}: '))
        if n <= stock:
            total_price = n * price
            break
        else:
            print(f'Jumlah terlalu banyak. {name.capitalize()} sisa stock {stock}')
    return total_price, n

def buy(database):
    cart = []
    while True:
        print("Buah yang tersedia:")
        for i, item in enumerate(database[1:]):
            print(f"{item[0]}. {item[1]} (stock: {item[2]}, harga: {item[3]})")
        
        try:
            index = int(input("Masukkan indeks buah yang ingin dibeli: "))
            selected_fruit = database[index+1]
            total_price, qty = input_fruit(selected_fruit[1], selected_fruit[2], selected_fruit[3])
        except ValueError:
            print("Mohon masukkan angka yang valid.")
            continue

        if index < 0 or index >= len(database) - 1:
            print("Indeks tidak valid.")
            continue

        if database[index+1][2] < qty:
            print(f"Stock {database[index+1][1]} tinggal {database[index+1][2]}")
            continue
        
        cart.append([selected_fruit[1], qty, selected_fruit[3], total_price])
        
        # Update stock in the database
        database[index+1][2] -= qty
        
        print("\nIsi Cart:")
        print("|".join(["Nama", "Qty", "Harga"]))
        for item in cart:
            print(f"{item[0]} | {item[1]} | {item[2]}")
        
        ans = input("\nMau beli yang lain? (ya/tidak): ")
        
        if ans.lower() != 'ya':
            break
    
    total_cost = 0
    print("\nDaftar Belanja:")
    print("|".join(["Nama", "Qty", "Harga", "Total Harga"]))
    for item in cart:
        total_cost += item[3]
        print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")

    # Tampilkan total yang harus dibayar
    print(f"\nTotal Yang Harus Dibayar: Rp.{total_cost}")
    while True:
        try:
            payment = int(input('\nSilahkan masukan nominal uang untuk membayar : '))
        except ValueError:
            print("Mohon masukkan angka yang valid.")
            continue
        
        if payment < total_cost:
            print(f'Maaf jumlah kekurangan yang anda harus bayar adalah Rp.{total_cost - payment}')
        elif payment > total_cost:
            change = payment - total_cost
            print(f'Terimakasih, berikut jumlah kembaliannya Rp.{change}')
            break
        else:
            print('Uang anda pas, Terimakasih')
            break





