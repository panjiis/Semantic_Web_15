# 📜 Web Streamlit Bhuwana Kosa
anggota
- 140810220011	Panji Iman Sujatmiko
- 140810220009	Muhammad Wildan Kamil
- 140810220062	drias ameliano kevin david

A Streamlit web-app to explore the **Bhuwana Kosa** manuscript:

* 🔎 **Search Mode** – find clauses by transliteration (Latin), Aksara Devanagari, or Indonesian translation.
* 🧠 **Manual SPARQL Mode** – write and run any SPARQL query against your Fuseki dataset.

---

## 🚀 Quick start

```bash
# 1 – install dependencies
pip install streamlit SPARQLWrapper pandas

# 2 – ensure Fuseki is running
java -jar fuseki-server.jar --update --mem /bhuwana-kosa

# 3 – launch the app
streamlit run app.py
```

The browser opens at **[http://localhost:8501](http://localhost:8501)**.
If it doesn’t, open the address manually.

> **Important** `app.py` expects a SPARQL endpoint at
> `http://localhost:3030/bhuwana-kosa/sparql`.
> Edit `FUSEKI_ENDPOINT_URL` in `app.py` if you use a different host, port, or dataset name.

---

## 🗌 Navigation

Use the **sidebar** to switch pages:

| Sidebar item               | Purpose                                        |
| -------------------------- | ---------------------------------------------- |
| **🔎 Pencarian Kata**      | Keyword search (Latin, Aksara, or Translation) |
| **🧠 Query SPARQL Manual** | Full manual SPARQL editor                      |

---

## 🔎 How to search (Pencarian Kata)

1. Go to **🔎 Pencarian Kata**.
2. Type a word or phrase in **Latin**, **Aksara Devanagari**, *or* the **Indonesian translation**.

   * Examples:

     * `sang` (Latin)
     * `संग` (Aksara)
     * `bumi` (Translation)
3. Press **Enter**.
4. Read results: each matching string is highlighted in **orange**.
5. Click **“Unduh data sebagai CSV”** to save the table (highlight removed).

| Column                 | Description                       |
| ---------------------- | --------------------------------- |
| Judul Bab (Terjemahan) | Indonesian chapter title          |
| No. Bab                | Chapter number                    |
| Judul Bab (Asli)       | Original chapter title (Sanskrit) |
| No. Klausa             | Clause number                     |
| Aksara                 | Clause in Devanagari              |
| Latin                  | Transliteration                   |
| Terjemahan Klausa      | Indonesian translation            |

---

## 🧠 How to run manual SPARQL (Query SPARQL Manual)

1. Open **🧠 Query SPARQL Manual**.
2. A sample query is pre-filled. Replace or edit it.
3. Click **“Jalankan Query”**.
4. Results appear in a table; you can sort/scroll.
5. Download with **“Unduh hasil sebagai CSV”**.

### Example queries

<details>
<summary>List chapter titles (10 rows)</summary>

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
<summary>Find every clause containing “sang” in transliteration</summary>

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

