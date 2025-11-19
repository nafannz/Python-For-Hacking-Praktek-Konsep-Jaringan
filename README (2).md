# TCP vs UDP vs BGP --- Penjelasan & Langkah Running

## 1. Apa itu TCP?

TCP (Transmission Control Protocol) adalah protokol komunikasi yang
menjamin **kehandalan**, **urutan paket**, dan **koneksi yang stabil**
antara pengirim dan penerima.\
TCP digunakan ketika data harus sampai dengan benar tanpa kehilangan,
seperti: - Web browsing (HTTP/HTTPS) - Email (SMTP) - File transfer
(FTP/SFTP)

### Ciri-ciri TCP:

-   Connection-oriented (harus handshake terlebih dahulu)
-   Reliable (mengirim ulang paket yang hilang)
-   Data berurutan
-   Lebih lambat karena banyak pengecekan

------------------------------------------------------------------------

## 2. Apa itu UDP?

UDP (User Datagram Protocol) adalah protokol komunikasi yang **tidak
menjamin kehandalan**, **tidak menjamin urutan paket**, tetapi **cepat**
dan ringan.\
UDP digunakan saat kecepatan lebih penting daripada akurasi, seperti: -
Video streaming - Voice call - Gaming online - DNS query

### Ciri-ciri UDP:

-   Connectionless (tanpa handshake)
-   Tidak reliable
-   Tidak berurutan
-   Sangat cepat

------------------------------------------------------------------------

## 3. Apa itu BGP?

BGP (Border Gateway Protocol) adalah **routing protocol** yang digunakan
pada jaringan internet berskala besar (antar ISP).\
Berbeda dari TCP/UDP yang dipakai untuk mengirim data aplikasi, BGP
digunakan oleh router untuk: - Menentukan jalur terbaik ke jaringan
lain - Mengatur routing antar Autonomous System (AS) - Menjaga
stabilitas internet global

### Ciri-ciri BGP:

-   Termasuk Exterior Gateway Protocol (EGP)
-   Menggunakan TCP port 179 untuk pertukaran routing
-   Stabil, scalable, dan mampu mengatur ratusan ribu rute

------------------------------------------------------------------------

## 4. Perbedaan TCP, UDP, dan BGP

  --------------------------------------------------------------------------------------
  Protokol   Fungsi       Keandalan    Koneksi               Kecepatan    Penggunaan
  ---------- ------------ ------------ --------------------- ------------ --------------
  **TCP**    Pengiriman   Reliable     Connection-oriented   Lebih lambat Web, Email,
             data                                                         File
             aplikasi                                                     

  **UDP**    Pengiriman   Unreliable   Connectionless        Sangat cepat Streaming,
             data cepat                                                   VoIP, Game

  **BGP**    Routing      Reliable     Connection-oriented   Lambat tapi  ISP, router
             antar        (via TCP)                          stabil       internet
             jaringan                                                     
             besar                                                        
  --------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 5. Langkah Menjalankan TCP

### **1. Jalankan TCP Server**

    python3 tcpServer.py

Jika berhasil, akan muncul:

    Server running at 127.0.0.1:12346

### **2. Jalankan TCP Client**

Buka terminal baru:

    python3 tcpSocket.py

Masukkan pesan → server akan mengirim balasan.

------------------------------------------------------------------------

## 6. Langkah Menjalankan UDP

### **1. Jalankan UDP Server**

    python3 UdpServer.py

Output:

    UDP server running at 127.0.0.1:12346

### **2. Jalankan UDP Client**

Buka terminal baru:

    python3 UdpSocket.py

Masukkan pesan → server membalas versi uppercase.

------------------------------------------------------------------------

## 7. Langkah Commit ke GitHub

    git init
    git add .
    git commit -m "Add TCP & UDP codes + README"
    git branch -M main
    git remote add origin <url-repo-kamu>
    git push -u origin main

------------------------------------------------------------------------

## Selesai 🎉

File README ini sudah siap untuk di-commit ke GitHub.
