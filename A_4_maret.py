
# Menerima beberapa input dalam satu baris
# nilai1, nilai2, nilai3 = input("Masukkan tiga nilai dipisahkan oleh spasi: ").split()

# # Menampilkan input nilai
# print("Nilai pertama: " + nilai1)
# print("Nilai kedua: " + nilai2)
# print("Nilai ketiga: " + nilai3)

# Konversi Data dari List to Tuple

# x= "Talita"
# y=list(x)
# print(y)


# OPERASI ARITMATIKA
# + (Penjumlahan)
# - (Pengurangan)
# * (Perkalian)
# / (Pembagian: float)
# // (Pembagian: integer)
# % (Sisa Pembagian (Modulus)) 
# ** (Pengkat)

# # Praktik
# x = 7
# y = 2
# print(x%y)


# OPERASI PERBANDINGAN
# x = 1000
# y = 100

# print(x<=y)


# x = 5
# print(bin(x))


# OPERASI IDENTITAS
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)   # True (b adalah alias dari a)
# print(a is c)   # False (walaupun isinya sama, ID objek berbeda)
# print(a is not c) # True


# OPERASI KEANGGOTAAN
# list_angka = [1, 2, 3, 4, 5]

# print(3 in list_angka)     # True
# print(6 not in list_angka) # True

# # Operasi keanggotaan pada string

# list_number = [100, 200, 384, 4049]
# print( 100 in list_number)

# fruits = ['apple', 'banana', 'orange', 'grape']

# # Memeriksa apakah 'banana' ada dalam list
# if 'es buah' not in fruits:
#     print("belum watktunya berbuka.")

# # Memeriksa apakah 'pear' tidak ada dalam list
# if 'pear' not in fruits:
#     print("Pear tidak ada dalam list buah-buahan.")


# a=10
# if(a>10):
#     print("Value of a is greater than 10")
# else :
#     print("Value of a is 10")


# # STATMENT 1
# JIKA A LEBIH BESAR DARI 10
# OUPUT: nilai lebih dari besar 10

# # STATMENT 2
# OUPUT: nilai lebih kecil dari 10

# OUTPUT TUGAS

def menentukan_nilai_lulus_berdasarkan_indeks (nilai_lulus):
    if 91 <= nilai_lulus <= 100:
        return "A"
    elif 86 <= nilai_lulus <= 90:
        return "A-"
    elif 81 <= nilai_lulus <= 85:
        return "B+"
    elif 76 <= nilai_lulus <= 80:
        return "B"
    elif 71 <= nilai_lulus <= 75:
        return "B-"
    elif 66 <= nilai_lulus <= 70:
        return "C+"
    elif 61 <= nilai_lulus <= 65:
        return "C"
    elif 56 <= nilai_lulus <= 60:
        return "C-"
    elif 51 <= nilai_lulus <= 55:
        return "D+"
    elif 46 <= nilai_lulus <= 50:
        return "D"
    elif 41 <= nilai_lulus <= 45:
        return "D-"
    else:
        return "E"
    
nilai_lulus = int(input("masukkan nilai"))
indeks = menentukan_nilai_lulus_berdasarkan_indeks(nilai_lulus)

if indeks in {"A", "A-", "B+", "B", "B-", "C+", "C", "C-"}:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print (f"Nilai Anda: {nilai_lulus}, Indeks: {indeks}, Status: {status}")