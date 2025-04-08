<template>
  <div class="container">
    <div class="glassmorphism-effect"></div>
    
    <header>
      <h1>Interaktive Textkorrektur</h1>
      <p class="subtitle">Verbessere deinen Text mit unserem intelligenten Korrektur-Tool</p>
    </header>
    
    <div class="content-wrapper">
      <div class="section input-section">
        <h2 class="section-title">Eingabe</h2>
        <textarea 
          class="text-field" 
          placeholder="Text hier eingeben..." 
          v-model="eingabeText"
        ></textarea>
      </div>

      <div class="arrow-container">
        <div class="arrow-circle">
          <svg class="arrow" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"></path>
          </svg>
        </div>
      </div>

      <div class="section output-section">
        <h2 class="section-title">Ausgabe</h2>
        <textarea 
          class="text-field" 
          v-model="korrigierterText" 
          readonly
        ></textarea>
      </div>
    </div>

    <div class="button-container">
      <button class="korrektur-button" @click="korrigieren" :disabled="isLoading" :class="{ 'loading': isLoading }">
        <span class="button-icon" v-if="!isLoading">✓</span>
        <span class="loading-spinner" v-if="isLoading"></span>
        {{ isLoading ? 'Korrigiere...' : 'Text korrigieren' }}
      </button>
    </div>
    
    <p v-if="error" class="error-message">
      <span class="error-icon">!</span>
      {{ error }}
    </p> 

    <footer>
      <p>Typo-Corrector <span class="separator">|</span> <span class="highlight">Alles ganz ohne KI</span></p>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Reaktive Variablen
const eingabeText = ref('')
const korrigierterText = ref('Korrigierter Text wird hier angezeigt...')
const isLoading = ref(false); // Hinzugefügt
const error = ref(''); // Hinzugefügt

// Backend URL (stelle sicher, dass der Port korrekt ist)
const backendUrl = 'http://localhost:5001/correct'; // Hinzugefügt

// Methoden
const korrigieren = async () => { // Umbenannt von correctText und Logik integriert
  isLoading.value = true;
  error.value = '';
  korrigierterText.value = ''; // Ausgabe leeren

  try {
    const response = await fetch(backendUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: eingabeText.value }), // angepasster Variablenname
    });

    if (!response.ok) {
      // Versuche, die Fehlermeldung vom Backend zu lesen
      let errorData;
      try {
        errorData = await response.json();
      } catch (e) {
        // Wenn die Antwort kein JSON ist
        throw new Error(`HTTP-Fehler ${response.status}: ${response.statusText}`);
      }
      throw new Error(`Fehler vom Backend: ${errorData.description || response.statusText}`);
    }

    const data = await response.json();
    korrigierterText.value = data.corrected_text; // angepasster Variablenname

  } catch (err: any) { // Typ für err hinzugefügt, da TypeScript
    console.error('Fehler beim Aufrufen der API:', err);
    error.value = `Fehler: ${err.message}`;
  } finally {
    isLoading.value = false;
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --primary-color: #6366f1;
  --primary-hover: #4f46e5;
  --primary-active: #4338ca;
  --secondary-color: #10b981;
  --bg-color: #f8fafc;
  --card-bg: #ffffff;
  --text-color: #1e293b;
  --text-light: #64748b;
  --border-radius: 16px;
  --shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
  --accent-gradient: linear-gradient(135deg, #6366f1, #8b5cf6);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}

.container {
  font-family: 'Inter', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 60px 24px;
  background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.08), transparent 70%),
              radial-gradient(circle at bottom left, rgba(139, 92, 246, 0.08), transparent 70%);
  background-color: var(--bg-color);
  min-height: 100vh;
  max-width: 1400px;
  margin: 0 auto;
  position: relative;
}

.glassmorphism-effect {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 240px;
  background: var(--accent-gradient);
  opacity: 0.03;
  z-index: -1;
}

header {
  text-align: center;
  margin-bottom: 50px;
  width: 100%;
  position: relative;
}

h1 {
  color: var(--text-color);
  font-size: 3.2rem;
  font-weight: 800;
  margin-bottom: 16px;
  letter-spacing: -1px;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  position: relative;
  display: inline-block;
}

h1::after {
  content: "";
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: var(--accent-gradient);
  border-radius: 2px;
}

.subtitle {
  color: var(--text-light);
  font-size: 1.15rem;
  font-weight: 400;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
  margin-top: 20px;
}

.content-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: stretch;
  width: 100%;
  margin-bottom: 40px;
  gap: 30px;
}

.section {
  flex: 1;
  min-width: 300px;
  max-width: 550px;
  background-color: var(--card-bg);
  padding: 30px;
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  transition: all 0.4s ease;
  border: 1px solid rgba(229, 231, 235, 0.5);
  position: relative;
  overflow: hidden;
}

.section::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 6px;
  background: var(--accent-gradient);
  opacity: 0.7;
}

.section:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.07);
}

.input-section::before {
  background: linear-gradient(135deg, #6366f1, #4f46e5);
}

.output-section::before {
  background: linear-gradient(135deg, #10b981, #0ea5e9);
}

.section-title {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 25px;
  color: var(--text-color);
  position: relative;
  padding-bottom: 12px;
  display: inline-block;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  width: 40px;
  background-color: var(--primary-color);
  border-radius: 3px;
}

.arrow-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 15px;
  z-index: 1;
}

.arrow-circle {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 56px;
  height: 56px;
  background: var(--card-bg);
  border-radius: 50%;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  border: 1px solid rgba(229, 231, 235, 0.5);
}

.arrow-circle:hover {
  transform: scale(1.1);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.15);
}

.arrow {
  width: 28px;
  height: 28px;
  fill: var(--primary-color);
}

@media (max-width: 940px) {
  .content-wrapper {
    flex-direction: column;
    align-items: center;
  }
  
  .arrow-circle {
    margin: 10px 0;
    transform: rotate(90deg);
  }

  .arrow-circle:hover {
    transform: rotate(90deg) scale(1.1);
  }
  
  .section {
    max-width: 100%;
  }
  
  h1 {
    font-size: 2.5rem;
  }
}

.text-field {
  width: 100%;
  min-height: 180px;
  padding: 18px;
  font-size: 16px;
  border: 1px solid rgba(229, 231, 235, 0.7);
  border-radius: 12px;
  resize: vertical;
  font-family: 'Inter', sans-serif;
  transition: all 0.3s ease;
  line-height: 1.7;
  color: var(--text-color);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.04);
}

.text-field::placeholder {
  color: #94a3b8;
  opacity: 0.8;
}

.text-field:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15);
}

.button-container {
  margin-top: 25px;
  display: flex;
  justify-content: center;
  width: 100%;
}

.korrektur-button { 
  background: var(--accent-gradient);
  color: white;
  border: none;
  padding: 16px 34px;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 15px rgba(99, 102, 241, 0.25);
  position: relative;
  overflow: hidden;
}

.korrektur-button::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: all 0.5s ease;
}

.korrektur-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.35);
}

.korrektur-button:hover::before {
  left: 100%;
}

.korrektur-button:active {
  transform: translateY(0);
}

.korrektur-button.loading {
  background: linear-gradient(135deg, #7c85f1, #6366f1);
}

.button-icon {
  margin-right: 10px;
  font-size: 1.2rem;
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 0.8s linear infinite;
  margin-right: 10px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

footer {
  margin-top: 70px;
  text-align: center;
  color: var(--text-light);
  font-size: 0.9rem;
  width: 100%;
  padding: 20px 0;
  border-top: 1px solid rgba(229, 231, 235, 0.5);
}

.input-section, .output-section {
  display: flex;
  flex-direction: column;
}

.text-field[readonly] {
  background-color: #f8fafc;
  border-color: rgba(229, 231, 235, 0.5);
  cursor: default;
}

.error-message {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ef4444;
  font-weight: 500;
  margin-top: 15px;
  background-color: rgba(239, 68, 68, 0.08);
  padding: 12px 20px;
  border-radius: 10px;
  max-width: 600px;
  text-align: center;
}

.error-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  background-color: #ef4444;
  color: white;
  border-radius: 50%;
  margin-right: 10px;
  font-weight: bold;
}

.separator {
  margin: 0 8px;
  opacity: 0.5;
}

.highlight {
  font-weight: 600;
  background: linear-gradient(135deg, #10b981, #0ea5e9);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
