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
