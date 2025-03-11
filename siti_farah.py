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