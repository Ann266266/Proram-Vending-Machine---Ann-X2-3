menu = {}
def hitung(harga, uang, menu, pilihan, total_belanja):
    if uang < harga:
        print("Uang sudah tidak cukup")
        return uang, total_belanja
    else:
        uang -= harga
        total_belanja += harga

        if pilihan in menu:
            menu[pilihan][0] += 1
            menu[pilihan][1] += harga
        else:
            menu[pilihan] = [1, harga]

        return uang, total_belanja
    
def cek(uang,menu):
    print("----------------")
    print("Total belanja:")
    for x in menu:
        print(f"{x} : {menu[x][0]}")
    print("----------------")
    print(f"Sisa uang: {uang}")

def bill(uang, menu, total_belanja):
    print("-----------------------------------------")
    print("BILL:")
    for x in menu:
        print(f"{x}  {menu[x][0]}x : {menu[x][1]}") 
    print("-----------------------------------------")
    print(f"TOTAL: {total_belanja}")
    print(f"KEMBALIAN: {uang}")

def pilih(uang, total_belanja):
    
    while True:
        try:
            pilih = int(input("Pilih menu:"))
        except:
            print("Error: Pilihan harus berupa angka")
        if pilih == 1:
            pilihan = "Fanta"
            harga = 7000
            uang, total_belanja = hitung(harga, uang, menu, pilihan, total_belanja)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang, menu, total_belanja)
                break
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
                
        elif pilih == 2:
            pilihan = "Teh Pucuk"
            harga = 5000
            uang, total_belanja = hitung(harga, uang, menu, pilihan, total_belanja)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang, menu, total_belanja)
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
        elif pilih == 3:
            pilihan = "Air Aqua"
            harga = 3000
            uang, total_belanja = hitung(harga, uang, menu, pilihan, total_belanja)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang, menu, total_belanja)
                break
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
        elif pilih == 4:
            pilihan = "Nescafe"
            harga = 10000
            uang, total_belanja = hitung(harga, uang, menu, pilihan, total_belanja)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang, menu, total_belanja)
                break
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
        elif pilih == 5:
            pilihan = "Indomilk"
            harga = 7500
            uang, total_belanja = hitung(harga, uang, menu, pilihan, total_belanja)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang, menu, total_belanja)
                break
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
        else:
            print("Error: Pilihan invalid")

            
        
        
while True:
    try:
        uang = int(input("Berapa Uangnya:"))
        total_belanja = 0
    except:
        print("Plihan harus berupa angka")
    print("[PILIH MENU]")
    print("1. FANTA Rp 7.000")
    print("2. TEH PUCUK Rp 5.000")
    print("3. AIR AQUA Rp 3.000")
    print("4. NESCAFE Rp 10.000")
    print("5. INDOMILK Rp 7.500")
    pilih(uang, total_belanja)
