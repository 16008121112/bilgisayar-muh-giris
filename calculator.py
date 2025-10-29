def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "Hata: Sıfıra bölme yapılamaz."
    return a / b

def main():
    print("Basit Hesap Makinesi")
    print("İşlemler: +, -, *, /")

    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        islem = input("İşlem seçin (+, -, *, /): ")
        sayi2 = float(input("İkinci sayıyı girin: "))

        if islem == '+':
            print("Sonuç:", topla(sayi1, sayi2))
        elif islem == '-':
            print("Sonuç:", cikar(sayi1, sayi2))
        elif islem == '*':
            print("Sonuç:", carp(sayi1, sayi2))
        elif islem == '/':
            print("Sonuç:", bol(sayi1, sayi2))
        else:
            print("Geçersiz işlem seçtiniz.")

    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
