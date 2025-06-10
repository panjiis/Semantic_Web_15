import streamlit as st
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import re

# 🔶 Highlight kata pencarian (case-insensitive, dengan mempertahankan huruf asli)
def highlight_search(text, keyword):
    if not text or not keyword:
        return text
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    highlighted_text = pattern.sub(lambda m: f":orange[{m.group(0)}]", text)
    return highlighted_text

# 🔍 Jalankan query SPARQL pencarian otomatis
def get_sparql_results(search_term, fuseki_url):
    sparql = SPARQLWrapper(fuseki_url)
    query = f"""
    PREFIX bk: <http://contoh.org/bhuwanakosa#>
    PREFIX dct: <http://purl.org/dc/terms/>

    SELECT ?judul ?nomorBab ?judulBab ?nomorKlausa ?aksara ?latin ?terjemahan
    WHERE {{
      ?bab a bk:Bab ;
           bk:judulBab ?judulBab ;
           bk:nomorBab ?nomorBab ;
           bk:terjemahanJudul ?judul ;
           bk:memilikiKlausa ?klausa .

      ?klausa a bk:Klausa ;
              bk:nomorKlausa ?nomorKlausa ;
              bk:aksaraDevanagari ?aksara ;
              bk:transliterasiLatin ?latin ;
              bk:terjemahan ?terjemahan .

      FILTER(
        CONTAINS(LCASE(?latin), LCASE("{search_term}")) ||
        CONTAINS(LCASE(?terjemahan), LCASE("{search_term}")) ||
        CONTAINS(LCASE(?aksara), LCASE("{search_term}"))
      )
    }}
    ORDER BY ?nomorBab ?nomorKlausa
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    try:
        results = sparql.query().convert()
        return results["results"]["bindings"]
    except Exception as e:
        st.error(f"Error querying SPARQL endpoint: {e}")
        return []

# 🧾 Ubah hasil SPARQL menjadi DataFrame dengan highlight
def process_results_for_table(sparql_results, keyword):
    processed_data = []
    if not sparql_results:
        return pd.DataFrame()

    for item in sparql_results:
        latin_text = item.get("latin", {}).get("value", "N/A")
        terjemahan_text = item.get("terjemahan", {}).get("value", "N/A")
        aksara_text = item.get("aksara", {}).get("value", "N/A")

        row = {
            "Judul Bab (Terjemahan)": item.get("judul", {}).get("value", "N/A"),
            "No. Bab": item.get("nomorBab", {}).get("value", "N/A"),
            "Judul Bab (Asli)": item.get("judulBab", {}).get("value", "N/A"),
            "No. Klausa": item.get("nomorKlausa", {}).get("value", "N/A"),
            "Aksara": highlight_search(aksara_text, keyword),
            "Latin": highlight_search(latin_text, keyword),
            "Terjemahan Klausa": highlight_search(terjemahan_text, keyword)
        }
        processed_data.append(row)

    return pd.DataFrame(processed_data)

# 🔧 Konfigurasi halaman utama
st.set_page_config(page_title="Naskah Bhuwana Kosa", layout="wide")
FUSEKI_ENDPOINT_URL = "http://localhost:3030/bhuwana-kosa/sparql"

# 📄 Navigasi halaman
page = st.sidebar.selectbox("Pilih Halaman", ["🔎 Pencarian Kata", "🧠 Query SPARQL Manual"])

# -------------------------------------------
# 🔎 Halaman 1: Pencarian kata
# -------------------------------------------
if page == "🔎 Pencarian Kata":
    st.title("📜 Pencarian Naskah Bhuwana Kosa (Latin, Aksara & Terjemahan)")
    st.caption("Cari isi Bhuwana Kosa berdasarkan transliterasi Latin, Aksara Devanagari, atau terjemahan klausa.")

    search_query = st.text_input("Masukkan kata kunci (Latin, Aksara, atau Terjemahan):", value="")

    if search_query:
        st.info(f"Mencari hasil untuk kata: *{search_query}*")
        raw_results = get_sparql_results(search_query, FUSEKI_ENDPOINT_URL)

        if raw_results:
            df_results = process_results_for_table(raw_results, search_query)
            st.success(f"Ditemukan {len(df_results)} hasil:")
            st.markdown(df_results.to_markdown(index=False), unsafe_allow_html=True)

            @st.cache_data
            def convert_df_to_csv(df):
                df_clean = df.copy()
                for col in ["Aksara", "Latin", "Terjemahan Klausa"]:
                    df_clean[col] = df_clean[col].str.replace(r":orange\[(.*?)\]", r"\1", regex=True)
                return df_clean.to_csv(index=False).encode('utf-8')

            csv = convert_df_to_csv(df_results)
            st.download_button(
                label="Unduh data sebagai CSV",
                data=csv,
                file_name=f'bhuwana_kosa_search_{search_query}.csv',
                mime='text/csv',
            )
        else:
            st.warning("Tidak ada hasil yang ditemukan.")
    else:
        st.info("Masukkan kata kunci untuk mulai mencari.")

# -------------------------------------------
# 🧠 Halaman 2: SPARQL Manual
# -------------------------------------------
elif page == "🧠 Query SPARQL Manual":
    st.title("🧠 Jalankan Query SPARQL Manual")
    st.caption("Tulis dan jalankan query SPARQL secara langsung ke endpoint Fuseki.")

    default_query = """PREFIX bk: <http://contoh.org/bhuwanakosa#>
SELECT ?judulBab ?aksara
WHERE {
  ?bab a bk:Bab ;
       bk:judulBab ?judulBab ;
       bk:memilikiKlausa ?klausa .
  ?klausa bk:aksaraDevanagari ?aksara .
}
LIMIT 10"""

    manual_query = st.text_area("Tulis Query SPARQL di bawah ini:", value=default_query, height=300)

    if st.button("Jalankan Query"):
        sparql = SPARQLWrapper(FUSEKI_ENDPOINT_URL)
        sparql.setQuery(manual_query)
        sparql.setReturnFormat(JSON)

        try:
            results = sparql.query().convert()
            bindings = results["results"]["bindings"]

            if bindings:
                columns = results["head"]["vars"]
                rows = []
                for item in bindings:
                    row = [item.get(col, {}).get("value", "") for col in columns]
                    rows.append(row)

                df = pd.DataFrame(rows, columns=columns)
                st.success(f"Ditemukan {len(df)} hasil.")
                st.dataframe(df)

                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Unduh hasil sebagai CSV", data=csv, file_name="query_sparql_manual.csv", mime="text/csv")
            else:
                st.warning("Query berhasil, tetapi tidak ada hasil ditemukan.")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat menjalankan query: {e}")
