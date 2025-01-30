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

# Generowanie przykładowych danych
random_data = np.random.randn(num_rows, 3)
df = pd.DataFrame(random_data, columns=["X", "Y", "Z"])

# Wyświetlenie tabeli z danymi
st.write("Oto wygenerowane dane:")
st.dataframe(df)

# Dodanie przycisku, który obliczy średnie i narysuje wykres
if st.button("Oblicz średnie i narysuj wykres"):
    mean_values = df.mean()
    
    st.write("Średnie wartości w kolumnach:")
    st.write(mean_values)  # wyświetlamy zwykłą tabelę/Series

    # Konwersja do DataFrame, aby można było wyświetlić w formie wykresu
    mean_df = pd.DataFrame(mean_values, columns=["Mean"])
    st.bar_chart(mean_df)

# Dodatkowe wskazówki
st.write("#### Jak dalej rozbudować aplikację?")
st.write("""
- Dodaj obsługę plików (np. wczytywanie CSV).
- Twórz inne rodzaje wykresów (wykres liniowy, kołowy itp.).
- Pozwól użytkownikowi filtrować dane według parametrów.
- Wykorzystaj modele Machine Learning do predykcji i pokaż wyniki w przejrzysty sposób.
""")
