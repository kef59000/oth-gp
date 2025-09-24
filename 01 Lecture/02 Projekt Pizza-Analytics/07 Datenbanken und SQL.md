## Datenbanken und SQL

**Was sind Datenbanken?**

Eine Datenbank ist im Wesentlichen eine organisierte Sammlung von Daten, die so strukturiert sind, dass sie einfach abgerufen, verwaltet und aktualisiert werden können. Stellen Sie sich eine Datenbank als ein digitales Ablagesystem vor, in dem Informationen in Kategorien und Unterkategorien sortiert sind. 

**Warum brauchen wir Datenbanken?**

Datenbanken spielen in der heutigen Welt eine entscheidende Rolle, da sie es uns ermöglichen, große Datenmengen effizient zu speichern und zu verarbeiten. Sie werden in einer Vielzahl von Anwendungen eingesetzt, darunter:

* **Unternehmen:** Kundendaten, Produktinformationen, Finanztransaktionen
* **E-Commerce:** Produktkataloge, Bestellungen, Kundenkonten
* **Soziale Medien:** Benutzerprofile, Beiträge, Verbindungen
* **Gesundheitswesen:** Patientenakten, medizinische Daten, Forschungsergebnisse

**Was ist SQL?**

SQL (Structured Query Language) ist die Standardsprache für die Interaktion mit relationalen Datenbanken. Mit SQL können Sie:

* **Daten abrufen:** Informationen aus der Datenbank abfragen.
* **Daten ändern:** Daten in der Datenbank hinzufügen, aktualisieren oder löschen.
* **Daten definieren:** Die Struktur der Datenbank erstellen und ändern.
* **Daten kontrollieren:** Den Zugriff auf die Daten steuern und die Datenintegrität gewährleisten.

**Wie funktioniert eine relationale Datenbank?**

Relationale Datenbanken speichern Daten in Tabellen, die in Zeilen und Spalten organisiert sind. Jede Zeile repräsentiert einen Datensatz, und jede Spalte repräsentiert ein Attribut. Beziehungen zwischen Tabellen werden durch gemeinsame Spalten hergestellt.

**Beispiel:**

Stellen Sie sich eine Datenbank für eine Bibliothek vor. Es könnte Tabellen für "Bücher", "Autoren" und "Ausleihen" geben. Die Tabelle "Bücher" könnte Spalten wie "Titel", "Autor_ID" und "ISBN" enthalten. Die Tabelle "Autoren" könnte Spalten wie "Autor_ID" und "Name" enthalten. Die "Autor_ID" wäre die gemeinsame Spalte, die die Beziehung zwischen den beiden Tabellen herstellt.

**Vorteile von SQL:**

* **Standardisiert:** SQL ist eine weit verbreitete Sprache, die von den meisten relationalen Datenbanken unterstützt wird.
* **Mächtig:** SQL bietet eine Vielzahl von Funktionen zur Datenmanipulation und -abfrage.
* **Einfach zu erlernen:** Die grundlegende Syntax von SQL ist relativ einfach zu verstehen.



## Grundlegende SQL-Befehle

**Data Definition Language (DDL)**

* **`CREATE`**: Erstellt Datenbankobjekte wie Tabellen.
    ```sql
    CREATE TABLE Mitarbeiter (
        ID INT PRIMARY KEY,
        Name VARCHAR(255),
        Abteilung VARCHAR(255)
    );
    ```

* **`ALTER`**: Ändert die Struktur bestehender Datenbankobjekte.
    ```sql
    ALTER TABLE Mitarbeiter
    ADD Gehalt DECIMAL(10,2);
    ```

* **`DROP`**: Löscht Datenbankobjekte.
    ```sql
    DROP TABLE Mitarbeiter; 
    ```

**Data Manipulation Language (DML)**

* **`SELECT`**: Ruft Daten aus einer Datenbank ab.
    ```sql
    SELECT Name, Abteilung 
    FROM Mitarbeiter;
    ```

* **`INSERT`**: Fügt neue Daten in eine Tabelle ein.
    ```sql
    INSERT INTO Mitarbeiter (ID, Name, Abteilung) 
    VALUES (1, 'Max Mustermann', 'Vertrieb');
    ```

* **`UPDATE`**: Aktualisiert bestehende Daten in einer Tabelle.
    ```sql
    UPDATE Mitarbeiter 
    SET Abteilung = 'Marketing' 
    WHERE ID = 1;
    ```

* **`DELETE`**: Löscht Daten aus einer Tabelle.
    ```sql
    DELETE FROM Mitarbeiter 
    WHERE ID = 1;
    ```

**Weitere wichtige Befehle:**

* **`WHERE`**: Filtert Daten basierend auf einer Bedingung.
    ```sql
    SELECT * FROM Mitarbeiter WHERE Abteilung = 'Vertrieb';
    ```

* **`ORDER BY`**: Sortiert die Ergebnismenge.
    ```sql
    SELECT * FROM Mitarbeiter ORDER BY Name ASC;
    ```

* **`GROUP BY`**: Gruppiert Zeilen mit gleichen Werten.
    ```sql
    SELECT Abteilung, COUNT(*) FROM Mitarbeiter GROUP BY Abteilung;
    ```

* **`JOIN`**: Verbindet Daten aus mehreren Tabellen.
    ```sql
    SELECT m.Name, a.Aufgaben 
    FROM Mitarbeiter m
    JOIN Aufgaben a ON m.ID = a.MitarbeiterID;
    ```

**Zusätzliche Hinweise:**

* SQL-Befehle werden in der Regel in Großbuchstaben geschrieben, dies ist jedoch nicht zwingend erforderlich.
* Die meisten DBMS bieten zusätzliche Befehle und Funktionen, die über diese grundlegenden Befehle hinausgehen.
