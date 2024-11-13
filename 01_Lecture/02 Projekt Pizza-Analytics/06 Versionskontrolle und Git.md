## Version Control und Git

Versionskontrolle ist ein System, das Änderungen an Dateien über die Zeit hinweg verfolgt, so dass du zu bestimmten Versionen zurückkehren kannst. Dies ist besonders nützlich bei der Softwareentwicklung, wo mehrere Personen an denselben Dateien arbeiten.

**Warum Versionskontrolle?**

* **Verlauf verfolgen:**  Sieh dir an, wer was geändert hat und wann.
* **Fehler beheben:** Kehre zu früheren Versionen zurück, um Fehler zu finden und zu beheben.
* **Zusammenarbeit:** Arbeite gleichzeitig mit anderen an denselben Dateien, ohne Konflikte zu verursachen.
* **Experimentieren:** Probiere neue Funktionen aus, ohne die Hauptentwicklungslinie zu beeinträchtigen.

**Was ist Git?**

Git ist ein verteiltes Versionskontrollsystem, das 2005 von Linus Torvalds (dem Schöpfer von Linux) entwickelt wurde. Es ist heute das beliebteste Versionskontrollsystem der Welt.

**Wie funktioniert Git?**

Git speichert den gesamten Verlauf eines Projekts in einem **Repository**. Jede Änderung wird als **Commit** gespeichert. Ein Commit enthält:

* Die geänderten Dateien
* Den Autor der Änderung
* Eine Nachricht, die die Änderung beschreibt
* Einen Zeitstempel

**Wichtige Git-Befehle:**

* `git init`: Erstellt ein neues Git-Repository.
* `git clone`: Kopiert ein bestehendes Repository.
* `git add`: Fügt Dateien zum Staging-Bereich hinzu.
* `git commit`: Speichert Änderungen im Repository.
* `git push`: Überträgt Änderungen zu einem entfernten Repository.
* `git pull`: Holt Änderungen von einem entfernten Repository.
* `git branch`: Erstellt oder listet Branches auf.
* `git checkout`: Wechselt zu einem anderen Branch.
* `git merge`: Führt zwei Branches zusammen.

**Branches:**

Branches ermöglichen es, parallel an verschiedenen Funktionen oder Versionen eines Projekts zu arbeiten, ohne die Hauptentwicklungslinie zu beeinträchtigen.

**Workflow mit Git:**

1. **Repository erstellen oder klonen.**
2. **Änderungen an Dateien vornehmen.**
3. **Änderungen zum Staging-Bereich hinzufügen.**
4. **Änderungen committen.**
5. **Änderungen zum entfernten Repository pushen.**

**Vorteile von Git:**

* **Schnell und effizient.**
* **Verteilt: Jeder Entwickler hat eine vollständige Kopie des Repositorys.**
* **Flexibel: Unterstützt verschiedene Workflows.**
* **Open Source und kostenlos.**
* **Große Community und viele Ressourcen.**

**Beliebte Plattformen zum Hosten von Git-Repositories:**
* **GitHub**
* **GitLab**
* **Bitbucket**
* **Azure DevOps**

**Git-Workflow:**

![alt text](git_workflow.jpeg)

**Git-Flow:**

![alt text](feature_branches.svg)