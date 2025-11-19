# PYTHON FUNCTION SESI 9

# nomor 4: fungsi untuk menampilkan bilangan ganjil yang kurang argumens

def bilangan(angka):
    for i in range (1,angka):
        if i % 2 != 0:
            print(i, end=", ")

bilangan(20)    




print()
# nomor 3: keterangan 

def nilai(n=0):
    if n <= 60:
        print(f"nilai {n} tidak lulus")
    elif n < 60 and n <= 100:
        print("lulus")   
    else:
        print("tidak diketahui")  

nilai(80)    




print()
#nomor 2 fungsi  bernama is_genap yangn menerima satu argumen : bilangan bulat

def is_genap(n):
    return n % 2 == 0

print(is_genap(2))






print()
#nomor 1 fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen : suhu dalam celcius 

def celcius_ke_fahrenheit(c):
    return (c*9/5) + 32 

print(celcius_ke_fahrenheit (0))
print(celcius_ke_fahrenheit (100))