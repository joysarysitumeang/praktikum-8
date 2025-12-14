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
