# Packages in Python

**Was sind Packages?**

Stell dir Packages wie Werkzeugkisten vor. In Python ist ein Package eine Möglichkeit, verwandten Code (Module) in einer übersichtlichen Struktur zusammenzufassen. So bleibt dein Code organisiert, und du kannst Funktionen und Klassen aus anderen Projekten wiederverwenden, ohne alles neu schreiben zu müssen.

**Warum sind sie nützlich?**

* **Modularität**: Dein Code wird übersichtlicher und leichter zu warten.
* **Wiederverwendbarkeit**: Du sparst Zeit, indem du bewährten Code wiederverwendest.
* **Zusammenarbeit**: Mehrere Entwickler können leichter an einem Projekt arbeiten.
* **Namensräume**: Packages verhindern Namenskonflikte zwischen deinem Code und anderen Bibliotheken.

**Wie benutzt man sie?**

1. **Installieren**: Die meisten Packages findest du im Python Package Index (PyPI). Du installierst sie mit dem Befehl `pip install package_name`.
2. **Importieren**: Verwende `import package_name` oder `from package_name import funktion_oder_klasse`, um auf den Code im Package zuzugreifen.

**Beispiel**

Nehmen wir an, du möchtest mit Datumsangaben arbeiten. Dafür gibt es das eingebaute Package `datetime`:

```python
import datetime

heute = datetime.date.today()
print("Heute ist:", heute)
```

**Wichtige Punkte**

* Packages können Unterpackages und Module enthalten, wodurch eine hierarchische Struktur entsteht.
* Die Datei `__init__.py` (kann leer sein) markiert ein Verzeichnis als Package.
* Du kannst auch eigene Packages erstellen, um deinen Code zu organisieren.