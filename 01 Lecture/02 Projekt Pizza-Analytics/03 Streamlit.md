# Package "Streamlit"

**Was ist Streamlit?**

Streamlit ist ein Open-Source-Framework in Python, mit dem du auf schnelle und einfache Weise interaktive Webanwendungen erstellen kannst, insbesondere für Datenvisualisierung, Machine Learning und Datenanalyse. Der große Vorteil ist, dass du dich voll und ganz auf deinen Python-Code konzentrieren kannst, ohne dich mit HTML, CSS oder JavaScript herumschlagen zu müssen.

**Warum Streamlit?**

* **Python pur:** Du schreibst deine gesamte Anwendung in Python, was die Entwicklung enorm beschleunigt.
* **Schnelle Prototypen:** Du kannst in kürzester Zeit interaktive Dashboards und Anwendungen erstellen, um deine Daten zu erkunden und zu präsentieren.
* **Live-Updates:** Änderungen an deinem Code werden sofort in der Anwendung sichtbar, was das Experimentieren und Debuggen erleichtert.
* **Einfache Bereitstellung:** Streamlit Cloud ermöglicht dir, deine Anwendungen mit wenigen Klicks zu veröffentlichen und mit anderen zu teilen.

**Grundlegende Elemente**

* **Widgets:** Streamlit bietet eine Vielzahl von Widgets wie Schieberegler, Auswahlfelder, Textfelder usw., um Benutzereingaben zu ermöglichen.
* **Datenvisualisierung:** Du kannst gängige Bibliotheken wie Matplotlib, Seaborn oder Plotly verwenden, um deine Daten ansprechend zu visualisieren.
* **Layouts:** Mit Containern und Spalten kannst du das Layout deiner Anwendung strukturieren und gestalten.
* **Caching:** Streamlit bietet Caching-Mechanismen, um die Leistung deiner Anwendung zu verbessern, indem teure Berechnungen nur bei Bedarf durchgeführt werden.

**Beispiel**

```python
import streamlit as st
import pandas as pd

# Daten laden
df = pd.read_csv("meine_daten.csv")

# Titel
st.title("Meine erste Streamlit-App")

# Auswahlfeld für Spalten
spalte = st.selectbox("Wähle eine Spalte aus:", df.columns)

# Daten anzeigen
st.write(df[spalte])

# Diagramm erstellen
st.bar_chart(df[spalte])
```