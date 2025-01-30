import streamlit as st
import pandas as pd
import numpy as np

st.title("Moja pierwsza aplikacja w Streamlit (z GitHuba)")

st.header("Krótka prezentacja danych")
st.write("""
Witaj! Ta aplikacja demonstruje, jak w prosty sposób możesz 
udostępnić kod w Pythonie w formie aplikacji webowej, 
korzystając z **Streamlit** i **GitHub**.
""")

num_rows = st.slider("Liczba wierszy danych do wygenerowania:", 5, 100, 10)

random_data = np.random.randn(num_rows, 3)
df = pd.DataFrame(random_data, columns=["X", "Y", "Z"])

st.write("Oto wygenerowane dane:")
st.dataframe(df)

if st.button("Oblicz średnie"):
    mean_values = df.mean()
    st.write("Średnie wartości w kolumnach:")
    st.write(mean_values)

st.write("#### Jak dalej rozbudować aplikację?")
st.write("""
- Dodaj obsługę plików (np. wczytywanie CSV).
- Twórz wykresy (`st.line_chart`, `st.bar_chart` albo `matplotlib/plotly`).
- Pozwól użytkownikowi filtrować dane według parametrów.
- Wykorzystaj modele Machine Learning do predykcji i pokaż wyniki w przejrzysty sposób.
""")
