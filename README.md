# praktikum8

## Latihan 1: Kalkulator Aman
Tujuan latihan ini adalah membuat program kalkulator sederhana yang mampu menangani tiga jenis kesalahan: input bukan angka (ValueError), pembagian dengan nol (ZeroDivisionError), dan operator yang tidak dikenal (raise Exception).

## Code Pemerograman Python (kalkulator_aman.py)
```py
def kalkulator_aman():
    
    try:
        
        num1_str = input("Masukkan angka pertama: ")
        num2_str = input("Masukkan angka kedua: ")
        operator = input("Masukkan operator (+, -, *, /): ")
        
        
        angka1 = float(num1_str)
        angka2 = float(num2_str)
        
     
        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            
            hasil = angka1 / angka2
        else:
            
            raise Exception("Operator tidak valid! Silakan gunakan +, -, *, atau /.")
            
        
        print(f"\nHasil dari {num1_str} {operator} {num2_str} = {hasil}")

    except ValueError:
        
        print("\nError: Input salah! Pastikan Anda memasukkan angka yang valid.")
        
    except ZeroDivisionError:

        print("\nError: Pembagian dengan nol tidak diperbolehkan.")
        
    except Exception as e:
        
        print(f"\nError Kustom: {e}")

kalkulator_aman()
```
## Penjelasan Pemerograman
Konsep yang Diterapkan:

1. ```try-except ValueError```: Untuk menangani kasus di mana pengguna memasukkan teks atau karakter yang tidak bisa diubah menjadi angka (misalnya, pengguna mengetik "lima" bukan 5).

2. ```try-except ZeroDivisionError```: Untuk menangani kasus pembagian yang tidak valid secara matematis, yaitu pembagian dengan angka nol.

3. ```raise Exception```: Untuk membuat kesalahan kustom (custom error) ketika pengguna memasukkan operator yang tidak didukung oleh kalkulator (misalnya, ^), sehingga program dapat memberikan pesan kesalahan yang spesifik dan mudah dipahami.

Program ini menunjukkan prinsip EAFP (Easier to Ask for Forgiveness than Permission) di mana kode dicoba jalankan, dan jika gagal, program "meminta maaf" melalui blok except.

## Output (kalkulator_aman.py)
<img width="1919" height="1075" alt="Screenshot 2025-12-14 103135" src="https://github.com/user-attachments/assets/15d412c2-3875-4d38-a401-c104ec112596" />


---
## Latihan 2: Validasi Daftar Nilai
Tujuan latihan ini adalah menghitung rata-rata nilai dari sebuah list yang bercampur antara angka dan string (nilai = [80, 90, 'A', 70, 100, 'B']). Program harus menggunakan try-except di dalam loop untuk melewati data yang bukan angka tanpa menghentikan program.

## code pemerograman Python (validasi_daftar_nilai.py)
```py
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
```
## Penjelasan Pemerograman
Konsep yang Diterapkan:

1. Iterasi (```for loop```): Program harus memproses setiap elemen dalam list secara berurutan.

2. ```try-except``` dalam Loop: Setiap item di dalam list dicoba untuk diubah menjadi angka (dengan ```float()``` atau ```int()```).

3. Penanganan ```ValueError```: Jika item berupa string ('A', 'B'), konversi akan gagal dan memicu ```ValueError```. Blok ```except``` akan menangkap error ini, mencatat item sebagai tidak valid, dan kemudian program melanjutkan ke item berikutnya di dalam list tanpa crash.

Hasil akhirnya adalah perhitungan rata-rata yang akurat, hanya menggunakan data nilai yang valid (berupa angka).

## Output (validasi_daftar_nilai.py)
<img width="1918" height="1064" alt="Screenshot 2025-12-14 103717" src="https://github.com/user-attachments/assets/c3ab0199-8313-4acc-a6c7-21510e5e8833" />
