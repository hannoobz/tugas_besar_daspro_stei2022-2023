# tugas_besar_daspro_stei2022-2023

### Anggota Kelompok :
##### M. Hanief Fatkhan Nashrullah
##### Filbert Fuvian
##### Muhammad Raihan Ariffianto

--------------------------------

## Deskripsi Persoalan
Tugas besar ini meminta untuk membuat sebuah program yang menirukan
sebuah sistem manajerial pembangunan candi pada cerita rakyat Roro Jonggrang.
Bandung Bondowoso memiliki misi untuk membangun 100 candi, sedangkan Roro
Jonggrang memiliki misi untuk mencegah pembangunan 100 candi selesai. Jika candi
mencapai jumlah lebih atau sama dengan 100 kemudian ayam berkokok, maka
Bandung Bondowoso berhasil menyelesaikan misinya. Jika candi belum mencapai
jumlah 100 dan ayam sudah berkokok, maka Roro Jonggrang berhasil menyelesaikan
misinya. Dalam pembangunan candi, diperlukan bahan bangunan dan juga jin.
Terdapat jin pengumpul yang bertugas mengumpulkan bahan bangunan dan jin
pembangun yang bertugas membangun candi. Tugas besar ini meminta untuk
memasukkan persoalan tersebut ke dalam sebuah program

Program ini memiliki 16 fitur utama, yaitu :

1. Login

Sebuah fungsi untuk autentikasi data dan akses dari pengguna.
Pengguna akan diminta untuk memasukkan username dan password yang
sesuai. Fungsi ini harus dapat mengidentifikasi pengguna berdasarkan
username dan memberikan akses terhadap fungsi lain sesuai dengan role yang
ada pada username yang sama. Setelah fungsi ini dijalankan, maka pengguna
dapat terlogin dan mengakses fungsi lain sesuai rolenya. Fungsi ini dapat
dijalankan tanpa role khusus.

2. Logout

Sebuah fungsi untuk keluar dari akses pengguna. Fungsi ini hanya
dapat berjalan ketika sudah terlogin. Setelah fungsi ini dijalankan, akses dari
fungsi yang memerlukan suatu role spesifik akan ditarik atau dengan kata lain
terlogout. Fungsi dapat dijalankan tanpa role khusus.

3. Summon Jin

Fungsi ini dijalankan untuk memanggil jin. Terdapat dua jenis jin yang
dapat dipanggil, yaitu jin pengumpul dan jin pembangun. Jumlah maksimal
dari jin yang dapat dipanggil adalah 100. Jika jumlah jin yang dipanggil telah
mencapai 100, fungsi ini tidak dapat memanggil jin lagi sampai jin yang ada
kurang dari 100. Fungsi ini hanya dapat diakses oleh Bandung Bondowoso.

4. Hilangkan Jin

Fungsi ini dijalankan untuk menghapus jin. Pengguna akan diminta
untuk memasukkan username dari jin yang akan dihapus. Jika username tidak
ada, maka fungsi akan menampilkan pesan bahwa tidak ada jin dengan
username tersebut. Jika username ada, maka pengguna akan diminta
konfirmasi untuk menghapus jin. Jika dikonfirmasi, makan jin akan terhapus
dan tidak jika sebaliknya. Fungsi ini hanya dapat diakses oleh Bandung
Bondowoso.

5. Ubah Tipe Jin

Fungsi ini dijalankan untuk mengubah tipe jin. Pengguna akan diminta
untuk memasukkan username dari jin yang akan diubah tipenya. Jika
username tidak ada, maka fungsi akan menampilkan pesan bahwa tidak ada jin
dengan username tersebut. Jika username ada, maka jin akan diubah tipenya.
Jika jin yang diubah bertipe pembangun, maka jin akan menjadi bertipe
pengumpul. Berlaku juga sebaliknya. Fungsi ini hanya dapat diakses oleh
Bandung Bondowoso.

6. Jin Pembangun

Fungsi ini merupakan fungsi untuk membangun candi. Syarat agar
fungsi ini dapat berjalan adalah terdapat bahan bangunan tersedia. Jika bahan
bangunan tidak cukup, maka candi tidak akan terbangun. Sebaliknya, jika
kondisi terpenuhi, candi akan terbangun. Fungsi ini hanya dapat diakses oleh
Jin Pembangun.

7. Jin Pengumpul

Fungsi ini merupakan fungsi untuk mengumpulkan bahan bangunan. Ketika
dijalankan, fungsi akan menambah bahan bangunan yang tersedia. Fungsi ini
hanya dapat diakses oleh Jin Pengumpul.

8. Batch Bangun/Kumpul

Bagian ini terdiri atas dua fungsi, yaitu batch bangun dan batch
kumpul. Sesuai dengan namanya, fungsi tersebut menjalankan fungsi bangun
atau fungsi kumpul secara “batch”. Jika batch bangun dijalankan, maka setiap
jin yang ada masing-masing membangun satu candi. Jika batch kumpul
dijalankan, maka setiap jin pengumpul akan mengumpulkan bahan bangunan.
Syarat agar fungsi ini bisa berjalan adalah adanya jin untuk masing masing
bagian. Jika tidak ada jin pengumpul, maka batch kumpul tidak bisa
dijalankan. Berlaku juga untuk batch bangun. Fungsi ini hanya dapat diakses
oleh Bandung Bondowoso.

9. Ambil Laporan Jin

Prosedur ini digunakan untuk mengambil laporan mengenai kinerja
dari para jin. Prosedur ini hanya dapat diakses oleh Bandung Bondowoso.

10. Ambil Laporan Candi

Prosedur ini digunakan untuk mengambil laporan progress dari pembangunan
candi. Prosedur ini hanya dapat diakses oleh Bandung Bondowoso.

11. Hancurkan Candi

Fungsi ini digunakan untuk menghancurkan candi. Fungsi ini akan
meminta ID dari candi yang akan dihancurkan. Jika sudah dihancurkan, maka
candi akan hilang dari data sementara dan akan hilang permanen jika prosedur
save dijalankan.

12. Ayam Berkokok

Prosedur ini digunakan untuk mengakhiri permainan. Jika candi yang
terbangun sudah mencapai 100, maka Bandung Bondowoso akan
memenangkan permainan ketika prosedur ini dijalankan. Jika candi yang
terbangun belum mencapai 100, maka Roro Jonggrang yang akan
memenangkan permainan ketika prosedur ini dijalankan. Prosedur ini hanya
dapat diakses oleh Roro Jonggrang.

13. Load

Prosedur ini digunakan untuk memuat file data eksternal ke dalam
permainan. Pengguna akan diminta sebuah argument berupa nama folder atau
directory dari file yang akan dimuat. Jika argumen tidak diberikan, maka
program akan menampilkan cara penggunaan Load dan keluar dari program.
Jika argument folder yang diberikan tidak ada, maka akan dikeluarkan pesan
bahwa folder tidak ada dan kemudian keluar dari program. Jika folder ada,
maka program akan memuat file eksternal dan menjalankan program utama.

14. Save

Prosedur ini digunakan untuk menyimpan data dari permainan ke file
data eksternal. Pengguna akan diminta nama folder yang akan digunakan
sebagai tempat penyimpanan dari file yang akan disimpan. Jika folder tidak
ada, maka folder akan dibuat, ditampilkan pesan folder telah dibuat, dan file
tersimpan di folder tersebut. Jika folder sudah ada dan kosong, maka file akan
disimpan ke folder tersebut. Jika folder sudah ada dan file data eksternal sudah
ada dalam folder tersebut, maka file yang ada akan di-overwrite oleh file data
yang akan disimpan. Prosedur ini tidak memerlukan role akses khusus.

15. Help

Prosedur ini digunakan untuk menampilkan bantuan perintah apa saja
yang tersedia untuk setiap role yang bersesuaian. Prosedur ini tidak
memerlukan role akses khusus.

16. Exit

Prosedur ini digunakan untuk keluar dari program. Pengguna akan diminta
konfirmasi apakah ingin menyimpan data permainan atau tidak. Jika iya, akan
dijalankan prosedur save dan kemudian keluar dari program. Jika tidak, maka
program akan langsung keluar. Prosedur ini tidak memerlukan role akses
khusus.
