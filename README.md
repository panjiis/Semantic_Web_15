# 📜 Web Streamlit Bhuwana Kosa

## 👥 Anggota

* 140810220011 Panji Iman Sujatmiko
* 140810220009 Muhammad Wildan Kamil
* 140810220062 Drias Ameliano Kevin David

Aplikasi web Streamlit untuk mengeksplorasi naskah **Bhuwana Kosa**:

* 🔎 **Mode Pencarian** – mencari klausa berdasarkan transliterasi (Latin), Aksara Devanagari, atau terjemahan Bahasa Indonesia.
* 🧠 **Mode SPARQL Manual** – menulis dan menjalankan query SPARQL terhadap dataset Fuseki Anda.

---

## 🚀 Langkah Cepat

```bash
# 1 – instalasi dependensi
pip install streamlit SPARQLWrapper pandas

# 2 – pastikan Fuseki berjalan
java -jar fuseki-server.jar --update --mem /bhuwana-kosa

# 3 – jalankan aplikasi
streamlit run app.py
```

Browser akan terbuka di **[http://localhost:8501](http://localhost:8501)**.
Jika tidak terbuka otomatis, buka alamat tersebut secara manual.

> **Penting** `app.py` mengharapkan endpoint SPARQL di
> `http://localhost:3030/bhuwana-kosa/sparql`.
> Ubah `FUSEKI_ENDPOINT_URL` di `app.py` jika Anda menggunakan host, port, atau nama dataset yang berbeda.

---

## 🗌 Navigasi

Gunakan **sidebar** untuk berpindah halaman:

| Menu Sidebar               | Tujuan                                                |
| -------------------------- | ----------------------------------------------------- |
| **🔎 Pencarian Kata**      | Pencarian kata kunci (Latin, Aksara, atau Terjemahan) |
| **🧠 Query SPARQL Manual** | Editor SPARQL manual penuh                            |

---

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

