import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("test matplotlib")

# Suwak do wyboru liczby wierszy
num_rows = st.slider("Liczba wierszy danych do wygenerowania:", 5, 100, 20)

# Generowanie przykładowych danych
random_data = np.random.randn(num_rows, 2)  # 2 kolumny
df = pd.DataFrame(random_data, columns=["X", "Y"])

st.write("Podgląd danych:")
st.dataframe(df)

# Dodaj przycisk, żeby rysować wykres
if st.button("Narysuj wykres z matplotlib"):
    st.write("**Wykres punktowy (Scatter Plot) z biblioteki matplotlib**")

    # Tworzymy figurę i osie
    fig, ax = plt.subplots()

    # Rysowanie wykresu punktowego
    ax.scatter(df["X"], df["Y"], color="blue", alpha=0.7)

    # Dodajemy etykiety osi
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Losowe punkty X vs Y")

    # Wyświetlamy wykres za pomocą Streamlit
    st.pyplot(fig)


