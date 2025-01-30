import streamlit as st
import pandas as pd
import numpy as np

# Tytuł i nagłówek aplikacji
st.title("TEST1")

st.header("Krótka prezentacja danych")
st.write("""
Ta aplikacja pomoże Ci wytresować kazachów.
""")

# Suwak do wyboru liczby wierszy
num_rows = st.slider("Liczba wierszy danych do wygenerowania:", 5, 100, 10)

# Generowanie przykładowych danych (3 kolumny: X, Y, Z)
random_data = np.random.randn(num_rows, 3)
df = pd.DataFrame(random_data, columns=["X", "Y", "Z"])

# Wyświetlenie tabeli z danymi
st.write("Oto wygenerowane dane:")
st.dataframe(df)

# Dodaj przycisk, po którego kliknięciu narysujemy wykres liniowy
if st.button("Pokaż wykres liniowy"):
    st.write("**Wykres liniowy wartości X, Y oraz Z**")
    # Rysowanie wykresu liniowego – każda kolumna (X, Y, Z) będzie osobną linią
    st.line_chart(df)

st.write("#### Jak dalej rozbudować aplikację?")
st.write("""
- Możesz dodać filtrację danych przed wyświetleniem (np. wybór zakresu wartości).
- Dodaj wykres słupkowy lub inny rodzaj wykresu, by przedstawić przetworzone dane (np. średnie, sumy).
- Pozwól użytkownikowi wczytywać własne pliki (CSV/Excel) i wyświetlać ich zawartość.
- Wykorzystaj modele Machine Learning do predykcji i wizualizacji wyników.
""")
