import sqlite3,datetime,prettytable
from prettytable import from_db_cursor
db = sqlite3.connect('datamhs.db')
cur = db.cursor()

# #untuk membuat table ke dalam database
# cur.execute('''CREATE TABLE Mahasiswa(NPM INTEGER PRIMARY KEY AUTOINCREMENT, Nama_Mhs TEXT,Prodi TEXT)''')
# cur.execute('''CREATE TABLE Presensi(No INTEGER PRIMARY KEY AUTOINCREMENT, NPM INTEGER, nama_Mhs TEXT,Matkul TEXT, Kehadiran TEXT,tanggal DATE)''')

# #untuk memasukkan data ke dalam Table Mahasiswa
# mhs = [(5210411351,'Lintang Dwi Cahya','Informatika'),
#         (5210411352,'Gilang Fathanatu Tantular','Informatika'),
#         (5210411353,'Muhammad Insan Kamil','Informatika'),
#         (5210411354,'Dandy Aurelio Pradana','Informatika'),
#        (5210411355,'Alfin Hasanul','Informatika')]
# sql = 'INSERT INTO Mahasiswa values(?,?,?)'
# for m in mhs:
#   cur.execute(sql,m)
#   db.commit()

#subprogram masuk/login
def masuk(npm):
  sql='SELECT * FROM Mahasiswa WHERE NPM='+ str(npm)
  cur.execute(sql)
  print('=========================')
  res=cur.fetchall()
  print(f'{res[0][0]:>17}')
  print(f'{res[0][1]:^25}')
  print(f'{res[0][2]:>18}')

  print('=========================')
  opsi()
npm=int(input('Masukkan NPM Anda : '))

#subprogram opsi/menu berisi presensi dan cek data kehadiran
def opsi():
  print('''==========OPSI==========
1. Presensi
2. Cek Data Kehadiran
===================''')
  while True:
    x = int(input('Pilihan: '))
    if x == 1:
      presensi()
      break
    elif x == 2:
      cek_data()
      break
    else:
      continue

#subprogram cek data kehadiran
def cek_data():
  cur.execute('SELECT * FROM Presensi')
  tp=from_db_cursor(cur)
  print(tp)
  

#subprogram untuk membaca dan mengambil data dari table Mahasiswa
def read(kolom,kunci,val):
  sql = 'SELECT '+kolom+' FROM Mahasiswa WHERE '+kunci+'='+str(val)+''
  cur.execute(sql)
  hasil = cur.fetchall()
  return hasil[0][0]

#subprogram untuk presensi Mahasiswa
def presensi():
  sql='INSERT INTO Presensi(NPM,Nama_Mhs,Matkul,Kehadiran,tanggal) VALUES(?,?,?,?,CURRENT_DATE)'
  print('''==========Mata Kuliah==========
1. Aplikasi Teknologi Informasi
2. Algoritma Pemrograman
3. Algoritma Pemrograman Praktik
4. Teknologi Berbasis Objek
5. Pengembangan Web
===================''')
  while True:
    Matkul = int(input('Pilih Matkul: '))
    if Matkul == 1:
      mk='Aplikasi Teknologi Informasi'
      jam=input('Presensi pada pukul : ')
      if jam > '10.40' and jam < '12.20' :
        hadir=input('Kehadiran : ')
        isi=(npm,read('Nama_Mhs','NPM',npm),mk,hadir)
        cur.execute(sql,isi)
        db.commit()
        break
      else: 
        print('Bukan Waktu Presensi, Waktu Presensi (10.40-12.20)')
      break
    elif Matkul == 2:
      mk='Algoritma Pemrograman'
      jam=input('Presensi pada pukul : ')
      if jam > '07.00' and jam < '09.30' :
        hadir=input('Kehadiran : ')
        isi=(npm,read('Nama_Mhs','NPM',npm),mk,hadir)
        cur.execute(sql,isi)
        db.commit()
        break
      else: 
        print('Bukan Waktu Presensi, Waktu Presensi (07.00-09.30)') 
      break
    elif Matkul == 3:
      mk='Algoritma Pemrograman Praktik'
      jam=input('Presensi pada pukul : ')
      if jam > '10.40' and jam < '14.40' :
        hadir=input('Kehadiran : ')
        isi=(npm,read('Nama_Mhs','NPM',npm),mk,hadir)
        cur.execute(sql,isi)
        db.commit()
        break
      else: 
        print('Bukan Waktu Presensi, Waktu Presensi (10.40-14.40)')
      break
    elif Matkul == 4:
      mk='Teknologi Berbasis Objek'
      jam=input('Presensi pada pukul : ')
      if jam > '14.40' and jam < '16.20' :
        hadir=input('Kehadiran : ')
        isi=(npm,read('Nama_Mhs','NPM',npm),mk,hadir)
        cur.execute(sql,isi)
        db.commit()
        break
      else: 
        print('Bukan Waktu Presensi, Waktu Presensi (14.40-16.20)')
      break
    elif Matkul == 5:
      mk='Pengembangan Web'
      jam=input('Presensi pada pukul : ')
      if jam > '16.30' and jam < '18.10' :
        hadir=input('Kehadiran : ')
        isi=(npm,read('Nama_Mhs','NPM',npm),mk,hadir)
        cur.execute(sql,isi)
        db.commit()
        break
      else: 
        print('Bukan Waktu Presensi, Waktu Presensi (16.30-18.10)')
      break
    else:
      continue
      

masuk(npm)
