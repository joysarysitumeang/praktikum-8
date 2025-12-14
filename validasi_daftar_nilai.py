def hitung_rata_rata_valid():
    
    nilai = [80, 90, 'A', 70, 100, 'B'] 
    
    total_nilai_valid = 0
    jumlah_nilai_valid = 0
    
    print(f"Daftar Nilai Awal: {nilai}\n")
    
    for item in nilai:
        try:
            
            nilai_angka = float(item)
            
            total_nilai_valid += nilai_angka
            jumlah_nilai_valid += 1
            print(f"Data valid: {nilai_angka}")
            
        except ValueError:
            
            print(f"Data tidak valid ditemukan: '{item}'. Data dilewati.")
            
    if jumlah_nilai_valid > 0:
        rata_rata = total_nilai_valid / jumlah_nilai_valid
        print("-" * 30)
        print(f"Total nilai yang valid: {total_nilai_valid}")
        print(f"Jumlah data valid: {jumlah_nilai_valid}")
        print(f"Rata-rata nilai valid adalah: {rata_rata:.2f}") 
    else:
        print("\nTidak ada data nilai yang valid untuk dihitung rata-ratanya.")

hitung_rata_rata_valid()
