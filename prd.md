## **📄 Product Requirement Document (PRD) – Typo-Corrector**

### **1\. Übersicht**

**Produktname:** Typo-Corrector  
 **Version:** MVP (Minimum Viable Product)  
 **Dokumentationsdatum:** 28\. März 2025  
 **Verantwortlich:** \[Dein Name/Team\]

---

### **2\. Ziel & Vision**

Der **Typo-Corrector** ist eine Webanwendung zur schnellen und intelligenten **Korrektur typografischer Fehler** in Texten. Er bietet zwei Modi – **Casual** für einfache Fehlerbereinigung und **Expert** für erweiterte Kontrolle. Die Vision ist ein Tool, das Textaufbereitung effizient, sauber und zugänglich für alle macht – von Studierenden bis hin zu Designprofis.

---

### **3\. Zielgruppe**

**Primäre Zielgruppe (MVP):**

* Studierende

* Content Creators

* Büroangestellte

* Redakteur:innen

**Sekundäre Zielgruppe (später):**

* Designer & Layouter

* Entwickler

* Personen mit spezifischen Formatierungsbedürfnissen

---

### **4\. Produktumfang (Scope)**

#### **✅ Casual Mode (MVP)**

* Ersetzen gerader durch typografische Anführungszeichen

* Entfernen doppelter Leerzeichen

* Korrektur typografischer Zeichen (Apostroph, Gedankenstrich, Ellipsen)

* Behebung defekter Zeichen (z. B. Encoding-Fehler wie „Ã¤“ → „ä“)

* Entfernung von PDF-Zeilenumbrüchen

#### **🧠 Expert Mode (MVP)**

* Selektives Aktivieren/Deaktivieren von Korrekturregeln (Checkboxes)

* Vorschau korrigierter Texte in HTML/Markdown

* Live-Vorschau der Korrekturen im Editor

* Option: Originalformatierung beibehalten

---

### **5\. Abgrenzung (Out-of-Scope – MVP)**

Folgende Features sind für eine spätere Version geplant:

* Benutzerkonten, gespeicherte Präferenzen

* OCR-Import (Text aus Bildern extrahieren)

* Batch-Verarbeitung mehrerer Dateien

* Dynamische, benutzerdefinierte Korrekturregeln

* HTML/Markdown-Export

* Datenpersistenz & Verlauf

---

### **6\. Funktionale Anforderungen**

| ID | Feature | Beschreibung |
| ----- | ----- | ----- |
| F1 | Text-Eingabe | User kann Text manuell eingeben oder per Datei hochladen |
| F2 | Text-Korrektur | Text wird via POST-Request ans Backend gesendet, Korrekturen angewendet |
| F3 | Korrektur-Modi | Casual Mode vs. Expert Mode, regelbasierte Optionen |
| F4 | Vorschau | Ergebnis wird im UI dargestellt, inkl. HTML/Markdown optional |
| F5 | Export | Nutzer kann den korrigierten Text herunterladen oder kopieren |

---

### **7\. Nicht-funktionale Anforderungen**

* **Performance:** Antwortzeit \< 500 ms für Texte bis 5.000 Wörter

* **Sicherheit:** Eingaben sanitizen (z. B. `bleach`), XSS-Schutz, Rate Limiting

* **Skalierbarkeit:** Modularer Aufbau, Containerisierung (Docker)

* **Wartbarkeit:** Klare Trennung von Frontend & Backend, CI/CD via GitHub Actions

---

### **8\. Technologie-Stack**

#### **Frontend**

* Framework: **Vue.js** oder **Nuxt.js**

* Komponenten: Material UI, TailwindCSS, Dropzone.js

* Texteditor: CodeMirror, react-textarea-autosize

* Export: FileSaver.js, Turndown (Markdown)

#### **Backend**

* Sprache: **Python**

* Framework: **Flask** (optional: Django)

* Bibliotheken: re, typogrify, Unidecode, pdfplumber

* OCR (zukünftig): pytesseract \+ OpenCV/Pillow

#### **Infrastruktur**

* Hosting: **Vercel** (Frontend), **Heroku** oder **Infomaniak** (Backend)

* Container: **Docker**

* CI/CD: GitHub Actions

* Datenhaltung (zukünftig): SQLite oder PostgreSQL

---

### **9\. Systemarchitektur (MVP)**

\[Nutzer-UI (Vue.js)\] → POST /correct → \[Flask-API\] → Korrekturlogik → JSON Response → Darstellung im Frontend

---

### **10\. Erfolgskriterien (KPIs)**

* ⏱️ Time-to-Correct \< 1 Sekunde

* ✅ Korrekturfunktion fehlerfrei bei \> 95 % der typischen Texte

* 📈 Zufriedenheit bei UX-Tests (Score ≥ 4 / 5\)

* 🧪 100 % Testabdeckung der Korrekturregeln im Backend

---

### **11\. Offene Fragen / ToDo**

* Entscheidung: **Vue** oder **React**?

* Wie sollen Nutzer im Expert Mode neue Regeln laden/speichern (später)?

* Anforderungen an Accessibility (Screenreader etc.)?

* Hosting-Budget und Deployment-Zeitfenster?

---

---

## **🚀 Roadmap – Typo-Corrector (MVP)**

### **🟢 Phase 1: Projekt-Setup & Architektur (Woche 1–2)**

**Ziele:** Arbeitsumgebung bereitstellen, technologische Basis klären

**Tasks:**

* Projektstruktur aufsetzen (Frontend & Backend getrennt)

* Entscheidung: Vue.js oder Nuxt.js

* GitHub-Repo \+ CI/CD mit GitHub Actions

* Docker-Setup (lokal & deploymentfähig)

* API-Routing & Schnittstellenplan definieren

* Basis-Flask-App mit `/correct`\-Endpoint

**Milestone:** Funktionsfähiges Grundgerüst mit einfachem Health-Check

---

### **🟡 Phase 2: Korrekturlogik & Backend-Entwicklung (Woche 3–4)**

**Ziele:** Textkorrektur-Regeln implementieren, API-Logik funktionsfähig

**Tasks:**

* Regex-basierte Korrekturmodule implementieren:

  * Anführungszeichen ersetzen

  * Doppelte Leerzeichen entfernen

  * Typografische Zeichen (Apostroph, Ellipse etc.)

  * Encoding-Fixer (`Unidecode`)

  * PDF-Zeilenumbrüche erkennen

* Unit-Tests für alle Regeln

* Fehlerhandling & Validierung der Inputs

* Logging, Rate Limiting & Input Sanitizing

**Milestone:** API korrigiert Texte zuverlässig & sicher

---

### **🟠 Phase 3: Frontend-UI & Casual Mode (Woche 5–6)**

**Ziele:** Minimal-UI mit Texteditor, Upload & Ergebnisdarstellung

**Tasks:**

* Vue/Nuxt-Projekt starten

* UI-Bibliothek (Tailwind oder Material UI) einbinden

* Textarea (CodeMirror o.ä.) für Eingabetext

* Button: „Korrigieren“

* Fetch/axios POST an `/correct`

* Ausgabe im Vorschaufenster

* Datei-Upload via Dropzone.js

* Copy/Download-Funktion (FileSaver.js)

**Milestone:** Casual Mode vollständig nutzbar über UI

---

### **🔵 Phase 4: Expert Mode (Woche 7–8)**

**Ziele:** Selektive Regeln, Live-Vorschau, Formatoptionen

**Tasks:**

* Checkboxen für Korrekturregeln

* Live-Update der Vorschau bei Textänderung

* Markdown-/HTML-Ansicht integrieren

* Export als `.md` oder `.html` via Turndown

* Toggle zwischen Casual und Expert Mode

**Milestone:** Expert Mode aktiv, differenzierte Kontrolle möglich

---

### **🟣 Phase 5: Testing, Polishing & Launch (Woche 9–10)**

**Ziele:** Stabilität, Usability, erste Release-Version

**Tasks:**

* End-to-End-Tests (z. B. Playwright oder Cypress)

* UX-Feinschliff (Responsive Design, Dark Mode optional)

* Accessibility-Check (Screenreader-Kompatibilität etc.)

* Deployment: Vercel (Frontend), Heroku/Infomaniak (Backend)

* Feedbackrunde mit 3–5 Testusern

* Roadmap-Update für zukünftige Features

**Milestone:** MVP ist live, Feedback kann gesammelt werden

---

## **🗓 Gesamtzeitrahmen: \~10 Wochen**

Falls du Sprints mit z. B. 2-Wochen-Taktung machst, ergibt sich folgendes Schema:

* **Sprint 1:** Architektur & Setup

* **Sprint 2:** Korrekturlogik

* **Sprint 3:** Frontend & Casual Mode

* **Sprint 4:** Expert Mode

* **Sprint 5:** Tests, Launch, Refactoring

---

Möchtest du daraus gleich ein **Trello-Board** oder eine **Notion-Vorlage** machen lassen? Oder brauchst du eine **Excel-Export**\-Version dieser Roadmap? Sag einfach Bescheid\!
