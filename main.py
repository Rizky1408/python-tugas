import collections


print("1. Nomor 1\n2. Nomor 2\n3. Nomor 3\n4. Nomor 4")
pilihan = int(input("Masukan Pilihan :"))

if pilihan == 1:
    bilangan1 = int(input("Masukan Bilangan 1 :"))
    bilangan2 = int(input("Masukan Bilangan 2 :"))
    bilangan3 = int(input("Masukan Bilangan 3 :"))

    if bilangan1 > bilangan2 & bilangan1 > bilangan3:
        print("Bilangan Terbesar = ", bilangan1)
    elif bilangan2  > bilangan1 & bilangan2 > bilangan3:
        print("Bilangan terbesar = ", bilangan2)
    else:
        print("Bilangan terbesar = ", bilangan3)
    

elif pilihan == 2:
    lst = []
    
    for i in range(3):
        masukan = int(input("masukan bilangan :"))
        lst.append(masukan)
        
    print("Bilangan yang sama",[item for item, count in collections.Counter(lst).items() if count > 1])
    
elif pilihan == 3:
    nama = input("Nama :") 
    tinggi = int(input("Tinggi :"))
    bd = tinggi - 100

    print("Saudara ", nama, "berat ideal anda adalah ",bd)
    

elif pilihan == 4:
    nama  = input("Nama :")
    tugas = float(input("Tugas :"))
    uts   = float(input("UTS   :"))
    uas   = float(input("UAS   :"))

    NA = (0.25 * tugas) + (0.35 * uts) + (0.4 * uas)
    
    print("\nData Nilai Mahasiswa")
    print("\nNama   : ", nama)
    print("Tugas    : ", tugas)
    print("UTS      : ", uts)
    print("UAS      : ", uas)
    
    if NA >= 75 and NA <= 100:
        grade = "A"
    elif NA >= 60 and NA < 70:
        grade = "B"
    elif NA >= 45 and NA < 60:
        grade = "C"
    elif NA < 45:
        grade = "D"
        
    print("\nNilai Akhir dan Grade")
    print("Nama         : ",nama)
    print("Nilai Akhir  : ", NA)
    print("Grade        : ",grade)
    
# elif pilihan == 5:
        
    
