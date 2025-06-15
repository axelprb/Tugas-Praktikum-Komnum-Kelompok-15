import numpy as np
import matplotlib.pyplot as plt
from math import *

def regula_falsi():
    print("\nMETODE REGULA FALSI")
    print("------------------")
    print("Program untuk mencari akar persamaan non-linear")
    print("Dengan pendekatan iterasi garis potong\n")
    
    fungsi = input("Masukkan fungsi (gunakan x sebagai variabel, contoh: x**2 - 4): ")
    a = float(input("Masukkan batas bawah (a): "))
    b = float(input("Masukkan batas atas (b): "))
    toleransi = float(input("Masukkan toleransi error (contoh: 0.0001): ") or 0.0001)
    
    def f(x):
        return eval(fungsi)
    
    if f(a) * f(b) >= 0:
        print("\nError: Fungsi harus berbeda tanda di a dan b")
        print("Silakan coba interval lain yang memenuhi f(a)*f(b) < 0")
        return
    
    print("\nProses Iterasi Regula Falsi:")
    print("-" * 60)
    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'c':<10} {'f(c)':<12} {'Error':<12}")
    print("-" * 60)
    
    iterasi = 0
    while True:
        iterasi += 1
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)
        error = abs(fc)
        
        print(f"{iterasi:<5} {a:<10.6f} {b:<10.6f} {c:<10.6f} {fc:<12.6f} {error:<12.6f}")
        
        if error < toleransi:
            print("-" * 60)
            print("\nKonvergensi tercapai!")
            print(f"Akar persamaan ditemukan pada x = {c:.8f}")
            print(f"Nilai f({c:.8f}) = {fc:.8f}")
            print(f"Jumlah iterasi: {iterasi}")
            break
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    print("\nMembuat visualisasi grafik...")
    x = np.linspace(a-1, b+1, 400)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {fungsi}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.scatter(c, 0, color='red', s=100, label=f'Akar (x={c:.6f})')
    plt.title('Metode Regula Falsi: Visualisasi Fungsi dan Akar', pad=20)
    plt.xlabel('Nilai x', labelpad=10)
    plt.ylabel('Nilai f(x)', labelpad=10)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    regula_falsi()