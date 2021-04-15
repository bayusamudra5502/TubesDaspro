# Database
Program ini telah dilengkapi dengan penanganan database. Dokumentasi ini akan berbicara mengenai file pada folder `/src/core/database/`. Berikut ini adalah dokumentasi dari sistem database pada program ini.

## Struktur Data
Pada program ini, terdapat tiga struktur data penting yang berkaitan dengan database, diantaranya sebagai berikut:

### Database (DB)
Struktur data ini terdapat pada file `database.py`. Berikut ini adalah formatnya:

```python
db = {
    "data" : dict of (str, table),
    "tableName" : list of (str),
    "numTable" : int
}
```
Berikut ini penjelasan struktur data DB:
* Key `data` berisi semua data dari berbagai tabel yang ada pada DB. Key ini berisi dictionary dengan key merupakan nama tabel. Nama tabel sendiri diambil dari nama file dari database yang telah diimportkan.
* Key `tableName` merupakan kumpulan nama tabel dari database yang diimportkan.
* Key `numTable` merupakan jumlah tabel yang berhasil diimport.

### Table
Struktur data ini terdapat pada file `load.py`. Struktur data ini merupakan nilai yang dikembalikan oleh fungsi `getTable()`.Struktur data ini merupakan hasil konversi dari sebuah file dalam folder yang berisikan seluruh file `.csv`. Berikut struktur  datanya:

```python
table = {
    "data" : list of (row),
    "columnName" : list of (str),
    "row_number" : int,
    "col_number" : int
}
```
Berikut ini adalah keterangan dari struktur data diatas:
* Key `data` berisi semua struktur data row pada tabel. Dalam python row sendiri merupakan sebuah `dict`.
* Key `columnName` berisi nama-nama key (yang berperan sebagai nama kolom) pada struktur data row.
* Key `row_number` menyatakan jumlah baris pada tabel. Nilai ini akan sama dengan `len(table["data"])`.
* Key `col_number` menyatakan jumlah kolom pada tabel. NIlai ini akan sama dengan `len(table["columnName"])`.

### Row
Struktur data ini terddapat pada file `load.py`. Struktur data ini berada pada struktur data table. Struktur data ini dalam python merupakan sebuah dictionary dengan key berupa nama kolom dan nilainya berisi nilai di file csv. Nama kolom yang diambil adalah nama kolom yang sama pada file csv yang diimport.

## Fungsi
Berikut ini adalah beberapa fungsi penting yang terdapat pada database:

### getTable
Berikut ini adalah prototipe dari fungsi diatas (dalam python):
```python
def getTable(name:str) -> dict
```
getTable menerima sebuah name yang merupakan nama dari tabel pada database. Nama tabel adalah nama file tanpa ekstensi. Misal nama file `consumable_history.csv` akan diimport dalam database dengan nama tabel `consumable_history`.

Fungsi ini akan mengembalikan sebuah dict yang merupakan struktur data tabel yang telah dijelaskan diatas.

Fungsi ini hanya boleh dijalankan bila database sudah diload dengan fungsi `loadDatabase()`. Hal ini sudah dilakukan pada awal program dijalankan.

### applyChange
Berikut ini adalah prototipe dari fungsi applyChange (dalam python):

```python
def applyChange(changedTable : dict, tableName:str)
```
applyChange akan menyimpan perubahan pada database. Parameter changeTable merupakan struktur data `table` yang diambil dengan menggunakan fungsi `getTable()` yang telah diubah. tableName merupakan nama tabel  yang dimaksud. Nama tabel harus sama dengan nama file tanpa ekstensi seperti pada `getTable()`.

FUngsi ini harus dijalankan setelah melakukan perubahan pada table agar tersimpan pada struktur data database.

## Contoh
### Contoh 1
Berikut ini adalah contoh dari implementasi struktur data diatas.
Sebagai contoh berikut ini merupakan file `user.csv`:
```csv
id;username;nama;alamat;password;role
P1;admin;administrator;Bandung;07a7b9.34a67df2bc69277c;admin
P2;user;pengguna;Bandung;07a7b9.34a67df2bc69277c;user
```

Bila file diatas saja yang diload, struktur data db akan berbentuk seperti berikut:
```python
db = {
    "data" : {
        "user": {...}
    },
    "columnName" : ["user"],
    "numTable" : 1
}
```

Bila dijalankan `getTable("user")`, akan didapatkan table user akan berbentuk seperti berikut:
```python
dataUser = getTable("user")

# Bila dilihat, user akan berisi sebagai berikut:
dataUser = {
    "data" : [{
        "id" : "P1",
        "username" : "admin",
        "nama" : "administrator",
        "alamat" : "Bandung",
        "password" : "07a7b9.34a67df2bc69277c",
        "role" : "admin"
    },
    {
        "id" : "P2",
        "username" : "user",
        "nama" : "pengguna",
        "alamat" : "Bandung",
        "password" : "07a7b9.34a67df2bc69277c",
        "role" : "user"
    }],
    "columnName" : [
        "id","username","nama","alamat",
        "password","role"],
    "row_number" : 1,
    "col_number" : 6
}
```

Misalkan ingin diambil password user dengan id P2. karena user terrsebut berada pada indeks 1, maka pengaksesannya adalah sebagai berikut:
```python
    password = dataUser["data"][1]["password"]
```

Bila sudah melakukan perubahan pada tabel user diatas, jalankan:
```python
    applyChange(dataUser, "user")
```

### Contoh 2
Akan diubah data di `gadget.csv`:
```csv
id;nama;deskripsi;jumlah;rarity;tahun_ditemukan
G1;Time Machine;Mesin waktu doremonangis;123;A;2099
G2;Bamboo Propeller;Baling-baling bambu (buat terbang);12;A;2080
C1;Tahu Bulat;Digoreng dadakan;20;S;2121
```

Akan dijalankan perintah getTable
```python
dataGadget = getTable("gadget")
dataGadget = {
    "data" : [{
        "id" : "G1",
        "nama" : "Time Machine",
        "deskripsi" : "Mesin waktu doremonangis",
        "jumlah" : "123",
        "rarity" : "A",
        "tahun_ditemukan" : "2080"
    },
    {
        "id" : "G2",
        "nama" : "Bamboo Propeller",
        "deskripsi" : "Baling-baling bambu (buat terbang)",
        "jumlah" : "12",
        "rarity" : "A",
        "tahun_ditemukan" : "2080"
    },
    {
        "id" : "C1",
        "nama" : "Tahu Bulat",
        "deskripsi" : "Digoreng dadakan",
        "jumlah" : "20",
        "rarity" : "S",
        "tahun_ditemukan" : "2121"
    }],
    "columnName" : [
        "id","nama","deskripsi","jumlah",
        "rarity","tahun_ditemukan"],
    "row_number" : 3,
    "col_number" : 6
}
```

Misalkan, akan diubah Tahu bulat jumlahnya menjadi 29 dan Bamboo Propeller ditambah jumlahnya sebanyak 10.
```python
# Mengubah tahu bulat
jumlahBaru = 29
dataGadget["data"][2]["jumlah"] = str(jumlahBaru)

# Mengubah bamboo propeller
nilaiSebelumnya = int(dataGadget["data"][1]["jumlah"])
nilaiSebeumnya += 10
dataGadget["data"][1]["jumlah"] = str(nilaiSebelumnya)
```

Setelah melakukan hal diatas, lakukan applyChange
```python
applyChange(dataGadget,"gadget")
```