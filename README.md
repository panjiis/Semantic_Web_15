-----

# 📜 Web Streamlit Bhuwana Kosa

## 👥 Anggota

  * 140810220011 Panji Iman Sujatmiko
  * 140810220009 Muhammad Wildan Kamil
  * 140810220062 Drias Ameliano Kevin David

Aplikasi web Streamlit untuk mengeksplorasi naskah **Bhuwana Kosa**:

  * 🔎 **Mode Pencarian** – mencari klausa berdasarkan transliterasi (Latin), Aksara Devanagari, atau terjemahan Bahasa Indonesia.
  * 🧠 **Mode SPARQL Manual** – menulis dan menjalankan query SPARQL terhadap dataset Fuseki Anda.

-----

## ⚙️ Instalasi dan Menjalankan Proyek Lokal

Berikut adalah panduan langkah demi langkah untuk menyiapkan server basis data RDF (Apache Jena Fuseki) dan menjalankan aplikasi web Streamlit di komputer lokal Anda.

### 1\. Instalasi dan Penggunaan Apache Jena Fuseki

Apache Jena Fuseki adalah server SPARQL yang akan berfungsi sebagai basis data untuk menyimpan dan melayani data RDF dari naskah Bhuwana Kosa.

**Prasyarat:** Pastikan Anda telah menginstal **Java Development Kit (JDK)** versi 8 atau yang lebih baru. Anda dapat memeriksa versi Java dengan membuka terminal atau command prompt dan mengetik:

```bash
java -version
```

**Langkah-langkah Instalasi:**

1.  **Unduh Apache Jena Fuseki**

      * Buka halaman unduhan resmi Apache Jena: [https://jena.apache.org/download/](https://jena.apache.org/download/)
      * Cari versi stabil terbaru dari `apache-jena-fuseki-x.x.x.zip` (atau `.tar.gz` untuk Linux/macOS).
      * Unduh dan ekstrak file tersebut ke direktori pilihan Anda.

2.  **Siapkan Data Naskah**

      * Salin berkas data naskah `bhuwana_kosa.ttl` ke dalam folder yang mudah diakses. Disarankan untuk menempatkannya di dalam folder hasil ekstraksi Fuseki, misalnya dalam sub-folder `data/`.

3.  **Jalankan Server Fuseki**

      * Buka terminal atau command prompt dan navigasikan ke dalam direktori Fuseki yang telah Anda ekstrak (misalnya, `cd apache-jena-fuseki-x.x.x`).
      * Jalankan server sambil memuat data `bhuwana_kosa.ttl` Anda. Perintah berikut akan membuat dataset bernama `/bhuwana-kosa` yang dapat diakses dan diperbarui:

    <!-- end list -->

    ```bash
    # Ganti 'path/to/bhuwana_kosa.ttl' dengan lokasi file Anda
    # Contoh untuk Windows (jika file ada di folder 'data'): .\fuseki-server.bat --file=data\bhuwana_kosa.ttl --update /bhuwana-kosa
    # Contoh untuk Linux/macOS: ./fuseki-server --file=data/bhuwana_kosa.ttl --update /bhuwana-kosa
    ```

      * Server akan berjalan dan menampilkan log di terminal. Fuseki secara default berjalan di port **3030**.

4.  **Verifikasi Server**

      * Buka browser web dan kunjungi **[http://localhost:3030](https://www.google.com/search?q=http://localhost:3030)**.
      * Anda akan melihat panel kontrol web Fuseki. Pastikan dataset `/bhuwana-kosa` muncul dalam daftar dataset yang aktif.

### 2\. Menjalankan Aplikasi Web Streamlit

Setelah server Fuseki berjalan dan melayani data naskah, Anda dapat menjalankan aplikasi antarmuka pengguna.

1.  **Instalasi Dependensi Python**

      * Pastikan Anda memiliki Python 3 di sistem Anda.
      * Buka terminal baru (biarkan terminal Fuseki tetap berjalan) dan jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

    <!-- end list -->

    ```bash
    pip install streamlit SPARQLWrapper pandas
    ```

2.  **Jalankan Aplikasi**

      * Navigasikan ke direktori tempat Anda menyimpan berkas `app.py`.
      * Jalankan perintah berikut di terminal:

    <!-- end list -->

    ```bash
    streamlit run app.py
    ```

3.  **Buka Aplikasi di Browser**

      * Setelah perintah dijalankan, browser Anda akan otomatis terbuka dan mengarah ke alamat aplikasi, biasanya **[http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)**.
      * Jika tidak terbuka otomatis, buka alamat tersebut secara manual di browser Anda.

> **Penting** Aplikasi `app.py` mengharapkan endpoint SPARQL berada di `http://localhost:3030/bhuwana-kosa/sparql`. Pastikan server Fuseki Anda berjalan dengan nama dataset yang benar. Jika berbeda, ubah variabel `FUSEKI_ENDPOINT_URL` di dalam berkas `app.py`.

-----

## 🗌 Navigasi

Gunakan **sidebar** untuk berpindah halaman:

| Menu Sidebar             | Tujuan                                                 |
| -------------------------- | ------------------------------------------------------ |
| **🔎 Pencarian Kata** | Pencarian kata kunci (Latin, Aksara, atau Terjemahan)  |
| **🧠 Query SPARQL Manual** | Editor SPARQL manual penuh                             |

-----

## 🔎 Cara Melakukan Pencarian (Pencarian Kata)

1. Buka halaman **🔎 Pencarian Kata**.
2. Ketikkan kata atau frasa dalam **Latin**, **Aksara Devanagari**, *atau* **Terjemahan Bahasa Indonesia**.

   * Contoh:

     * `sang` (Latin)
     * `संग` (Aksara)
     * `bumi` (Terjemahan)
3. Tekan **Enter**.
4. Baca hasil: setiap string yang cocok akan ditandai dengan warna **oranye**.
5. Klik **“Unduh data sebagai CSV”** untuk menyimpan tabel (highlight akan dihapus).

| Kolom                  | Deskripsi                                |
| ---------------------- | ---------------------------------------- |
| Judul Bab (Terjemahan) | Judul bab dalam Bahasa Indonesia         |
| No. Bab                | Nomor bab                                |
| Judul Bab (Asli)       | Judul bab asli (Sanskrit)                |
| No. Klausa             | Nomor klausa                             |
| Aksara                 | Klausa dalam Aksara Devanagari           |
| Latin                  | Transliterasi                            |
| Terjemahan Klausa      | Terjemahan klausa dalam Bahasa Indonesia |

---

## 🧠 Cara Menjalankan SPARQL Manual (Query SPARQL Manual)

1. Buka halaman **🧠 Query SPARQL Manual**.
2. Sebuah query contoh telah diisi sebelumnya. Ubah atau sunting sesuai kebutuhan.
3. Klik **“Jalankan Query”**.
4. Hasil akan muncul dalam bentuk tabel yang dapat diurutkan dan digulir.
5. Unduh hasil dengan **“Unduh hasil sebagai CSV”**.

### Contoh Query

<details>
<summary>Daftar judul bab (10 baris)</summary>

```sparql
PREFIX bk: <http://contoh.org/bhuwanakosa#>
SELECT ?nomorBab ?judulBab
WHERE {
  ?bab a bk:Bab ;
       bk:nomorBab ?nomorBab ;
       bk:judulBab ?judulBab .
}
ORDER BY ?nomorBab
LIMIT 10
```

</details>

<details>
<summary>Temukan semua klausa yang mengandung “sang” dalam transliterasi</summary>

```sparql
PREFIX bk: <http://contoh.org/bhuwanakosa#>
SELECT ?nomorBab ?nomorKlausa ?latin
WHERE {
  ?klausa a bk:Klausa ;
          bk:nomorKlausa ?nomorKlausa ;
          bk:transliterasiLatin ?latin ;
          bk:bagianDariBab ?bab .
  ?bab bk:nomorBab ?nomorBab .
  FILTER CONTAINS(LCASE(?latin), "sang")
}
ORDER BY ?nomorBab ?nomorKlausa
```

</details>

---

## 🖼️ Tampilan Antarmuka

![Tampilan Pencarian Aksara Devanagari Bhuwana Kosa](https://drive.google.com/uc?export=view\&id=1wPjktqKrHUvcpa6cMTidfGYGkB_CIsbz)

![Tampilan Pencarian Transliterasi Latin Bhuwana Kosa](https://drive.google.com/uc?export=view\&id=10WTZdMpCWxPGAl8Y6Pt9KtJ4FyUbrAnF)

![Tampilan Pencarian Terjemahan Bahasa Indonesia Bhuwana Kosa](https://drive.google.com/uc?export=view\&id=1dlXtXdtkNNnpl03ToHAbmS2x9e8tJkfr)

![Tampilan Input Query Bhuwana Kosa](https://drive.google.com/uc?export=view\&id=19jFikk0bQScfCD2SYmFdqnmGntbdh3Vf)

---

