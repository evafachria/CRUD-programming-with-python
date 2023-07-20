Data_Mahasiswa = [
    ['20180005','Banu Azandanu','Ekonomi',278,141],
    ['20190001','Fierda Mustari','Manajemen',465,141],
    ['20190002','Yayang Muhazir','Akuntansi',500,141],
    ['20190003','Atang Mendes','Akuntansi',244,120],
    ['20190004','Zalsa Lahira','Manajemen',540,141],
    ['20190005','Agista Bagja','Ekonomi',500,130],
    ['20190006','M. Dennis Ong','Ekonomi',400,141]   
]

def Sistem_Utama():
    print('''
Selamat Datang di Sistem Informasi Akademik Universitas XYZ

Pilihlah menu 1-7 sesuai dengan kebutuhan informasi Anda:

1. Melihat Data Mahasiswa
2. Menambah Data Mahasiswa
3. Memperbarui Data Mahasiswa
4. Menghapus Data Mahasiswa
5. Status Akademik Mahasiswa
6. Statistik Akademik Mahasiswa
7. Keluar Dari Sistem Informasi Akademik Universitas XYZ
    ''')

def template_database_0():
    print('\n===========================================================')
    print('DATA MAHASISWA FAKULTAS EKONOMI UNIVERSITAS XYZ')
    print('===========================================================\n')

    print('NPM\t\t|NAMA\t\t|PRODI\t\t|TOTAL MUTU\tTOTAL SKS')
    print('-------------------------------------------------------------------------')
    for Mahasiswa in Data_Mahasiswa:
        print(f'{Mahasiswa[0]}\t|{Mahasiswa[1]}\t|{Mahasiswa[2]}\t|{Mahasiswa[3]}\t\t|{Mahasiswa[4]}')

    print('\n***Total Mutu adalah total jumlah SKS × bobot nilai yang diperoleh Mahasiswa\n\n')

def template_database_1(Mahasiswa):
    print('NPM\t\t|NAMA\t\t|PRODI\t\t|TOTAL MUTU\t|TOTAL SKS\t')
    print('-----------------------------------------------------------------------')
    print(f"{Mahasiswa[0]}\t|{Mahasiswa[1]}\t|{Mahasiswa[2]}\t|{Mahasiswa[3]}\t\t|{Mahasiswa[4]}")

def syarat_kelulusan(Total_SKS, ipk):
    if Total_SKS < 141:
        status_akademik = "Belum Lulus"
        keterangan = "Jumlah SKS belum mencukupi."
    elif ipk < 2.0:
        status_akademik = "Belum Lulus"
        keterangan = "IPK kurang dari 2.0."
    elif 2.0 <= ipk < 3.0:
        status_akademik = "Lulus-Memuaskan"
        keterangan = "IPK di antara 2.0 dan 3.0."
    elif 3.0 <= ipk < 3.5:
        status_akademik = "Lulus-Sangat Memuaskan"
        keterangan = "IPK di antara 3.0 dan 3.5."
    else:
        status_akademik = "Lulus-Cumlaude"
        keterangan = "IPK di atas atau sama dengan 3.5."

    return status_akademik, keterangan
    
def Menu_Tampilan_Daftar_Mahasiswa():
    while True:
        Pilihan_menu = input('''
            Pilihlah menu berikut
            1. Menampilkan semua daftar mahasiswa
            2. Menampilkan daftar mahasiswa per individu
            3. Kembali ke menu utama
            Masukkan pilihan menu: ''')
        
        if Pilihan_menu == '1':
            if Data_Mahasiswa:
                template_database_0()
            else:
                print("Data mahasiswa kosong.\n")
    
        elif Pilihan_menu == '2':
            if Data_Mahasiswa:
                print("\n=== Cari Data Mahasiswa ===")
                NPM = input("Masukkan NPM mahasiswa yang ingin dicari: ")
                found = False
                for Mahasiswa in Data_Mahasiswa:
                    if Mahasiswa[0] == NPM:
                        template_database_1(Mahasiswa)
                        found = True
                        break
                if not found:
                    print(f"Data mahasiswa {NPM} tidak ditemukan.\n")
            else:
                print("Data mahasiswa kosong.\n")
        
        elif Pilihan_menu == '3':
            break    
        
        else:
            print('Pilihan tidak valid')
    
def Menambah_Data_Mahasiswa():
    while True:
        Pilihan_menu = input('''
            Pilihlah menu berikut
            1. Menambah data mahasiswa
            2. Kembali ke menu utama
            Masukkan pilihan menu: ''')
        
        if Pilihan_menu == '1':
            found = False
            print("=== Tambah Data Mahasiswa ===")
            while True:
                NPM = input("Masukkan NPM mahasiswa: ")
                if NPM.isdigit() and int(NPM) >=20170001 and int(NPM) <=20199999:
                    break
                else:
                    print('NPM harus berisi angka saja dan dimulai dari angkatan 2017 sampai 2019.')
                    print('Perhatikan jumlah inputan setelah tahun angkatan. Tidak melebihi 9999 Mahasiswa\n')
            for Mahasiswa in Data_Mahasiswa:
                if Mahasiswa[0] == NPM:
                    found = True
                    break
            if found:
                print('\nNPM SUDAH TERDAFTAR. TAMBAHKAN DATA NPM MAHASISWA DENGAN NILAI BERBEDA.\n')
                continue  
            else:
                while True:
                    Nama = input("Masukkan Nama Mahasiswa: ")
                    Nama = Nama.title()
                    if Nama.replace(' ', '').replace('.', '').replace("'", '').isalpha():
                        break
                    else:
                        print("Nama harus berisi huruf, spasi, titik, dan tanda apostrof saja.")
                                    
                while True:
                    Prodi = input("Masukkan Program Studi Mahasiswa: ")
                    Prodi = Prodi.capitalize()
                    if Prodi in ["Manajemen", "Akuntansi", "Ekonomi"]:
                        break
                    else:
                        print("Masukan Program Studi Yang Sesuai")
                
                while True:
                    Total_Mutu = input("Masukkan Total Mutu: ")
                    if Total_Mutu.isdigit() and int(Total_Mutu) > 0 and int(Total_Mutu) <=564:
                        break
                    else:
                        print("Total mutu harus berisi bilangan bulat lebih dari 0 sampai 564.")
                Total_Mutu = int(Total_Mutu)

                while True:
                    Total_SKS = input("Masukkan Total SKS: ")
                    if Total_SKS.isdigit() and int(Total_SKS) > 0 and int(Total_SKS) <=141:
                        break
                    else:
                        print("Total SKS harus berisi bilangan bulat lebih dari 0 sampai 141.")
                Total_SKS = int(Total_SKS)
                  
                Mahasiswa = [NPM, Nama, Prodi, Total_Mutu, Total_SKS]
                template_database_1(Mahasiswa)
                            
                simpan = (input('\n\tSimpan Data (YA/TIDAK) : ')).lower()
                if simpan == 'ya':
                    Data_Mahasiswa.append(Mahasiswa)
                    print("\n\nData mahasiswa berhasil ditambahkan.\n")
                elif simpan=='tidak':
                    print("\n\nData mahasiswa tidak ditambahkan.\n")
                else:
                    print('Pilihan tidak valid')
                       
                    
        elif Pilihan_menu == '2':        
            break
        
        else:
            print('Pilihan tidak valid')

def Memperbarui_Data_Mahasiswa():
    while True:
        print('''
            Pilihlah menu berikut
            1. Memperbarui data mahasiswa
            2. Kembali ke menu utama
        ''')

        Pilihan_menu = input("Masukkan pilihan menu: ")

        if Pilihan_menu == '1':
            if not Data_Mahasiswa:
                print("Database mahasiswa kosong. Tidak ada data untuk diperbarui.\n")
            else:
                print("=== Memperbarui Data Mahasiswa ===")
                while True:
                    NPM = input("Masukkan NPM mahasiswa: ")
                    if NPM.isdigit() and int(NPM) >=20170001 and int(NPM) <=20199999:
                        break
                    else:
                        print('NPM harus berisi angka saja dan dimulai dari angkatan 2017 sampai 2019.')
                        print('Perhatikan jumlah inputan setelah tahun angkatan. Tidak melebihi 9999 Mahasiswa\n')

                found = False
                
                for Mahasiswa in Data_Mahasiswa:
                    if Mahasiswa[0] == NPM:
                        template_database_1(Mahasiswa)
                        Nama = ""
                        NPM_Baru = ""
                        Prodi = ""
                        Total_Mutu = ""
                        Total_SKS = ""
                        while True:
                            lanjut_perbarui = input('\n\tLanjutkan Memperbarui Data (YA/TIDAK) : ').lower()
                            if lanjut_perbarui == 'ya':                             
                                data_ubah = input('Masukkan item data yang ingin diubah (NPM/NAMA/PRODI/TOTAL MUTU/TOTAL SKS): ').lower()
                                if data_ubah == 'npm':
                                    while True:
                                        NPM_Baru = input('Masukkan NPM Mahasiswa Baru: ')
                                        if NPM_Baru.isdigit() and NPM_Baru not in [mhs[0] for mhs in Data_Mahasiswa] and int(NPM) >=20170001 and int(NPM) <=20199999:
                                            break
                                        else:
                                            print("NPM sudah terdaftar atau harus berisi angka saja. Masukkan NPM yang berbeda.")
                                elif data_ubah == 'nama':
                                    while True:
                                        Nama= input('Masukkan Nama Mahasiswa Baru: ')
                                        Nama= Nama.title()
                                        if Nama.replace(' ', '').replace('.', '').replace("'", '').isalpha():                                            
                                            break
                                        else:
                                            print("Nama harus berisi huruf, spasi, titik, dan tanda apostrof saja.")
                                elif data_ubah == 'prodi':
                                    while True:
                                        Prodi= input('Masukkan Prodi Mahasiswa Baru: ')
                                        Prodi= Prodi.capitalize()
                                        if Prodi in ["Manajemen", "Akuntansi", "Ekonomi"]:
                                            break
                                        else:
                                            print("Masukkan Program Studi Yang Sesuai")
                                elif data_ubah == 'total mutu':
                                    while True:
                                        Total_Mutu= input('Masukkan Total Mutu Baru: ')
                                        if Total_Mutu.isdigit() and int(Total_Mutu) > 0 and int(Total_Mutu) <=564:
                                            break
                                        else:
                                            print("Total mutu harus berisi bilangan bulat lebih dari 0 sampai 564.")  
                                    Total_Mutu = int(Total_Mutu)     
                                elif data_ubah == 'total sks':
                                    while True:
                                        Total_SKS= input('Masukkan Total SKS Baru: ')
                                        if Total_SKS.isdigit() and int(Total_SKS) > 0 and int(Total_SKS) <=141:
                                            break
                                        else:
                                            print("Total SKS harus berisi bilangan bulat lebih dari 0 sampai 141.") 
                                    Total_SKS = int(Total_SKS)                                    
                                else:
                                    print("Data yang ingin diubah tidak valid.")
                                    continue
                        

                                while True:
                                    perbarui = input('\n\tApakah Anda yakin ingin mengubah data (YA/TIDAK) : ').lower()
                                    if perbarui == 'ya':
                                        if NPM_Baru != "":
                                            Mahasiswa[0] = NPM_Baru
                                        elif Nama != "":
                                            Mahasiswa[1] = Nama                                    
                                        elif Prodi != "":
                                            Mahasiswa[2] = Prodi
                                        elif Total_Mutu != "":
                                            Mahasiswa[3] = Total_Mutu
                                        elif Total_SKS!= "":
                                            Mahasiswa[4] = Total_SKS

                                        print("\n\nData mahasiswa berhasil diperbarui.\n")
                                        break
                                    elif perbarui == 'tidak':
                                        print("\n\nData mahasiswa tidak diperbarui.\n")
                                        break
                                    else:
                                        print('Pilihan tidak valid.')
                                break

                            elif lanjut_perbarui == 'tidak':
                                print("\n\nData mahasiswa tidak diperbarui.\n")
                                break
                            else:
                                print('Pilihan tidak valid')

                        found = True
                        break

                if not found:
                    print('\nNPM TIDAK DITEMUKAN. MASUKAN DATA NPM MAHASISWA DENGAN NILAI BERBEDA.\n')
        elif Pilihan_menu == '2':
            break
        else:
            print('Pilihan tidak valid')

def Status_akademik():
    while True:
        Pilihan_menu = input('''
            Pilihlah menu berikut
            1. Menampilkan status kelulusan mahasiswa
            2. Menampilkan status kelulusan mahasiswa per individu
            3. Memfilter Mahasiswa berdasarkan status kelulusan 
            4. Kembali ke menu utama
            Masukkan pilihan menu: ''')
        
        if Pilihan_menu == '1':
            if Data_Mahasiswa:
                print("=== Status Akademik Mahasiswa ===")
                print('NPM\t\t|NAMA\t\t|PRODI\t\t|TOTAL SKS\t|IPK\t|STATUS AKADEMIK\t\t|KETERANGAN')
                print('-----------------------------------------------------------------------------------------------------------------------------------')
                for Mahasiswa in Data_Mahasiswa:
                    [NPM, Nama, Prodi, Total_Mutu, Total_SKS]=Mahasiswa
                    ipk = Total_Mutu / Total_SKS
                    status_akademik = ""
                    keterangan = ""
                    
                    status_akademik,keterangan =syarat_kelulusan(Total_SKS, ipk)
                    
                    print(f'{NPM}\t|{Nama}\t|{Prodi}\t|{Total_SKS}\t\t|{ipk:.2f}\t|{status_akademik}\t\t\t|{keterangan}')     
            else:
                print("Data mahasiswa kosong.\n")
    
        elif Pilihan_menu == '2':
            if Data_Mahasiswa:
                print("=== Cari Data Mahasiswa ===")
                NPM_cari = input("Masukkan NPM mahasiswa yang ingin Anda cari: ")
                found=False
                for Mahasiswa in Data_Mahasiswa:
                    [NPM, Nama, Prodi, Total_Mutu, Total_SKS] = Mahasiswa
                    if NPM == NPM_cari:
                        found = True
                        ipk = Total_Mutu / Total_SKS
                        status_akademik = ""
                        keterangan = ""

                        status_akademik,keterangan =syarat_kelulusan(Total_SKS, ipk)
                        
                        print("=== Data Mahasiswa ===")
                        print('NPM\t\t|NAMA\t\t|PRODI\t\t|TOTAL SKS\t|IPK\t|STATUS AKADEMIK\t\t|KETERANGAN\t\t')
                        print('----------------------------------------------------------------------------------------------------------------------')
                        print(f'{NPM}\t|{Nama}\t|{Prodi}\t|{Total_SKS}\t\t|{ipk:.2f}\t|{status_akademik}\t\t|{keterangan}')
                        break

                if not found:
                    print(f"Mahasiswa dengan NPM {NPM_cari} tidak ditemukan.")

            else:
                print("Data mahasiswa kosong.\n")

        elif Pilihan_menu == '3':
            if Data_Mahasiswa:
                status_input = input("Masukkan status kelulusan yang ingin Anda cari (Cumlaude, Lulus-Sangat Memuaskan, Lulus-Memuaskan, atau Belum Lulus.): ")
                found = False
                
                print("=== Data Mahasiswa ===")
                print('NPM\t\t|NAMA\t\t|PRODI\t\t|TOTAL SKS\t|IPK\t|STATUS AKADEMIK\t\t|KETERANGAN\t\t')
                print('----------------------------------------------------------------------------------------------------------------------')

                for Mahasiswa in Data_Mahasiswa:
                    [NPM, Nama, Prodi, Total_Mutu, Total_SKS] = Mahasiswa
                    ipk = Total_Mutu / Total_SKS
                    status_akademik = ""
                    keterangan = ""

                    status_akademik,keterangan =syarat_kelulusan(Total_SKS, ipk)

                    if status_input.lower() in status_akademik.lower():
                        
                        found = True
                
                        print(f'{NPM}\t|{Nama}\t|{Prodi}\t|{Total_SKS}\t\t|{ipk:.2f}\t|{status_akademik}\t\t|{keterangan}')
                        
                if not found:
                    print(f"Mahasiswa dengan status kelulusan '{status_input}' tidak ditemukan.")
            else:
                print("Data mahasiswa kosong.\n")

        elif Pilihan_menu == '4':
            break    
        
        else:
            print('Pilihan tidak valid')    

def Statistik_akademik():
    
    total_mahasiswa = len(Data_Mahasiswa)

    ipk = [mhs[3] / mhs[4] for mhs in Data_Mahasiswa]
    ipk_tertinggi = max(ipk) if ipk else 0
    ipk_terendah = min(ipk) if ipk else 0

    status_kelulusan = [syarat_kelulusan(mhs[4], ipk)[0] for mhs, ipk in zip(Data_Mahasiswa, ipk)]
    jumlah_lulus = status_kelulusan.count("Lulus-Cumlaude") + status_kelulusan.count("Lulus-Sangat Memuaskan") + status_kelulusan.count("Lulus-Memuaskan")
    jumlah_tidak_lulus = status_kelulusan.count("Belum Lulus")
    persentase_lulus = (jumlah_lulus / total_mahasiswa) * 100 if total_mahasiswa > 0 else 0
    persentase_tidak_lulus = (jumlah_tidak_lulus / total_mahasiswa) * 100 if total_mahasiswa > 0 else 0
    
    persentase_cumlaude = (status_kelulusan.count("Lulus-Cumlaude") / total_mahasiswa) * 100 if total_mahasiswa > 0 else 0
    persentase_sangat_memuaskan = (status_kelulusan.count("Lulus-Sangat Memuaskan") / total_mahasiswa) * 100 if total_mahasiswa > 0 else 0
    persentase_memuaskan = (status_kelulusan.count("Lulus-Memuaskan") / total_mahasiswa) * 100 if total_mahasiswa > 0 else 0
    persentase_belum_lulus = (status_kelulusan.count("Belum Lulus") / total_mahasiswa) * 100 if total_mahasiswa > 0 else 0

    print("\n=== Statistik Akademik ===\n")
    print("\n======================================================================")
    print(f"Total Mahasiswa: {total_mahasiswa}")
    print(f"IPK Tertinggi: {ipk_tertinggi:.2f}")
    print(f"IPK Terendah: {ipk_terendah:.2f}")
    print(f"Jumlah Mahasiswa Berdasarkan Status Kelulusan:")
    print(f"  - Lulus-Cumlaude: {status_kelulusan.count('Lulus-Cumlaude')}")
    print(f"  - Lulus-Sangat Memuaskan: {status_kelulusan.count('Lulus-Sangat Memuaskan')}")
    print(f"  - Lulus-Memuaskan: {status_kelulusan.count('Lulus-Memuaskan')}")
    print(f"  - Belum Lulus: {status_kelulusan.count('Belum Lulus')}")
    print(f"Persentase Mahasiswa yang Lulus: {persentase_lulus:.2f}%")
    print(f"Persentase Mahasiswa yang Tidak Lulus: {persentase_tidak_lulus:.2f}%")
    print(f"  - Cumlaude: {persentase_cumlaude:.2f}%")
    print(f"  - Sangat Memuaskan: {persentase_sangat_memuaskan:.2f}%")
    print(f"  - Memuaskan: {persentase_memuaskan:.2f}%")
    print(f"  - Belum Lulus: {persentase_belum_lulus:.2f}%")
    print("======================================================================\n\n")

def Menghapus_Data_Mahasiswa():
    while True:
        Pilihan_menu = input('''
            Pilihlah menu berikut
            1. Menghapus data mahasiswa
            2. Kembali ke menu utama
            Masukkan pilihan menu: ''')
        
        if Pilihan_menu == '1':
            if not Data_Mahasiswa:
                print("Database mahasiswa kosong. Tidak ada data untuk dihapus.\n")
            else:
                found = False
                print("=== Hapus Data Mahasiswa ===")
                while True:
                    NPM = input("Masukkan NPM mahasiswa yang ingin dihapus (hanya angka): ")
                    if NPM.isdigit():
                        break
                    else:
                        print("NPM harus berisi angka saja.")

                for Mahasiswa in Data_Mahasiswa:
                    if Mahasiswa[0] == NPM:
                        found = True
                        template_database_1(Mahasiswa)

                        hapus = (input('\n\thapus Data (YA/TIDAK) : ')).lower()
                        if hapus == 'ya':
                            Data_Mahasiswa.remove(Mahasiswa)
                            print("\n\nData mahasiswa berhasil dihapus.\n")
                        elif hapus == 'tidak':
                            print("\n\nData mahasiswa tidak dihapus.\n")
                        else:
                            print('Pilihan tidak valid')
                        break

                if not found:
                    print('\nNPM TIDAK DITEMUKAN. MASUKAN DATA NPM MAHASISWA DENGAN NILAI BERBEDA.\n')
            
        elif Pilihan_menu == '2':
            break
        
        else:
            print('Pilihan tidak valid')
    
def sistem():
    while True:
        Sistem_Utama()
        Pilihan_Sistem = input('Pilihlah sistem yang ingin dijalankan : ')
        if Pilihan_Sistem == '1':
            Menu_Tampilan_Daftar_Mahasiswa()
        elif Pilihan_Sistem == '2':
            Menambah_Data_Mahasiswa()
        elif Pilihan_Sistem == '3':
            Memperbarui_Data_Mahasiswa()
        elif Pilihan_Sistem == '4':
            Menghapus_Data_Mahasiswa()
        elif Pilihan_Sistem == '5':
            Status_akademik()
        elif Pilihan_Sistem == '6':
            Statistik_akademik()            
        elif Pilihan_Sistem == '7':
            print('========================================================================')
            print('Terima Kasih Telah Menggunakan Sistem Informasi Akademik Universitas XYZ')
            print('========================================================================')
            break
        else:
            print('=======================================================')
            print('PILIHAN TIDAK ADA DALAM MENU SISTEM, MOHON COBA KEMBALI')
            print('=======================================================')

sistem()