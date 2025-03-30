Hier ist ein detaillierter 5-Schritte-Plan, um den MVP (Minimum Viable Product) deines Typo-Correctors umzusetzen. Dieser Plan ist darauf ausgelegt, im Rahmen eines Semesters realistisch zu sein und konzentriert sich auf die Kernfunktionalität.

---

**Projektplan: Typo-Corrector MVP**

**Ziel:** Eine funktionierende Webanwendung mit Frontend (Vue.js) und Backend (Python/Flask), die Texteingaben entgegennimmt, grundlegende typografische Korrekturen (Anführungszeichen, doppelte Leerzeichen, Apostrophe) serverseitig durchführt und das Ergebnis anzeigt.

---

**Schritt 1: Dockerisiertes Setup & Grundlagen

*   **Ziel:** Eine Docker-basierte Entwicklungsumgebung für Frontend (Vue.js) und Backend (Python/Flask) ist eingerichtet und versioniert. Die Basisstruktur für beide Services existiert, und die Container können erfolgreich gebaut und gestartet werden.
*   **Aktueller Schritt:** **Dockerisiertes Setup & Grundlagen**
*   **Aufgaben:**

    1.  **Versionskontrolle:**
        *   Erstelle ein neues Repository auf GitHub oder GitLab.
        *   Klone das Repository lokal.
        *   Erstelle eine grundlegende `.gitignore`-Datei im Hauptverzeichnis (Vorlagen für Python, Node und Docker kombinieren). Wichtige Einträge: `venv/`, `node_modules/`, `__pycache__/`, `*.pyc`, `.env`, `.docker/volumes/` (falls du benannte Volumes verwendest).

    2.  **Projektstruktur:**
        *   Lege die Hauptverzeichnisstruktur an:
            ```
            typo-corrector/
            ├── backend/
            │   ├── Dockerfile
            │   ├── requirements.txt
            │   └── app.py           # Minimale Flask App
            │   └── .dockerignore    # Backend-spezifisch
            ├── frontend/
            │   ├── Dockerfile
            │   ├── package.json     # Wird von Vue/Vite erstellt
            │   └── ...              # Andere Vue/Vite Projektdateien
            │   └── .dockerignore    # Frontend-spezifisch
            ├── docker-compose.yml   # Orchestriert die Container
            ├── .gitignore           # Im Hauptverzeichnis
            └── README.md
            ```

    3.  **Backend Basis definieren (`backend/`):**
        *   **`requirements.txt` erstellen:** Füge die initialen Abhängigkeiten hinzu:
            ```txt
            Flask
            Flask-CORS
            ```
        *   **Minimale `app.py` erstellen:**
            ```python
            from flask import Flask, jsonify, request
            from flask_cors import CORS

            app = Flask(__name__)
            # Erlaube Anfragen vom Frontend (läuft auf anderem Port/Container)
            CORS(app)

            @app.route('/')
            def index():
                return jsonify({"message": "Backend is running!"})

            # Platzhalter für den späteren Korrektur-Endpunkt
            @app.route('/correct', methods=['POST'])
            def correct_text_endpoint():
                # Später: Logik zum Extrahieren und Verarbeiten des Textes
                data = request.get_json()
                text = data.get('text', '')
                # Platzhalter: Gibt den Text einfach zurück
                corrected_text = text.upper() # Nur zum Testen
                return jsonify({"corrected_text": corrected_text})

            # Kein 'if __name__ == "__main__":' Block nötig, wenn über Flask CLI oder Gunicorn gestartet wird
            ```
        *   **`backend/Dockerfile` erstellen:**
            ```dockerfile
            # Base Image mit Python
            FROM python:3.10-slim

            # Arbeitsverzeichnis im Container setzen
            WORKDIR /app

            # Abhängigkeiten installieren (kopiere erst die requirements Datei, um Caching zu nutzen)
            COPY requirements.txt .
            RUN pip install --no-cache-dir -r requirements.txt

            # Restlichen Code kopieren
            COPY . .

            # Port freigeben, auf dem Flask laufen wird
            EXPOSE 5000

            # Startbefehl (nutzt Flask's eingebauten Server für Entwicklung)
            # --host=0.0.0.0 ist wichtig, damit der Server von außerhalb des Containers erreichbar ist
            CMD ["flask", "run", "--host=0.0.0.0"]
            ```
        *   **`backend/.dockerignore` erstellen:**
            ```
            venv/
            __pycache__/
            *.pyc
            .git
            .gitignore
            ```

    4.  **Frontend Basis definieren (`frontend/`):**
        *   **Nuxt.js Projekt initialisieren:** Navigiere in den `frontend`-Ordner *im Terminal deines Host-Systems* und erstelle das Nuxt-Projekt:
            ```bash
            cd frontend
            npm create vue@latest . # Punkt am Ende wichtig!
            # Wähle wieder Optionen: Kein Router, kein Pinia, kein TS, ESLint, Prettier
            npm install # Installiert node_modules LOKAL, damit der Editor/IDE die Abhängigkeiten kennt
            cd .. # Zurück ins Hauptverzeichnis
            ```
            *Hinweis: `node_modules` wird lokal erstellt, aber dank `.dockerignore` nicht in den Container kopiert. Die Installation im Container erfolgt separat.*
        *   **`frontend/Dockerfile` erstellen:**
            ```dockerfile
            # Base Image mit Node.js
            FROM node:18

            # Arbeitsverzeichnis im Container setzen
            WORKDIR /app

            # Abhängigkeiten installieren (package*.json zuerst kopieren für Caching)
            COPY package.json package-lock.json ./
            RUN npm install

            # Restlichen Code kopieren (nachdem node_modules installiert wurden)
            COPY . .

            # Vite Dev-Server Port freigeben
            EXPOSE 5173

            # Startbefehl für den Vite Dev-Server
            # --host macht den Server im Netzwerk des Containers verfügbar
            CMD ["npm", "run", "dev", "--", "--host"]
            ```
        *   **`frontend/.dockerignore` erstellen:**
            ```
            node_modules/
            dist/
            .git
            .gitignore
            ```

    5.  **Docker Compose definieren (`docker-compose.yml` im Hauptverzeichnis):**
        ```yaml
        version: '3.8'

        services:
          backend:
            build: ./backend          # Pfad zum Backend Dockerfile
            ports:
              - "5001:5000"         # Mappt Host-Port 5001 auf Container-Port 5000 (Backend ist erreichbar unter http://localhost:5001)
            volumes:
              - ./backend:/app      # Mountet lokalen Code ins Container-Verzeichnis für Live-Reload
            environment:
              - FLASK_ENV=development # Aktiviert Flask Debug Modus (automatischer Neustart bei Änderungen)

          frontend:
            build: ./frontend         # Pfad zum Frontend Dockerfile
            ports:
              - "3001:5173"         # Mappt Host-Port 3001 auf Container-Port 5173 (Frontend ist erreichbar unter http://localhost:3001)
            volumes:
              - ./frontend:/app       # Mountet lokalen Code für HMR (Hot Module Replacement)
              - /app/node_modules   # Wichtig: Verhindert, dass lokaler node_modules Ordner den im Container überschreibt
            depends_on:
              - backend             # Startet Backend bevor Frontend (optional, aber gute Praxis)

        # Optional: Netzwerk definieren, wenn spezielle Konfiguration nötig (oft nicht für einfache Setups)
        # networks:
        #   app-network:
        #     driver: bridge
        ```

    6.  **Erster Build & Start:**
        *   Stelle sicher, dass Docker Desktop (oder Docker Engine/Compose auf Linux) läuft.
        *   Öffne ein Terminal im Hauptverzeichnis (`typo-corrector/`).
        *   Führe den Befehl aus, um die Images zu bauen und die Container zu starten:
            ```bash
            docker-compose up --build
            ```
        *   Du solltest Logs von beiden Services (Backend und Frontend) sehen.
        *   Öffne deinen Browser:
            *   Frontend: `http://localhost:3001` (Sollte die Standard-Vue-Seite zeigen)
            *   Backend-Test: `http://localhost:5001` (Sollte `{"message": "Backend is running!"}` zeigen)
        *   Stoppe die Container mit `Ctrl + C` im Terminal und räume sie auf mit:
            ```bash
            docker-compose down
            ```

    7.  **Commit:**
        *   Füge alle erstellten und geänderten Dateien zum Git-Repository hinzu (`git add .`).
        *   Mache einen aussagekräftigen ersten Commit (z. B. `feat: Initial project setup with Docker Compose`).

---

Mit diesem Schritt 1 hast du eine solide, containerisierte Basis für dein Projekt geschaffen. Änderungen am Code im `backend`- oder `frontend`-Ordner werden dank der Volumes direkt in den laufenden Containern reflektiert, was die Entwicklung erleichtert. Der nächste Schritt (Backend-Entwicklung) kann nun direkt in dieser Umgebung erfolgen.

---

**Schritt 2: Backend-Entwicklung (API & Korrekturlogik)**

*   **Ziel:** Eine funktionierende Flask-API, die Text über einen Endpunkt (`/correct`) empfängt, die Kern-Korrekturregeln anwendet und den korrigierten Text zurückgibt.
*   **Aktueller Schritt:** **Backend-Entwicklung (API & Korrekturlogik)**
*   **Aufgaben:**
    1.  **API-Endpunkt erstellen:**
        *   Definiere in `backend/app.py` eine Route `/correct`, die `POST`-Requests akzeptiert.
        *   Nutze `request.get_json()` von Flask, um den eingehenden Text (im JSON-Body) zu lesen.
        *   Implementiere grundlegendes Fehlerhandling (z. B. wenn kein Text gesendet wird).
    2.  **Korrekturlogik implementieren:**
        *   Erstelle eine separate Funktion (z. B. `apply_corrections(text)`) in einer `corrections.py` Datei.
        *   Implementiere die ersten Korrekturregeln mithilfe des `re`-Moduls (RegEx):
            *   Entfernen doppelter Leerzeichen: `re.sub(r' +', ' ', text)`
            *   Korrektur einfacher Anführungszeichen (z.B. deutsche Typografie):
                *   `"` oder `”` am Wortanfang zu `„`
                *   `"` oder `”` am Wortende zu `“`
                *   *Hinweis: Regex für Anführungszeichen kann knifflig sein, starte einfach!*
            *   Korrektur von `'` zu `’` (Apostroph).
        *   Strukturiere die Regeln übersichtlich (z. B. als Liste von `(pattern, replacement)`-Tupeln).
    3.  **API-Antwort:**
        *   Gib den korrigierten Text in einem JSON-Objekt zurück, z. B. `{'corrected_text': corrected_text}`.
        *   Konfiguriere `Flask-CORS` in `app.py`, um Anfragen vom Frontend (läuft auf einem anderen Port) zu erlauben.
    4.  **Testen:**
        *   Teste die API lokal mit Tools wie `curl` oder Postman/Insomnia. Sende Beispieltexte und prüfe die Ergebnisse.

---

**Schritt 3: Frontend-Entwicklung (UI & API-Anbindung)

*   **Ziel:** Eine Benutzeroberfläche in Vue.js mit Eingabe-/Ausgabefeldern und einem Button, die die Backend-API aufruft und das Ergebnis anzeigt.
*   **Aktueller Schritt:** **Frontend-Entwicklung (UI & API-Anbindung)**
*   **Aufgaben:**
    1.  **UI-Komponenten erstellen:**
        *   Entwickle die Hauptansicht (`App.vue` oder eine dedizierte Komponente).
        *   Füge zwei `<textarea>`-Elemente hinzu.
        *   Binde die Textareas mit `v-model` an Datenvariablen im `<script setup>` (z. B. `inputText`, `outputText`).
    2.  **Interaktion hinzufügen:**
        *   Füge einen Button "Korrigieren" hinzu.
        *   Erstelle eine Methode (z. B. `correctText`), die bei Klick auf den Button (`@click`) aufgerufen wird.
    3.  **API-Anbindung:**
        *   Installiere `axios` (`npm install axios`) oder nutze das native `fetch`.
        *   Implementiere in `correctText` den API-Aufruf (POST) an deinen lokalen Backend-Endpunkt (`http://localhost:5001/correct`). Sende `{ 'text': inputText.value }` im Body.
        *   Verarbeite die Antwort: Aktualisiere `outputText` mit dem `corrected_text` aus der JSON-Antwort.
        *   Füge einfaches Fehlerhandling hinzu (z. B. `console.error` oder eine Meldung für den Benutzer bei fehlgeschlagener Anfrage).
    4.  **Zusatzfeatures (Nice-to-have für MVP):**
        *   Füge einen "Kopieren"-Button für das Ausgabefeld hinzu (nutzt die Clipboard API).
        *   Zeige einen einfachen Ladezustand an, während die API-Anfrage läuft.
    5.  **Styling:**
        *   Füge grundlegendes CSS hinzu, um die Seite ansprechend und benutzbar zu gestalten (entweder eigenes CSS oder ein Framework wie Bootstrap/Tailwind).

---

**Schritt 4: Integration & Test

*   **Ziel:** Sicherstellen, dass Frontend und Backend nahtlos zusammenarbeiten und die Korrekturen für verschiedene Eingaben korrekt funktionieren.
*   **Aktueller Schritt:** **Integration & Test**
*   **Aufgaben:**
    1.  **Gemeinsames Starten:** Starte sowohl den Flask-Entwicklungsserver (`flask run` im `backend/`-Ordner mit aktivierter `venv`) als auch den Vue-Entwicklungsserver (`npm run dev` im `frontend/`-Ordner).
    2.  **End-to-End-Tests:**
        *   Öffne die Frontend-App im Browser.
        *   Gib verschiedene Testtexte ein:
            *   Texte mit den zu korrigierenden Fehlern (Anführungszeichen, Leerzeichen, Apostrophe).
            *   Texte ohne Fehler.
            *   Leere Texte.
            *   Texte mit Sonderzeichen.
        *   Überprüfe, ob die Ausgabe im Frontend korrekt ist.
    3.  **Debugging:**
        *   Nutze die Browser-Entwicklertools (Netzwerk-Tab, Konsole) zur Analyse von Frontend-Problemen oder API-Aufrufen.
        *   Nutze Flasks Debug-Modus und `print()`-Anweisungen oder einen Debugger (wie in VS Code) für Backend-Probleme.
    4.  **Fehlerbehandlung prüfen:** Teste, was passiert, wenn das Backend nicht läuft oder einen Fehler zurückgibt.

---

**Schritt 5: Deployment & Verfeinerung (Puffer / Optional)

*   **Ziel:** Die Anwendung (optional) online bereitstellen und den Code/die UX basierend auf den Tests verbessern.
*   **Aktueller Schritt:** **Deployment & Verfeinerung**
*   **Aufgaben:**
    1.  **Deployment (Optional):**
        *   **Frontend:** Baue die Vue-App (`npm run build`) und deploye den statischen Output auf Vercel oder Netlify.
        *   **Backend:** Bereite die Flask-App für das Deployment vor (z. B. mit Gunicorn als WSGI-Server) und deploye sie auf Heroku (oder einem ähnlichen PaaS-Anbieter).
        *   **Konfiguration:** Stelle sicher, dass das Frontend die korrekte URL der deployten Backend-API kennt (z. B. über Umgebungsvariablen).
    2.  **Code-Qualität:**
        *   Überprüfe den Code auf Lesbarkeit und Konsistenz.
        *   Führe Linter (ESLint für Frontend, z. B. Flake8/Black für Backend) aus und behebe Warnungen.
        *   Füge Kommentare hinzu, wo nötig.
    3.  **Dokumentation:**
        *   Aktualisiere die `README.md` mit einer Beschreibung des Projekts, Setup-Anweisungen für die lokale Entwicklung und (falls deployt) einem Link zur Live-Anwendung.
    4.  **Feinschliff:** Kleinere UI/UX-Verbesserungen basierend auf den Testergebnissen.

---

Dieser Plan gibt dir eine klare Struktur. Denk daran, dass dies Schätzungen sind. Je nach deiner Vorerfahrung und auftretenden Herausforderungen können sich die Zeiten verschieben. Wichtig ist, regelmäßig Commits zu machen und bei Problemen nicht zu zögern, nach Lösungen zu suchen oder Fragen zu stellen. Viel Erfolg bei deinem Projekt!
