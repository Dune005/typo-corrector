# Base Image mit Node.js (z.B. Version 18)
FROM node:18

# Arbeitsverzeichnis im Container setzen
WORKDIR /app

# package.json und package-lock.json kopieren (für Caching)
COPY package*.json ./

# Abhängigkeiten installieren
RUN npm install

# Restlichen Code kopieren
COPY . .

# Port freigeben, auf dem Nuxt läuft (Standard: 3000)
EXPOSE 3000

# Startbefehl für den Nuxt Dev-Server
# --host ist wichtig, damit der Server von außerhalb des Containers erreichbar ist
CMD ["npm", "run", "dev", "--", "--host"]
