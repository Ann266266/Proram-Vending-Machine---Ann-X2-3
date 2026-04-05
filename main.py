menu = {}
def hitung(harga,uang,menu,pilihan):
    if uang < harga:
            print("Uang sudah tidak cukup")
            return uang
    else:
        uang -= harga
        if pilihan in menu:
            menu[pilihan][0] += 1
            menu[pilihan][1] += harga
        else:
            menu[pilihan] = [0,0]
            menu[pilihan][0] = 1
            menu[pilihan][1] = harga
        return uang
    
def cek(uang,menu):
    print("----------------")
    print("Total belanja:")
    for x in menu:
        print(f"{x} : {menu[x][0]}")
    print("----------------")
    print(f"Sisa uang: {uang}")

def bill(uang,menu):
    print("-----------------------------------------")
    print("BILL:")
    for x in menu:
        print(f"{x}  {menu[x][0]}x : {menu[x][1]}") 
    print("-----------------------------------------")
    print(f"KEMBALIAN: {uang}")

def pilih(uang):
    
    while True:
        try:
            pilih = int(input("Pilih menu:"))
        except:
            print("Error: Pilihan harus berupa angka")
        if pilih == 1:
            pilihan = "Fanta"
            harga = 7000
            uang = hitung(harga,uang,menu,pilihan)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang,menu)
                break
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
                
        elif pilih == 2:
            pilihan = "Teh Pucuk"
            harga = 5000
            uang = hitung(harga,uang,menu,pilihan)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang,menu)
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
        elif pilih == 3:
            pilihan = "Air Aqua"
            harga = 3000
            uang = hitung(harga,uang,menu,pilihan)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang,menu)
                break
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
        elif pilih == 4:
            pilihan = "Nescafe"
            harga = 10000
            uang = hitung(harga,uang,menu,pilihan)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang,menu)
                break
            elif keluar == "y":
                continue
            else:
                print("Error: pilihan harus berupa y / n")
        elif pilih == 5:
            pilihan = "Indomilk"
            harga = 7500
            uang = hitung(harga,uang,menu,pilihan)
            cek(uang,menu)
            keluar = input("Mau menambah?(y/n):")
            if keluar == "n":
                bill(uang,menu)
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
    except:
        print("Plihan harus berupa angka")
    print("[PILIH MENU]")
    print("1. FANTA Rp 7.000")
    print("2. TEH PUCUK Rp 5.000")
    print("3. AIR AQUA Rp 3.000")
    print("4. NESCAFE Rp 10.000")
    print("5. INDOMILK Rp 7.500")
    pilih (uang)
    
#Kalau ada kekurangan tolong kasih saran pak :)
