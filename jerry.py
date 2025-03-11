# TASK ALGORITMA 1
# NAMA : JERRRY HERNIS
# NIM  : 2409075014

print ('================================')
print ('Indeks Nilai Kelulusan Mahasiswa')
print ('================================')

nilai = int(input ('Masukkan Nilai : '))

# Membuat Kondisi(Statement)
if nilai >= 91:
    na = 'A'
elif nilai >= 86:
    na = 'A-'
elif nilai >= 81:
    na = 'B+'
elif nilai >= 76:
    na = 'B'
elif nilai >= 71:
    na = 'B-'
elif nilai >= 66:
    na = 'C+'
elif nilai >= 61:
    na = 'C'
elif nilai >= 56:
    na = 'C-'
elif nilai >= 51:
    na = 'D+'
elif nilai >= 46:
    na = 'D'
elif nilai >= 41:
    na = 'D-'
else:
    na = 'E'
print ('Indeks : ' + na)

# Membuat Kondisi (Statement) Kedua
if nilai >= 71:
    deks = 'Selamat - Anda Lulus'
else:
    deks = 'Maaf - Anda Tidak Lulus'
print ('Status : ' + deks)